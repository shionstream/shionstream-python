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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class V1CommentsPostRequest(BaseModel):
    """
    V1CommentsPostRequest
    """ # noqa: E501
    anime_id: Annotated[str, Field(min_length=1, strict=True)] = Field(alias="animeId")
    episode_id: Annotated[str, Field(min_length=1, strict=True)] = Field(alias="episodeId")
    content: Annotated[str, Field(min_length=1, strict=True, max_length=2000)]
    parent_id: Optional[StrictStr] = Field(default=None, alias="parentId")
    is_spoiler: Optional[StrictBool] = Field(default=False, alias="isSpoiler")
    guest_name: Optional[StrictStr] = Field(default=None, alias="guestName")
    guest_email: Optional[StrictStr] = Field(default=None, alias="guestEmail")
    __properties: ClassVar[List[str]] = ["animeId", "episodeId", "content", "parentId", "isSpoiler", "guestName", "guestEmail"]

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
        """Create an instance of V1CommentsPostRequest from a JSON string"""
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
        """Create an instance of V1CommentsPostRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "animeId": obj.get("animeId"),
            "episodeId": obj.get("episodeId"),
            "content": obj.get("content"),
            "parentId": obj.get("parentId"),
            "isSpoiler": obj.get("isSpoiler") if obj.get("isSpoiler") is not None else False,
            "guestName": obj.get("guestName"),
            "guestEmail": obj.get("guestEmail")
        })
        return _obj


