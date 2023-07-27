# Python Imports
# Framework Imports
# Third-Party Imports
# Project Imports
from core import WakuRpcClient
from .responses import WakuVersionResponse, WakuInfoResponse


class DebugApi:
    def __init__(self, client: WakuRpcClient) -> None:
        self.client: WakuRpcClient = client

    def info(self) -> WakuInfoResponse:
        return WakuInfoResponse.from_dict(self.client.get_waku_v2_debug_v1_info())

    def version(self) -> WakuVersionResponse:
        return WakuVersionResponse(self.client.get_waku_v2_debug_v1_version())
