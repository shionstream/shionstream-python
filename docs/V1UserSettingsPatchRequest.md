# V1UserSettingsPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | [**V1UserSettingsPatchRequestProfile**](V1UserSettingsPatchRequestProfile.md) |  | [optional] 
**player** | [**V1UserSettingsPatchRequestPlayer**](V1UserSettingsPatchRequestPlayer.md) |  | [optional] 
**notifications** | [**V1UserSettingsPatchRequestNotifications**](V1UserSettingsPatchRequestNotifications.md) |  | [optional] 

## Example

```python
from shionstream_sdk.models.v1_user_settings_patch_request import V1UserSettingsPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1UserSettingsPatchRequest from a JSON string
v1_user_settings_patch_request_instance = V1UserSettingsPatchRequest.from_json(json)
# print the JSON string representation of the object
print(V1UserSettingsPatchRequest.to_json())

# convert the object into a dict
v1_user_settings_patch_request_dict = v1_user_settings_patch_request_instance.to_dict()
# create an instance of V1UserSettingsPatchRequest from a dict
v1_user_settings_patch_request_from_dict = V1UserSettingsPatchRequest.from_dict(v1_user_settings_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


