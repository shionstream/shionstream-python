# V1DashboardSeasonsGet200ResponseSeasonsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**year** | **float** |  | 
**quarter** | **str** |  | 
**name** | **str** |  | 
**total_anime** | **float** |  | 
**is_current** | **bool** |  | 
**is_active** | **bool** |  | 

## Example

```python
from shionstream_sdk.models.v1_dashboard_seasons_get200_response_seasons_inner import V1DashboardSeasonsGet200ResponseSeasonsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1DashboardSeasonsGet200ResponseSeasonsInner from a JSON string
v1_dashboard_seasons_get200_response_seasons_inner_instance = V1DashboardSeasonsGet200ResponseSeasonsInner.from_json(json)
# print the JSON string representation of the object
print(V1DashboardSeasonsGet200ResponseSeasonsInner.to_json())

# convert the object into a dict
v1_dashboard_seasons_get200_response_seasons_inner_dict = v1_dashboard_seasons_get200_response_seasons_inner_instance.to_dict()
# create an instance of V1DashboardSeasonsGet200ResponseSeasonsInner from a dict
v1_dashboard_seasons_get200_response_seasons_inner_from_dict = V1DashboardSeasonsGet200ResponseSeasonsInner.from_dict(v1_dashboard_seasons_get200_response_seasons_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


