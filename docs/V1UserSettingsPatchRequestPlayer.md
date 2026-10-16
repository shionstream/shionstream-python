# V1UserSettingsPatchRequestPlayer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_quality** | **str** |  | [optional] 
**default_subtitle** | **str** |  | [optional] 
**auto_play_next** | **bool** |  | [optional] 
**auto_skip_intro** | **bool** |  | [optional] 
**preferred_audio** | **str** |  | [optional] 

## Example

```python
from shionstream_sdk.models.v1_user_settings_patch_request_player import V1UserSettingsPatchRequestPlayer

# TODO update the JSON string below
json = "{}"
# create an instance of V1UserSettingsPatchRequestPlayer from a JSON string
v1_user_settings_patch_request_player_instance = V1UserSettingsPatchRequestPlayer.from_json(json)
# print the JSON string representation of the object
print(V1UserSettingsPatchRequestPlayer.to_json())

# convert the object into a dict
v1_user_settings_patch_request_player_dict = v1_user_settings_patch_request_player_instance.to_dict()
# create an instance of V1UserSettingsPatchRequestPlayer from a dict
v1_user_settings_patch_request_player_from_dict = V1UserSettingsPatchRequestPlayer.from_dict(v1_user_settings_patch_request_player_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


