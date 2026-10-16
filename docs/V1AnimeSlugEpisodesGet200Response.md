# V1AnimeSlugEpisodesGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**anime** | [**V1AnimeSlugEpisodesGet200ResponseAnime**](V1AnimeSlugEpisodesGet200ResponseAnime.md) |  | 
**data** | [**List[V1AnimeSlugEpisodesGet200ResponseDataInner]**](V1AnimeSlugEpisodesGet200ResponseDataInner.md) |  | 
**pagination** | [**V1AnimeGet200ResponsePagination**](V1AnimeGet200ResponsePagination.md) |  | 

## Example

```python
from shionstream_sdk.models.v1_anime_slug_episodes_get200_response import V1AnimeSlugEpisodesGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1AnimeSlugEpisodesGet200Response from a JSON string
v1_anime_slug_episodes_get200_response_instance = V1AnimeSlugEpisodesGet200Response.from_json(json)
# print the JSON string representation of the object
print(V1AnimeSlugEpisodesGet200Response.to_json())

# convert the object into a dict
v1_anime_slug_episodes_get200_response_dict = v1_anime_slug_episodes_get200_response_instance.to_dict()
# create an instance of V1AnimeSlugEpisodesGet200Response from a dict
v1_anime_slug_episodes_get200_response_from_dict = V1AnimeSlugEpisodesGet200Response.from_dict(v1_anime_slug_episodes_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


