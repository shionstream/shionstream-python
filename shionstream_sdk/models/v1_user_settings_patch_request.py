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
from typing import Any, ClassVar, Dict, List, Optional
from shionstream_sdk.models.v1_user_settings_patch_request_notifications import V1UserSettingsPatchRequestNotifications
from shionstream_sdk.models.v1_user_settings_patch_request_player import V1UserSettingsPatchRequestPlayer
from shionstream_sdk.models.v1_user_settings_patch_request_profile import V1UserSettingsPatchRequestProfile
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class V1UserSettingsPatchRequest(BaseModel):
    """
    V1UserSettingsPatchRequest
    """ # noqa: E501
    profile: Optional[V1UserSettingsPatchRequestProfile] = None
    player: Optional[V1UserSettingsPatchRequestPlayer] = None
    notifications: Optional[V1UserSettingsPatchRequestNotifications] = None
    __properties: ClassVar[List[str]] = ["profile", "player", "notifications"]

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
        """Create an instance of V1UserSettingsPatchRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of profile
        if self.profile:
            _dict['profile'] = self.profile.to_dict()
        # override the default output from pydantic by calling `to_dict()` of player
        if self.player:
            _dict['player'] = self.player.to_dict()
        # override the default output from pydantic by calling `to_dict()` of notifications
        if self.notifications:
            _dict['notifications'] = self.notifications.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1UserSettingsPatchRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "profile": V1UserSettingsPatchRequestProfile.from_dict(obj["profile"]) if obj.get("profile") is not None else None,
            "player": V1UserSettingsPatchRequestPlayer.from_dict(obj["player"]) if obj.get("player") is not None else None,
            "notifications": V1UserSettingsPatchRequestNotifications.from_dict(obj["notifications"]) if obj.get("notifications") is not None else None
        })
        return _obj


