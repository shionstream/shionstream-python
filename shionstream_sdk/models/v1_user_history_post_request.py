# coding: utf-8

"""
    ShionStream API

    Modular anime streaming and metadata API built with Hono on Cloudflare Workers.

    The version of the OpenAPI document: 1.0.0
    Author: ShionStream Engineering Team
    Contact: dev@gox.my.id
    Website: https://gox.my.id

    Generated for ShionStream API SDK.
    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class V1UserHistoryPostRequest(BaseModel):
    """
    V1UserHistoryPostRequest
    """ # noqa: E501
    anime_id: Annotated[str, Field(min_length=1, strict=True)] = Field(alias="animeId")
    episode_id: Annotated[str, Field(min_length=1, strict=True)] = Field(alias="episodeId")
    episode_number: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="episodeNumber")
    progress_percent: Optional[Union[Annotated[float, Field(le=100, strict=True, ge=0)], Annotated[int, Field(le=100, strict=True, ge=0)]]] = Field(default=0, alias="progressPercent")
    duration_seconds: Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=0, alias="durationSeconds")
    progress_seconds: Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=0, alias="progressSeconds")
    __properties: ClassVar[List[str]] = ["animeId", "episodeId", "episodeNumber", "progressPercent", "durationSeconds", "progressSeconds"]

    model_config = ConfigDict(
        validate_by_name=True,
        validate_by_alias=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(to_jsonable_python(self.to_dict()))

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of V1UserHistoryPostRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1UserHistoryPostRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "animeId": obj.get("animeId"),
            "episodeId": obj.get("episodeId"),
            "episodeNumber": obj.get("episodeNumber"),
            "progressPercent": obj.get("progressPercent") if obj.get("progressPercent") is not None else 0,
            "durationSeconds": obj.get("durationSeconds") if obj.get("durationSeconds") is not None else 0,
            "progressSeconds": obj.get("progressSeconds") if obj.get("progressSeconds") is not None else 0
        })
        return _obj


