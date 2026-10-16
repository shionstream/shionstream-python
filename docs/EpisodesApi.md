# shionstream_sdk.EpisodesApi

All URIs are relative to *https://api.gox.my.id*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_anime_slug_episodes_get**](EpisodesApi.md#v1_anime_slug_episodes_get) | **GET** /v1/anime/{slug}/episodes | List Episodes by Anime Slug
[**v1_episodes_id_stream_get**](EpisodesApi.md#v1_episodes_id_stream_get) | **GET** /v1/episodes/{id}/stream | Get Episode Stream Sources


# **v1_anime_slug_episodes_get**
> V1AnimeSlugEpisodesGet200Response v1_anime_slug_episodes_get(slug, page=page, limit=limit, sort=sort)

List Episodes by Anime Slug

Retrieve an ordered list of published episodes for a specific anime.

### Example


```python
import shionstream_sdk
from shionstream_sdk.models.v1_anime_slug_episodes_get200_response import V1AnimeSlugEpisodesGet200Response
from shionstream_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.gox.my.id
# See configuration.py for a list of all supported configuration parameters.
configuration = shionstream_sdk.Configuration(
    host = "https://api.gox.my.id"
)


# Enter a context with an instance of the API client
with shionstream_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shionstream_sdk.EpisodesApi(api_client)
    slug = 'slug_example' # str | 
    page = '1' # str |  (optional) (default to '1')
    limit = '50' # str |  (optional) (default to '50')
    sort = 'asc' # str |  (optional) (default to 'asc')

    try:
        # List Episodes by Anime Slug
        api_response = api_instance.v1_anime_slug_episodes_get(slug, page=page, limit=limit, sort=sort)
        print("The response of EpisodesApi->v1_anime_slug_episodes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EpisodesApi->v1_anime_slug_episodes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **page** | **str**|  | [optional] [default to &#39;1&#39;]
 **limit** | **str**|  | [optional] [default to &#39;50&#39;]
 **sort** | **str**|  | [optional] [default to &#39;asc&#39;]

### Return type

[**V1AnimeSlugEpisodesGet200Response**](V1AnimeSlugEpisodesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of anime episodes |  -  |
**404** | Anime not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_episodes_id_stream_get**
> V1EpisodesIdStreamGet200Response v1_episodes_id_stream_get(id)

Get Episode Stream Sources

Retrieve video playback manifests, multi-resolution URLs, subtitles, and audio tracks for an episode.

### Example


```python
import shionstream_sdk
from shionstream_sdk.models.v1_episodes_id_stream_get200_response import V1EpisodesIdStreamGet200Response
from shionstream_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.gox.my.id
# See configuration.py for a list of all supported configuration parameters.
configuration = shionstream_sdk.Configuration(
    host = "https://api.gox.my.id"
)


# Enter a context with an instance of the API client
with shionstream_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shionstream_sdk.EpisodesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Episode Stream Sources
        api_response = api_instance.v1_episodes_id_stream_get(id)
        print("The response of EpisodesApi->v1_episodes_id_stream_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EpisodesApi->v1_episodes_id_stream_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**V1EpisodesIdStreamGet200Response**](V1EpisodesIdStreamGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stream sources and media tracks |  -  |
**404** | Episode not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

