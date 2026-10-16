# V1DashboardEpisodesGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**episodes** | **List[object]** |  | 
**total** | **float** |  | 
**page** | **float** |  | 
**limit** | **float** |  | 

## Example

```python
from shionstream_sdk.models.v1_dashboard_episodes_get200_response import V1DashboardEpisodesGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1DashboardEpisodesGet200Response from a JSON string
v1_dashboard_episodes_get200_response_instance = V1DashboardEpisodesGet200Response.from_json(json)
# print the JSON string representation of the object
print(V1DashboardEpisodesGet200Response.to_json())

# convert the object into a dict
v1_dashboard_episodes_get200_response_dict = v1_dashboard_episodes_get200_response_instance.to_dict()
# create an instance of V1DashboardEpisodesGet200Response from a dict
v1_dashboard_episodes_get200_response_from_dict = V1DashboardEpisodesGet200Response.from_dict(v1_dashboard_episodes_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


