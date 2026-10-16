# V1DashboardUsersGet200ResponseUsersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**email** | **str** |  | 
**image** | **str** |  | [optional] 
**role** | **str** |  | 
**email_verified** | **bool** |  | 
**created_at** | **str** |  | 

## Example

```python
from shionstream_sdk.models.v1_dashboard_users_get200_response_users_inner import V1DashboardUsersGet200ResponseUsersInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1DashboardUsersGet200ResponseUsersInner from a JSON string
v1_dashboard_users_get200_response_users_inner_instance = V1DashboardUsersGet200ResponseUsersInner.from_json(json)
# print the JSON string representation of the object
print(V1DashboardUsersGet200ResponseUsersInner.to_json())

# convert the object into a dict
v1_dashboard_users_get200_response_users_inner_dict = v1_dashboard_users_get200_response_users_inner_instance.to_dict()
# create an instance of V1DashboardUsersGet200ResponseUsersInner from a dict
v1_dashboard_users_get200_response_users_inner_from_dict = V1DashboardUsersGet200ResponseUsersInner.from_dict(v1_dashboard_users_get200_response_users_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


