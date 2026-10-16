# V1DashboardUsersGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[V1DashboardUsersGet200ResponseUsersInner]**](V1DashboardUsersGet200ResponseUsersInner.md) |  | 
**total** | **float** |  | 
**page** | **float** |  | 
**limit** | **float** |  | 

## Example

```python
from shionstream_sdk.models.v1_dashboard_users_get200_response import V1DashboardUsersGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1DashboardUsersGet200Response from a JSON string
v1_dashboard_users_get200_response_instance = V1DashboardUsersGet200Response.from_json(json)
# print the JSON string representation of the object
print(V1DashboardUsersGet200Response.to_json())

# convert the object into a dict
v1_dashboard_users_get200_response_dict = v1_dashboard_users_get200_response_instance.to_dict()
# create an instance of V1DashboardUsersGet200Response from a dict
v1_dashboard_users_get200_response_from_dict = V1DashboardUsersGet200Response.from_dict(v1_dashboard_users_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


