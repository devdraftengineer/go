# devdraft.TransfersApi

All URIs are relative to *https://api.devdraft.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transfer_controller_create_direct_bank_transfer**](TransfersApi.md#transfer_controller_create_direct_bank_transfer) | **POST** /api/v0/transfers/direct-bank | Create a direct bank transfer
[**transfer_controller_create_direct_wallet_transfer**](TransfersApi.md#transfer_controller_create_direct_wallet_transfer) | **POST** /api/v0/transfers/direct-wallet | Create a direct wallet transfer
[**transfer_controller_create_external_bank_transfer**](TransfersApi.md#transfer_controller_create_external_bank_transfer) | **POST** /api/v0/transfers/external-bank-transfer | Create an external bank transfer
[**transfer_controller_create_external_stablecoin_transfer**](TransfersApi.md#transfer_controller_create_external_stablecoin_transfer) | **POST** /api/v0/transfers/external-stablecoin-transfer | Create an external stablecoin transfer
[**transfer_controller_create_stablecoin_conversion**](TransfersApi.md#transfer_controller_create_stablecoin_conversion) | **POST** /api/v0/transfers/stablecoin-conversion | Create a stablecoin conversion


# **transfer_controller_create_direct_bank_transfer**
> transfer_controller_create_direct_bank_transfer(create_direct_bank_transfer_dto)

Create a direct bank transfer

### Example

* Api Key Authentication (x-client-secret):
* Api Key Authentication (x-client-key):

```python
import devdraft
from devdraft.models.create_direct_bank_transfer_dto import CreateDirectBankTransferDto
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
    api_instance = devdraft.TransfersApi(api_client)
    create_direct_bank_transfer_dto = devdraft.CreateDirectBankTransferDto() # CreateDirectBankTransferDto | 

    try:
        # Create a direct bank transfer
        api_instance.transfer_controller_create_direct_bank_transfer(create_direct_bank_transfer_dto)
    except Exception as e:
        print("Exception when calling TransfersApi->transfer_controller_create_direct_bank_transfer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_direct_bank_transfer_dto** | [**CreateDirectBankTransferDto**](CreateDirectBankTransferDto.md)|  | 

### Return type

void (empty response body)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The transfer has been successfully created. |  -  |
**400** | Bad Request - Invalid input |  -  |
**404** | Not Found - Bridge wallet not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_controller_create_direct_wallet_transfer**
> transfer_controller_create_direct_wallet_transfer(create_direct_wallet_transfer_dto)

Create a direct wallet transfer

### Example

* Api Key Authentication (x-client-secret):
* Api Key Authentication (x-client-key):

```python
import devdraft
from devdraft.models.create_direct_wallet_transfer_dto import CreateDirectWalletTransferDto
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
    api_instance = devdraft.TransfersApi(api_client)
    create_direct_wallet_transfer_dto = devdraft.CreateDirectWalletTransferDto() # CreateDirectWalletTransferDto | 

    try:
        # Create a direct wallet transfer
        api_instance.transfer_controller_create_direct_wallet_transfer(create_direct_wallet_transfer_dto)
    except Exception as e:
        print("Exception when calling TransfersApi->transfer_controller_create_direct_wallet_transfer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_direct_wallet_transfer_dto** | [**CreateDirectWalletTransferDto**](CreateDirectWalletTransferDto.md)|  | 

### Return type

void (empty response body)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The transfer has been successfully created. |  -  |
**400** | Bad Request - Invalid input |  -  |
**404** | Not Found - Bridge wallet not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_controller_create_external_bank_transfer**
> transfer_controller_create_external_bank_transfer(create_external_bank_transfer_dto)

Create an external bank transfer

### Example

* Api Key Authentication (x-client-secret):
* Api Key Authentication (x-client-key):

```python
import devdraft
from devdraft.models.create_external_bank_transfer_dto import CreateExternalBankTransferDto
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
    api_instance = devdraft.TransfersApi(api_client)
    create_external_bank_transfer_dto = devdraft.CreateExternalBankTransferDto() # CreateExternalBankTransferDto | 

    try:
        # Create an external bank transfer
        api_instance.transfer_controller_create_external_bank_transfer(create_external_bank_transfer_dto)
    except Exception as e:
        print("Exception when calling TransfersApi->transfer_controller_create_external_bank_transfer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_external_bank_transfer_dto** | [**CreateExternalBankTransferDto**](CreateExternalBankTransferDto.md)|  | 

### Return type

void (empty response body)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The external bank transfer has been successfully created. |  -  |
**400** | Bad Request - Invalid input |  -  |
**404** | Not Found - Bridge wallet not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_controller_create_external_stablecoin_transfer**
> transfer_controller_create_external_stablecoin_transfer(create_external_stablecoin_transfer_dto)

Create an external stablecoin transfer

### Example

* Api Key Authentication (x-client-secret):
* Api Key Authentication (x-client-key):

```python
import devdraft
from devdraft.models.create_external_stablecoin_transfer_dto import CreateExternalStablecoinTransferDto
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
    api_instance = devdraft.TransfersApi(api_client)
    create_external_stablecoin_transfer_dto = devdraft.CreateExternalStablecoinTransferDto() # CreateExternalStablecoinTransferDto | 

    try:
        # Create an external stablecoin transfer
        api_instance.transfer_controller_create_external_stablecoin_transfer(create_external_stablecoin_transfer_dto)
    except Exception as e:
        print("Exception when calling TransfersApi->transfer_controller_create_external_stablecoin_transfer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_external_stablecoin_transfer_dto** | [**CreateExternalStablecoinTransferDto**](CreateExternalStablecoinTransferDto.md)|  | 

### Return type

void (empty response body)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The external stablecoin transfer has been successfully created. |  -  |
**400** | Bad Request - Invalid input |  -  |
**404** | Not Found - Bridge wallet not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_controller_create_stablecoin_conversion**
> transfer_controller_create_stablecoin_conversion(create_stablecoin_conversion_dto)

Create a stablecoin conversion

### Example

* Api Key Authentication (x-client-secret):
* Api Key Authentication (x-client-key):

```python
import devdraft
from devdraft.models.create_stablecoin_conversion_dto import CreateStablecoinConversionDto
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
    api_instance = devdraft.TransfersApi(api_client)
    create_stablecoin_conversion_dto = devdraft.CreateStablecoinConversionDto() # CreateStablecoinConversionDto | 

    try:
        # Create a stablecoin conversion
        api_instance.transfer_controller_create_stablecoin_conversion(create_stablecoin_conversion_dto)
    except Exception as e:
        print("Exception when calling TransfersApi->transfer_controller_create_stablecoin_conversion: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_stablecoin_conversion_dto** | [**CreateStablecoinConversionDto**](CreateStablecoinConversionDto.md)|  | 

### Return type

void (empty response body)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The conversion has been successfully created. |  -  |
**400** | Bad Request - Invalid input |  -  |
**404** | Not Found - Bridge wallet not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

