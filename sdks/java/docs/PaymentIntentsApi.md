# PaymentIntentsApi

All URIs are relative to *https://api.devdraft.ai*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**paymentIntentControllerCreateBankPaymentIntent**](PaymentIntentsApi.md#paymentIntentControllerCreateBankPaymentIntent) | **POST** /api/v0/payment-intents/bank | Create a bank payment intent |
| [**paymentIntentControllerCreateBankPaymentIntentWithHttpInfo**](PaymentIntentsApi.md#paymentIntentControllerCreateBankPaymentIntentWithHttpInfo) | **POST** /api/v0/payment-intents/bank | Create a bank payment intent |
| [**paymentIntentControllerCreateStablePaymentIntent**](PaymentIntentsApi.md#paymentIntentControllerCreateStablePaymentIntent) | **POST** /api/v0/payment-intents/stablecoin | Create a stable payment intent |
| [**paymentIntentControllerCreateStablePaymentIntentWithHttpInfo**](PaymentIntentsApi.md#paymentIntentControllerCreateStablePaymentIntentWithHttpInfo) | **POST** /api/v0/payment-intents/stablecoin | Create a stable payment intent |



## paymentIntentControllerCreateBankPaymentIntent

> void paymentIntentControllerCreateBankPaymentIntent(idempotencyKey, createBankPaymentIntentDto)

Create a bank payment intent

Creates a new bank payment intent for fiat-to-stablecoin transfers.      This endpoint allows you to create payment intents for bank transfers (ACH, Wire, SEPA) that convert to stablecoins. Perfect for onboarding users from traditional banking to crypto.  ## Supported Payment Rails - **ACH_PUSH**: US bank transfers (same-day or standard) - **WIRE**: International wire transfers - **SEPA**: European bank transfers  ## Use Cases - USD bank account to USDC conversion - EUR bank account to EURC conversion - MXN bank account to stablecoin conversion - Flexible amount payment intents for variable pricing  ## Supported Source Currencies - **USD**: US Dollar - **EUR**: Euro - **MXN**: Mexican Peso  ## Example: USD Bank to USDC &#x60;&#x60;&#x60;json {   \&quot;sourcePaymentRail\&quot;: \&quot;ach_push\&quot;,   \&quot;sourceCurrency\&quot;: \&quot;usd\&quot;,   \&quot;destinationCurrency\&quot;: \&quot;usdc\&quot;,   \&quot;destinationNetwork\&quot;: \&quot;ethereum\&quot;,   \&quot;destinationAddress\&quot;: \&quot;0x742d35Cc6634C0532925a3b8D4C9db96c4b4d8e1\&quot;,   \&quot;amount\&quot;: \&quot;1000.00\&quot;,   \&quot;customer_first_name\&quot;: \&quot;John\&quot;,   \&quot;customer_last_name\&quot;: \&quot;Doe\&quot;,   \&quot;customer_email\&quot;: \&quot;john.doe@example.com\&quot;,   \&quot;ach_reference\&quot;: \&quot;INV12345\&quot; } &#x60;&#x60;&#x60;  ## Reference Fields Use appropriate reference fields based on the payment rail: - &#x60;ach_reference&#x60;: For ACH transfers (max 10 chars, alphanumeric + spaces) - &#x60;wire_message&#x60;: For wire transfers (max 256 chars) - &#x60;sepa_reference&#x60;: For SEPA transfers (6-140 chars, specific character set)  ## Idempotency Include an &#x60;idempotency-key&#x60; header with a unique UUID v4 to prevent duplicate payments. Subsequent requests with the same key will return the original response.

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentIntentsApi;

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

        PaymentIntentsApi apiInstance = new PaymentIntentsApi(defaultClient);
        String idempotencyKey = "idempotencyKey_example"; // String | Unique UUID v4 for idempotent requests. Prevents duplicate payments.
        CreateBankPaymentIntentDto createBankPaymentIntentDto = new CreateBankPaymentIntentDto(); // CreateBankPaymentIntentDto | Bank payment intent creation data
        try {
            apiInstance.paymentIntentControllerCreateBankPaymentIntent(idempotencyKey, createBankPaymentIntentDto);
        } catch (ApiException e) {
            System.err.println("Exception when calling PaymentIntentsApi#paymentIntentControllerCreateBankPaymentIntent");
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
| **idempotencyKey** | **String**| Unique UUID v4 for idempotent requests. Prevents duplicate payments. | |
| **createBankPaymentIntentDto** | [**CreateBankPaymentIntentDto**](CreateBankPaymentIntentDto.md)| Bank payment intent creation data | |

### Return type


null (empty response body)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Bank payment intent created successfully |  -  |
| **400** | Bad Request - Invalid input data |  -  |
| **401** | Unauthorized - Invalid API credentials |  -  |
| **404** | Not Found - App not found |  -  |
| **409** | Conflict - Idempotency key already used with different parameters |  -  |

## paymentIntentControllerCreateBankPaymentIntentWithHttpInfo

> ApiResponse<Void> paymentIntentControllerCreateBankPaymentIntent paymentIntentControllerCreateBankPaymentIntentWithHttpInfo(idempotencyKey, createBankPaymentIntentDto)

Create a bank payment intent

Creates a new bank payment intent for fiat-to-stablecoin transfers.      This endpoint allows you to create payment intents for bank transfers (ACH, Wire, SEPA) that convert to stablecoins. Perfect for onboarding users from traditional banking to crypto.  ## Supported Payment Rails - **ACH_PUSH**: US bank transfers (same-day or standard) - **WIRE**: International wire transfers - **SEPA**: European bank transfers  ## Use Cases - USD bank account to USDC conversion - EUR bank account to EURC conversion - MXN bank account to stablecoin conversion - Flexible amount payment intents for variable pricing  ## Supported Source Currencies - **USD**: US Dollar - **EUR**: Euro - **MXN**: Mexican Peso  ## Example: USD Bank to USDC &#x60;&#x60;&#x60;json {   \&quot;sourcePaymentRail\&quot;: \&quot;ach_push\&quot;,   \&quot;sourceCurrency\&quot;: \&quot;usd\&quot;,   \&quot;destinationCurrency\&quot;: \&quot;usdc\&quot;,   \&quot;destinationNetwork\&quot;: \&quot;ethereum\&quot;,   \&quot;destinationAddress\&quot;: \&quot;0x742d35Cc6634C0532925a3b8D4C9db96c4b4d8e1\&quot;,   \&quot;amount\&quot;: \&quot;1000.00\&quot;,   \&quot;customer_first_name\&quot;: \&quot;John\&quot;,   \&quot;customer_last_name\&quot;: \&quot;Doe\&quot;,   \&quot;customer_email\&quot;: \&quot;john.doe@example.com\&quot;,   \&quot;ach_reference\&quot;: \&quot;INV12345\&quot; } &#x60;&#x60;&#x60;  ## Reference Fields Use appropriate reference fields based on the payment rail: - &#x60;ach_reference&#x60;: For ACH transfers (max 10 chars, alphanumeric + spaces) - &#x60;wire_message&#x60;: For wire transfers (max 256 chars) - &#x60;sepa_reference&#x60;: For SEPA transfers (6-140 chars, specific character set)  ## Idempotency Include an &#x60;idempotency-key&#x60; header with a unique UUID v4 to prevent duplicate payments. Subsequent requests with the same key will return the original response.

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentIntentsApi;

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

        PaymentIntentsApi apiInstance = new PaymentIntentsApi(defaultClient);
        String idempotencyKey = "idempotencyKey_example"; // String | Unique UUID v4 for idempotent requests. Prevents duplicate payments.
        CreateBankPaymentIntentDto createBankPaymentIntentDto = new CreateBankPaymentIntentDto(); // CreateBankPaymentIntentDto | Bank payment intent creation data
        try {
            ApiResponse<Void> response = apiInstance.paymentIntentControllerCreateBankPaymentIntentWithHttpInfo(idempotencyKey, createBankPaymentIntentDto);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling PaymentIntentsApi#paymentIntentControllerCreateBankPaymentIntent");
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
| **idempotencyKey** | **String**| Unique UUID v4 for idempotent requests. Prevents duplicate payments. | |
| **createBankPaymentIntentDto** | [**CreateBankPaymentIntentDto**](CreateBankPaymentIntentDto.md)| Bank payment intent creation data | |

### Return type


ApiResponse<Void>

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Bank payment intent created successfully |  -  |
| **400** | Bad Request - Invalid input data |  -  |
| **401** | Unauthorized - Invalid API credentials |  -  |
| **404** | Not Found - App not found |  -  |
| **409** | Conflict - Idempotency key already used with different parameters |  -  |


## paymentIntentControllerCreateStablePaymentIntent

> void paymentIntentControllerCreateStablePaymentIntent(idempotencyKey, createStablePaymentIntentDto)

Create a stable payment intent

Creates a new stable payment intent for stablecoin-to-stablecoin transfers.      This endpoint allows you to create payment intents for transfers between different stablecoins and networks. Perfect for cross-chain stablecoin swaps and conversions.  ## Use Cases - USDC to EURC conversions - Cross-chain stablecoin transfers (e.g., Ethereum USDC to Polygon USDC) - Flexible amount payment intents for dynamic pricing  ## Example: USDC to EURC Conversion &#x60;&#x60;&#x60;json {   \&quot;sourceCurrency\&quot;: \&quot;usdc\&quot;,   \&quot;sourceNetwork\&quot;: \&quot;ethereum\&quot;,   \&quot;destinationCurrency\&quot;: \&quot;eurc\&quot;,   \&quot;destinationNetwork\&quot;: \&quot;polygon\&quot;,   \&quot;destinationAddress\&quot;: \&quot;0x742d35Cc6634C0532925a3b8D4C9db96c4b4d8e1\&quot;,   \&quot;amount\&quot;: \&quot;100.00\&quot;,   \&quot;customer_first_name\&quot;: \&quot;John\&quot;,   \&quot;customer_last_name\&quot;: \&quot;Doe\&quot;,   \&quot;customer_email\&quot;: \&quot;john.doe@example.com\&quot; } &#x60;&#x60;&#x60;  ## Flexible Amount Payments Omit the &#x60;amount&#x60; field to create a flexible payment intent where users can specify the amount during payment.  ## Idempotency Include an &#x60;idempotency-key&#x60; header with a unique UUID v4 to prevent duplicate payments. Subsequent requests with the same key will return the original response.

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentIntentsApi;

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

        PaymentIntentsApi apiInstance = new PaymentIntentsApi(defaultClient);
        String idempotencyKey = "idempotencyKey_example"; // String | Unique UUID v4 for idempotent requests. Prevents duplicate payments.
        CreateStablePaymentIntentDto createStablePaymentIntentDto = new CreateStablePaymentIntentDto(); // CreateStablePaymentIntentDto | Stable payment intent creation data
        try {
            apiInstance.paymentIntentControllerCreateStablePaymentIntent(idempotencyKey, createStablePaymentIntentDto);
        } catch (ApiException e) {
            System.err.println("Exception when calling PaymentIntentsApi#paymentIntentControllerCreateStablePaymentIntent");
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
| **idempotencyKey** | **String**| Unique UUID v4 for idempotent requests. Prevents duplicate payments. | |
| **createStablePaymentIntentDto** | [**CreateStablePaymentIntentDto**](CreateStablePaymentIntentDto.md)| Stable payment intent creation data | |

### Return type


null (empty response body)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Stable payment intent created successfully |  -  |
| **400** | Bad Request - Invalid input data |  -  |
| **401** | Unauthorized - Invalid API credentials |  -  |
| **404** | Not Found - App not found |  -  |
| **409** | Conflict - Idempotency key already used with different parameters |  -  |

## paymentIntentControllerCreateStablePaymentIntentWithHttpInfo

> ApiResponse<Void> paymentIntentControllerCreateStablePaymentIntent paymentIntentControllerCreateStablePaymentIntentWithHttpInfo(idempotencyKey, createStablePaymentIntentDto)

Create a stable payment intent

Creates a new stable payment intent for stablecoin-to-stablecoin transfers.      This endpoint allows you to create payment intents for transfers between different stablecoins and networks. Perfect for cross-chain stablecoin swaps and conversions.  ## Use Cases - USDC to EURC conversions - Cross-chain stablecoin transfers (e.g., Ethereum USDC to Polygon USDC) - Flexible amount payment intents for dynamic pricing  ## Example: USDC to EURC Conversion &#x60;&#x60;&#x60;json {   \&quot;sourceCurrency\&quot;: \&quot;usdc\&quot;,   \&quot;sourceNetwork\&quot;: \&quot;ethereum\&quot;,   \&quot;destinationCurrency\&quot;: \&quot;eurc\&quot;,   \&quot;destinationNetwork\&quot;: \&quot;polygon\&quot;,   \&quot;destinationAddress\&quot;: \&quot;0x742d35Cc6634C0532925a3b8D4C9db96c4b4d8e1\&quot;,   \&quot;amount\&quot;: \&quot;100.00\&quot;,   \&quot;customer_first_name\&quot;: \&quot;John\&quot;,   \&quot;customer_last_name\&quot;: \&quot;Doe\&quot;,   \&quot;customer_email\&quot;: \&quot;john.doe@example.com\&quot; } &#x60;&#x60;&#x60;  ## Flexible Amount Payments Omit the &#x60;amount&#x60; field to create a flexible payment intent where users can specify the amount during payment.  ## Idempotency Include an &#x60;idempotency-key&#x60; header with a unique UUID v4 to prevent duplicate payments. Subsequent requests with the same key will return the original response.

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentIntentsApi;

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

        PaymentIntentsApi apiInstance = new PaymentIntentsApi(defaultClient);
        String idempotencyKey = "idempotencyKey_example"; // String | Unique UUID v4 for idempotent requests. Prevents duplicate payments.
        CreateStablePaymentIntentDto createStablePaymentIntentDto = new CreateStablePaymentIntentDto(); // CreateStablePaymentIntentDto | Stable payment intent creation data
        try {
            ApiResponse<Void> response = apiInstance.paymentIntentControllerCreateStablePaymentIntentWithHttpInfo(idempotencyKey, createStablePaymentIntentDto);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling PaymentIntentsApi#paymentIntentControllerCreateStablePaymentIntent");
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
| **idempotencyKey** | **String**| Unique UUID v4 for idempotent requests. Prevents duplicate payments. | |
| **createStablePaymentIntentDto** | [**CreateStablePaymentIntentDto**](CreateStablePaymentIntentDto.md)| Stable payment intent creation data | |

### Return type


ApiResponse<Void>

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Stable payment intent created successfully |  -  |
| **400** | Bad Request - Invalid input data |  -  |
| **401** | Unauthorized - Invalid API credentials |  -  |
| **404** | Not Found - App not found |  -  |
| **409** | Conflict - Idempotency key already used with different parameters |  -  |

