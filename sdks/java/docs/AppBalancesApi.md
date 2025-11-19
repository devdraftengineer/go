# AppBalancesApi

All URIs are relative to *https://api.devdraft.ai*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**balanceControllerGetAllBalances**](AppBalancesApi.md#balanceControllerGetAllBalances) | **GET** /api/v0/balance | Get all stablecoin balances for an app |
| [**balanceControllerGetAllBalancesWithHttpInfo**](AppBalancesApi.md#balanceControllerGetAllBalancesWithHttpInfo) | **GET** /api/v0/balance | Get all stablecoin balances for an app |
| [**balanceControllerGetEURCBalance**](AppBalancesApi.md#balanceControllerGetEURCBalance) | **GET** /api/v0/balance/eurc | Get EURC balance for an app |
| [**balanceControllerGetEURCBalanceWithHttpInfo**](AppBalancesApi.md#balanceControllerGetEURCBalanceWithHttpInfo) | **GET** /api/v0/balance/eurc | Get EURC balance for an app |
| [**balanceControllerGetUSDCBalance**](AppBalancesApi.md#balanceControllerGetUSDCBalance) | **GET** /api/v0/balance/usdc | Get USDC balance for an app |
| [**balanceControllerGetUSDCBalanceWithHttpInfo**](AppBalancesApi.md#balanceControllerGetUSDCBalanceWithHttpInfo) | **GET** /api/v0/balance/usdc | Get USDC balance for an app |



## balanceControllerGetAllBalances

> AllBalancesResponse balanceControllerGetAllBalances()

Get all stablecoin balances for an app

Retrieves both USDC and EURC balances across all wallets for the specified app.      This comprehensive endpoint provides: - Complete USDC balance aggregation with detailed breakdown - Complete EURC balance aggregation with detailed breakdown - Total USD equivalent value across both currencies - Individual wallet and chain-specific balance details  ## Use Cases - Complete financial dashboard overview - Multi-currency balance reporting - Comprehensive wallet management - Cross-currency analytics and reporting  ## Response Format The response includes separate aggregations for each currency plus a combined USD value estimate, providing complete visibility into stablecoin holdings.

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppBalancesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://api.devdraft.ai");
        
        // Configure API key authorization: x-client-secret
        ApiKeyAuth x-client-secret = (ApiKeyAuth) defaultClient.getAuthentication("x-client-secret");
        x-client-secret.setApiKey("YOUR API KEY");
        // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
        //x-client-secret.setApiKeyPrefix("Token");

        // Configure API key authorization: x-client-key
        ApiKeyAuth x-client-key = (ApiKeyAuth) defaultClient.getAuthentication("x-client-key");
        x-client-key.setApiKey("YOUR API KEY");
        // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
        //x-client-key.setApiKeyPrefix("Token");

        AppBalancesApi apiInstance = new AppBalancesApi(defaultClient);
        try {
            AllBalancesResponse result = apiInstance.balanceControllerGetAllBalances();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AppBalancesApi#balanceControllerGetAllBalances");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
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
| **200** | All stablecoin balances retrieved successfully |  -  |
| **401** | Unauthorized - Invalid or missing API credentials |  -  |
| **404** | App not found or no access permission |  -  |
| **500** | Internal server error |  -  |

## balanceControllerGetAllBalancesWithHttpInfo

> ApiResponse<AllBalancesResponse> balanceControllerGetAllBalances balanceControllerGetAllBalancesWithHttpInfo()

Get all stablecoin balances for an app

Retrieves both USDC and EURC balances across all wallets for the specified app.      This comprehensive endpoint provides: - Complete USDC balance aggregation with detailed breakdown - Complete EURC balance aggregation with detailed breakdown - Total USD equivalent value across both currencies - Individual wallet and chain-specific balance details  ## Use Cases - Complete financial dashboard overview - Multi-currency balance reporting - Comprehensive wallet management - Cross-currency analytics and reporting  ## Response Format The response includes separate aggregations for each currency plus a combined USD value estimate, providing complete visibility into stablecoin holdings.

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppBalancesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://api.devdraft.ai");
        
        // Configure API key authorization: x-client-secret
        ApiKeyAuth x-client-secret = (ApiKeyAuth) defaultClient.getAuthentication("x-client-secret");
        x-client-secret.setApiKey("YOUR API KEY");
        // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
        //x-client-secret.setApiKeyPrefix("Token");

        // Configure API key authorization: x-client-key
        ApiKeyAuth x-client-key = (ApiKeyAuth) defaultClient.getAuthentication("x-client-key");
        x-client-key.setApiKey("YOUR API KEY");
        // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
        //x-client-key.setApiKeyPrefix("Token");

        AppBalancesApi apiInstance = new AppBalancesApi(defaultClient);
        try {
            ApiResponse<AllBalancesResponse> response = apiInstance.balanceControllerGetAllBalancesWithHttpInfo();
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AppBalancesApi#balanceControllerGetAllBalances");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

ApiResponse<[**AllBalancesResponse**](AllBalancesResponse.md)>


### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All stablecoin balances retrieved successfully |  -  |
| **401** | Unauthorized - Invalid or missing API credentials |  -  |
| **404** | App not found or no access permission |  -  |
| **500** | Internal server error |  -  |


## balanceControllerGetEURCBalance

> AggregatedBalanceResponse balanceControllerGetEURCBalance()

Get EURC balance for an app

Retrieves the total EURC balance across all wallets for the specified app.      This endpoint aggregates EURC balances from all associated wallets and provides: - Total EURC balance across all chains and wallets - Detailed breakdown by individual wallet and blockchain network - Contract addresses and wallet identifiers for each balance  ## Use Cases - Dashboard balance display - European market operations - Euro-denominated financial reporting - Cross-currency balance tracking  ## Response Format The response includes both the aggregated total and detailed breakdown, enabling comprehensive euro stablecoin balance management.

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppBalancesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://api.devdraft.ai");
        
        // Configure API key authorization: x-client-secret
        ApiKeyAuth x-client-secret = (ApiKeyAuth) defaultClient.getAuthentication("x-client-secret");
        x-client-secret.setApiKey("YOUR API KEY");
        // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
        //x-client-secret.setApiKeyPrefix("Token");

        // Configure API key authorization: x-client-key
        ApiKeyAuth x-client-key = (ApiKeyAuth) defaultClient.getAuthentication("x-client-key");
        x-client-key.setApiKey("YOUR API KEY");
        // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
        //x-client-key.setApiKeyPrefix("Token");

        AppBalancesApi apiInstance = new AppBalancesApi(defaultClient);
        try {
            AggregatedBalanceResponse result = apiInstance.balanceControllerGetEURCBalance();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AppBalancesApi#balanceControllerGetEURCBalance");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
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
| **200** | EURC balance retrieved successfully |  -  |
| **401** | Unauthorized - Invalid or missing API credentials |  -  |
| **404** | App not found or no access permission |  -  |
| **500** | Internal server error |  -  |

## balanceControllerGetEURCBalanceWithHttpInfo

> ApiResponse<AggregatedBalanceResponse> balanceControllerGetEURCBalance balanceControllerGetEURCBalanceWithHttpInfo()

Get EURC balance for an app

Retrieves the total EURC balance across all wallets for the specified app.      This endpoint aggregates EURC balances from all associated wallets and provides: - Total EURC balance across all chains and wallets - Detailed breakdown by individual wallet and blockchain network - Contract addresses and wallet identifiers for each balance  ## Use Cases - Dashboard balance display - European market operations - Euro-denominated financial reporting - Cross-currency balance tracking  ## Response Format The response includes both the aggregated total and detailed breakdown, enabling comprehensive euro stablecoin balance management.

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppBalancesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://api.devdraft.ai");
        
        // Configure API key authorization: x-client-secret
        ApiKeyAuth x-client-secret = (ApiKeyAuth) defaultClient.getAuthentication("x-client-secret");
        x-client-secret.setApiKey("YOUR API KEY");
        // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
        //x-client-secret.setApiKeyPrefix("Token");

        // Configure API key authorization: x-client-key
        ApiKeyAuth x-client-key = (ApiKeyAuth) defaultClient.getAuthentication("x-client-key");
        x-client-key.setApiKey("YOUR API KEY");
        // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
        //x-client-key.setApiKeyPrefix("Token");

        AppBalancesApi apiInstance = new AppBalancesApi(defaultClient);
        try {
            ApiResponse<AggregatedBalanceResponse> response = apiInstance.balanceControllerGetEURCBalanceWithHttpInfo();
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AppBalancesApi#balanceControllerGetEURCBalance");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

ApiResponse<[**AggregatedBalanceResponse**](AggregatedBalanceResponse.md)>


### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | EURC balance retrieved successfully |  -  |
| **401** | Unauthorized - Invalid or missing API credentials |  -  |
| **404** | App not found or no access permission |  -  |
| **500** | Internal server error |  -  |


## balanceControllerGetUSDCBalance

> AggregatedBalanceResponse balanceControllerGetUSDCBalance()

Get USDC balance for an app

Retrieves the total USDC balance across all wallets for the specified app.      This endpoint aggregates USDC balances from all associated wallets and provides: - Total USDC balance across all chains and wallets - Detailed breakdown by individual wallet and blockchain network - Contract addresses and wallet identifiers for each balance  ## Use Cases - Dashboard balance display - Financial reporting and reconciliation - Real-time balance monitoring - Multi-chain balance aggregation  ## Response Format The response includes both the aggregated total and detailed breakdown, allowing for comprehensive balance tracking and wallet-specific analysis.

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppBalancesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://api.devdraft.ai");
        
        // Configure API key authorization: x-client-secret
        ApiKeyAuth x-client-secret = (ApiKeyAuth) defaultClient.getAuthentication("x-client-secret");
        x-client-secret.setApiKey("YOUR API KEY");
        // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
        //x-client-secret.setApiKeyPrefix("Token");

        // Configure API key authorization: x-client-key
        ApiKeyAuth x-client-key = (ApiKeyAuth) defaultClient.getAuthentication("x-client-key");
        x-client-key.setApiKey("YOUR API KEY");
        // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
        //x-client-key.setApiKeyPrefix("Token");

        AppBalancesApi apiInstance = new AppBalancesApi(defaultClient);
        try {
            AggregatedBalanceResponse result = apiInstance.balanceControllerGetUSDCBalance();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AppBalancesApi#balanceControllerGetUSDCBalance");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
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
| **200** | USDC balance retrieved successfully |  -  |
| **401** | Unauthorized - Invalid or missing API credentials |  -  |
| **404** | App not found or no access permission |  -  |
| **500** | Internal server error |  -  |

## balanceControllerGetUSDCBalanceWithHttpInfo

> ApiResponse<AggregatedBalanceResponse> balanceControllerGetUSDCBalance balanceControllerGetUSDCBalanceWithHttpInfo()

Get USDC balance for an app

Retrieves the total USDC balance across all wallets for the specified app.      This endpoint aggregates USDC balances from all associated wallets and provides: - Total USDC balance across all chains and wallets - Detailed breakdown by individual wallet and blockchain network - Contract addresses and wallet identifiers for each balance  ## Use Cases - Dashboard balance display - Financial reporting and reconciliation - Real-time balance monitoring - Multi-chain balance aggregation  ## Response Format The response includes both the aggregated total and detailed breakdown, allowing for comprehensive balance tracking and wallet-specific analysis.

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppBalancesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://api.devdraft.ai");
        
        // Configure API key authorization: x-client-secret
        ApiKeyAuth x-client-secret = (ApiKeyAuth) defaultClient.getAuthentication("x-client-secret");
        x-client-secret.setApiKey("YOUR API KEY");
        // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
        //x-client-secret.setApiKeyPrefix("Token");

        // Configure API key authorization: x-client-key
        ApiKeyAuth x-client-key = (ApiKeyAuth) defaultClient.getAuthentication("x-client-key");
        x-client-key.setApiKey("YOUR API KEY");
        // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
        //x-client-key.setApiKeyPrefix("Token");

        AppBalancesApi apiInstance = new AppBalancesApi(defaultClient);
        try {
            ApiResponse<AggregatedBalanceResponse> response = apiInstance.balanceControllerGetUSDCBalanceWithHttpInfo();
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AppBalancesApi#balanceControllerGetUSDCBalance");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

ApiResponse<[**AggregatedBalanceResponse**](AggregatedBalanceResponse.md)>


### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | USDC balance retrieved successfully |  -  |
| **401** | Unauthorized - Invalid or missing API credentials |  -  |
| **404** | App not found or no access permission |  -  |
| **500** | Internal server error |  -  |

