# InvoicesApi

All URIs are relative to *https://api.devdraft.ai*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**invoiceControllerCreate**](InvoicesApi.md#invoiceControllerCreate) | **POST** /api/v0/invoices | Create a new invoice |
| [**invoiceControllerCreateWithHttpInfo**](InvoicesApi.md#invoiceControllerCreateWithHttpInfo) | **POST** /api/v0/invoices | Create a new invoice |
| [**invoiceControllerFindAll**](InvoicesApi.md#invoiceControllerFindAll) | **GET** /api/v0/invoices | Get all invoices |
| [**invoiceControllerFindAllWithHttpInfo**](InvoicesApi.md#invoiceControllerFindAllWithHttpInfo) | **GET** /api/v0/invoices | Get all invoices |
| [**invoiceControllerFindOne**](InvoicesApi.md#invoiceControllerFindOne) | **GET** /api/v0/invoices/{id} | Get an invoice by ID |
| [**invoiceControllerFindOneWithHttpInfo**](InvoicesApi.md#invoiceControllerFindOneWithHttpInfo) | **GET** /api/v0/invoices/{id} | Get an invoice by ID |
| [**invoiceControllerUpdate**](InvoicesApi.md#invoiceControllerUpdate) | **PUT** /api/v0/invoices/{id} | Update an invoice |
| [**invoiceControllerUpdateWithHttpInfo**](InvoicesApi.md#invoiceControllerUpdateWithHttpInfo) | **PUT** /api/v0/invoices/{id} | Update an invoice |



## invoiceControllerCreate

> void invoiceControllerCreate(createInvoiceDto)

Create a new invoice

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesApi;

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

        InvoicesApi apiInstance = new InvoicesApi(defaultClient);
        CreateInvoiceDto createInvoiceDto = new CreateInvoiceDto(); // CreateInvoiceDto | 
        try {
            apiInstance.invoiceControllerCreate(createInvoiceDto);
        } catch (ApiException e) {
            System.err.println("Exception when calling InvoicesApi#invoiceControllerCreate");
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
| **createInvoiceDto** | [**CreateInvoiceDto**](CreateInvoiceDto.md)|  | |

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
| **201** | The invoice has been successfully created. |  -  |
| **400** | Bad Request. |  -  |

## invoiceControllerCreateWithHttpInfo

> ApiResponse<Void> invoiceControllerCreate invoiceControllerCreateWithHttpInfo(createInvoiceDto)

Create a new invoice

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesApi;

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

        InvoicesApi apiInstance = new InvoicesApi(defaultClient);
        CreateInvoiceDto createInvoiceDto = new CreateInvoiceDto(); // CreateInvoiceDto | 
        try {
            ApiResponse<Void> response = apiInstance.invoiceControllerCreateWithHttpInfo(createInvoiceDto);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling InvoicesApi#invoiceControllerCreate");
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
| **createInvoiceDto** | [**CreateInvoiceDto**](CreateInvoiceDto.md)|  | |

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
| **201** | The invoice has been successfully created. |  -  |
| **400** | Bad Request. |  -  |


## invoiceControllerFindAll

> void invoiceControllerFindAll(skip, take)

Get all invoices

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesApi;

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

        InvoicesApi apiInstance = new InvoicesApi(defaultClient);
        BigDecimal skip = new BigDecimal(78); // BigDecimal | Number of records to skip
        BigDecimal take = new BigDecimal(78); // BigDecimal | Number of records to take
        try {
            apiInstance.invoiceControllerFindAll(skip, take);
        } catch (ApiException e) {
            System.err.println("Exception when calling InvoicesApi#invoiceControllerFindAll");
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
| **skip** | **BigDecimal**| Number of records to skip | [optional] |
| **take** | **BigDecimal**| Number of records to take | [optional] |

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
| **200** | Return all invoices. |  -  |

## invoiceControllerFindAllWithHttpInfo

> ApiResponse<Void> invoiceControllerFindAll invoiceControllerFindAllWithHttpInfo(skip, take)

Get all invoices

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesApi;

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

        InvoicesApi apiInstance = new InvoicesApi(defaultClient);
        BigDecimal skip = new BigDecimal(78); // BigDecimal | Number of records to skip
        BigDecimal take = new BigDecimal(78); // BigDecimal | Number of records to take
        try {
            ApiResponse<Void> response = apiInstance.invoiceControllerFindAllWithHttpInfo(skip, take);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling InvoicesApi#invoiceControllerFindAll");
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
| **skip** | **BigDecimal**| Number of records to skip | [optional] |
| **take** | **BigDecimal**| Number of records to take | [optional] |

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
| **200** | Return all invoices. |  -  |


## invoiceControllerFindOne

> void invoiceControllerFindOne(id)

Get an invoice by ID

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesApi;

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

        InvoicesApi apiInstance = new InvoicesApi(defaultClient);
        String id = "id_example"; // String | Invoice ID
        try {
            apiInstance.invoiceControllerFindOne(id);
        } catch (ApiException e) {
            System.err.println("Exception when calling InvoicesApi#invoiceControllerFindOne");
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
| **id** | **String**| Invoice ID | |

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
| **200** | Return the invoice. |  -  |
| **404** | Invoice not found. |  -  |

## invoiceControllerFindOneWithHttpInfo

> ApiResponse<Void> invoiceControllerFindOne invoiceControllerFindOneWithHttpInfo(id)

Get an invoice by ID

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesApi;

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

        InvoicesApi apiInstance = new InvoicesApi(defaultClient);
        String id = "id_example"; // String | Invoice ID
        try {
            ApiResponse<Void> response = apiInstance.invoiceControllerFindOneWithHttpInfo(id);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling InvoicesApi#invoiceControllerFindOne");
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
| **id** | **String**| Invoice ID | |

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
| **200** | Return the invoice. |  -  |
| **404** | Invoice not found. |  -  |


## invoiceControllerUpdate

> void invoiceControllerUpdate(id, createInvoiceDto)

Update an invoice

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesApi;

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

        InvoicesApi apiInstance = new InvoicesApi(defaultClient);
        String id = "id_example"; // String | Invoice ID
        CreateInvoiceDto createInvoiceDto = new CreateInvoiceDto(); // CreateInvoiceDto | 
        try {
            apiInstance.invoiceControllerUpdate(id, createInvoiceDto);
        } catch (ApiException e) {
            System.err.println("Exception when calling InvoicesApi#invoiceControllerUpdate");
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
| **id** | **String**| Invoice ID | |
| **createInvoiceDto** | [**CreateInvoiceDto**](CreateInvoiceDto.md)|  | |

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
| **200** | The invoice has been successfully updated. |  -  |
| **404** | Invoice not found. |  -  |

## invoiceControllerUpdateWithHttpInfo

> ApiResponse<Void> invoiceControllerUpdate invoiceControllerUpdateWithHttpInfo(id, createInvoiceDto)

Update an invoice

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesApi;

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

        InvoicesApi apiInstance = new InvoicesApi(defaultClient);
        String id = "id_example"; // String | Invoice ID
        CreateInvoiceDto createInvoiceDto = new CreateInvoiceDto(); // CreateInvoiceDto | 
        try {
            ApiResponse<Void> response = apiInstance.invoiceControllerUpdateWithHttpInfo(id, createInvoiceDto);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling InvoicesApi#invoiceControllerUpdate");
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
| **id** | **String**| Invoice ID | |
| **createInvoiceDto** | [**CreateInvoiceDto**](CreateInvoiceDto.md)|  | |

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
| **200** | The invoice has been successfully updated. |  -  |
| **404** | Invoice not found. |  -  |

