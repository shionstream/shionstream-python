# V1DashboardSeasonsGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seasons** | [**List[V1DashboardSeasonsGet200ResponseSeasonsInner]**](V1DashboardSeasonsGet200ResponseSeasonsInner.md) |  | 

## Example

```python
from shionstream_sdk.models.v1_dashboard_seasons_get200_response import V1DashboardSeasonsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1DashboardSeasonsGet200Response from a JSON string
v1_dashboard_seasons_get200_response_instance = V1DashboardSeasonsGet200Response.from_json(json)
# print the JSON string representation of the object
print(V1DashboardSeasonsGet200Response.to_json())

# convert the object into a dict
v1_dashboard_seasons_get200_response_dict = v1_dashboard_seasons_get200_response_instance.to_dict()
# create an instance of V1DashboardSeasonsGet200Response from a dict
v1_dashboard_seasons_get200_response_from_dict = V1DashboardSeasonsGet200Response.from_dict(v1_dashboard_seasons_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


