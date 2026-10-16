# V1UserSettingsGet200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**player** | [**V1UserSettingsGet200ResponseDataPlayer**](V1UserSettingsGet200ResponseDataPlayer.md) |  | 
**notifications** | [**V1UserSettingsGet200ResponseDataNotifications**](V1UserSettingsGet200ResponseDataNotifications.md) |  | 

## Example

```python
from shionstream_sdk.models.v1_user_settings_get200_response_data import V1UserSettingsGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of V1UserSettingsGet200ResponseData from a JSON string
v1_user_settings_get200_response_data_instance = V1UserSettingsGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print(V1UserSettingsGet200ResponseData.to_json())

# convert the object into a dict
v1_user_settings_get200_response_data_dict = v1_user_settings_get200_response_data_instance.to_dict()
# create an instance of V1UserSettingsGet200ResponseData from a dict
v1_user_settings_get200_response_data_from_dict = V1UserSettingsGet200ResponseData.from_dict(v1_user_settings_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


