# shionstream_sdk.UserApi

All URIs are relative to *https://api.gox.my.id*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_user_history_delete**](UserApi.md#v1_user_history_delete) | **DELETE** /v1/user/history | Clear All History
[**v1_user_history_get**](UserApi.md#v1_user_history_get) | **GET** /v1/user/history | Get Watch History
[**v1_user_history_id_delete**](UserApi.md#v1_user_history_id_delete) | **DELETE** /v1/user/history/{id} | Delete History Item
[**v1_user_history_post**](UserApi.md#v1_user_history_post) | **POST** /v1/user/history | Record Playback Progress
[**v1_user_profile_get**](UserApi.md#v1_user_profile_get) | **GET** /v1/user/profile | Get User Profile
[**v1_user_settings_get**](UserApi.md#v1_user_settings_get) | **GET** /v1/user/settings | Get User Settings
[**v1_user_settings_patch**](UserApi.md#v1_user_settings_patch) | **PATCH** /v1/user/settings | Update User Settings
[**v1_user_watchlist_anime_id_delete**](UserApi.md#v1_user_watchlist_anime_id_delete) | **DELETE** /v1/user/watchlist/{animeId} | Remove from Watchlist
[**v1_user_watchlist_anime_id_patch**](UserApi.md#v1_user_watchlist_anime_id_patch) | **PATCH** /v1/user/watchlist/{animeId} | Update Watchlist Entry
[**v1_user_watchlist_get**](UserApi.md#v1_user_watchlist_get) | **GET** /v1/user/watchlist | Get User Watchlist
[**v1_user_watchlist_post**](UserApi.md#v1_user_watchlist_post) | **POST** /v1/user/watchlist | Add to Watchlist


# **v1_user_history_delete**
> V1UserSettingsPatch200Response v1_user_history_delete()

Clear All History

Clears the authenticated user's entire watch history.

### Example

* Bearer (JWT / API-Key) Authentication (Bearer):

```python
import shionstream_sdk
from shionstream_sdk.models.v1_user_settings_patch200_response import V1UserSettingsPatch200Response
from shionstream_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.gox.my.id
# See configuration.py for a list of all supported configuration parameters.
configuration = shionstream_sdk.Configuration(
    host = "https://api.gox.my.id"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT / API-Key): Bearer
configuration = shionstream_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with shionstream_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shionstream_sdk.UserApi(api_client)

    try:
        # Clear All History
        api_response = api_instance.v1_user_history_delete()
        print("The response of UserApi->v1_user_history_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->v1_user_history_delete: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V1UserSettingsPatch200Response**](V1UserSettingsPatch200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | History cleared |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_user_history_get**
> V1UserHistoryGet200Response v1_user_history_get(limit=limit)

Get Watch History

Retrieves the authenticated user's watch history sorted by most recent.

### Example

* Bearer (JWT / API-Key) Authentication (Bearer):

```python
import shionstream_sdk
from shionstream_sdk.models.v1_user_history_get200_response import V1UserHistoryGet200Response
from shionstream_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.gox.my.id
# See configuration.py for a list of all supported configuration parameters.
configuration = shionstream_sdk.Configuration(
    host = "https://api.gox.my.id"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT / API-Key): Bearer
configuration = shionstream_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with shionstream_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shionstream_sdk.UserApi(api_client)
    limit = '50' # str |  (optional) (default to '50')

    try:
        # Get Watch History
        api_response = api_instance.v1_user_history_get(limit=limit)
        print("The response of UserApi->v1_user_history_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->v1_user_history_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**|  | [optional] [default to &#39;50&#39;]

### Return type

[**V1UserHistoryGet200Response**](V1UserHistoryGet200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Watch history |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_user_history_id_delete**
> V1UserSettingsPatch200Response v1_user_history_id_delete(id)

Delete History Item

Deletes a single watch history record.

### Example

* Bearer (JWT / API-Key) Authentication (Bearer):

```python
import shionstream_sdk
from shionstream_sdk.models.v1_user_settings_patch200_response import V1UserSettingsPatch200Response
from shionstream_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.gox.my.id
# See configuration.py for a list of all supported configuration parameters.
configuration = shionstream_sdk.Configuration(
    host = "https://api.gox.my.id"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT / API-Key): Bearer
configuration = shionstream_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with shionstream_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shionstream_sdk.UserApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete History Item
        api_response = api_instance.v1_user_history_id_delete(id)
        print("The response of UserApi->v1_user_history_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->v1_user_history_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**V1UserSettingsPatch200Response**](V1UserSettingsPatch200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deleted |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_user_history_post**
> V1UserSettingsPatch200Response v1_user_history_post(v1_user_history_post_request=v1_user_history_post_request)

Record Playback Progress

Records or updates playback progress for an episode (heartbeat). Upserts on [userId, episodeId].

### Example

* Bearer (JWT / API-Key) Authentication (Bearer):

```python
import shionstream_sdk
from shionstream_sdk.models.v1_user_history_post_request import V1UserHistoryPostRequest
from shionstream_sdk.models.v1_user_settings_patch200_response import V1UserSettingsPatch200Response
from shionstream_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.gox.my.id
# See configuration.py for a list of all supported configuration parameters.
configuration = shionstream_sdk.Configuration(
    host = "https://api.gox.my.id"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT / API-Key): Bearer
configuration = shionstream_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with shionstream_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shionstream_sdk.UserApi(api_client)
    v1_user_history_post_request = shionstream_sdk.V1UserHistoryPostRequest() # V1UserHistoryPostRequest |  (optional)

    try:
        # Record Playback Progress
        api_response = api_instance.v1_user_history_post(v1_user_history_post_request=v1_user_history_post_request)
        print("The response of UserApi->v1_user_history_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->v1_user_history_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1_user_history_post_request** | [**V1UserHistoryPostRequest**](V1UserHistoryPostRequest.md)|  | [optional] 

### Return type

[**V1UserSettingsPatch200Response**](V1UserSettingsPatch200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Progress recorded |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_user_profile_get**
> V1UserProfileGet200Response v1_user_profile_get()

Get User Profile

Retrieves the authenticated user's profile with activity summary (watchlist count and recent history count).

### Example

* Bearer (JWT / API-Key) Authentication (Bearer):

```python
import shionstream_sdk
from shionstream_sdk.models.v1_user_profile_get200_response import V1UserProfileGet200Response
from shionstream_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.gox.my.id
# See configuration.py for a list of all supported configuration parameters.
configuration = shionstream_sdk.Configuration(
    host = "https://api.gox.my.id"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT / API-Key): Bearer
configuration = shionstream_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with shionstream_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shionstream_sdk.UserApi(api_client)

    try:
        # Get User Profile
        api_response = api_instance.v1_user_profile_get()
        print("The response of UserApi->v1_user_profile_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->v1_user_profile_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V1UserProfileGet200Response**](V1UserProfileGet200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User profile |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_user_settings_get**
> V1UserSettingsGet200Response v1_user_settings_get()

Get User Settings

Retrieves player preferences and notification settings for the authenticated user.

### Example

* Bearer (JWT / API-Key) Authentication (Bearer):

```python
import shionstream_sdk
from shionstream_sdk.models.v1_user_settings_get200_response import V1UserSettingsGet200Response
from shionstream_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.gox.my.id
# See configuration.py for a list of all supported configuration parameters.
configuration = shionstream_sdk.Configuration(
    host = "https://api.gox.my.id"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT / API-Key): Bearer
configuration = shionstream_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with shionstream_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shionstream_sdk.UserApi(api_client)

    try:
        # Get User Settings
        api_response = api_instance.v1_user_settings_get()
        print("The response of UserApi->v1_user_settings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->v1_user_settings_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V1UserSettingsGet200Response**](V1UserSettingsGet200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User settings |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_user_settings_patch**
> V1UserSettingsPatch200Response v1_user_settings_patch(v1_user_settings_patch_request=v1_user_settings_patch_request)

Update User Settings

Updates player preferences and notification settings.

### Example

* Bearer (JWT / API-Key) Authentication (Bearer):

```python
import shionstream_sdk
from shionstream_sdk.models.v1_user_settings_patch200_response import V1UserSettingsPatch200Response
from shionstream_sdk.models.v1_user_settings_patch_request import V1UserSettingsPatchRequest
from shionstream_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.gox.my.id
# See configuration.py for a list of all supported configuration parameters.
configuration = shionstream_sdk.Configuration(
    host = "https://api.gox.my.id"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT / API-Key): Bearer
configuration = shionstream_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with shionstream_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shionstream_sdk.UserApi(api_client)
    v1_user_settings_patch_request = shionstream_sdk.V1UserSettingsPatchRequest() # V1UserSettingsPatchRequest |  (optional)

    try:
        # Update User Settings
        api_response = api_instance.v1_user_settings_patch(v1_user_settings_patch_request=v1_user_settings_patch_request)
        print("The response of UserApi->v1_user_settings_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->v1_user_settings_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1_user_settings_patch_request** | [**V1UserSettingsPatchRequest**](V1UserSettingsPatchRequest.md)|  | [optional] 

### Return type

[**V1UserSettingsPatch200Response**](V1UserSettingsPatch200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Settings updated |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_user_watchlist_anime_id_delete**
> V1UserSettingsPatch200Response v1_user_watchlist_anime_id_delete(anime_id)

Remove from Watchlist

Removes an anime from the user's watchlist.

### Example

* Bearer (JWT / API-Key) Authentication (Bearer):

```python
import shionstream_sdk
from shionstream_sdk.models.v1_user_settings_patch200_response import V1UserSettingsPatch200Response
from shionstream_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.gox.my.id
# See configuration.py for a list of all supported configuration parameters.
configuration = shionstream_sdk.Configuration(
    host = "https://api.gox.my.id"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT / API-Key): Bearer
configuration = shionstream_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with shionstream_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shionstream_sdk.UserApi(api_client)
    anime_id = 'anime_id_example' # str | 

    try:
        # Remove from Watchlist
        api_response = api_instance.v1_user_watchlist_anime_id_delete(anime_id)
        print("The response of UserApi->v1_user_watchlist_anime_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->v1_user_watchlist_anime_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anime_id** | **str**|  | 

### Return type

[**V1UserSettingsPatch200Response**](V1UserSettingsPatch200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Removed |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_user_watchlist_anime_id_patch**
> V1UserSettingsPatch200Response v1_user_watchlist_anime_id_patch(anime_id, v1_user_watchlist_anime_id_patch_request=v1_user_watchlist_anime_id_patch_request)

Update Watchlist Entry

Updates status or favorite flag for a specific anime in the user's watchlist.

### Example

* Bearer (JWT / API-Key) Authentication (Bearer):

```python
import shionstream_sdk
from shionstream_sdk.models.v1_user_settings_patch200_response import V1UserSettingsPatch200Response
from shionstream_sdk.models.v1_user_watchlist_anime_id_patch_request import V1UserWatchlistAnimeIdPatchRequest
from shionstream_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.gox.my.id
# See configuration.py for a list of all supported configuration parameters.
configuration = shionstream_sdk.Configuration(
    host = "https://api.gox.my.id"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT / API-Key): Bearer
configuration = shionstream_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with shionstream_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shionstream_sdk.UserApi(api_client)
    anime_id = 'anime_id_example' # str | 
    v1_user_watchlist_anime_id_patch_request = shionstream_sdk.V1UserWatchlistAnimeIdPatchRequest() # V1UserWatchlistAnimeIdPatchRequest |  (optional)

    try:
        # Update Watchlist Entry
        api_response = api_instance.v1_user_watchlist_anime_id_patch(anime_id, v1_user_watchlist_anime_id_patch_request=v1_user_watchlist_anime_id_patch_request)
        print("The response of UserApi->v1_user_watchlist_anime_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->v1_user_watchlist_anime_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anime_id** | **str**|  | 
 **v1_user_watchlist_anime_id_patch_request** | [**V1UserWatchlistAnimeIdPatchRequest**](V1UserWatchlistAnimeIdPatchRequest.md)|  | [optional] 

### Return type

[**V1UserSettingsPatch200Response**](V1UserSettingsPatch200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Watchlist updated |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_user_watchlist_get**
> V1UserWatchlistGet200Response v1_user_watchlist_get(status=status)

Get User Watchlist

Retrieves the authenticated user's anime watchlist with optional status filter.

### Example

* Bearer (JWT / API-Key) Authentication (Bearer):

```python
import shionstream_sdk
from shionstream_sdk.models.v1_user_watchlist_get200_response import V1UserWatchlistGet200Response
from shionstream_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.gox.my.id
# See configuration.py for a list of all supported configuration parameters.
configuration = shionstream_sdk.Configuration(
    host = "https://api.gox.my.id"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT / API-Key): Bearer
configuration = shionstream_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with shionstream_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shionstream_sdk.UserApi(api_client)
    status = 'status_example' # str |  (optional)

    try:
        # Get User Watchlist
        api_response = api_instance.v1_user_watchlist_get(status=status)
        print("The response of UserApi->v1_user_watchlist_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->v1_user_watchlist_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**|  | [optional] 

### Return type

[**V1UserWatchlistGet200Response**](V1UserWatchlistGet200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Watchlist items |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_user_watchlist_post**
> V1UserSettingsPatch200Response v1_user_watchlist_post(v1_user_watchlist_post_request=v1_user_watchlist_post_request)

Add to Watchlist

Adds an anime to the user's watchlist. Upserts if the anime already exists in the watchlist.

### Example

* Bearer (JWT / API-Key) Authentication (Bearer):

```python
import shionstream_sdk
from shionstream_sdk.models.v1_user_settings_patch200_response import V1UserSettingsPatch200Response
from shionstream_sdk.models.v1_user_watchlist_post_request import V1UserWatchlistPostRequest
from shionstream_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.gox.my.id
# See configuration.py for a list of all supported configuration parameters.
configuration = shionstream_sdk.Configuration(
    host = "https://api.gox.my.id"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT / API-Key): Bearer
configuration = shionstream_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with shionstream_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shionstream_sdk.UserApi(api_client)
    v1_user_watchlist_post_request = shionstream_sdk.V1UserWatchlistPostRequest() # V1UserWatchlistPostRequest |  (optional)

    try:
        # Add to Watchlist
        api_response = api_instance.v1_user_watchlist_post(v1_user_watchlist_post_request=v1_user_watchlist_post_request)
        print("The response of UserApi->v1_user_watchlist_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->v1_user_watchlist_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1_user_watchlist_post_request** | [**V1UserWatchlistPostRequest**](V1UserWatchlistPostRequest.md)|  | [optional] 

### Return type

[**V1UserSettingsPatch200Response**](V1UserSettingsPatch200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Added to watchlist |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

