# V1DashboardStatsGet200ResponseStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_anime** | **float** |  | 
**total_episodes** | **float** |  | 
**total_users** | **float** |  | 
**pending_reports** | **float** |  | 
**active_streams** | **float** |  | 
**bandwidth_usage_gb** | **float** |  | 
**cpu_load_percent** | **float** |  | 
**storage_used_gb** | **float** |  | 
**monthly_growth_percent** | **float** |  | 

## Example

```python
from shionstream_sdk.models.v1_dashboard_stats_get200_response_stats import V1DashboardStatsGet200ResponseStats

# TODO update the JSON string below
json = "{}"
# create an instance of V1DashboardStatsGet200ResponseStats from a JSON string
v1_dashboard_stats_get200_response_stats_instance = V1DashboardStatsGet200ResponseStats.from_json(json)
# print the JSON string representation of the object
print(V1DashboardStatsGet200ResponseStats.to_json())

# convert the object into a dict
v1_dashboard_stats_get200_response_stats_dict = v1_dashboard_stats_get200_response_stats_instance.to_dict()
# create an instance of V1DashboardStatsGet200ResponseStats from a dict
v1_dashboard_stats_get200_response_stats_from_dict = V1DashboardStatsGet200ResponseStats.from_dict(v1_dashboard_stats_get200_response_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


