# Python Imports
from typing import TypeVar, Type, Any
# Framework Imports
# Third-Party Imports
# Project Imports
from pydantic import BaseModel


_T = TypeVar("_T", bound="BaseModel")


class BaseWakuModel(BaseModel):
    pass


class StringWakuModel(BaseWakuModel):
    value: str

    def __init__(__pydantic_self__, value: Any) -> None:
        super().__init__(value=value)


class DictWakuModel(BaseWakuModel):
    @classmethod
    def from_dict(cls: Type[_T], d: dict) -> _T:
        return cls(**d)
