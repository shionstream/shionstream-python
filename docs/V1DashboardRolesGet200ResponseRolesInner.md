# V1DashboardRolesGet200ResponseRolesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**slug** | **str** |  | 
**description** | **str** |  | 
**member_count** | **float** |  | 
**permissions** | **List[str]** |  | 
**is_default** | **bool** |  | [optional] 

## Example

```python
from shionstream_sdk.models.v1_dashboard_roles_get200_response_roles_inner import V1DashboardRolesGet200ResponseRolesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1DashboardRolesGet200ResponseRolesInner from a JSON string
v1_dashboard_roles_get200_response_roles_inner_instance = V1DashboardRolesGet200ResponseRolesInner.from_json(json)
# print the JSON string representation of the object
print(V1DashboardRolesGet200ResponseRolesInner.to_json())

# convert the object into a dict
v1_dashboard_roles_get200_response_roles_inner_dict = v1_dashboard_roles_get200_response_roles_inner_instance.to_dict()
# create an instance of V1DashboardRolesGet200ResponseRolesInner from a dict
v1_dashboard_roles_get200_response_roles_inner_from_dict = V1DashboardRolesGet200ResponseRolesInner.from_dict(v1_dashboard_roles_get200_response_roles_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


