# Python Imports
from typing import Optional
# Framework Imports
# Third-Party Imports
# Project Imports
from core import StringWakuModel, DictWakuModel


class WakuVersionResponse(StringWakuModel):
    pass


class WakuInfoResponse(DictWakuModel):
    listenAddresses: list[str]
    enrUri: Optional[str]
