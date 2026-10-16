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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from shionstream_sdk.models.v1_dashboard_categories_get200_response_categories_inner import V1DashboardCategoriesGet200ResponseCategoriesInner
from shionstream_sdk.models.v1_dashboard_categories_get200_response_genres_inner import V1DashboardCategoriesGet200ResponseGenresInner
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class V1DashboardCategoriesGet200Response(BaseModel):
    """
    V1DashboardCategoriesGet200Response
    """ # noqa: E501
    categories: List[V1DashboardCategoriesGet200ResponseCategoriesInner]
    genres: List[V1DashboardCategoriesGet200ResponseGenresInner]
    __properties: ClassVar[List[str]] = ["categories", "genres"]

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
        """Create an instance of V1DashboardCategoriesGet200Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in categories (list)
        _items = []
        if self.categories:
            for _item_categories in self.categories:
                _items.append(_item_categories.to_dict() if _item_categories is not None else None)
            _dict['categories'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in genres (list)
        _items = []
        if self.genres:
            for _item_genres in self.genres:
                _items.append(_item_genres.to_dict() if _item_genres is not None else None)
            _dict['genres'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1DashboardCategoriesGet200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "categories": [V1DashboardCategoriesGet200ResponseCategoriesInner.from_dict(_item) for _item in obj["categories"]] if obj.get("categories") is not None else None,
            "genres": [V1DashboardCategoriesGet200ResponseGenresInner.from_dict(_item) for _item in obj["genres"]] if obj.get("genres") is not None else None
        })
        return _obj


