# V1DashboardCategoriesGet200ResponseCategoriesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**code** | **str** |  | 
**name** | **str** |  | 
**slug** | **str** |  | 
**anime_count** | **float** |  | 
**description** | **str** |  | 
**is_active** | **bool** |  | 
**updated_at** | **str** |  | 

## Example

```python
from shionstream_sdk.models.v1_dashboard_categories_get200_response_categories_inner import V1DashboardCategoriesGet200ResponseCategoriesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1DashboardCategoriesGet200ResponseCategoriesInner from a JSON string
v1_dashboard_categories_get200_response_categories_inner_instance = V1DashboardCategoriesGet200ResponseCategoriesInner.from_json(json)
# print the JSON string representation of the object
print(V1DashboardCategoriesGet200ResponseCategoriesInner.to_json())

# convert the object into a dict
v1_dashboard_categories_get200_response_categories_inner_dict = v1_dashboard_categories_get200_response_categories_inner_instance.to_dict()
# create an instance of V1DashboardCategoriesGet200ResponseCategoriesInner from a dict
v1_dashboard_categories_get200_response_categories_inner_from_dict = V1DashboardCategoriesGet200ResponseCategoriesInner.from_dict(v1_dashboard_categories_get200_response_categories_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


