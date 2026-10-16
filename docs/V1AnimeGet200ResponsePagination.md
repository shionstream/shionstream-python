# V1AnimeGet200ResponsePagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **float** |  | 
**limit** | **float** |  | 
**total** | **float** |  | 
**total_pages** | **float** |  | 

## Example

```python
from shionstream_sdk.models.v1_anime_get200_response_pagination import V1AnimeGet200ResponsePagination

# TODO update the JSON string below
json = "{}"
# create an instance of V1AnimeGet200ResponsePagination from a JSON string
v1_anime_get200_response_pagination_instance = V1AnimeGet200ResponsePagination.from_json(json)
# print the JSON string representation of the object
print(V1AnimeGet200ResponsePagination.to_json())

# convert the object into a dict
v1_anime_get200_response_pagination_dict = v1_anime_get200_response_pagination_instance.to_dict()
# create an instance of V1AnimeGet200ResponsePagination from a dict
v1_anime_get200_response_pagination_from_dict = V1AnimeGet200ResponsePagination.from_dict(v1_anime_get200_response_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


