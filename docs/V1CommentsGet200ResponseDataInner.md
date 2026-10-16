# V1CommentsGet200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**anime_id** | **str** |  | 
**episode_id** | **str** |  | 
**user_id** | **str** |  | [optional] 
**guest_name** | **str** |  | [optional] 
**parent_id** | **str** |  | [optional] 
**content** | **str** |  | 
**is_spoiler** | **bool** |  | 
**created_at** | **str** |  | 
**updated_at** | **str** |  | 
**likes** | **float** |  | 
**dislikes** | **float** |  | 

## Example

```python
from shionstream_sdk.models.v1_comments_get200_response_data_inner import V1CommentsGet200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1CommentsGet200ResponseDataInner from a JSON string
v1_comments_get200_response_data_inner_instance = V1CommentsGet200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(V1CommentsGet200ResponseDataInner.to_json())

# convert the object into a dict
v1_comments_get200_response_data_inner_dict = v1_comments_get200_response_data_inner_instance.to_dict()
# create an instance of V1CommentsGet200ResponseDataInner from a dict
v1_comments_get200_response_data_inner_from_dict = V1CommentsGet200ResponseDataInner.from_dict(v1_comments_get200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


