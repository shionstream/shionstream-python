# V1CommentsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anime_id** | **str** |  | 
**episode_id** | **str** |  | 
**content** | **str** |  | 
**parent_id** | **str** |  | [optional] 
**is_spoiler** | **bool** |  | [optional] [default to False]
**guest_name** | **str** |  | [optional] 
**guest_email** | **str** |  | [optional] 

## Example

```python
from shionstream_sdk.models.v1_comments_post_request import V1CommentsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1CommentsPostRequest from a JSON string
v1_comments_post_request_instance = V1CommentsPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1CommentsPostRequest.to_json())

# convert the object into a dict
v1_comments_post_request_dict = v1_comments_post_request_instance.to_dict()
# create an instance of V1CommentsPostRequest from a dict
v1_comments_post_request_from_dict = V1CommentsPostRequest.from_dict(v1_comments_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


