# V1UserHistoryGet200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**anime_id** | **str** |  | 
**episode_id** | **str** |  | 
**episode_number** | **float** |  | [optional] 
**progress_percent** | **float** |  | 
**duration_seconds** | **float** |  | 
**progress_seconds** | **float** |  | 
**last_watched_at** | **str** |  | 

## Example

```python
from shionstream_sdk.models.v1_user_history_get200_response_data_inner import V1UserHistoryGet200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1UserHistoryGet200ResponseDataInner from a JSON string
v1_user_history_get200_response_data_inner_instance = V1UserHistoryGet200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(V1UserHistoryGet200ResponseDataInner.to_json())

# convert the object into a dict
v1_user_history_get200_response_data_inner_dict = v1_user_history_get200_response_data_inner_instance.to_dict()
# create an instance of V1UserHistoryGet200ResponseDataInner from a dict
v1_user_history_get200_response_data_inner_from_dict = V1UserHistoryGet200ResponseDataInner.from_dict(v1_user_history_get200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


