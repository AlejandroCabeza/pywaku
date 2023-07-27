# Python Imports
from typing import Callable
# Framework Imports
# Third-Party Imports
# Project Imports
from tinyrpc import RPCProxy, RPCClient
from tinyrpc.protocols.jsonrpc import JSONRPCProtocol
from tinyrpc.transports.http import HttpPostClientTransport


class WakuRpcClient:
    def __init__(self, url: str):
        client = RPCClient(
            JSONRPCProtocol(),
            HttpPostClientTransport(url)
        )
        self.remote_server: RPCProxy = client.get_proxy()

    def __getattr__(self, name: str) -> Callable:
        return self.remote_server.__getattr__(name)
