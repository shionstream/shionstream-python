# V1EpisodesIdStreamGet200ResponseSubtitlesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**label** | **str** |  | 
**language_code** | **str** |  | 
**file_url** | **str** |  | 
**format** | **str** |  | 
**is_default** | **bool** |  | 

## Example

```python
from shionstream_sdk.models.v1_episodes_id_stream_get200_response_subtitles_inner import V1EpisodesIdStreamGet200ResponseSubtitlesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1EpisodesIdStreamGet200ResponseSubtitlesInner from a JSON string
v1_episodes_id_stream_get200_response_subtitles_inner_instance = V1EpisodesIdStreamGet200ResponseSubtitlesInner.from_json(json)
# print the JSON string representation of the object
print(V1EpisodesIdStreamGet200ResponseSubtitlesInner.to_json())

# convert the object into a dict
v1_episodes_id_stream_get200_response_subtitles_inner_dict = v1_episodes_id_stream_get200_response_subtitles_inner_instance.to_dict()
# create an instance of V1EpisodesIdStreamGet200ResponseSubtitlesInner from a dict
v1_episodes_id_stream_get200_response_subtitles_inner_from_dict = V1EpisodesIdStreamGet200ResponseSubtitlesInner.from_dict(v1_episodes_id_stream_get200_response_subtitles_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


