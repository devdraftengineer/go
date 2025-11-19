# devdraft.APIHealthApi

All URIs are relative to *https://api.devdraft.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health_controller_check_v0**](APIHealthApi.md#health_controller_check_v0) | **GET** /api/v0/health | Authenticated health check endpoint
[**health_controller_public_health_check_v0**](APIHealthApi.md#health_controller_public_health_check_v0) | **GET** /api/v0/health/public | Public health check endpoint


# **health_controller_check_v0**
> HealthResponseDto health_controller_check_v0()

Authenticated health check endpoint

### Example

* Api Key Authentication (x-client-secret):
* Api Key Authentication (x-client-key):

```python
import devdraft
from devdraft.models.health_response_dto import HealthResponseDto
from devdraft.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.devdraft.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = devdraft.Configuration(
    host = "https://api.devdraft.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x-client-secret
configuration.api_key['x-client-secret'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-client-secret'] = 'Bearer'

# Configure API key authorization: x-client-key
configuration.api_key['x-client-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-client-key'] = 'Bearer'

# Enter a context with an instance of the API client
with devdraft.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = devdraft.APIHealthApi(api_client)

    try:
        # Authenticated health check endpoint
        api_response = api_instance.health_controller_check_v0()
        print("The response of APIHealthApi->health_controller_check_v0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIHealthApi->health_controller_check_v0: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**HealthResponseDto**](HealthResponseDto.md)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Service is up and running |  -  |
**401** | Unauthorized. Client key or secret is invalid or missing. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health_controller_public_health_check_v0**
> PublicHealthResponseDto health_controller_public_health_check_v0()

Public health check endpoint

### Example


```python
import devdraft
from devdraft.models.public_health_response_dto import PublicHealthResponseDto
from devdraft.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.devdraft.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = devdraft.Configuration(
    host = "https://api.devdraft.ai"
)


# Enter a context with an instance of the API client
with devdraft.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = devdraft.APIHealthApi(api_client)

    try:
        # Public health check endpoint
        api_response = api_instance.health_controller_public_health_check_v0()
        print("The response of APIHealthApi->health_controller_public_health_check_v0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIHealthApi->health_controller_public_health_check_v0: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PublicHealthResponseDto**](PublicHealthResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Basic service health check |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

