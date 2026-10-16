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
from typing import Any, ClassVar, Dict, List, Union
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class V1DashboardStatsGet200ResponseStats(BaseModel):
    """
    V1DashboardStatsGet200ResponseStats
    """ # noqa: E501
    total_anime: Union[StrictFloat, StrictInt] = Field(alias="totalAnime")
    total_episodes: Union[StrictFloat, StrictInt] = Field(alias="totalEpisodes")
    total_users: Union[StrictFloat, StrictInt] = Field(alias="totalUsers")
    pending_reports: Union[StrictFloat, StrictInt] = Field(alias="pendingReports")
    active_streams: Union[StrictFloat, StrictInt] = Field(alias="activeStreams")
    bandwidth_usage_gb: Union[StrictFloat, StrictInt] = Field(alias="bandwidthUsageGb")
    cpu_load_percent: Union[StrictFloat, StrictInt] = Field(alias="cpuLoadPercent")
    storage_used_gb: Union[StrictFloat, StrictInt] = Field(alias="storageUsedGb")
    monthly_growth_percent: Union[StrictFloat, StrictInt] = Field(alias="monthlyGrowthPercent")
    __properties: ClassVar[List[str]] = ["totalAnime", "totalEpisodes", "totalUsers", "pendingReports", "activeStreams", "bandwidthUsageGb", "cpuLoadPercent", "storageUsedGb", "monthlyGrowthPercent"]

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
        """Create an instance of V1DashboardStatsGet200ResponseStats from a JSON string"""
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
        """Create an instance of V1DashboardStatsGet200ResponseStats from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "totalAnime": obj.get("totalAnime"),
            "totalEpisodes": obj.get("totalEpisodes"),
            "totalUsers": obj.get("totalUsers"),
            "pendingReports": obj.get("pendingReports"),
            "activeStreams": obj.get("activeStreams"),
            "bandwidthUsageGb": obj.get("bandwidthUsageGb"),
            "cpuLoadPercent": obj.get("cpuLoadPercent"),
            "storageUsedGb": obj.get("storageUsedGb"),
            "monthlyGrowthPercent": obj.get("monthlyGrowthPercent")
        })
        return _obj


