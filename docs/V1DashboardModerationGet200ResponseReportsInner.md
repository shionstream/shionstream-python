# V1DashboardModerationGet200ResponseReportsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**comment_id** | **str** |  | 
**comment_text** | **str** |  | 
**anime_title** | **str** |  | 
**episode_number** | **float** |  | 
**author** | [**V1DashboardModerationGet200ResponseReportsInnerAuthor**](V1DashboardModerationGet200ResponseReportsInnerAuthor.md) |  | 
**reporter** | [**V1DashboardModerationGet200ResponseReportsInnerReporter**](V1DashboardModerationGet200ResponseReportsInnerReporter.md) |  | 
**reason** | **str** |  | 
**status** | **str** |  | 
**reported_at** | **str** |  | 
**flagged_by_system** | **bool** |  | 

## Example

```python
from shionstream_sdk.models.v1_dashboard_moderation_get200_response_reports_inner import V1DashboardModerationGet200ResponseReportsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1DashboardModerationGet200ResponseReportsInner from a JSON string
v1_dashboard_moderation_get200_response_reports_inner_instance = V1DashboardModerationGet200ResponseReportsInner.from_json(json)
# print the JSON string representation of the object
print(V1DashboardModerationGet200ResponseReportsInner.to_json())

# convert the object into a dict
v1_dashboard_moderation_get200_response_reports_inner_dict = v1_dashboard_moderation_get200_response_reports_inner_instance.to_dict()
# create an instance of V1DashboardModerationGet200ResponseReportsInner from a dict
v1_dashboard_moderation_get200_response_reports_inner_from_dict = V1DashboardModerationGet200ResponseReportsInner.from_dict(v1_dashboard_moderation_get200_response_reports_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


