# shionstream_sdk.DashboardApi

All URIs are relative to *https://api.gox.my.id*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_dashboard_anime_get**](DashboardApi.md#v1_dashboard_anime_get) | **GET** /v1/dashboard/anime | Get Administrative Anime List
[**v1_dashboard_categories_get**](DashboardApi.md#v1_dashboard_categories_get) | **GET** /v1/dashboard/categories | Get Category &amp; Genre Distributions
[**v1_dashboard_episodes_get**](DashboardApi.md#v1_dashboard_episodes_get) | **GET** /v1/dashboard/episodes | Get Administrative Episodes List
[**v1_dashboard_moderation_get**](DashboardApi.md#v1_dashboard_moderation_get) | **GET** /v1/dashboard/moderation | Get Comment Moderation Reports
[**v1_dashboard_moderation_id_patch**](DashboardApi.md#v1_dashboard_moderation_id_patch) | **PATCH** /v1/dashboard/moderation/{id} | Resolve or Dismiss Moderation Report
[**v1_dashboard_overview_get**](DashboardApi.md#v1_dashboard_overview_get) | **GET** /v1/dashboard/overview | Get Dashboard Overview
[**v1_dashboard_roles_get**](DashboardApi.md#v1_dashboard_roles_get) | **GET** /v1/dashboard/roles | Get System Roles &amp; Permissions
[**v1_dashboard_seasons_get**](DashboardApi.md#v1_dashboard_seasons_get) | **GET** /v1/dashboard/seasons | Get Seasonal Broadcast Distributions
[**v1_dashboard_stats_get**](DashboardApi.md#v1_dashboard_stats_get) | **GET** /v1/dashboard/stats | Get Platform Stats
[**v1_dashboard_users_get**](DashboardApi.md#v1_dashboard_users_get) | **GET** /v1/dashboard/users | Get Users Directory (Admin Only)


# **v1_dashboard_anime_get**
> V1DashboardAnimeGet200Response v1_dashboard_anime_get(page=page, limit=limit, status=status, search=search)

Get Administrative Anime List

Returns paginated anime catalog with filters for administration.

### Example

* Bearer (JWT / API-Key) Authentication (Bearer):

```python
import shionstream_sdk
from shionstream_sdk.models.v1_dashboard_anime_get200_response import V1DashboardAnimeGet200Response
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
    api_instance = shionstream_sdk.DashboardApi(api_client)
    page = '1' # str |  (optional) (default to '1')
    limit = '20' # str |  (optional) (default to '20')
    status = 'status_example' # str |  (optional)
    search = 'search_example' # str |  (optional)

    try:
        # Get Administrative Anime List
        api_response = api_instance.v1_dashboard_anime_get(page=page, limit=limit, status=status, search=search)
        print("The response of DashboardApi->v1_dashboard_anime_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardApi->v1_dashboard_anime_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**|  | [optional] [default to &#39;1&#39;]
 **limit** | **str**|  | [optional] [default to &#39;20&#39;]
 **status** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 

### Return type

[**V1DashboardAnimeGet200Response**](V1DashboardAnimeGet200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated anime list |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_dashboard_categories_get**
> V1DashboardCategoriesGet200Response v1_dashboard_categories_get()

Get Category & Genre Distributions

Returns format categories and genres with associated anime counts.

### Example

* Bearer (JWT / API-Key) Authentication (Bearer):

```python
import shionstream_sdk
from shionstream_sdk.models.v1_dashboard_categories_get200_response import V1DashboardCategoriesGet200Response
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
    api_instance = shionstream_sdk.DashboardApi(api_client)

    try:
        # Get Category & Genre Distributions
        api_response = api_instance.v1_dashboard_categories_get()
        print("The response of DashboardApi->v1_dashboard_categories_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardApi->v1_dashboard_categories_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V1DashboardCategoriesGet200Response**](V1DashboardCategoriesGet200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Category and genre statistics |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_dashboard_episodes_get**
> V1DashboardEpisodesGet200Response v1_dashboard_episodes_get(page=page, limit=limit, anime_id=anime_id)

Get Administrative Episodes List

Returns paginated episodes with upload status for administration.

### Example

* Bearer (JWT / API-Key) Authentication (Bearer):

```python
import shionstream_sdk
from shionstream_sdk.models.v1_dashboard_episodes_get200_response import V1DashboardEpisodesGet200Response
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
    api_instance = shionstream_sdk.DashboardApi(api_client)
    page = '1' # str |  (optional) (default to '1')
    limit = '20' # str |  (optional) (default to '20')
    anime_id = 'anime_id_example' # str |  (optional)

    try:
        # Get Administrative Episodes List
        api_response = api_instance.v1_dashboard_episodes_get(page=page, limit=limit, anime_id=anime_id)
        print("The response of DashboardApi->v1_dashboard_episodes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardApi->v1_dashboard_episodes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**|  | [optional] [default to &#39;1&#39;]
 **limit** | **str**|  | [optional] [default to &#39;20&#39;]
 **anime_id** | **str**|  | [optional] 

### Return type

[**V1DashboardEpisodesGet200Response**](V1DashboardEpisodesGet200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated episodes list |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_dashboard_moderation_get**
> V1DashboardModerationGet200Response v1_dashboard_moderation_get(status=status)

Get Comment Moderation Reports

Returns reported comments queue with status filter.

### Example

* Bearer (JWT / API-Key) Authentication (Bearer):

```python
import shionstream_sdk
from shionstream_sdk.models.v1_dashboard_moderation_get200_response import V1DashboardModerationGet200Response
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
    api_instance = shionstream_sdk.DashboardApi(api_client)
    status = 'pending' # str |  (optional) (default to 'pending')

    try:
        # Get Comment Moderation Reports
        api_response = api_instance.v1_dashboard_moderation_get(status=status)
        print("The response of DashboardApi->v1_dashboard_moderation_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardApi->v1_dashboard_moderation_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**|  | [optional] [default to &#39;pending&#39;]

### Return type

[**V1DashboardModerationGet200Response**](V1DashboardModerationGet200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Moderation reports list |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_dashboard_moderation_id_patch**
> V1UserSettingsPatch200Response v1_dashboard_moderation_id_patch(id, v1_dashboard_moderation_id_patch_request=v1_dashboard_moderation_id_patch_request)

Resolve or Dismiss Moderation Report

Updates comment report status and optionally deletes the reported comment.

### Example

* Bearer (JWT / API-Key) Authentication (Bearer):

```python
import shionstream_sdk
from shionstream_sdk.models.v1_dashboard_moderation_id_patch_request import V1DashboardModerationIdPatchRequest
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
    api_instance = shionstream_sdk.DashboardApi(api_client)
    id = 'id_example' # str | 
    v1_dashboard_moderation_id_patch_request = shionstream_sdk.V1DashboardModerationIdPatchRequest() # V1DashboardModerationIdPatchRequest |  (optional)

    try:
        # Resolve or Dismiss Moderation Report
        api_response = api_instance.v1_dashboard_moderation_id_patch(id, v1_dashboard_moderation_id_patch_request=v1_dashboard_moderation_id_patch_request)
        print("The response of DashboardApi->v1_dashboard_moderation_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardApi->v1_dashboard_moderation_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **v1_dashboard_moderation_id_patch_request** | [**V1DashboardModerationIdPatchRequest**](V1DashboardModerationIdPatchRequest.md)|  | [optional] 

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
**200** | Report updated |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_dashboard_overview_get**
> V1DashboardOverviewGet200Response v1_dashboard_overview_get()

Get Dashboard Overview

Returns traffic telemetry, recent activity logs, and administrative notifications.

### Example

* Bearer (JWT / API-Key) Authentication (Bearer):

```python
import shionstream_sdk
from shionstream_sdk.models.v1_dashboard_overview_get200_response import V1DashboardOverviewGet200Response
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
    api_instance = shionstream_sdk.DashboardApi(api_client)

    try:
        # Get Dashboard Overview
        api_response = api_instance.v1_dashboard_overview_get()
        print("The response of DashboardApi->v1_dashboard_overview_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardApi->v1_dashboard_overview_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V1DashboardOverviewGet200Response**](V1DashboardOverviewGet200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Overview data |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_dashboard_roles_get**
> V1DashboardRolesGet200Response v1_dashboard_roles_get()

Get System Roles & Permissions

Returns role definitions and active user member counts.

### Example

* Bearer (JWT / API-Key) Authentication (Bearer):

```python
import shionstream_sdk
from shionstream_sdk.models.v1_dashboard_roles_get200_response import V1DashboardRolesGet200Response
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
    api_instance = shionstream_sdk.DashboardApi(api_client)

    try:
        # Get System Roles & Permissions
        api_response = api_instance.v1_dashboard_roles_get()
        print("The response of DashboardApi->v1_dashboard_roles_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardApi->v1_dashboard_roles_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V1DashboardRolesGet200Response**](V1DashboardRolesGet200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Role definitions |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_dashboard_seasons_get**
> V1DashboardSeasonsGet200Response v1_dashboard_seasons_get()

Get Seasonal Broadcast Distributions

Returns anime release distribution grouped by season and year.

### Example

* Bearer (JWT / API-Key) Authentication (Bearer):

```python
import shionstream_sdk
from shionstream_sdk.models.v1_dashboard_seasons_get200_response import V1DashboardSeasonsGet200Response
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
    api_instance = shionstream_sdk.DashboardApi(api_client)

    try:
        # Get Seasonal Broadcast Distributions
        api_response = api_instance.v1_dashboard_seasons_get()
        print("The response of DashboardApi->v1_dashboard_seasons_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardApi->v1_dashboard_seasons_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V1DashboardSeasonsGet200Response**](V1DashboardSeasonsGet200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Seasonal distribution |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_dashboard_stats_get**
> V1DashboardStatsGet200Response v1_dashboard_stats_get()

Get Platform Stats

Returns aggregated platform metrics including anime count, episode count, user count, and storage estimates.

### Example

* Bearer (JWT / API-Key) Authentication (Bearer):

```python
import shionstream_sdk
from shionstream_sdk.models.v1_dashboard_stats_get200_response import V1DashboardStatsGet200Response
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
    api_instance = shionstream_sdk.DashboardApi(api_client)

    try:
        # Get Platform Stats
        api_response = api_instance.v1_dashboard_stats_get()
        print("The response of DashboardApi->v1_dashboard_stats_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardApi->v1_dashboard_stats_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V1DashboardStatsGet200Response**](V1DashboardStatsGet200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Aggregated stats |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_dashboard_users_get**
> V1DashboardUsersGet200Response v1_dashboard_users_get(page=page, limit=limit, role=role, search=search)

Get Users Directory (Admin Only)

Returns registered users directory with role and status information.

### Example

* Bearer (JWT / API-Key) Authentication (Bearer):

```python
import shionstream_sdk
from shionstream_sdk.models.v1_dashboard_users_get200_response import V1DashboardUsersGet200Response
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
    api_instance = shionstream_sdk.DashboardApi(api_client)
    page = '1' # str |  (optional) (default to '1')
    limit = '20' # str |  (optional) (default to '20')
    role = 'role_example' # str |  (optional)
    search = 'search_example' # str |  (optional)

    try:
        # Get Users Directory (Admin Only)
        api_response = api_instance.v1_dashboard_users_get(page=page, limit=limit, role=role, search=search)
        print("The response of DashboardApi->v1_dashboard_users_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardApi->v1_dashboard_users_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**|  | [optional] [default to &#39;1&#39;]
 **limit** | **str**|  | [optional] [default to &#39;20&#39;]
 **role** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 

### Return type

[**V1DashboardUsersGet200Response**](V1DashboardUsersGet200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated user directory |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

