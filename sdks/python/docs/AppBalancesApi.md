# devdraft.AppBalancesApi

All URIs are relative to *https://api.devdraft.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**balance_controller_get_all_balances**](AppBalancesApi.md#balance_controller_get_all_balances) | **GET** /api/v0/balance | Get all stablecoin balances for an app
[**balance_controller_get_eurc_balance**](AppBalancesApi.md#balance_controller_get_eurc_balance) | **GET** /api/v0/balance/eurc | Get EURC balance for an app
[**balance_controller_get_usdc_balance**](AppBalancesApi.md#balance_controller_get_usdc_balance) | **GET** /api/v0/balance/usdc | Get USDC balance for an app


# **balance_controller_get_all_balances**
> AllBalancesResponse balance_controller_get_all_balances()

Get all stablecoin balances for an app

Retrieves both USDC and EURC balances across all wallets for the specified app.
    
This comprehensive endpoint provides:
- Complete USDC balance aggregation with detailed breakdown
- Complete EURC balance aggregation with detailed breakdown
- Total USD equivalent value across both currencies
- Individual wallet and chain-specific balance details

## Use Cases
- Complete financial dashboard overview
- Multi-currency balance reporting
- Comprehensive wallet management
- Cross-currency analytics and reporting

## Response Format
The response includes separate aggregations for each currency plus a combined
USD value estimate, providing complete visibility into stablecoin holdings.

### Example

* Api Key Authentication (x-client-secret):
* Api Key Authentication (x-client-key):

```python
import devdraft
from devdraft.models.all_balances_response import AllBalancesResponse
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
    api_instance = devdraft.AppBalancesApi(api_client)

    try:
        # Get all stablecoin balances for an app
        api_response = api_instance.balance_controller_get_all_balances()
        print("The response of AppBalancesApi->balance_controller_get_all_balances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppBalancesApi->balance_controller_get_all_balances: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AllBalancesResponse**](AllBalancesResponse.md)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All stablecoin balances retrieved successfully |  -  |
**401** | Unauthorized - Invalid or missing API credentials |  -  |
**404** | App not found or no access permission |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **balance_controller_get_eurc_balance**
> AggregatedBalanceResponse balance_controller_get_eurc_balance()

Get EURC balance for an app

Retrieves the total EURC balance across all wallets for the specified app.
    
This endpoint aggregates EURC balances from all associated wallets and provides:
- Total EURC balance across all chains and wallets
- Detailed breakdown by individual wallet and blockchain network
- Contract addresses and wallet identifiers for each balance

## Use Cases
- Dashboard balance display
- European market operations
- Euro-denominated financial reporting
- Cross-currency balance tracking

## Response Format
The response includes both the aggregated total and detailed breakdown, enabling
comprehensive euro stablecoin balance management.

### Example

* Api Key Authentication (x-client-secret):
* Api Key Authentication (x-client-key):

```python
import devdraft
from devdraft.models.aggregated_balance_response import AggregatedBalanceResponse
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
    api_instance = devdraft.AppBalancesApi(api_client)

    try:
        # Get EURC balance for an app
        api_response = api_instance.balance_controller_get_eurc_balance()
        print("The response of AppBalancesApi->balance_controller_get_eurc_balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppBalancesApi->balance_controller_get_eurc_balance: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AggregatedBalanceResponse**](AggregatedBalanceResponse.md)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | EURC balance retrieved successfully |  -  |
**401** | Unauthorized - Invalid or missing API credentials |  -  |
**404** | App not found or no access permission |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **balance_controller_get_usdc_balance**
> AggregatedBalanceResponse balance_controller_get_usdc_balance()

Get USDC balance for an app

Retrieves the total USDC balance across all wallets for the specified app.
    
This endpoint aggregates USDC balances from all associated wallets and provides:
- Total USDC balance across all chains and wallets
- Detailed breakdown by individual wallet and blockchain network
- Contract addresses and wallet identifiers for each balance

## Use Cases
- Dashboard balance display
- Financial reporting and reconciliation
- Real-time balance monitoring
- Multi-chain balance aggregation

## Response Format
The response includes both the aggregated total and detailed breakdown, allowing for
comprehensive balance tracking and wallet-specific analysis.

### Example

* Api Key Authentication (x-client-secret):
* Api Key Authentication (x-client-key):

```python
import devdraft
from devdraft.models.aggregated_balance_response import AggregatedBalanceResponse
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
    api_instance = devdraft.AppBalancesApi(api_client)

    try:
        # Get USDC balance for an app
        api_response = api_instance.balance_controller_get_usdc_balance()
        print("The response of AppBalancesApi->balance_controller_get_usdc_balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppBalancesApi->balance_controller_get_usdc_balance: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AggregatedBalanceResponse**](AggregatedBalanceResponse.md)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | USDC balance retrieved successfully |  -  |
**401** | Unauthorized - Invalid or missing API credentials |  -  |
**404** | App not found or no access permission |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

