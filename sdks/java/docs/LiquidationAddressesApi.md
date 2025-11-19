# LiquidationAddressesApi

All URIs are relative to *https://api.devdraft.ai*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**liquidationAddressControllerCreateLiquidationAddress**](LiquidationAddressesApi.md#liquidationAddressControllerCreateLiquidationAddress) | **POST** /api/v0/customers/{customerId}/liquidation_addresses | Create a new liquidation address for a customer |
| [**liquidationAddressControllerCreateLiquidationAddressWithHttpInfo**](LiquidationAddressesApi.md#liquidationAddressControllerCreateLiquidationAddressWithHttpInfo) | **POST** /api/v0/customers/{customerId}/liquidation_addresses | Create a new liquidation address for a customer |
| [**liquidationAddressControllerGetLiquidationAddress**](LiquidationAddressesApi.md#liquidationAddressControllerGetLiquidationAddress) | **GET** /api/v0/customers/{customerId}/liquidation_addresses/{liquidationAddressId} | Get a specific liquidation address |
| [**liquidationAddressControllerGetLiquidationAddressWithHttpInfo**](LiquidationAddressesApi.md#liquidationAddressControllerGetLiquidationAddressWithHttpInfo) | **GET** /api/v0/customers/{customerId}/liquidation_addresses/{liquidationAddressId} | Get a specific liquidation address |
| [**liquidationAddressControllerGetLiquidationAddresses**](LiquidationAddressesApi.md#liquidationAddressControllerGetLiquidationAddresses) | **GET** /api/v0/customers/{customerId}/liquidation_addresses | Get all liquidation addresses for a customer |
| [**liquidationAddressControllerGetLiquidationAddressesWithHttpInfo**](LiquidationAddressesApi.md#liquidationAddressControllerGetLiquidationAddressesWithHttpInfo) | **GET** /api/v0/customers/{customerId}/liquidation_addresses | Get all liquidation addresses for a customer |



## liquidationAddressControllerCreateLiquidationAddress

> LiquidationAddressResponseDto liquidationAddressControllerCreateLiquidationAddress(customerId, createLiquidationAddressDto)

Create a new liquidation address for a customer

       Create a new liquidation address for a customer. Liquidation addresses allow        customers to automatically liquidate cryptocurrency holdings to fiat or other        stablecoins based on configured parameters.        **Required fields:**       - chain: Blockchain network (ethereum, polygon, arbitrum, base)       - currency: Stablecoin currency (usdc, eurc, dai, pyusd, usdt)       - address: Valid blockchain address        **At least one destination must be specified:**       - external_account_id: External bank account       - prefunded_account_id: Developer&#39;s prefunded account       - bridge_wallet_id: Bridge wallet       - destination_address: Crypto wallet address        **Payment Rails:**       Different payment rails have different requirements:       - ACH: Requires external_account_id, supports destination_ach_reference       - SEPA: Requires external_account_id, supports destination_sepa_reference       - Wire: Requires external_account_id, supports destination_wire_message       - Crypto: Requires destination_address, supports destination_blockchain_memo     

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LiquidationAddressesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://api.devdraft.ai");

        LiquidationAddressesApi apiInstance = new LiquidationAddressesApi(defaultClient);
        String customerId = "cust_123"; // String | Unique identifier for the customer
        CreateLiquidationAddressDto createLiquidationAddressDto = new CreateLiquidationAddressDto(); // CreateLiquidationAddressDto | 
        try {
            LiquidationAddressResponseDto result = apiInstance.liquidationAddressControllerCreateLiquidationAddress(customerId, createLiquidationAddressDto);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling LiquidationAddressesApi#liquidationAddressControllerCreateLiquidationAddress");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **customerId** | **String**| Unique identifier for the customer | |
| **createLiquidationAddressDto** | [**CreateLiquidationAddressDto**](CreateLiquidationAddressDto.md)|  | |

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
| **201** | Liquidation address created successfully |  -  |
| **400** | Invalid request data |  -  |
| **404** | Customer not found |  -  |
| **500** | Internal server error |  -  |

## liquidationAddressControllerCreateLiquidationAddressWithHttpInfo

> ApiResponse<LiquidationAddressResponseDto> liquidationAddressControllerCreateLiquidationAddress liquidationAddressControllerCreateLiquidationAddressWithHttpInfo(customerId, createLiquidationAddressDto)

Create a new liquidation address for a customer

       Create a new liquidation address for a customer. Liquidation addresses allow        customers to automatically liquidate cryptocurrency holdings to fiat or other        stablecoins based on configured parameters.        **Required fields:**       - chain: Blockchain network (ethereum, polygon, arbitrum, base)       - currency: Stablecoin currency (usdc, eurc, dai, pyusd, usdt)       - address: Valid blockchain address        **At least one destination must be specified:**       - external_account_id: External bank account       - prefunded_account_id: Developer&#39;s prefunded account       - bridge_wallet_id: Bridge wallet       - destination_address: Crypto wallet address        **Payment Rails:**       Different payment rails have different requirements:       - ACH: Requires external_account_id, supports destination_ach_reference       - SEPA: Requires external_account_id, supports destination_sepa_reference       - Wire: Requires external_account_id, supports destination_wire_message       - Crypto: Requires destination_address, supports destination_blockchain_memo     

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LiquidationAddressesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://api.devdraft.ai");

        LiquidationAddressesApi apiInstance = new LiquidationAddressesApi(defaultClient);
        String customerId = "cust_123"; // String | Unique identifier for the customer
        CreateLiquidationAddressDto createLiquidationAddressDto = new CreateLiquidationAddressDto(); // CreateLiquidationAddressDto | 
        try {
            ApiResponse<LiquidationAddressResponseDto> response = apiInstance.liquidationAddressControllerCreateLiquidationAddressWithHttpInfo(customerId, createLiquidationAddressDto);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling LiquidationAddressesApi#liquidationAddressControllerCreateLiquidationAddress");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **customerId** | **String**| Unique identifier for the customer | |
| **createLiquidationAddressDto** | [**CreateLiquidationAddressDto**](CreateLiquidationAddressDto.md)|  | |

### Return type

ApiResponse<[**LiquidationAddressResponseDto**](LiquidationAddressResponseDto.md)>


### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Liquidation address created successfully |  -  |
| **400** | Invalid request data |  -  |
| **404** | Customer not found |  -  |
| **500** | Internal server error |  -  |


## liquidationAddressControllerGetLiquidationAddress

> LiquidationAddressResponseDto liquidationAddressControllerGetLiquidationAddress(customerId, liquidationAddressId)

Get a specific liquidation address

Retrieve a specific liquidation address by its ID for a given customer.

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LiquidationAddressesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://api.devdraft.ai");

        LiquidationAddressesApi apiInstance = new LiquidationAddressesApi(defaultClient);
        String customerId = "cust_123"; // String | Unique identifier for the customer
        String liquidationAddressId = "la_generated_id_123"; // String | Unique identifier for the liquidation address
        try {
            LiquidationAddressResponseDto result = apiInstance.liquidationAddressControllerGetLiquidationAddress(customerId, liquidationAddressId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling LiquidationAddressesApi#liquidationAddressControllerGetLiquidationAddress");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **customerId** | **String**| Unique identifier for the customer | |
| **liquidationAddressId** | **String**| Unique identifier for the liquidation address | |

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
| **200** | Liquidation address details |  -  |
| **404** | Liquidation address not found |  -  |
| **500** | Internal server error |  -  |

## liquidationAddressControllerGetLiquidationAddressWithHttpInfo

> ApiResponse<LiquidationAddressResponseDto> liquidationAddressControllerGetLiquidationAddress liquidationAddressControllerGetLiquidationAddressWithHttpInfo(customerId, liquidationAddressId)

Get a specific liquidation address

Retrieve a specific liquidation address by its ID for a given customer.

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LiquidationAddressesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://api.devdraft.ai");

        LiquidationAddressesApi apiInstance = new LiquidationAddressesApi(defaultClient);
        String customerId = "cust_123"; // String | Unique identifier for the customer
        String liquidationAddressId = "la_generated_id_123"; // String | Unique identifier for the liquidation address
        try {
            ApiResponse<LiquidationAddressResponseDto> response = apiInstance.liquidationAddressControllerGetLiquidationAddressWithHttpInfo(customerId, liquidationAddressId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling LiquidationAddressesApi#liquidationAddressControllerGetLiquidationAddress");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **customerId** | **String**| Unique identifier for the customer | |
| **liquidationAddressId** | **String**| Unique identifier for the liquidation address | |

### Return type

ApiResponse<[**LiquidationAddressResponseDto**](LiquidationAddressResponseDto.md)>


### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Liquidation address details |  -  |
| **404** | Liquidation address not found |  -  |
| **500** | Internal server error |  -  |


## liquidationAddressControllerGetLiquidationAddresses

> List<LiquidationAddressResponseDto> liquidationAddressControllerGetLiquidationAddresses(customerId)

Get all liquidation addresses for a customer

Retrieve all liquidation addresses associated with a specific customer.

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LiquidationAddressesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://api.devdraft.ai");

        LiquidationAddressesApi apiInstance = new LiquidationAddressesApi(defaultClient);
        String customerId = "cust_123"; // String | Unique identifier for the customer
        try {
            List<LiquidationAddressResponseDto> result = apiInstance.liquidationAddressControllerGetLiquidationAddresses(customerId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling LiquidationAddressesApi#liquidationAddressControllerGetLiquidationAddresses");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **customerId** | **String**| Unique identifier for the customer | |

### Return type

[**List&lt;LiquidationAddressResponseDto&gt;**](LiquidationAddressResponseDto.md)


### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of liquidation addresses |  -  |
| **404** | Customer not found |  -  |
| **500** | Internal server error |  -  |

## liquidationAddressControllerGetLiquidationAddressesWithHttpInfo

> ApiResponse<List<LiquidationAddressResponseDto>> liquidationAddressControllerGetLiquidationAddresses liquidationAddressControllerGetLiquidationAddressesWithHttpInfo(customerId)

Get all liquidation addresses for a customer

Retrieve all liquidation addresses associated with a specific customer.

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LiquidationAddressesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://api.devdraft.ai");

        LiquidationAddressesApi apiInstance = new LiquidationAddressesApi(defaultClient);
        String customerId = "cust_123"; // String | Unique identifier for the customer
        try {
            ApiResponse<List<LiquidationAddressResponseDto>> response = apiInstance.liquidationAddressControllerGetLiquidationAddressesWithHttpInfo(customerId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling LiquidationAddressesApi#liquidationAddressControllerGetLiquidationAddresses");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **customerId** | **String**| Unique identifier for the customer | |

### Return type

ApiResponse<[**List&lt;LiquidationAddressResponseDto&gt;**](LiquidationAddressResponseDto.md)>


### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of liquidation addresses |  -  |
| **404** | Customer not found |  -  |
| **500** | Internal server error |  -  |

