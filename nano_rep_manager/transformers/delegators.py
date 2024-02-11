import asyncio
from deps.rpc_client import nanorpc


class AccountTransformer:

    @staticmethod
    async def generate_account_info(seed):
        generated_info = {}

        async def fetch_and_process_data(index):
            try:
                key_data = await nanorpc.deterministic_key(seed, index)
                account = key_data.get('account')
                private_key = key_data.get('private')

                account_info_data = await nanorpc.account_info(account, representative=True)
                rep = account_info_data.get('representative')
                balance = int(account_info_data.get('balance', 0)) / (10 ** 30)

                if balance > 0:  # Ensure rep is not None or empty
                    return rep, {"account": account, "private_key": private_key, "weight": balance}, balance
                else:
                    return None

            except Exception as e:
                print(f"Error processing data for index {index}: {e}")
                return None  # Handle the error as needed

        async def process_data():
            tasks = [fetch_and_process_data(i) for i in range(1000)]
            results = await asyncio.gather(*tasks, return_exceptions=True)

            for result in results:
                if result:
                    rep, delegator_info, balance = result
                    if rep not in generated_info:
                        generated_info[rep] = {
                            "delegators": [], "sum_weight": 0}
                    generated_info[rep]["delegators"].append(delegator_info)
                    generated_info[rep]["sum_weight"] += balance

        await process_data()

        return generated_info

    @staticmethod
    async def reassign_accounts(account_info, rep_id, skip_n, take_m, new_rep):
        response = []
        if new_rep not in account_info:
            account_info[new_rep] = {"delegators": []}

        delegators_to_move = account_info[rep_id]['delegators'][skip_n: skip_n + take_m]

        # Prepare a list of coroutines for asyncio.gather
        tasks = [nanorpc.change(delegator["private_key"], new_rep, process=True)
                 for delegator in delegators_to_move]

        responses = await asyncio.gather(*tasks)
        response.extend(responses)
        return response
