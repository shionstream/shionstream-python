# V1DashboardModerationIdPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**action** | **str** |  | [optional] [default to 'keep']

## Example

```python
from shionstream_sdk.models.v1_dashboard_moderation_id_patch_request import V1DashboardModerationIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1DashboardModerationIdPatchRequest from a JSON string
v1_dashboard_moderation_id_patch_request_instance = V1DashboardModerationIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print(V1DashboardModerationIdPatchRequest.to_json())

# convert the object into a dict
v1_dashboard_moderation_id_patch_request_dict = v1_dashboard_moderation_id_patch_request_instance.to_dict()
# create an instance of V1DashboardModerationIdPatchRequest from a dict
v1_dashboard_moderation_id_patch_request_from_dict = V1DashboardModerationIdPatchRequest.from_dict(v1_dashboard_moderation_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


