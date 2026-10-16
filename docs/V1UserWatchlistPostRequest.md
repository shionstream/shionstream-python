# V1UserWatchlistPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anime_id** | **str** |  | 
**status** | **str** |  | [optional] [default to 'plan_to_watch']

## Example

```python
from shionstream_sdk.models.v1_user_watchlist_post_request import V1UserWatchlistPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1UserWatchlistPostRequest from a JSON string
v1_user_watchlist_post_request_instance = V1UserWatchlistPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1UserWatchlistPostRequest.to_json())

# convert the object into a dict
v1_user_watchlist_post_request_dict = v1_user_watchlist_post_request_instance.to_dict()
# create an instance of V1UserWatchlistPostRequest from a dict
v1_user_watchlist_post_request_from_dict = V1UserWatchlistPostRequest.from_dict(v1_user_watchlist_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


