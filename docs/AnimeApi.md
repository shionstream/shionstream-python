# shionstream_sdk.AnimeApi

All URIs are relative to *https://api.gox.my.id*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_anime_get**](AnimeApi.md#v1_anime_get) | **GET** /v1/anime | List Anime Catalog
[**v1_anime_slug_get**](AnimeApi.md#v1_anime_slug_get) | **GET** /v1/anime/{slug} | Get Anime Details by Slug


# **v1_anime_get**
> V1AnimeGet200Response v1_anime_get(page=page, limit=limit, search=search, type=type, status=status, genre=genre, season=season, year=year, sort=sort)

List Anime Catalog

Retrieve paginated list of anime with filters for type, status, season, year, genre, and search.

### Example


```python
import shionstream_sdk
from shionstream_sdk.models.v1_anime_get200_response import V1AnimeGet200Response
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
    api_instance = shionstream_sdk.AnimeApi(api_client)
    page = '1' # str |  (optional) (default to '1')
    limit = '20' # str |  (optional) (default to '20')
    search = 'search_example' # str |  (optional)
    type = 'type_example' # str |  (optional)
    status = 'status_example' # str |  (optional)
    genre = 'genre_example' # str |  (optional)
    season = 'season_example' # str |  (optional)
    year = 'year_example' # str |  (optional)
    sort = 'latest' # str |  (optional) (default to 'latest')

    try:
        # List Anime Catalog
        api_response = api_instance.v1_anime_get(page=page, limit=limit, search=search, type=type, status=status, genre=genre, season=season, year=year, sort=sort)
        print("The response of AnimeApi->v1_anime_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnimeApi->v1_anime_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**|  | [optional] [default to &#39;1&#39;]
 **limit** | **str**|  | [optional] [default to &#39;20&#39;]
 **search** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **genre** | **str**|  | [optional] 
 **season** | **str**|  | [optional] 
 **year** | **str**|  | [optional] 
 **sort** | **str**|  | [optional] [default to &#39;latest&#39;]

### Return type

[**V1AnimeGet200Response**](V1AnimeGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated anime list |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_anime_slug_get**
> V1AnimeSlugGet200Response v1_anime_slug_get(slug)

Get Anime Details by Slug

Retrieve comprehensive anime metadata including associated genres, studios, schedule, and trending stats.

### Example


```python
import shionstream_sdk
from shionstream_sdk.models.v1_anime_slug_get200_response import V1AnimeSlugGet200Response
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
    api_instance = shionstream_sdk.AnimeApi(api_client)
    slug = 'slug_example' # str | 

    try:
        # Get Anime Details by Slug
        api_response = api_instance.v1_anime_slug_get(slug)
        print("The response of AnimeApi->v1_anime_slug_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnimeApi->v1_anime_slug_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

### Return type

[**V1AnimeSlugGet200Response**](V1AnimeSlugGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Anime detailed metadata |  -  |
**404** | Anime not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

