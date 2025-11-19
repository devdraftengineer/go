# devdraft.LiquidationAddressesApi

All URIs are relative to *https://api.devdraft.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**liquidation_address_controller_create_liquidation_address**](LiquidationAddressesApi.md#liquidation_address_controller_create_liquidation_address) | **POST** /api/v0/customers/{customerId}/liquidation_addresses | Create a new liquidation address for a customer
[**liquidation_address_controller_get_liquidation_address**](LiquidationAddressesApi.md#liquidation_address_controller_get_liquidation_address) | **GET** /api/v0/customers/{customerId}/liquidation_addresses/{liquidationAddressId} | Get a specific liquidation address
[**liquidation_address_controller_get_liquidation_addresses**](LiquidationAddressesApi.md#liquidation_address_controller_get_liquidation_addresses) | **GET** /api/v0/customers/{customerId}/liquidation_addresses | Get all liquidation addresses for a customer


# **liquidation_address_controller_create_liquidation_address**
> LiquidationAddressResponseDto liquidation_address_controller_create_liquidation_address(customer_id, create_liquidation_address_dto)

Create a new liquidation address for a customer


      Create a new liquidation address for a customer. Liquidation addresses allow 
      customers to automatically liquidate cryptocurrency holdings to fiat or other 
      stablecoins based on configured parameters.

      **Required fields:**
      - chain: Blockchain network (ethereum, polygon, arbitrum, base)
      - currency: Stablecoin currency (usdc, eurc, dai, pyusd, usdt)
      - address: Valid blockchain address

      **At least one destination must be specified:**
      - external_account_id: External bank account
      - prefunded_account_id: Developer's prefunded account
      - bridge_wallet_id: Bridge wallet
      - destination_address: Crypto wallet address

      **Payment Rails:**
      Different payment rails have different requirements:
      - ACH: Requires external_account_id, supports destination_ach_reference
      - SEPA: Requires external_account_id, supports destination_sepa_reference
      - Wire: Requires external_account_id, supports destination_wire_message
      - Crypto: Requires destination_address, supports destination_blockchain_memo
    

### Example


```python
import devdraft
from devdraft.models.create_liquidation_address_dto import CreateLiquidationAddressDto
from devdraft.models.liquidation_address_response_dto import LiquidationAddressResponseDto
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
    api_instance = devdraft.LiquidationAddressesApi(api_client)
    customer_id = 'cust_123' # str | Unique identifier for the customer
    create_liquidation_address_dto = devdraft.CreateLiquidationAddressDto() # CreateLiquidationAddressDto | 

    try:
        # Create a new liquidation address for a customer
        api_response = api_instance.liquidation_address_controller_create_liquidation_address(customer_id, create_liquidation_address_dto)
        print("The response of LiquidationAddressesApi->liquidation_address_controller_create_liquidation_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiquidationAddressesApi->liquidation_address_controller_create_liquidation_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Unique identifier for the customer | 
 **create_liquidation_address_dto** | [**CreateLiquidationAddressDto**](CreateLiquidationAddressDto.md)|  | 

### Return type

[**LiquidationAddressResponseDto**](LiquidationAddressResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Liquidation address created successfully |  -  |
**400** | Invalid request data |  -  |
**404** | Customer not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **liquidation_address_controller_get_liquidation_address**
> LiquidationAddressResponseDto liquidation_address_controller_get_liquidation_address(customer_id, liquidation_address_id)

Get a specific liquidation address

Retrieve a specific liquidation address by its ID for a given customer.

### Example


```python
import devdraft
from devdraft.models.liquidation_address_response_dto import LiquidationAddressResponseDto
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
    api_instance = devdraft.LiquidationAddressesApi(api_client)
    customer_id = 'cust_123' # str | Unique identifier for the customer
    liquidation_address_id = 'la_generated_id_123' # str | Unique identifier for the liquidation address

    try:
        # Get a specific liquidation address
        api_response = api_instance.liquidation_address_controller_get_liquidation_address(customer_id, liquidation_address_id)
        print("The response of LiquidationAddressesApi->liquidation_address_controller_get_liquidation_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiquidationAddressesApi->liquidation_address_controller_get_liquidation_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Unique identifier for the customer | 
 **liquidation_address_id** | **str**| Unique identifier for the liquidation address | 

### Return type

[**LiquidationAddressResponseDto**](LiquidationAddressResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Liquidation address details |  -  |
**404** | Liquidation address not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **liquidation_address_controller_get_liquidation_addresses**
> List[LiquidationAddressResponseDto] liquidation_address_controller_get_liquidation_addresses(customer_id)

Get all liquidation addresses for a customer

Retrieve all liquidation addresses associated with a specific customer.

### Example


```python
import devdraft
from devdraft.models.liquidation_address_response_dto import LiquidationAddressResponseDto
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
    api_instance = devdraft.LiquidationAddressesApi(api_client)
    customer_id = 'cust_123' # str | Unique identifier for the customer

    try:
        # Get all liquidation addresses for a customer
        api_response = api_instance.liquidation_address_controller_get_liquidation_addresses(customer_id)
        print("The response of LiquidationAddressesApi->liquidation_address_controller_get_liquidation_addresses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiquidationAddressesApi->liquidation_address_controller_get_liquidation_addresses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Unique identifier for the customer | 

### Return type

[**List[LiquidationAddressResponseDto]**](LiquidationAddressResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of liquidation addresses |  -  |
**404** | Customer not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

