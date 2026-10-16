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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from shionstream_sdk.models.v1_dashboard_overview_get200_response_notifications_inner import V1DashboardOverviewGet200ResponseNotificationsInner
from shionstream_sdk.models.v1_dashboard_overview_get200_response_recent_activities_inner import V1DashboardOverviewGet200ResponseRecentActivitiesInner
from shionstream_sdk.models.v1_dashboard_overview_get200_response_traffic_data_inner import V1DashboardOverviewGet200ResponseTrafficDataInner
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class V1DashboardOverviewGet200Response(BaseModel):
    """
    V1DashboardOverviewGet200Response
    """ # noqa: E501
    traffic_data: List[V1DashboardOverviewGet200ResponseTrafficDataInner] = Field(alias="trafficData")
    recent_activities: List[V1DashboardOverviewGet200ResponseRecentActivitiesInner] = Field(alias="recentActivities")
    notifications: List[V1DashboardOverviewGet200ResponseNotificationsInner]
    __properties: ClassVar[List[str]] = ["trafficData", "recentActivities", "notifications"]

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
        """Create an instance of V1DashboardOverviewGet200Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in traffic_data (list)
        _items = []
        if self.traffic_data:
            for _item_traffic_data in self.traffic_data:
                _items.append(_item_traffic_data.to_dict() if _item_traffic_data is not None else None)
            _dict['trafficData'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in recent_activities (list)
        _items = []
        if self.recent_activities:
            for _item_recent_activities in self.recent_activities:
                _items.append(_item_recent_activities.to_dict() if _item_recent_activities is not None else None)
            _dict['recentActivities'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in notifications (list)
        _items = []
        if self.notifications:
            for _item_notifications in self.notifications:
                _items.append(_item_notifications.to_dict() if _item_notifications is not None else None)
            _dict['notifications'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1DashboardOverviewGet200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "trafficData": [V1DashboardOverviewGet200ResponseTrafficDataInner.from_dict(_item) for _item in obj["trafficData"]] if obj.get("trafficData") is not None else None,
            "recentActivities": [V1DashboardOverviewGet200ResponseRecentActivitiesInner.from_dict(_item) for _item in obj["recentActivities"]] if obj.get("recentActivities") is not None else None,
            "notifications": [V1DashboardOverviewGet200ResponseNotificationsInner.from_dict(_item) for _item in obj["notifications"]] if obj.get("notifications") is not None else None
        })
        return _obj


