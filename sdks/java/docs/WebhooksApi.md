# WebhooksApi

All URIs are relative to *https://api.devdraft.ai*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**webhookControllerCreate**](WebhooksApi.md#webhookControllerCreate) | **POST** /api/v0/webhooks | Create a new webhook |
| [**webhookControllerCreateWithHttpInfo**](WebhooksApi.md#webhookControllerCreateWithHttpInfo) | **POST** /api/v0/webhooks | Create a new webhook |
| [**webhookControllerFindAll**](WebhooksApi.md#webhookControllerFindAll) | **GET** /api/v0/webhooks | Get all webhooks |
| [**webhookControllerFindAllWithHttpInfo**](WebhooksApi.md#webhookControllerFindAllWithHttpInfo) | **GET** /api/v0/webhooks | Get all webhooks |
| [**webhookControllerFindOne**](WebhooksApi.md#webhookControllerFindOne) | **GET** /api/v0/webhooks/{id} | Get a webhook by id |
| [**webhookControllerFindOneWithHttpInfo**](WebhooksApi.md#webhookControllerFindOneWithHttpInfo) | **GET** /api/v0/webhooks/{id} | Get a webhook by id |
| [**webhookControllerRemove**](WebhooksApi.md#webhookControllerRemove) | **DELETE** /api/v0/webhooks/{id} | Delete a webhook |
| [**webhookControllerRemoveWithHttpInfo**](WebhooksApi.md#webhookControllerRemoveWithHttpInfo) | **DELETE** /api/v0/webhooks/{id} | Delete a webhook |
| [**webhookControllerUpdate**](WebhooksApi.md#webhookControllerUpdate) | **PATCH** /api/v0/webhooks/{id} | Update a webhook |
| [**webhookControllerUpdateWithHttpInfo**](WebhooksApi.md#webhookControllerUpdateWithHttpInfo) | **PATCH** /api/v0/webhooks/{id} | Update a webhook |



## webhookControllerCreate

> WebhookResponseDto webhookControllerCreate(createWebhookDto)

Create a new webhook

Creates a new webhook endpoint for receiving event notifications. Requires webhook:create scope.

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

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

        WebhooksApi apiInstance = new WebhooksApi(defaultClient);
        CreateWebhookDto createWebhookDto = new CreateWebhookDto(); // CreateWebhookDto | Webhook configuration details
        try {
            WebhookResponseDto result = apiInstance.webhookControllerCreate(createWebhookDto);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhooksApi#webhookControllerCreate");
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
| **createWebhookDto** | [**CreateWebhookDto**](CreateWebhookDto.md)| Webhook configuration details | |

### Return type

[**WebhookResponseDto**](WebhookResponseDto.md)


### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The webhook has been successfully created. |  -  |
| **400** | Invalid input data. |  -  |
| **401** | Unauthorized - Missing or invalid API key. |  -  |
| **403** | Forbidden - Missing required scope or API key not found. |  -  |

## webhookControllerCreateWithHttpInfo

> ApiResponse<WebhookResponseDto> webhookControllerCreate webhookControllerCreateWithHttpInfo(createWebhookDto)

Create a new webhook

Creates a new webhook endpoint for receiving event notifications. Requires webhook:create scope.

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

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

        WebhooksApi apiInstance = new WebhooksApi(defaultClient);
        CreateWebhookDto createWebhookDto = new CreateWebhookDto(); // CreateWebhookDto | Webhook configuration details
        try {
            ApiResponse<WebhookResponseDto> response = apiInstance.webhookControllerCreateWithHttpInfo(createWebhookDto);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhooksApi#webhookControllerCreate");
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
| **createWebhookDto** | [**CreateWebhookDto**](CreateWebhookDto.md)| Webhook configuration details | |

### Return type

ApiResponse<[**WebhookResponseDto**](WebhookResponseDto.md)>


### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The webhook has been successfully created. |  -  |
| **400** | Invalid input data. |  -  |
| **401** | Unauthorized - Missing or invalid API key. |  -  |
| **403** | Forbidden - Missing required scope or API key not found. |  -  |


## webhookControllerFindAll

> List<WebhookResponseDto> webhookControllerFindAll(skip, take)

Get all webhooks

Retrieves a list of all webhooks for your application. Requires webhook:read scope.

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

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

        WebhooksApi apiInstance = new WebhooksApi(defaultClient);
        BigDecimal skip = new BigDecimal(78); // BigDecimal | Number of records to skip (default: 0)
        BigDecimal take = new BigDecimal(78); // BigDecimal | Number of records to return (default: 10)
        try {
            List<WebhookResponseDto> result = apiInstance.webhookControllerFindAll(skip, take);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhooksApi#webhookControllerFindAll");
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
| **skip** | **BigDecimal**| Number of records to skip (default: 0) | [optional] |
| **take** | **BigDecimal**| Number of records to return (default: 10) | [optional] |

### Return type

[**List&lt;WebhookResponseDto&gt;**](WebhookResponseDto.md)


### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return all webhooks. |  -  |
| **401** | Unauthorized - Missing or invalid API key. |  -  |
| **403** | Forbidden - Missing required scope or API key not found. |  -  |

## webhookControllerFindAllWithHttpInfo

> ApiResponse<List<WebhookResponseDto>> webhookControllerFindAll webhookControllerFindAllWithHttpInfo(skip, take)

Get all webhooks

Retrieves a list of all webhooks for your application. Requires webhook:read scope.

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

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

        WebhooksApi apiInstance = new WebhooksApi(defaultClient);
        BigDecimal skip = new BigDecimal(78); // BigDecimal | Number of records to skip (default: 0)
        BigDecimal take = new BigDecimal(78); // BigDecimal | Number of records to return (default: 10)
        try {
            ApiResponse<List<WebhookResponseDto>> response = apiInstance.webhookControllerFindAllWithHttpInfo(skip, take);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhooksApi#webhookControllerFindAll");
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
| **skip** | **BigDecimal**| Number of records to skip (default: 0) | [optional] |
| **take** | **BigDecimal**| Number of records to return (default: 10) | [optional] |

### Return type

ApiResponse<[**List&lt;WebhookResponseDto&gt;**](WebhookResponseDto.md)>


### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return all webhooks. |  -  |
| **401** | Unauthorized - Missing or invalid API key. |  -  |
| **403** | Forbidden - Missing required scope or API key not found. |  -  |


## webhookControllerFindOne

> WebhookResponseDto webhookControllerFindOne(id)

Get a webhook by id

Retrieves details for a specific webhook. Requires webhook:read scope.

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

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

        WebhooksApi apiInstance = new WebhooksApi(defaultClient);
        UUID id = UUID.randomUUID(); // UUID | Webhook unique identifier (UUID)
        try {
            WebhookResponseDto result = apiInstance.webhookControllerFindOne(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhooksApi#webhookControllerFindOne");
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
| **id** | **UUID**| Webhook unique identifier (UUID) | |

### Return type

[**WebhookResponseDto**](WebhookResponseDto.md)


### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return the webhook. |  -  |
| **401** | Unauthorized - Missing or invalid API key. |  -  |
| **403** | Forbidden - Missing required scope or API key not found. |  -  |
| **404** | Webhook not found. |  -  |

## webhookControllerFindOneWithHttpInfo

> ApiResponse<WebhookResponseDto> webhookControllerFindOne webhookControllerFindOneWithHttpInfo(id)

Get a webhook by id

Retrieves details for a specific webhook. Requires webhook:read scope.

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

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

        WebhooksApi apiInstance = new WebhooksApi(defaultClient);
        UUID id = UUID.randomUUID(); // UUID | Webhook unique identifier (UUID)
        try {
            ApiResponse<WebhookResponseDto> response = apiInstance.webhookControllerFindOneWithHttpInfo(id);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhooksApi#webhookControllerFindOne");
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
| **id** | **UUID**| Webhook unique identifier (UUID) | |

### Return type

ApiResponse<[**WebhookResponseDto**](WebhookResponseDto.md)>


### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return the webhook. |  -  |
| **401** | Unauthorized - Missing or invalid API key. |  -  |
| **403** | Forbidden - Missing required scope or API key not found. |  -  |
| **404** | Webhook not found. |  -  |


## webhookControllerRemove

> WebhookResponseDto webhookControllerRemove(id)

Delete a webhook

Deletes a webhook configuration. Requires webhook:delete scope.

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

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

        WebhooksApi apiInstance = new WebhooksApi(defaultClient);
        UUID id = UUID.randomUUID(); // UUID | Webhook unique identifier (UUID)
        try {
            WebhookResponseDto result = apiInstance.webhookControllerRemove(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhooksApi#webhookControllerRemove");
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
| **id** | **UUID**| Webhook unique identifier (UUID) | |

### Return type

[**WebhookResponseDto**](WebhookResponseDto.md)


### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The webhook has been successfully deleted. |  -  |
| **401** | Unauthorized - Missing or invalid API key. |  -  |
| **403** | Forbidden - Missing required scope or API key not found. |  -  |
| **404** | Webhook not found. |  -  |

## webhookControllerRemoveWithHttpInfo

> ApiResponse<WebhookResponseDto> webhookControllerRemove webhookControllerRemoveWithHttpInfo(id)

Delete a webhook

Deletes a webhook configuration. Requires webhook:delete scope.

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

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

        WebhooksApi apiInstance = new WebhooksApi(defaultClient);
        UUID id = UUID.randomUUID(); // UUID | Webhook unique identifier (UUID)
        try {
            ApiResponse<WebhookResponseDto> response = apiInstance.webhookControllerRemoveWithHttpInfo(id);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhooksApi#webhookControllerRemove");
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
| **id** | **UUID**| Webhook unique identifier (UUID) | |

### Return type

ApiResponse<[**WebhookResponseDto**](WebhookResponseDto.md)>


### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The webhook has been successfully deleted. |  -  |
| **401** | Unauthorized - Missing or invalid API key. |  -  |
| **403** | Forbidden - Missing required scope or API key not found. |  -  |
| **404** | Webhook not found. |  -  |


## webhookControllerUpdate

> WebhookResponseDto webhookControllerUpdate(id, updateWebhookDto)

Update a webhook

Updates an existing webhook configuration. Requires webhook:update scope.

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

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

        WebhooksApi apiInstance = new WebhooksApi(defaultClient);
        UUID id = UUID.randomUUID(); // UUID | Webhook unique identifier (UUID)
        UpdateWebhookDto updateWebhookDto = new UpdateWebhookDto(); // UpdateWebhookDto | Webhook update details
        try {
            WebhookResponseDto result = apiInstance.webhookControllerUpdate(id, updateWebhookDto);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhooksApi#webhookControllerUpdate");
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
| **id** | **UUID**| Webhook unique identifier (UUID) | |
| **updateWebhookDto** | [**UpdateWebhookDto**](UpdateWebhookDto.md)| Webhook update details | |

### Return type

[**WebhookResponseDto**](WebhookResponseDto.md)


### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The webhook has been successfully updated. |  -  |
| **400** | Invalid input data. |  -  |
| **401** | Unauthorized - Missing or invalid API key. |  -  |
| **403** | Forbidden - Missing required scope or API key not found. |  -  |
| **404** | Webhook not found. |  -  |

## webhookControllerUpdateWithHttpInfo

> ApiResponse<WebhookResponseDto> webhookControllerUpdate webhookControllerUpdateWithHttpInfo(id, updateWebhookDto)

Update a webhook

Updates an existing webhook configuration. Requires webhook:update scope.

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

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

        WebhooksApi apiInstance = new WebhooksApi(defaultClient);
        UUID id = UUID.randomUUID(); // UUID | Webhook unique identifier (UUID)
        UpdateWebhookDto updateWebhookDto = new UpdateWebhookDto(); // UpdateWebhookDto | Webhook update details
        try {
            ApiResponse<WebhookResponseDto> response = apiInstance.webhookControllerUpdateWithHttpInfo(id, updateWebhookDto);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhooksApi#webhookControllerUpdate");
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
| **id** | **UUID**| Webhook unique identifier (UUID) | |
| **updateWebhookDto** | [**UpdateWebhookDto**](UpdateWebhookDto.md)| Webhook update details | |

### Return type

ApiResponse<[**WebhookResponseDto**](WebhookResponseDto.md)>


### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The webhook has been successfully updated. |  -  |
| **400** | Invalid input data. |  -  |
| **401** | Unauthorized - Missing or invalid API key. |  -  |
| **403** | Forbidden - Missing required scope or API key not found. |  -  |
| **404** | Webhook not found. |  -  |

