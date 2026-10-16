# V1DashboardOverviewGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**traffic_data** | [**List[V1DashboardOverviewGet200ResponseTrafficDataInner]**](V1DashboardOverviewGet200ResponseTrafficDataInner.md) |  | 
**recent_activities** | [**List[V1DashboardOverviewGet200ResponseRecentActivitiesInner]**](V1DashboardOverviewGet200ResponseRecentActivitiesInner.md) |  | 
**notifications** | [**List[V1DashboardOverviewGet200ResponseNotificationsInner]**](V1DashboardOverviewGet200ResponseNotificationsInner.md) |  | 

## Example

```python
from shionstream_sdk.models.v1_dashboard_overview_get200_response import V1DashboardOverviewGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1DashboardOverviewGet200Response from a JSON string
v1_dashboard_overview_get200_response_instance = V1DashboardOverviewGet200Response.from_json(json)
# print the JSON string representation of the object
print(V1DashboardOverviewGet200Response.to_json())

# convert the object into a dict
v1_dashboard_overview_get200_response_dict = v1_dashboard_overview_get200_response_instance.to_dict()
# create an instance of V1DashboardOverviewGet200Response from a dict
v1_dashboard_overview_get200_response_from_dict = V1DashboardOverviewGet200Response.from_dict(v1_dashboard_overview_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


