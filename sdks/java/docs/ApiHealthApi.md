# ApiHealthApi

All URIs are relative to *https://api.devdraft.ai*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**healthControllerCheckV0**](ApiHealthApi.md#healthControllerCheckV0) | **GET** /api/v0/health | Authenticated health check endpoint |
| [**healthControllerCheckV0WithHttpInfo**](ApiHealthApi.md#healthControllerCheckV0WithHttpInfo) | **GET** /api/v0/health | Authenticated health check endpoint |
| [**healthControllerPublicHealthCheckV0**](ApiHealthApi.md#healthControllerPublicHealthCheckV0) | **GET** /api/v0/health/public | Public health check endpoint |
| [**healthControllerPublicHealthCheckV0WithHttpInfo**](ApiHealthApi.md#healthControllerPublicHealthCheckV0WithHttpInfo) | **GET** /api/v0/health/public | Public health check endpoint |



## healthControllerCheckV0

> HealthResponseDto healthControllerCheckV0()

Authenticated health check endpoint

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiHealthApi;

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

        ApiHealthApi apiInstance = new ApiHealthApi(defaultClient);
        try {
            HealthResponseDto result = apiInstance.healthControllerCheckV0();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ApiHealthApi#healthControllerCheckV0");
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

[**HealthResponseDto**](HealthResponseDto.md)


### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Service is up and running |  -  |
| **401** | Unauthorized. Client key or secret is invalid or missing. |  -  |

## healthControllerCheckV0WithHttpInfo

> ApiResponse<HealthResponseDto> healthControllerCheckV0 healthControllerCheckV0WithHttpInfo()

Authenticated health check endpoint

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiHealthApi;

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

        ApiHealthApi apiInstance = new ApiHealthApi(defaultClient);
        try {
            ApiResponse<HealthResponseDto> response = apiInstance.healthControllerCheckV0WithHttpInfo();
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ApiHealthApi#healthControllerCheckV0");
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

ApiResponse<[**HealthResponseDto**](HealthResponseDto.md)>


### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Service is up and running |  -  |
| **401** | Unauthorized. Client key or secret is invalid or missing. |  -  |


## healthControllerPublicHealthCheckV0

> PublicHealthResponseDto healthControllerPublicHealthCheckV0()

Public health check endpoint

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiHealthApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://api.devdraft.ai");

        ApiHealthApi apiInstance = new ApiHealthApi(defaultClient);
        try {
            PublicHealthResponseDto result = apiInstance.healthControllerPublicHealthCheckV0();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ApiHealthApi#healthControllerPublicHealthCheckV0");
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

[**PublicHealthResponseDto**](PublicHealthResponseDto.md)


### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Basic service health check |  -  |

## healthControllerPublicHealthCheckV0WithHttpInfo

> ApiResponse<PublicHealthResponseDto> healthControllerPublicHealthCheckV0 healthControllerPublicHealthCheckV0WithHttpInfo()

Public health check endpoint

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiHealthApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://api.devdraft.ai");

        ApiHealthApi apiInstance = new ApiHealthApi(defaultClient);
        try {
            ApiResponse<PublicHealthResponseDto> response = apiInstance.healthControllerPublicHealthCheckV0WithHttpInfo();
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ApiHealthApi#healthControllerPublicHealthCheckV0");
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

ApiResponse<[**PublicHealthResponseDto**](PublicHealthResponseDto.md)>


### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Basic service health check |  -  |

