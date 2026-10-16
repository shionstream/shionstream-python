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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from shionstream_sdk.models.v1_anime_slug_get200_response_data_genres_inner import V1AnimeSlugGet200ResponseDataGenresInner
from shionstream_sdk.models.v1_anime_slug_get200_response_data_schedule import V1AnimeSlugGet200ResponseDataSchedule
from shionstream_sdk.models.v1_anime_slug_get200_response_data_trending_stats import V1AnimeSlugGet200ResponseDataTrendingStats
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class V1AnimeSlugGet200ResponseData(BaseModel):
    """
    V1AnimeSlugGet200ResponseData
    """ # noqa: E501
    id: StrictStr
    slug: StrictStr
    title_romaji: StrictStr = Field(alias="titleRomaji")
    title_english: Optional[StrictStr] = Field(default=None, alias="titleEnglish")
    title_japanese: Optional[StrictStr] = Field(default=None, alias="titleJapanese")
    synopsis: Optional[StrictStr] = None
    cover_image: Optional[StrictStr] = Field(default=None, alias="coverImage")
    banner_image: Optional[StrictStr] = Field(default=None, alias="bannerImage")
    type: StrictStr
    status: StrictStr
    season_name: Optional[StrictStr] = Field(default=None, alias="seasonName")
    season_year: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="seasonYear")
    episodes_count: Union[StrictFloat, StrictInt] = Field(alias="episodesCount")
    duration_per_ep: Optional[StrictStr] = Field(default=None, alias="durationPerEp")
    rating: Optional[Union[StrictFloat, StrictInt]] = None
    is_featured: StrictBool = Field(alias="isFeatured")
    is_trending: StrictBool = Field(alias="isTrending")
    sub_or_dub: StrictStr = Field(alias="subOrDub")
    genres: List[V1AnimeSlugGet200ResponseDataGenresInner]
    studios: List[V1AnimeSlugGet200ResponseDataGenresInner]
    schedule: Optional[V1AnimeSlugGet200ResponseDataSchedule] = None
    trending_stats: Optional[V1AnimeSlugGet200ResponseDataTrendingStats] = Field(default=None, alias="trendingStats")
    __properties: ClassVar[List[str]] = ["id", "slug", "titleRomaji", "titleEnglish", "titleJapanese", "synopsis", "coverImage", "bannerImage", "type", "status", "seasonName", "seasonYear", "episodesCount", "durationPerEp", "rating", "isFeatured", "isTrending", "subOrDub", "genres", "studios", "schedule", "trendingStats"]

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
        """Create an instance of V1AnimeSlugGet200ResponseData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in genres (list)
        _items = []
        if self.genres:
            for _item_genres in self.genres:
                _items.append(_item_genres.to_dict() if _item_genres is not None else None)
            _dict['genres'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in studios (list)
        _items = []
        if self.studios:
            for _item_studios in self.studios:
                _items.append(_item_studios.to_dict() if _item_studios is not None else None)
            _dict['studios'] = _items
        # override the default output from pydantic by calling `to_dict()` of schedule
        if self.schedule:
            _dict['schedule'] = self.schedule.to_dict()
        # override the default output from pydantic by calling `to_dict()` of trending_stats
        if self.trending_stats:
            _dict['trendingStats'] = self.trending_stats.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1AnimeSlugGet200ResponseData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "slug": obj.get("slug"),
            "titleRomaji": obj.get("titleRomaji"),
            "titleEnglish": obj.get("titleEnglish"),
            "titleJapanese": obj.get("titleJapanese"),
            "synopsis": obj.get("synopsis"),
            "coverImage": obj.get("coverImage"),
            "bannerImage": obj.get("bannerImage"),
            "type": obj.get("type"),
            "status": obj.get("status"),
            "seasonName": obj.get("seasonName"),
            "seasonYear": obj.get("seasonYear"),
            "episodesCount": obj.get("episodesCount"),
            "durationPerEp": obj.get("durationPerEp"),
            "rating": obj.get("rating"),
            "isFeatured": obj.get("isFeatured"),
            "isTrending": obj.get("isTrending"),
            "subOrDub": obj.get("subOrDub"),
            "genres": [V1AnimeSlugGet200ResponseDataGenresInner.from_dict(_item) for _item in obj["genres"]] if obj.get("genres") is not None else None,
            "studios": [V1AnimeSlugGet200ResponseDataGenresInner.from_dict(_item) for _item in obj["studios"]] if obj.get("studios") is not None else None,
            "schedule": V1AnimeSlugGet200ResponseDataSchedule.from_dict(obj["schedule"]) if obj.get("schedule") is not None else None,
            "trendingStats": V1AnimeSlugGet200ResponseDataTrendingStats.from_dict(obj["trendingStats"]) if obj.get("trendingStats") is not None else None
        })
        return _obj


