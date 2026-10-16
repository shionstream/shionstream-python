# V1DashboardCategoriesGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | [**List[V1DashboardCategoriesGet200ResponseCategoriesInner]**](V1DashboardCategoriesGet200ResponseCategoriesInner.md) |  | 
**genres** | [**List[V1DashboardCategoriesGet200ResponseGenresInner]**](V1DashboardCategoriesGet200ResponseGenresInner.md) |  | 

## Example

```python
from shionstream_sdk.models.v1_dashboard_categories_get200_response import V1DashboardCategoriesGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1DashboardCategoriesGet200Response from a JSON string
v1_dashboard_categories_get200_response_instance = V1DashboardCategoriesGet200Response.from_json(json)
# print the JSON string representation of the object
print(V1DashboardCategoriesGet200Response.to_json())

# convert the object into a dict
v1_dashboard_categories_get200_response_dict = v1_dashboard_categories_get200_response_instance.to_dict()
# create an instance of V1DashboardCategoriesGet200Response from a dict
v1_dashboard_categories_get200_response_from_dict = V1DashboardCategoriesGet200Response.from_dict(v1_dashboard_categories_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


