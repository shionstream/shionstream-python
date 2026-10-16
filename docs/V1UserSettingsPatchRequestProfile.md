# V1UserSettingsPatchRequestProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | [optional] 
**bio** | **str** |  | [optional] 
**avatar_url** | **str** |  | [optional] 

## Example

```python
from shionstream_sdk.models.v1_user_settings_patch_request_profile import V1UserSettingsPatchRequestProfile

# TODO update the JSON string below
json = "{}"
# create an instance of V1UserSettingsPatchRequestProfile from a JSON string
v1_user_settings_patch_request_profile_instance = V1UserSettingsPatchRequestProfile.from_json(json)
# print the JSON string representation of the object
print(V1UserSettingsPatchRequestProfile.to_json())

# convert the object into a dict
v1_user_settings_patch_request_profile_dict = v1_user_settings_patch_request_profile_instance.to_dict()
# create an instance of V1UserSettingsPatchRequestProfile from a dict
v1_user_settings_patch_request_profile_from_dict = V1UserSettingsPatchRequestProfile.from_dict(v1_user_settings_patch_request_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


