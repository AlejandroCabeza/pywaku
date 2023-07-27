# Python Imports
from typing import Optional, Any, TypeVar, Type
# Framework Imports
# Third-Party Imports
from pydantic import BaseModel
# Project Imports


_T = TypeVar("_T", bound="BaseModel")


class BaseResponse(BaseModel):
    pass


class StringResponse(BaseResponse):
    value: str

    def __init__(__pydantic_self__, value: Any) -> None:
        super().__init__(value=value)


class WakuVersionResponse(StringResponse):
    pass


class DictResponse(BaseResponse):
    @classmethod
    def from_dict(cls: Type[_T], d: dict) -> _T:
        return cls(**d)


class WakuInfoResponse(DictResponse):
    listenAddresses: list[str]
    enrUri: Optional[str]
