# shionstream_sdk.SampleApi

All URIs are relative to *https://api.gox.my.id*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_protected_sample_get**](SampleApi.md#v1_protected_sample_get) | **GET** /v1/protected/sample | Protected Sample Endpoint


# **v1_protected_sample_get**
> V1ProtectedSampleGet200Response v1_protected_sample_get()

Protected Sample Endpoint

Example endpoint that requires a valid Better Auth session or Bearer token.

### Example

* Bearer (JWT / API-Key) Authentication (Bearer):

```python
import shionstream_sdk
from shionstream_sdk.models.v1_protected_sample_get200_response import V1ProtectedSampleGet200Response
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
    api_instance = shionstream_sdk.SampleApi(api_client)

    try:
        # Protected Sample Endpoint
        api_response = api_instance.v1_protected_sample_get()
        print("The response of SampleApi->v1_protected_sample_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SampleApi->v1_protected_sample_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V1ProtectedSampleGet200Response**](V1ProtectedSampleGet200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User is authenticated |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

