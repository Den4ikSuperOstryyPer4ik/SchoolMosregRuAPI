from enum import Enum
import json
import typing
from pydantic import BaseModel


class Type(BaseModel):
    @staticmethod
    def default(type: "Type"):
        return {
            "_": type.__class__.__name__,
            **{
                attr: getattr(type, attr)
                for attr in filter(lambda x: not x.startswith("_"), type.__dict__)
                if getattr(type, attr) is not None
            }
        }

    def __str__(self) -> str:
        return json.dumps(
            self,
            indent=4,
            default=Type.default,
            ensure_ascii=False
        )
