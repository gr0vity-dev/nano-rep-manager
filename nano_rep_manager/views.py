from quart import Blueprint, render_template, request, redirect, url_for
from transformers.delegators import AccountTransformer
import logging

main = Blueprint('main', __name__)
logger = logging.getLogger(__name__)

# Assuming you have some way to store and retrieve account information in memory
account_info = {}


@main.route('/manage/<seed>')
async def manage(seed):
    global account_info
    account_info = await AccountTransformer().generate_account_info(seed)
    return await render_template('manage_accounts.html', account_info=account_info, seed=seed)


@main.route('/')
async def index():
    # Pass the account info to the template
    return await render_template('manage_accounts.html', account_info=account_info)


@main.route('/reassign', methods=['POST'])
async def reassign_accounts():
    global account_info

    # Extract form data
    form = await request.form
    rep_id = form['rep_id']
    skip_n = int(form['skip_n'])
    take_m = int(form['take_m'])
    new_rep = form['new_rep']
    seed = form['seed']

    logger.info(f"Reassigning accounts for rep_id: {rep_id}")

    change_blocks = await AccountTransformer.reassign_accounts(account_info, rep_id, skip_n, take_m, new_rep)

    # Your reassign logic
    # Redirect or respond as needed
    return redirect(url_for('main.manage', seed=seed))
