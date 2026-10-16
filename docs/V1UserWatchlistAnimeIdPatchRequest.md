# V1UserWatchlistAnimeIdPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**is_favorite** | **bool** |  | [optional] 

## Example

```python
from shionstream_sdk.models.v1_user_watchlist_anime_id_patch_request import V1UserWatchlistAnimeIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1UserWatchlistAnimeIdPatchRequest from a JSON string
v1_user_watchlist_anime_id_patch_request_instance = V1UserWatchlistAnimeIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print(V1UserWatchlistAnimeIdPatchRequest.to_json())

# convert the object into a dict
v1_user_watchlist_anime_id_patch_request_dict = v1_user_watchlist_anime_id_patch_request_instance.to_dict()
# create an instance of V1UserWatchlistAnimeIdPatchRequest from a dict
v1_user_watchlist_anime_id_patch_request_from_dict = V1UserWatchlistAnimeIdPatchRequest.from_dict(v1_user_watchlist_anime_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


