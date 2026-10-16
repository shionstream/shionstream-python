# V1EpisodesIdStreamGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**episode** | [**V1EpisodesIdStreamGet200ResponseEpisode**](V1EpisodesIdStreamGet200ResponseEpisode.md) |  | 
**sources** | [**List[V1EpisodesIdStreamGet200ResponseSourcesInner]**](V1EpisodesIdStreamGet200ResponseSourcesInner.md) |  | 
**subtitles** | [**List[V1EpisodesIdStreamGet200ResponseSubtitlesInner]**](V1EpisodesIdStreamGet200ResponseSubtitlesInner.md) |  | 
**audio** | [**List[V1EpisodesIdStreamGet200ResponseAudioInner]**](V1EpisodesIdStreamGet200ResponseAudioInner.md) |  | 

## Example

```python
from shionstream_sdk.models.v1_episodes_id_stream_get200_response import V1EpisodesIdStreamGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1EpisodesIdStreamGet200Response from a JSON string
v1_episodes_id_stream_get200_response_instance = V1EpisodesIdStreamGet200Response.from_json(json)
# print the JSON string representation of the object
print(V1EpisodesIdStreamGet200Response.to_json())

# convert the object into a dict
v1_episodes_id_stream_get200_response_dict = v1_episodes_id_stream_get200_response_instance.to_dict()
# create an instance of V1EpisodesIdStreamGet200Response from a dict
v1_episodes_id_stream_get200_response_from_dict = V1EpisodesIdStreamGet200Response.from_dict(v1_episodes_id_stream_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


