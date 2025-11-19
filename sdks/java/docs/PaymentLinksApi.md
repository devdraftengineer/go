# PaymentLinksApi

All URIs are relative to *https://api.devdraft.ai*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**paymentLinksControllerCreate**](PaymentLinksApi.md#paymentLinksControllerCreate) | **POST** /api/v0/payment-links | Create a new payment link |
| [**paymentLinksControllerCreateWithHttpInfo**](PaymentLinksApi.md#paymentLinksControllerCreateWithHttpInfo) | **POST** /api/v0/payment-links | Create a new payment link |
| [**paymentLinksControllerFindAll**](PaymentLinksApi.md#paymentLinksControllerFindAll) | **GET** /api/v0/payment-links | Get all payment links |
| [**paymentLinksControllerFindAllWithHttpInfo**](PaymentLinksApi.md#paymentLinksControllerFindAllWithHttpInfo) | **GET** /api/v0/payment-links | Get all payment links |
| [**paymentLinksControllerFindOne**](PaymentLinksApi.md#paymentLinksControllerFindOne) | **GET** /api/v0/payment-links/{id} | Get a payment link by ID |
| [**paymentLinksControllerFindOneWithHttpInfo**](PaymentLinksApi.md#paymentLinksControllerFindOneWithHttpInfo) | **GET** /api/v0/payment-links/{id} | Get a payment link by ID |
| [**paymentLinksControllerUpdate**](PaymentLinksApi.md#paymentLinksControllerUpdate) | **PUT** /api/v0/payment-links/{id} | Update a payment link |
| [**paymentLinksControllerUpdateWithHttpInfo**](PaymentLinksApi.md#paymentLinksControllerUpdateWithHttpInfo) | **PUT** /api/v0/payment-links/{id} | Update a payment link |



## paymentLinksControllerCreate

> void paymentLinksControllerCreate(createPaymentLinkDto)

Create a new payment link

Creates a new payment link with the provided details. Supports both simple one-time payments and complex product bundles.

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentLinksApi;

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

        PaymentLinksApi apiInstance = new PaymentLinksApi(defaultClient);
        CreatePaymentLinkDto createPaymentLinkDto = new CreatePaymentLinkDto(); // CreatePaymentLinkDto | Payment link creation data
        try {
            apiInstance.paymentLinksControllerCreate(createPaymentLinkDto);
        } catch (ApiException e) {
            System.err.println("Exception when calling PaymentLinksApi#paymentLinksControllerCreate");
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
| **createPaymentLinkDto** | [**CreatePaymentLinkDto**](CreatePaymentLinkDto.md)| Payment link creation data | |

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
| **201** | The payment link has been successfully created. |  -  |
| **400** | Bad Request. |  -  |

## paymentLinksControllerCreateWithHttpInfo

> ApiResponse<Void> paymentLinksControllerCreate paymentLinksControllerCreateWithHttpInfo(createPaymentLinkDto)

Create a new payment link

Creates a new payment link with the provided details. Supports both simple one-time payments and complex product bundles.

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentLinksApi;

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

        PaymentLinksApi apiInstance = new PaymentLinksApi(defaultClient);
        CreatePaymentLinkDto createPaymentLinkDto = new CreatePaymentLinkDto(); // CreatePaymentLinkDto | Payment link creation data
        try {
            ApiResponse<Void> response = apiInstance.paymentLinksControllerCreateWithHttpInfo(createPaymentLinkDto);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling PaymentLinksApi#paymentLinksControllerCreate");
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
| **createPaymentLinkDto** | [**CreatePaymentLinkDto**](CreatePaymentLinkDto.md)| Payment link creation data | |

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
| **201** | The payment link has been successfully created. |  -  |
| **400** | Bad Request. |  -  |


## paymentLinksControllerFindAll

> void paymentLinksControllerFindAll(skip, take)

Get all payment links

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentLinksApi;

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

        PaymentLinksApi apiInstance = new PaymentLinksApi(defaultClient);
        String skip = "skip_example"; // String | Number of records to skip (must be non-negative)
        String take = "take_example"; // String | Number of records to take (must be positive)
        try {
            apiInstance.paymentLinksControllerFindAll(skip, take);
        } catch (ApiException e) {
            System.err.println("Exception when calling PaymentLinksApi#paymentLinksControllerFindAll");
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
| **skip** | **String**| Number of records to skip (must be non-negative) | [optional] |
| **take** | **String**| Number of records to take (must be positive) | [optional] |

### Return type


null (empty response body)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return all payment links. |  -  |

## paymentLinksControllerFindAllWithHttpInfo

> ApiResponse<Void> paymentLinksControllerFindAll paymentLinksControllerFindAllWithHttpInfo(skip, take)

Get all payment links

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentLinksApi;

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

        PaymentLinksApi apiInstance = new PaymentLinksApi(defaultClient);
        String skip = "skip_example"; // String | Number of records to skip (must be non-negative)
        String take = "take_example"; // String | Number of records to take (must be positive)
        try {
            ApiResponse<Void> response = apiInstance.paymentLinksControllerFindAllWithHttpInfo(skip, take);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling PaymentLinksApi#paymentLinksControllerFindAll");
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
| **skip** | **String**| Number of records to skip (must be non-negative) | [optional] |
| **take** | **String**| Number of records to take (must be positive) | [optional] |

### Return type


ApiResponse<Void>

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return all payment links. |  -  |


## paymentLinksControllerFindOne

> void paymentLinksControllerFindOne(id)

Get a payment link by ID

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentLinksApi;

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

        PaymentLinksApi apiInstance = new PaymentLinksApi(defaultClient);
        String id = "id_example"; // String | Payment Link ID
        try {
            apiInstance.paymentLinksControllerFindOne(id);
        } catch (ApiException e) {
            System.err.println("Exception when calling PaymentLinksApi#paymentLinksControllerFindOne");
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
| **id** | **String**| Payment Link ID | |

### Return type


null (empty response body)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return the payment link. |  -  |
| **404** | Payment link not found. |  -  |

## paymentLinksControllerFindOneWithHttpInfo

> ApiResponse<Void> paymentLinksControllerFindOne paymentLinksControllerFindOneWithHttpInfo(id)

Get a payment link by ID

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentLinksApi;

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

        PaymentLinksApi apiInstance = new PaymentLinksApi(defaultClient);
        String id = "id_example"; // String | Payment Link ID
        try {
            ApiResponse<Void> response = apiInstance.paymentLinksControllerFindOneWithHttpInfo(id);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling PaymentLinksApi#paymentLinksControllerFindOne");
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
| **id** | **String**| Payment Link ID | |

### Return type


ApiResponse<Void>

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return the payment link. |  -  |
| **404** | Payment link not found. |  -  |


## paymentLinksControllerUpdate

> void paymentLinksControllerUpdate(id, body)

Update a payment link

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentLinksApi;

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

        PaymentLinksApi apiInstance = new PaymentLinksApi(defaultClient);
        String id = "id_example"; // String | Payment Link ID
        Object body = null; // Object | 
        try {
            apiInstance.paymentLinksControllerUpdate(id, body);
        } catch (ApiException e) {
            System.err.println("Exception when calling PaymentLinksApi#paymentLinksControllerUpdate");
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
| **id** | **String**| Payment Link ID | |
| **body** | **Object**|  | |

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
| **200** | The payment link has been successfully updated. |  -  |
| **404** | Payment link not found. |  -  |

## paymentLinksControllerUpdateWithHttpInfo

> ApiResponse<Void> paymentLinksControllerUpdate paymentLinksControllerUpdateWithHttpInfo(id, body)

Update a payment link

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentLinksApi;

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

        PaymentLinksApi apiInstance = new PaymentLinksApi(defaultClient);
        String id = "id_example"; // String | Payment Link ID
        Object body = null; // Object | 
        try {
            ApiResponse<Void> response = apiInstance.paymentLinksControllerUpdateWithHttpInfo(id, body);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling PaymentLinksApi#paymentLinksControllerUpdate");
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
| **id** | **String**| Payment Link ID | |
| **body** | **Object**|  | |

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
| **200** | The payment link has been successfully updated. |  -  |
| **404** | Payment link not found. |  -  |

