# V1DashboardAnimeGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anime_list** | **List[object]** |  | 
**total** | **float** |  | 
**page** | **float** |  | 
**limit** | **float** |  | 

## Example

```python
from shionstream_sdk.models.v1_dashboard_anime_get200_response import V1DashboardAnimeGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1DashboardAnimeGet200Response from a JSON string
v1_dashboard_anime_get200_response_instance = V1DashboardAnimeGet200Response.from_json(json)
# print the JSON string representation of the object
print(V1DashboardAnimeGet200Response.to_json())

# convert the object into a dict
v1_dashboard_anime_get200_response_dict = v1_dashboard_anime_get200_response_instance.to_dict()
# create an instance of V1DashboardAnimeGet200Response from a dict
v1_dashboard_anime_get200_response_from_dict = V1DashboardAnimeGet200Response.from_dict(v1_dashboard_anime_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


