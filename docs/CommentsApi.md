# shionstream_sdk.CommentsApi

All URIs are relative to *https://api.gox.my.id*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_comments_get**](CommentsApi.md#v1_comments_get) | **GET** /v1/comments | Get Episode Comments
[**v1_comments_id_like_post**](CommentsApi.md#v1_comments_id_like_post) | **POST** /v1/comments/{id}/like | Like or Dislike Comment
[**v1_comments_id_report_post**](CommentsApi.md#v1_comments_id_report_post) | **POST** /v1/comments/{id}/report | Report Comment
[**v1_comments_post**](CommentsApi.md#v1_comments_post) | **POST** /v1/comments | Create Comment


# **v1_comments_get**
> V1CommentsGet200Response v1_comments_get(episode_id)

Get Episode Comments

Retrieves threaded comments for an episode, ordered by newest first, with like/dislike counts.

### Example


```python
import shionstream_sdk
from shionstream_sdk.models.v1_comments_get200_response import V1CommentsGet200Response
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
    api_instance = shionstream_sdk.CommentsApi(api_client)
    episode_id = 'episode_id_example' # str | 

    try:
        # Get Episode Comments
        api_response = api_instance.v1_comments_get(episode_id)
        print("The response of CommentsApi->v1_comments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->v1_comments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **episode_id** | **str**|  | 

### Return type

[**V1CommentsGet200Response**](V1CommentsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comments list |  -  |
**400** | Missing episodeId |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_comments_id_like_post**
> V1CommentsIdLikePost200Response v1_comments_id_like_post(id, v1_comments_id_like_post_request=v1_comments_id_like_post_request)

Like or Dislike Comment

Adds or toggles a like/dislike reaction on a comment. Upserts on [commentId, userId].

### Example

* Bearer (JWT / API-Key) Authentication (Bearer):

```python
import shionstream_sdk
from shionstream_sdk.models.v1_comments_id_like_post200_response import V1CommentsIdLikePost200Response
from shionstream_sdk.models.v1_comments_id_like_post_request import V1CommentsIdLikePostRequest
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
    api_instance = shionstream_sdk.CommentsApi(api_client)
    id = 'id_example' # str | 
    v1_comments_id_like_post_request = shionstream_sdk.V1CommentsIdLikePostRequest() # V1CommentsIdLikePostRequest |  (optional)

    try:
        # Like or Dislike Comment
        api_response = api_instance.v1_comments_id_like_post(id, v1_comments_id_like_post_request=v1_comments_id_like_post_request)
        print("The response of CommentsApi->v1_comments_id_like_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->v1_comments_id_like_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **v1_comments_id_like_post_request** | [**V1CommentsIdLikePostRequest**](V1CommentsIdLikePostRequest.md)|  | [optional] 

### Return type

[**V1CommentsIdLikePost200Response**](V1CommentsIdLikePost200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Reaction recorded |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_comments_id_report_post**
> V1CommentsIdLikePost200Response v1_comments_id_report_post(id, v1_comments_id_report_post_request=v1_comments_id_report_post_request)

Report Comment

Submits a comment to the moderation queue with a reason.

### Example


```python
import shionstream_sdk
from shionstream_sdk.models.v1_comments_id_like_post200_response import V1CommentsIdLikePost200Response
from shionstream_sdk.models.v1_comments_id_report_post_request import V1CommentsIdReportPostRequest
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
    api_instance = shionstream_sdk.CommentsApi(api_client)
    id = 'id_example' # str | 
    v1_comments_id_report_post_request = shionstream_sdk.V1CommentsIdReportPostRequest() # V1CommentsIdReportPostRequest |  (optional)

    try:
        # Report Comment
        api_response = api_instance.v1_comments_id_report_post(id, v1_comments_id_report_post_request=v1_comments_id_report_post_request)
        print("The response of CommentsApi->v1_comments_id_report_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->v1_comments_id_report_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **v1_comments_id_report_post_request** | [**V1CommentsIdReportPostRequest**](V1CommentsIdReportPostRequest.md)|  | [optional] 

### Return type

[**V1CommentsIdLikePost200Response**](V1CommentsIdLikePost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Report submitted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_comments_post**
> V1CommentsPost201Response v1_comments_post(v1_comments_post_request=v1_comments_post_request)

Create Comment

Creates a new comment or reply on an episode. Supports both authenticated users and guests (guest requires name and email).

### Example


```python
import shionstream_sdk
from shionstream_sdk.models.v1_comments_post201_response import V1CommentsPost201Response
from shionstream_sdk.models.v1_comments_post_request import V1CommentsPostRequest
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
    api_instance = shionstream_sdk.CommentsApi(api_client)
    v1_comments_post_request = shionstream_sdk.V1CommentsPostRequest() # V1CommentsPostRequest |  (optional)

    try:
        # Create Comment
        api_response = api_instance.v1_comments_post(v1_comments_post_request=v1_comments_post_request)
        print("The response of CommentsApi->v1_comments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->v1_comments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1_comments_post_request** | [**V1CommentsPostRequest**](V1CommentsPostRequest.md)|  | [optional] 

### Return type

[**V1CommentsPost201Response**](V1CommentsPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Comment created |  -  |
**400** | Validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

