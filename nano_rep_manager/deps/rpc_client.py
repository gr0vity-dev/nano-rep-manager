from nanorpc.client_extended import NanoRpcExtended
import os

RPC_URL = os.getenv("RPC_URL")
AUTH_USERNAME = os.getenv("AUTH_USERNAME")
AUTH_PASSWORD = os.getenv("AUTH_PASSWORD")
NANO_TO_AUTH_KEY = os.getenv("NANO_TO_AUTH_KEY")  # optinal


def get_nanorpc_client(rpc_url=None, auth_username=None, auth_password=None, node_version=None):
    # Set the environment variables if they don't exist and parameters are provided
    rpc_url = rpc_url or RPC_URL
    auth_username = auth_username or AUTH_USERNAME
    auth_password = auth_password or AUTH_PASSWORD

    # Initialize and return the NanoRpc client
    return NanoRpcExtended(url=rpc_url,
                           username=auth_username,
                           password=auth_password)


# Create a single instance of NanoRpc client
nanorpc: NanoRpcExtended = get_nanorpc_client()
