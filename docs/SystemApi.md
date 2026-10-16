# shionstream_sdk.SystemApi

All URIs are relative to *https://api.gox.my.id*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health_get**](SystemApi.md#health_get) | **GET** /health | Health Check


# **health_get**
> HealthGet200Response health_get()

Health Check

Check if the API and Cloudflare D1 database connection are healthy.

### Example


```python
import shionstream_sdk
from shionstream_sdk.models.health_get200_response import HealthGet200Response
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
    api_instance = shionstream_sdk.SystemApi(api_client)

    try:
        # Health Check
        api_response = api_instance.health_get()
        print("The response of SystemApi->health_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->health_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**HealthGet200Response**](HealthGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Service is operational |  -  |
**500** | Service is degraded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

