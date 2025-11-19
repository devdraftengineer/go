# devdraft.WalletsApi

All URIs are relative to *https://api.devdraft.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**wallet_controller_get_wallets**](WalletsApi.md#wallet_controller_get_wallets) | **GET** /api/v0/wallets | Get wallets for an app


# **wallet_controller_get_wallets**
> wallet_controller_get_wallets()

Get wallets for an app

### Example

* Api Key Authentication (x-client-secret):
* Api Key Authentication (x-client-key):

```python
import devdraft
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
    api_instance = devdraft.WalletsApi(api_client)

    try:
        # Get wallets for an app
        api_instance.wallet_controller_get_wallets()
    except Exception as e:
        print("Exception when calling WalletsApi->wallet_controller_get_wallets: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

