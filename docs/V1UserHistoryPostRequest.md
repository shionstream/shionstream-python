# V1UserHistoryPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anime_id** | **str** |  | 
**episode_id** | **str** |  | 
**episode_number** | **float** |  | [optional] 
**progress_percent** | **float** |  | [optional] [default to 0]
**duration_seconds** | **float** |  | [optional] [default to 0]
**progress_seconds** | **float** |  | [optional] [default to 0]

## Example

```python
from shionstream_sdk.models.v1_user_history_post_request import V1UserHistoryPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1UserHistoryPostRequest from a JSON string
v1_user_history_post_request_instance = V1UserHistoryPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1UserHistoryPostRequest.to_json())

# convert the object into a dict
v1_user_history_post_request_dict = v1_user_history_post_request_instance.to_dict()
# create an instance of V1UserHistoryPostRequest from a dict
v1_user_history_post_request_from_dict = V1UserHistoryPostRequest.from_dict(v1_user_history_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


