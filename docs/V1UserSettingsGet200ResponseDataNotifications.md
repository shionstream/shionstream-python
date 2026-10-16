# V1UserSettingsGet200ResponseDataNotifications


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_episode_alerts** | **bool** |  | 
**watchlist_updates** | **bool** |  | 
**marketing_emails** | **bool** |  | 
**public_watchlist** | **bool** |  | 

## Example

```python
from shionstream_sdk.models.v1_user_settings_get200_response_data_notifications import V1UserSettingsGet200ResponseDataNotifications

# TODO update the JSON string below
json = "{}"
# create an instance of V1UserSettingsGet200ResponseDataNotifications from a JSON string
v1_user_settings_get200_response_data_notifications_instance = V1UserSettingsGet200ResponseDataNotifications.from_json(json)
# print the JSON string representation of the object
print(V1UserSettingsGet200ResponseDataNotifications.to_json())

# convert the object into a dict
v1_user_settings_get200_response_data_notifications_dict = v1_user_settings_get200_response_data_notifications_instance.to_dict()
# create an instance of V1UserSettingsGet200ResponseDataNotifications from a dict
v1_user_settings_get200_response_data_notifications_from_dict = V1UserSettingsGet200ResponseDataNotifications.from_dict(v1_user_settings_get200_response_data_notifications_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


