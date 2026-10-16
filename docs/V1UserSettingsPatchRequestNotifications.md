# V1UserSettingsPatchRequestNotifications


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_episode_alerts** | **bool** |  | [optional] 
**watchlist_updates** | **bool** |  | [optional] 
**marketing_emails** | **bool** |  | [optional] 
**public_watchlist** | **bool** |  | [optional] 

## Example

```python
from shionstream_sdk.models.v1_user_settings_patch_request_notifications import V1UserSettingsPatchRequestNotifications

# TODO update the JSON string below
json = "{}"
# create an instance of V1UserSettingsPatchRequestNotifications from a JSON string
v1_user_settings_patch_request_notifications_instance = V1UserSettingsPatchRequestNotifications.from_json(json)
# print the JSON string representation of the object
print(V1UserSettingsPatchRequestNotifications.to_json())

# convert the object into a dict
v1_user_settings_patch_request_notifications_dict = v1_user_settings_patch_request_notifications_instance.to_dict()
# create an instance of V1UserSettingsPatchRequestNotifications from a dict
v1_user_settings_patch_request_notifications_from_dict = V1UserSettingsPatchRequestNotifications.from_dict(v1_user_settings_patch_request_notifications_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


