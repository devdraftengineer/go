# TransfersApi

All URIs are relative to *https://api.devdraft.ai*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**transferControllerCreateDirectBankTransfer**](TransfersApi.md#transferControllerCreateDirectBankTransfer) | **POST** /api/v0/transfers/direct-bank | Create a direct bank transfer |
| [**transferControllerCreateDirectBankTransferWithHttpInfo**](TransfersApi.md#transferControllerCreateDirectBankTransferWithHttpInfo) | **POST** /api/v0/transfers/direct-bank | Create a direct bank transfer |
| [**transferControllerCreateDirectWalletTransfer**](TransfersApi.md#transferControllerCreateDirectWalletTransfer) | **POST** /api/v0/transfers/direct-wallet | Create a direct wallet transfer |
| [**transferControllerCreateDirectWalletTransferWithHttpInfo**](TransfersApi.md#transferControllerCreateDirectWalletTransferWithHttpInfo) | **POST** /api/v0/transfers/direct-wallet | Create a direct wallet transfer |
| [**transferControllerCreateExternalBankTransfer**](TransfersApi.md#transferControllerCreateExternalBankTransfer) | **POST** /api/v0/transfers/external-bank-transfer | Create an external bank transfer |
| [**transferControllerCreateExternalBankTransferWithHttpInfo**](TransfersApi.md#transferControllerCreateExternalBankTransferWithHttpInfo) | **POST** /api/v0/transfers/external-bank-transfer | Create an external bank transfer |
| [**transferControllerCreateExternalStablecoinTransfer**](TransfersApi.md#transferControllerCreateExternalStablecoinTransfer) | **POST** /api/v0/transfers/external-stablecoin-transfer | Create an external stablecoin transfer |
| [**transferControllerCreateExternalStablecoinTransferWithHttpInfo**](TransfersApi.md#transferControllerCreateExternalStablecoinTransferWithHttpInfo) | **POST** /api/v0/transfers/external-stablecoin-transfer | Create an external stablecoin transfer |
| [**transferControllerCreateStablecoinConversion**](TransfersApi.md#transferControllerCreateStablecoinConversion) | **POST** /api/v0/transfers/stablecoin-conversion | Create a stablecoin conversion |
| [**transferControllerCreateStablecoinConversionWithHttpInfo**](TransfersApi.md#transferControllerCreateStablecoinConversionWithHttpInfo) | **POST** /api/v0/transfers/stablecoin-conversion | Create a stablecoin conversion |



## transferControllerCreateDirectBankTransfer

> void transferControllerCreateDirectBankTransfer(createDirectBankTransferDto)

Create a direct bank transfer

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransfersApi;

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

        TransfersApi apiInstance = new TransfersApi(defaultClient);
        CreateDirectBankTransferDto createDirectBankTransferDto = new CreateDirectBankTransferDto(); // CreateDirectBankTransferDto | 
        try {
            apiInstance.transferControllerCreateDirectBankTransfer(createDirectBankTransferDto);
        } catch (ApiException e) {
            System.err.println("Exception when calling TransfersApi#transferControllerCreateDirectBankTransfer");
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
| **createDirectBankTransferDto** | [**CreateDirectBankTransferDto**](CreateDirectBankTransferDto.md)|  | |

### Return type


null (empty response body)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The transfer has been successfully created. |  -  |
| **400** | Bad Request - Invalid input |  -  |
| **404** | Not Found - Bridge wallet not found |  -  |

## transferControllerCreateDirectBankTransferWithHttpInfo

> ApiResponse<Void> transferControllerCreateDirectBankTransfer transferControllerCreateDirectBankTransferWithHttpInfo(createDirectBankTransferDto)

Create a direct bank transfer

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransfersApi;

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

        TransfersApi apiInstance = new TransfersApi(defaultClient);
        CreateDirectBankTransferDto createDirectBankTransferDto = new CreateDirectBankTransferDto(); // CreateDirectBankTransferDto | 
        try {
            ApiResponse<Void> response = apiInstance.transferControllerCreateDirectBankTransferWithHttpInfo(createDirectBankTransferDto);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling TransfersApi#transferControllerCreateDirectBankTransfer");
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
| **createDirectBankTransferDto** | [**CreateDirectBankTransferDto**](CreateDirectBankTransferDto.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The transfer has been successfully created. |  -  |
| **400** | Bad Request - Invalid input |  -  |
| **404** | Not Found - Bridge wallet not found |  -  |


## transferControllerCreateDirectWalletTransfer

> void transferControllerCreateDirectWalletTransfer(createDirectWalletTransferDto)

Create a direct wallet transfer

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransfersApi;

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

        TransfersApi apiInstance = new TransfersApi(defaultClient);
        CreateDirectWalletTransferDto createDirectWalletTransferDto = new CreateDirectWalletTransferDto(); // CreateDirectWalletTransferDto | 
        try {
            apiInstance.transferControllerCreateDirectWalletTransfer(createDirectWalletTransferDto);
        } catch (ApiException e) {
            System.err.println("Exception when calling TransfersApi#transferControllerCreateDirectWalletTransfer");
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
| **createDirectWalletTransferDto** | [**CreateDirectWalletTransferDto**](CreateDirectWalletTransferDto.md)|  | |

### Return type


null (empty response body)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The transfer has been successfully created. |  -  |
| **400** | Bad Request - Invalid input |  -  |
| **404** | Not Found - Bridge wallet not found |  -  |

## transferControllerCreateDirectWalletTransferWithHttpInfo

> ApiResponse<Void> transferControllerCreateDirectWalletTransfer transferControllerCreateDirectWalletTransferWithHttpInfo(createDirectWalletTransferDto)

Create a direct wallet transfer

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransfersApi;

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

        TransfersApi apiInstance = new TransfersApi(defaultClient);
        CreateDirectWalletTransferDto createDirectWalletTransferDto = new CreateDirectWalletTransferDto(); // CreateDirectWalletTransferDto | 
        try {
            ApiResponse<Void> response = apiInstance.transferControllerCreateDirectWalletTransferWithHttpInfo(createDirectWalletTransferDto);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling TransfersApi#transferControllerCreateDirectWalletTransfer");
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
| **createDirectWalletTransferDto** | [**CreateDirectWalletTransferDto**](CreateDirectWalletTransferDto.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The transfer has been successfully created. |  -  |
| **400** | Bad Request - Invalid input |  -  |
| **404** | Not Found - Bridge wallet not found |  -  |


## transferControllerCreateExternalBankTransfer

> void transferControllerCreateExternalBankTransfer(createExternalBankTransferDto)

Create an external bank transfer

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransfersApi;

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

        TransfersApi apiInstance = new TransfersApi(defaultClient);
        CreateExternalBankTransferDto createExternalBankTransferDto = new CreateExternalBankTransferDto(); // CreateExternalBankTransferDto | 
        try {
            apiInstance.transferControllerCreateExternalBankTransfer(createExternalBankTransferDto);
        } catch (ApiException e) {
            System.err.println("Exception when calling TransfersApi#transferControllerCreateExternalBankTransfer");
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
| **createExternalBankTransferDto** | [**CreateExternalBankTransferDto**](CreateExternalBankTransferDto.md)|  | |

### Return type


null (empty response body)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The external bank transfer has been successfully created. |  -  |
| **400** | Bad Request - Invalid input |  -  |
| **404** | Not Found - Bridge wallet not found |  -  |

## transferControllerCreateExternalBankTransferWithHttpInfo

> ApiResponse<Void> transferControllerCreateExternalBankTransfer transferControllerCreateExternalBankTransferWithHttpInfo(createExternalBankTransferDto)

Create an external bank transfer

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransfersApi;

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

        TransfersApi apiInstance = new TransfersApi(defaultClient);
        CreateExternalBankTransferDto createExternalBankTransferDto = new CreateExternalBankTransferDto(); // CreateExternalBankTransferDto | 
        try {
            ApiResponse<Void> response = apiInstance.transferControllerCreateExternalBankTransferWithHttpInfo(createExternalBankTransferDto);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling TransfersApi#transferControllerCreateExternalBankTransfer");
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
| **createExternalBankTransferDto** | [**CreateExternalBankTransferDto**](CreateExternalBankTransferDto.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The external bank transfer has been successfully created. |  -  |
| **400** | Bad Request - Invalid input |  -  |
| **404** | Not Found - Bridge wallet not found |  -  |


## transferControllerCreateExternalStablecoinTransfer

> void transferControllerCreateExternalStablecoinTransfer(createExternalStablecoinTransferDto)

Create an external stablecoin transfer

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransfersApi;

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

        TransfersApi apiInstance = new TransfersApi(defaultClient);
        CreateExternalStablecoinTransferDto createExternalStablecoinTransferDto = new CreateExternalStablecoinTransferDto(); // CreateExternalStablecoinTransferDto | 
        try {
            apiInstance.transferControllerCreateExternalStablecoinTransfer(createExternalStablecoinTransferDto);
        } catch (ApiException e) {
            System.err.println("Exception when calling TransfersApi#transferControllerCreateExternalStablecoinTransfer");
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
| **createExternalStablecoinTransferDto** | [**CreateExternalStablecoinTransferDto**](CreateExternalStablecoinTransferDto.md)|  | |

### Return type


null (empty response body)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The external stablecoin transfer has been successfully created. |  -  |
| **400** | Bad Request - Invalid input |  -  |
| **404** | Not Found - Bridge wallet not found |  -  |

## transferControllerCreateExternalStablecoinTransferWithHttpInfo

> ApiResponse<Void> transferControllerCreateExternalStablecoinTransfer transferControllerCreateExternalStablecoinTransferWithHttpInfo(createExternalStablecoinTransferDto)

Create an external stablecoin transfer

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransfersApi;

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

        TransfersApi apiInstance = new TransfersApi(defaultClient);
        CreateExternalStablecoinTransferDto createExternalStablecoinTransferDto = new CreateExternalStablecoinTransferDto(); // CreateExternalStablecoinTransferDto | 
        try {
            ApiResponse<Void> response = apiInstance.transferControllerCreateExternalStablecoinTransferWithHttpInfo(createExternalStablecoinTransferDto);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling TransfersApi#transferControllerCreateExternalStablecoinTransfer");
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
| **createExternalStablecoinTransferDto** | [**CreateExternalStablecoinTransferDto**](CreateExternalStablecoinTransferDto.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The external stablecoin transfer has been successfully created. |  -  |
| **400** | Bad Request - Invalid input |  -  |
| **404** | Not Found - Bridge wallet not found |  -  |


## transferControllerCreateStablecoinConversion

> void transferControllerCreateStablecoinConversion(createStablecoinConversionDto)

Create a stablecoin conversion

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransfersApi;

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

        TransfersApi apiInstance = new TransfersApi(defaultClient);
        CreateStablecoinConversionDto createStablecoinConversionDto = new CreateStablecoinConversionDto(); // CreateStablecoinConversionDto | 
        try {
            apiInstance.transferControllerCreateStablecoinConversion(createStablecoinConversionDto);
        } catch (ApiException e) {
            System.err.println("Exception when calling TransfersApi#transferControllerCreateStablecoinConversion");
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
| **createStablecoinConversionDto** | [**CreateStablecoinConversionDto**](CreateStablecoinConversionDto.md)|  | |

### Return type


null (empty response body)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The conversion has been successfully created. |  -  |
| **400** | Bad Request - Invalid input |  -  |
| **404** | Not Found - Bridge wallet not found |  -  |

## transferControllerCreateStablecoinConversionWithHttpInfo

> ApiResponse<Void> transferControllerCreateStablecoinConversion transferControllerCreateStablecoinConversionWithHttpInfo(createStablecoinConversionDto)

Create a stablecoin conversion

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransfersApi;

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

        TransfersApi apiInstance = new TransfersApi(defaultClient);
        CreateStablecoinConversionDto createStablecoinConversionDto = new CreateStablecoinConversionDto(); // CreateStablecoinConversionDto | 
        try {
            ApiResponse<Void> response = apiInstance.transferControllerCreateStablecoinConversionWithHttpInfo(createStablecoinConversionDto);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling TransfersApi#transferControllerCreateStablecoinConversion");
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
| **createStablecoinConversionDto** | [**CreateStablecoinConversionDto**](CreateStablecoinConversionDto.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The conversion has been successfully created. |  -  |
| **400** | Bad Request - Invalid input |  -  |
| **404** | Not Found - Bridge wallet not found |  -  |

