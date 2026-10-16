# V1EpisodesIdStreamGet200ResponseSourcesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**server_name** | **str** |  | [optional] 
**stream_url** | **str** |  | 
**format** | **str** |  | 
**quality** | **str** |  | 
**url1080p** | **str** |  | [optional] 
**url720p** | **str** |  | [optional] 
**url480p** | **str** |  | [optional] 
**url360p** | **str** |  | [optional] 
**is_primary** | **bool** |  | 

## Example

```python
from shionstream_sdk.models.v1_episodes_id_stream_get200_response_sources_inner import V1EpisodesIdStreamGet200ResponseSourcesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1EpisodesIdStreamGet200ResponseSourcesInner from a JSON string
v1_episodes_id_stream_get200_response_sources_inner_instance = V1EpisodesIdStreamGet200ResponseSourcesInner.from_json(json)
# print the JSON string representation of the object
print(V1EpisodesIdStreamGet200ResponseSourcesInner.to_json())

# convert the object into a dict
v1_episodes_id_stream_get200_response_sources_inner_dict = v1_episodes_id_stream_get200_response_sources_inner_instance.to_dict()
# create an instance of V1EpisodesIdStreamGet200ResponseSourcesInner from a dict
v1_episodes_id_stream_get200_response_sources_inner_from_dict = V1EpisodesIdStreamGet200ResponseSourcesInner.from_dict(v1_episodes_id_stream_get200_response_sources_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


