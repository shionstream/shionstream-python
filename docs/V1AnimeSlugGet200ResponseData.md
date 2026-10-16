# V1AnimeSlugGet200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**slug** | **str** |  | 
**title_romaji** | **str** |  | 
**title_english** | **str** |  | [optional] 
**title_japanese** | **str** |  | [optional] 
**synopsis** | **str** |  | [optional] 
**cover_image** | **str** |  | [optional] 
**banner_image** | **str** |  | [optional] 
**type** | **str** |  | 
**status** | **str** |  | 
**season_name** | **str** |  | [optional] 
**season_year** | **float** |  | [optional] 
**episodes_count** | **float** |  | 
**duration_per_ep** | **str** |  | [optional] 
**rating** | **float** |  | [optional] 
**is_featured** | **bool** |  | 
**is_trending** | **bool** |  | 
**sub_or_dub** | **str** |  | 
**genres** | [**List[V1AnimeSlugGet200ResponseDataGenresInner]**](V1AnimeSlugGet200ResponseDataGenresInner.md) |  | 
**studios** | [**List[V1AnimeSlugGet200ResponseDataGenresInner]**](V1AnimeSlugGet200ResponseDataGenresInner.md) |  | 
**schedule** | [**V1AnimeSlugGet200ResponseDataSchedule**](V1AnimeSlugGet200ResponseDataSchedule.md) |  | [optional] 
**trending_stats** | [**V1AnimeSlugGet200ResponseDataTrendingStats**](V1AnimeSlugGet200ResponseDataTrendingStats.md) |  | [optional] 

## Example

```python
from shionstream_sdk.models.v1_anime_slug_get200_response_data import V1AnimeSlugGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of V1AnimeSlugGet200ResponseData from a JSON string
v1_anime_slug_get200_response_data_instance = V1AnimeSlugGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print(V1AnimeSlugGet200ResponseData.to_json())

# convert the object into a dict
v1_anime_slug_get200_response_data_dict = v1_anime_slug_get200_response_data_instance.to_dict()
# create an instance of V1AnimeSlugGet200ResponseData from a dict
v1_anime_slug_get200_response_data_from_dict = V1AnimeSlugGet200ResponseData.from_dict(v1_anime_slug_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


