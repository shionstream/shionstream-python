# V1AnimeGet200ResponseDataInner


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

## Example

```python
from shionstream_sdk.models.v1_anime_get200_response_data_inner import V1AnimeGet200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1AnimeGet200ResponseDataInner from a JSON string
v1_anime_get200_response_data_inner_instance = V1AnimeGet200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(V1AnimeGet200ResponseDataInner.to_json())

# convert the object into a dict
v1_anime_get200_response_data_inner_dict = v1_anime_get200_response_data_inner_instance.to_dict()
# create an instance of V1AnimeGet200ResponseDataInner from a dict
v1_anime_get200_response_data_inner_from_dict = V1AnimeGet200ResponseDataInner.from_dict(v1_anime_get200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


