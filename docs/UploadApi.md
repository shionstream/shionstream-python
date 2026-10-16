# shionstream_sdk.UploadApi

All URIs are relative to *https://api.gox.my.id*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_upload_hls_post**](UploadApi.md#v1_upload_hls_post) | **POST** /v1/upload/hls | Upload HLS Package to Cloudflare R2
[**v1_upload_image_post**](UploadApi.md#v1_upload_image_post) | **POST** /v1/upload/image | Upload Image to Cloudflare R2


# **v1_upload_hls_post**
> V1UploadHlsPost200Response v1_upload_hls_post()

Upload HLS Package to Cloudflare R2

Ingests multi-resolution HLS package (master playlist, variants, and .ts segment chunks) directly into Cloudflare R2 object storage.

### Example

* Bearer (JWT / API-Key) Authentication (Bearer):

```python
import shionstream_sdk
from shionstream_sdk.models.v1_upload_hls_post200_response import V1UploadHlsPost200Response
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
    api_instance = shionstream_sdk.UploadApi(api_client)

    try:
        # Upload HLS Package to Cloudflare R2
        api_response = api_instance.v1_upload_hls_post()
        print("The response of UploadApi->v1_upload_hls_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadApi->v1_upload_hls_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V1UploadHlsPost200Response**](V1UploadHlsPost200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | HLS package successfully uploaded |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal upload failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_upload_image_post**
> V1UploadImagePost200Response v1_upload_image_post()

Upload Image to Cloudflare R2

Uploads posters, banners, or avatars directly to Cloudflare R2.

### Example

* Bearer (JWT / API-Key) Authentication (Bearer):

```python
import shionstream_sdk
from shionstream_sdk.models.v1_upload_image_post200_response import V1UploadImagePost200Response
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
    api_instance = shionstream_sdk.UploadApi(api_client)

    try:
        # Upload Image to Cloudflare R2
        api_response = api_instance.v1_upload_image_post()
        print("The response of UploadApi->v1_upload_image_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadApi->v1_upload_image_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V1UploadImagePost200Response**](V1UploadImagePost200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Image successfully uploaded |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal upload failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

