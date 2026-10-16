# V1UserSettingsGet200ResponseDataPlayer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_quality** | **str** |  | 
**default_subtitle** | **str** |  | 
**auto_play_next** | **bool** |  | 
**auto_skip_intro** | **bool** |  | 
**preferred_audio** | **str** |  | 

## Example

```python
from shionstream_sdk.models.v1_user_settings_get200_response_data_player import V1UserSettingsGet200ResponseDataPlayer

# TODO update the JSON string below
json = "{}"
# create an instance of V1UserSettingsGet200ResponseDataPlayer from a JSON string
v1_user_settings_get200_response_data_player_instance = V1UserSettingsGet200ResponseDataPlayer.from_json(json)
# print the JSON string representation of the object
print(V1UserSettingsGet200ResponseDataPlayer.to_json())

# convert the object into a dict
v1_user_settings_get200_response_data_player_dict = v1_user_settings_get200_response_data_player_instance.to_dict()
# create an instance of V1UserSettingsGet200ResponseDataPlayer from a dict
v1_user_settings_get200_response_data_player_from_dict = V1UserSettingsGet200ResponseDataPlayer.from_dict(v1_user_settings_get200_response_data_player_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


