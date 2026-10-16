# V1AnimeSlugEpisodesGet200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**number** | **float** |  | 
**title** | **str** |  | 
**duration_seconds** | **float** |  | 
**thumbnail** | **str** |  | [optional] 
**air_date** | **str** |  | [optional] 
**status** | **str** |  | 
**views_count** | **float** |  | 
**is_vip** | **bool** |  | 
**created_at** | **str** |  | 

## Example

```python
from shionstream_sdk.models.v1_anime_slug_episodes_get200_response_data_inner import V1AnimeSlugEpisodesGet200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1AnimeSlugEpisodesGet200ResponseDataInner from a JSON string
v1_anime_slug_episodes_get200_response_data_inner_instance = V1AnimeSlugEpisodesGet200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(V1AnimeSlugEpisodesGet200ResponseDataInner.to_json())

# convert the object into a dict
v1_anime_slug_episodes_get200_response_data_inner_dict = v1_anime_slug_episodes_get200_response_data_inner_instance.to_dict()
# create an instance of V1AnimeSlugEpisodesGet200ResponseDataInner from a dict
v1_anime_slug_episodes_get200_response_data_inner_from_dict = V1AnimeSlugEpisodesGet200ResponseDataInner.from_dict(v1_anime_slug_episodes_get200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


