# TaxesApi

All URIs are relative to *https://api.devdraft.ai*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**taxControllerCreate**](TaxesApi.md#taxControllerCreate) | **POST** /api/v0/taxes | Create a new tax |
| [**taxControllerCreateWithHttpInfo**](TaxesApi.md#taxControllerCreateWithHttpInfo) | **POST** /api/v0/taxes | Create a new tax |
| [**taxControllerDeleteWithoutId**](TaxesApi.md#taxControllerDeleteWithoutId) | **DELETE** /api/v0/taxes | Tax ID required for deletion |
| [**taxControllerDeleteWithoutIdWithHttpInfo**](TaxesApi.md#taxControllerDeleteWithoutIdWithHttpInfo) | **DELETE** /api/v0/taxes | Tax ID required for deletion |
| [**taxControllerFindAll**](TaxesApi.md#taxControllerFindAll) | **GET** /api/v0/taxes | Get all taxes with filters |
| [**taxControllerFindAllWithHttpInfo**](TaxesApi.md#taxControllerFindAllWithHttpInfo) | **GET** /api/v0/taxes | Get all taxes with filters |
| [**taxControllerFindOne**](TaxesApi.md#taxControllerFindOne) | **GET** /api/v0/taxes/{id} | Get a tax by ID |
| [**taxControllerFindOneWithHttpInfo**](TaxesApi.md#taxControllerFindOneWithHttpInfo) | **GET** /api/v0/taxes/{id} | Get a tax by ID |
| [**taxControllerRemove**](TaxesApi.md#taxControllerRemove) | **DELETE** /api/v0/taxes/{id} | Delete a tax |
| [**taxControllerRemoveWithHttpInfo**](TaxesApi.md#taxControllerRemoveWithHttpInfo) | **DELETE** /api/v0/taxes/{id} | Delete a tax |
| [**taxControllerUpdate**](TaxesApi.md#taxControllerUpdate) | **PUT** /api/v0/taxes/{id} | Update a tax |
| [**taxControllerUpdateWithHttpInfo**](TaxesApi.md#taxControllerUpdateWithHttpInfo) | **PUT** /api/v0/taxes/{id} | Update a tax |
| [**taxControllerUpdateWithoutId**](TaxesApi.md#taxControllerUpdateWithoutId) | **PUT** /api/v0/taxes | Tax ID required for updates |
| [**taxControllerUpdateWithoutIdWithHttpInfo**](TaxesApi.md#taxControllerUpdateWithoutIdWithHttpInfo) | **PUT** /api/v0/taxes | Tax ID required for updates |



## taxControllerCreate

> TaxControllerCreate201Response taxControllerCreate(createTaxDto)

Create a new tax

Creates a new tax rate that can be applied to products, invoices, and payment links.  ## Use Cases - Set up sales tax for different regions - Create VAT rates for international customers - Configure state and local tax rates - Manage tax compliance requirements  ## Example: Create Basic Sales Tax &#x60;&#x60;&#x60;json {   \&quot;name\&quot;: \&quot;Sales Tax\&quot;,   \&quot;description\&quot;: \&quot;Standard sales tax for retail transactions\&quot;,   \&quot;percentage\&quot;: 8.5,   \&quot;active\&quot;: true } &#x60;&#x60;&#x60;  ## Required Fields - &#x60;name&#x60;: Tax name for identification (1-100 characters) - &#x60;percentage&#x60;: Tax rate percentage (0-100)  ## Optional Fields - &#x60;description&#x60;: Explanation of what this tax covers (max 255 characters) - &#x60;active&#x60;: Whether this tax is currently active (default: true) - &#x60;appIds&#x60;: Array of app IDs where this tax should be available

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaxesApi;

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

        TaxesApi apiInstance = new TaxesApi(defaultClient);
        CreateTaxDto createTaxDto = new CreateTaxDto(); // CreateTaxDto | Tax creation data
        try {
            TaxControllerCreate201Response result = apiInstance.taxControllerCreate(createTaxDto);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TaxesApi#taxControllerCreate");
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
| **createTaxDto** | [**CreateTaxDto**](CreateTaxDto.md)| Tax creation data | |

### Return type

[**TaxControllerCreate201Response**](TaxControllerCreate201Response.md)


### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Tax created successfully |  -  |
| **400** | Bad Request - Invalid input data |  -  |
| **401** | Unauthorized - Invalid API credentials |  -  |

## taxControllerCreateWithHttpInfo

> ApiResponse<TaxControllerCreate201Response> taxControllerCreate taxControllerCreateWithHttpInfo(createTaxDto)

Create a new tax

Creates a new tax rate that can be applied to products, invoices, and payment links.  ## Use Cases - Set up sales tax for different regions - Create VAT rates for international customers - Configure state and local tax rates - Manage tax compliance requirements  ## Example: Create Basic Sales Tax &#x60;&#x60;&#x60;json {   \&quot;name\&quot;: \&quot;Sales Tax\&quot;,   \&quot;description\&quot;: \&quot;Standard sales tax for retail transactions\&quot;,   \&quot;percentage\&quot;: 8.5,   \&quot;active\&quot;: true } &#x60;&#x60;&#x60;  ## Required Fields - &#x60;name&#x60;: Tax name for identification (1-100 characters) - &#x60;percentage&#x60;: Tax rate percentage (0-100)  ## Optional Fields - &#x60;description&#x60;: Explanation of what this tax covers (max 255 characters) - &#x60;active&#x60;: Whether this tax is currently active (default: true) - &#x60;appIds&#x60;: Array of app IDs where this tax should be available

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaxesApi;

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

        TaxesApi apiInstance = new TaxesApi(defaultClient);
        CreateTaxDto createTaxDto = new CreateTaxDto(); // CreateTaxDto | Tax creation data
        try {
            ApiResponse<TaxControllerCreate201Response> response = apiInstance.taxControllerCreateWithHttpInfo(createTaxDto);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TaxesApi#taxControllerCreate");
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
| **createTaxDto** | [**CreateTaxDto**](CreateTaxDto.md)| Tax creation data | |

### Return type

ApiResponse<[**TaxControllerCreate201Response**](TaxControllerCreate201Response.md)>


### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Tax created successfully |  -  |
| **400** | Bad Request - Invalid input data |  -  |
| **401** | Unauthorized - Invalid API credentials |  -  |


## taxControllerDeleteWithoutId

> void taxControllerDeleteWithoutId()

Tax ID required for deletion

This endpoint requires a tax ID in the URL path. Use DELETE /api/v0/taxes/{id} instead.

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaxesApi;

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

        TaxesApi apiInstance = new TaxesApi(defaultClient);
        try {
            apiInstance.taxControllerDeleteWithoutId();
        } catch (ApiException e) {
            System.err.println("Exception when calling TaxesApi#taxControllerDeleteWithoutId");
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


null (empty response body)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request - Tax ID is required in the URL path |  -  |

## taxControllerDeleteWithoutIdWithHttpInfo

> ApiResponse<Void> taxControllerDeleteWithoutId taxControllerDeleteWithoutIdWithHttpInfo()

Tax ID required for deletion

This endpoint requires a tax ID in the URL path. Use DELETE /api/v0/taxes/{id} instead.

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaxesApi;

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

        TaxesApi apiInstance = new TaxesApi(defaultClient);
        try {
            ApiResponse<Void> response = apiInstance.taxControllerDeleteWithoutIdWithHttpInfo();
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling TaxesApi#taxControllerDeleteWithoutId");
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


ApiResponse<Void>

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request - Tax ID is required in the URL path |  -  |


## taxControllerFindAll

> void taxControllerFindAll(skip, take, name, active)

Get all taxes with filters

Retrieves a list of taxes with optional filtering and pagination.  ## Use Cases - List all available tax rates - Search taxes by name - Filter active/inactive taxes - Export tax configuration  ## Query Parameters - &#x60;skip&#x60;: Number of records to skip (default: 0, min: 0) - &#x60;take&#x60;: Number of records to return (default: 10, min: 1, max: 100) - &#x60;name&#x60;: Filter taxes by name (partial match, case-insensitive) - &#x60;active&#x60;: Filter by active status (true/false)  ## Example Request &#x60;GET /api/v0/taxes?skip&#x3D;0&amp;take&#x3D;20&amp;active&#x3D;true&amp;name&#x3D;Sales&#x60;  ## Example Response &#x60;&#x60;&#x60;json [   {     \&quot;id\&quot;: \&quot;tax_123456\&quot;,     \&quot;name\&quot;: \&quot;Sales Tax\&quot;,     \&quot;description\&quot;: \&quot;Standard sales tax for retail transactions\&quot;,     \&quot;percentage\&quot;: 8.5,     \&quot;active\&quot;: true,     \&quot;created_at\&quot;: \&quot;2024-03-20T10:00:00Z\&quot;,     \&quot;updated_at\&quot;: \&quot;2024-03-20T10:00:00Z\&quot;   } ] &#x60;&#x60;&#x60;

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaxesApi;

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

        TaxesApi apiInstance = new TaxesApi(defaultClient);
        BigDecimal skip = new BigDecimal("0"); // BigDecimal | Number of records to skip for pagination
        BigDecimal take = new BigDecimal("10"); // BigDecimal | Number of records to return (max 100)
        String name = "Sales"; // String | Filter taxes by name (partial match, case-insensitive)
        Boolean active = true; // Boolean | Filter by active status
        try {
            apiInstance.taxControllerFindAll(skip, take, name, active);
        } catch (ApiException e) {
            System.err.println("Exception when calling TaxesApi#taxControllerFindAll");
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
| **skip** | **BigDecimal**| Number of records to skip for pagination | [optional] [default to 0] |
| **take** | **BigDecimal**| Number of records to return (max 100) | [optional] [default to 10] |
| **name** | **String**| Filter taxes by name (partial match, case-insensitive) | [optional] |
| **active** | **Boolean**| Filter by active status | [optional] |

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
| **200** | Successfully retrieved taxes |  -  |
| **400** | Bad Request - Invalid query parameters |  -  |
| **401** | Unauthorized - Invalid API credentials |  -  |

## taxControllerFindAllWithHttpInfo

> ApiResponse<Void> taxControllerFindAll taxControllerFindAllWithHttpInfo(skip, take, name, active)

Get all taxes with filters

Retrieves a list of taxes with optional filtering and pagination.  ## Use Cases - List all available tax rates - Search taxes by name - Filter active/inactive taxes - Export tax configuration  ## Query Parameters - &#x60;skip&#x60;: Number of records to skip (default: 0, min: 0) - &#x60;take&#x60;: Number of records to return (default: 10, min: 1, max: 100) - &#x60;name&#x60;: Filter taxes by name (partial match, case-insensitive) - &#x60;active&#x60;: Filter by active status (true/false)  ## Example Request &#x60;GET /api/v0/taxes?skip&#x3D;0&amp;take&#x3D;20&amp;active&#x3D;true&amp;name&#x3D;Sales&#x60;  ## Example Response &#x60;&#x60;&#x60;json [   {     \&quot;id\&quot;: \&quot;tax_123456\&quot;,     \&quot;name\&quot;: \&quot;Sales Tax\&quot;,     \&quot;description\&quot;: \&quot;Standard sales tax for retail transactions\&quot;,     \&quot;percentage\&quot;: 8.5,     \&quot;active\&quot;: true,     \&quot;created_at\&quot;: \&quot;2024-03-20T10:00:00Z\&quot;,     \&quot;updated_at\&quot;: \&quot;2024-03-20T10:00:00Z\&quot;   } ] &#x60;&#x60;&#x60;

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaxesApi;

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

        TaxesApi apiInstance = new TaxesApi(defaultClient);
        BigDecimal skip = new BigDecimal("0"); // BigDecimal | Number of records to skip for pagination
        BigDecimal take = new BigDecimal("10"); // BigDecimal | Number of records to return (max 100)
        String name = "Sales"; // String | Filter taxes by name (partial match, case-insensitive)
        Boolean active = true; // Boolean | Filter by active status
        try {
            ApiResponse<Void> response = apiInstance.taxControllerFindAllWithHttpInfo(skip, take, name, active);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling TaxesApi#taxControllerFindAll");
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
| **skip** | **BigDecimal**| Number of records to skip for pagination | [optional] [default to 0] |
| **take** | **BigDecimal**| Number of records to return (max 100) | [optional] [default to 10] |
| **name** | **String**| Filter taxes by name (partial match, case-insensitive) | [optional] |
| **active** | **Boolean**| Filter by active status | [optional] |

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
| **200** | Successfully retrieved taxes |  -  |
| **400** | Bad Request - Invalid query parameters |  -  |
| **401** | Unauthorized - Invalid API credentials |  -  |


## taxControllerFindOne

> void taxControllerFindOne(id)

Get a tax by ID

Retrieves detailed information about a specific tax.  ## Use Cases - View tax details - Verify tax configuration - Check tax status before applying to products  ## Path Parameters - &#x60;id&#x60;: Tax UUID (required) - Must be a valid UUID format  ## Example Request &#x60;GET /api/v0/taxes/123e4567-e89b-12d3-a456-426614174000&#x60;  ## Example Response &#x60;&#x60;&#x60;json {   \&quot;id\&quot;: \&quot;tax_123456\&quot;,   \&quot;name\&quot;: \&quot;Sales Tax\&quot;,   \&quot;description\&quot;: \&quot;Standard sales tax for retail transactions\&quot;,   \&quot;percentage\&quot;: 8.5,   \&quot;active\&quot;: true,   \&quot;created_at\&quot;: \&quot;2024-03-20T10:00:00Z\&quot;,   \&quot;updated_at\&quot;: \&quot;2024-03-20T10:00:00Z\&quot; } &#x60;&#x60;&#x60;

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaxesApi;

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

        TaxesApi apiInstance = new TaxesApi(defaultClient);
        UUID id = UUID.randomUUID(); // UUID | Tax unique identifier (UUID)
        try {
            apiInstance.taxControllerFindOne(id);
        } catch (ApiException e) {
            System.err.println("Exception when calling TaxesApi#taxControllerFindOne");
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
| **id** | **UUID**| Tax unique identifier (UUID) | |

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
| **200** | Successfully retrieved tax |  -  |
| **400** | Bad Request - Invalid tax ID format |  -  |
| **401** | Unauthorized - Invalid API credentials |  -  |
| **404** | Not Found - Tax not found |  -  |

## taxControllerFindOneWithHttpInfo

> ApiResponse<Void> taxControllerFindOne taxControllerFindOneWithHttpInfo(id)

Get a tax by ID

Retrieves detailed information about a specific tax.  ## Use Cases - View tax details - Verify tax configuration - Check tax status before applying to products  ## Path Parameters - &#x60;id&#x60;: Tax UUID (required) - Must be a valid UUID format  ## Example Request &#x60;GET /api/v0/taxes/123e4567-e89b-12d3-a456-426614174000&#x60;  ## Example Response &#x60;&#x60;&#x60;json {   \&quot;id\&quot;: \&quot;tax_123456\&quot;,   \&quot;name\&quot;: \&quot;Sales Tax\&quot;,   \&quot;description\&quot;: \&quot;Standard sales tax for retail transactions\&quot;,   \&quot;percentage\&quot;: 8.5,   \&quot;active\&quot;: true,   \&quot;created_at\&quot;: \&quot;2024-03-20T10:00:00Z\&quot;,   \&quot;updated_at\&quot;: \&quot;2024-03-20T10:00:00Z\&quot; } &#x60;&#x60;&#x60;

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaxesApi;

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

        TaxesApi apiInstance = new TaxesApi(defaultClient);
        UUID id = UUID.randomUUID(); // UUID | Tax unique identifier (UUID)
        try {
            ApiResponse<Void> response = apiInstance.taxControllerFindOneWithHttpInfo(id);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling TaxesApi#taxControllerFindOne");
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
| **id** | **UUID**| Tax unique identifier (UUID) | |

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
| **200** | Successfully retrieved tax |  -  |
| **400** | Bad Request - Invalid tax ID format |  -  |
| **401** | Unauthorized - Invalid API credentials |  -  |
| **404** | Not Found - Tax not found |  -  |


## taxControllerRemove

> void taxControllerRemove(id)

Delete a tax

Deletes an existing tax.  ## Use Cases - Remove obsolete tax rates - Clean up unused taxes - Comply with regulatory changes  ## Path Parameters - &#x60;id&#x60;: Tax UUID (required) - Must be a valid UUID format  ## Example Request &#x60;DELETE /api/v0/taxes/123e4567-e89b-12d3-a456-426614174000&#x60;  ## Warning This action cannot be undone. Consider deactivating the tax instead of deleting it if it has been used in transactions.

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaxesApi;

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

        TaxesApi apiInstance = new TaxesApi(defaultClient);
        UUID id = UUID.randomUUID(); // UUID | Tax unique identifier (UUID)
        try {
            apiInstance.taxControllerRemove(id);
        } catch (ApiException e) {
            System.err.println("Exception when calling TaxesApi#taxControllerRemove");
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
| **id** | **UUID**| Tax unique identifier (UUID) | |

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
| **200** | Successfully deleted tax |  -  |
| **400** | Bad Request - Invalid tax ID format |  -  |
| **401** | Unauthorized - Invalid API credentials |  -  |
| **404** | Not Found - Tax not found |  -  |

## taxControllerRemoveWithHttpInfo

> ApiResponse<Void> taxControllerRemove taxControllerRemoveWithHttpInfo(id)

Delete a tax

Deletes an existing tax.  ## Use Cases - Remove obsolete tax rates - Clean up unused taxes - Comply with regulatory changes  ## Path Parameters - &#x60;id&#x60;: Tax UUID (required) - Must be a valid UUID format  ## Example Request &#x60;DELETE /api/v0/taxes/123e4567-e89b-12d3-a456-426614174000&#x60;  ## Warning This action cannot be undone. Consider deactivating the tax instead of deleting it if it has been used in transactions.

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaxesApi;

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

        TaxesApi apiInstance = new TaxesApi(defaultClient);
        UUID id = UUID.randomUUID(); // UUID | Tax unique identifier (UUID)
        try {
            ApiResponse<Void> response = apiInstance.taxControllerRemoveWithHttpInfo(id);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling TaxesApi#taxControllerRemove");
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
| **id** | **UUID**| Tax unique identifier (UUID) | |

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
| **200** | Successfully deleted tax |  -  |
| **400** | Bad Request - Invalid tax ID format |  -  |
| **401** | Unauthorized - Invalid API credentials |  -  |
| **404** | Not Found - Tax not found |  -  |


## taxControllerUpdate

> void taxControllerUpdate(id, updateTaxDto)

Update a tax

Updates an existing tax&#39;s information.  ## Use Cases - Modify tax percentage rates - Update tax descriptions - Activate/deactivate taxes - Change tax names  ## Path Parameters - &#x60;id&#x60;: Tax UUID (required) - Must be a valid UUID format  ## Example Request &#x60;PUT /api/v0/taxes/123e4567-e89b-12d3-a456-426614174000&#x60;  ## Example Request Body &#x60;&#x60;&#x60;json {   \&quot;name\&quot;: \&quot;Updated Sales Tax\&quot;,   \&quot;description\&quot;: \&quot;Updated sales tax rate\&quot;,   \&quot;percentage\&quot;: 9.0,   \&quot;active\&quot;: true } &#x60;&#x60;&#x60;  ## Notes - Only include fields that need to be updated - All fields are optional in updates - Percentage changes affect future calculations only

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaxesApi;

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

        TaxesApi apiInstance = new TaxesApi(defaultClient);
        UUID id = UUID.randomUUID(); // UUID | Tax unique identifier (UUID)
        UpdateTaxDto updateTaxDto = new UpdateTaxDto(); // UpdateTaxDto | Tax update data - only include fields you want to update
        try {
            apiInstance.taxControllerUpdate(id, updateTaxDto);
        } catch (ApiException e) {
            System.err.println("Exception when calling TaxesApi#taxControllerUpdate");
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
| **id** | **UUID**| Tax unique identifier (UUID) | |
| **updateTaxDto** | [**UpdateTaxDto**](UpdateTaxDto.md)| Tax update data - only include fields you want to update | |

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
| **200** | Successfully updated tax |  -  |
| **400** | Bad Request - Invalid input data or tax ID format |  -  |
| **401** | Unauthorized - Invalid API credentials |  -  |
| **404** | Not Found - Tax not found |  -  |

## taxControllerUpdateWithHttpInfo

> ApiResponse<Void> taxControllerUpdate taxControllerUpdateWithHttpInfo(id, updateTaxDto)

Update a tax

Updates an existing tax&#39;s information.  ## Use Cases - Modify tax percentage rates - Update tax descriptions - Activate/deactivate taxes - Change tax names  ## Path Parameters - &#x60;id&#x60;: Tax UUID (required) - Must be a valid UUID format  ## Example Request &#x60;PUT /api/v0/taxes/123e4567-e89b-12d3-a456-426614174000&#x60;  ## Example Request Body &#x60;&#x60;&#x60;json {   \&quot;name\&quot;: \&quot;Updated Sales Tax\&quot;,   \&quot;description\&quot;: \&quot;Updated sales tax rate\&quot;,   \&quot;percentage\&quot;: 9.0,   \&quot;active\&quot;: true } &#x60;&#x60;&#x60;  ## Notes - Only include fields that need to be updated - All fields are optional in updates - Percentage changes affect future calculations only

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaxesApi;

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

        TaxesApi apiInstance = new TaxesApi(defaultClient);
        UUID id = UUID.randomUUID(); // UUID | Tax unique identifier (UUID)
        UpdateTaxDto updateTaxDto = new UpdateTaxDto(); // UpdateTaxDto | Tax update data - only include fields you want to update
        try {
            ApiResponse<Void> response = apiInstance.taxControllerUpdateWithHttpInfo(id, updateTaxDto);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling TaxesApi#taxControllerUpdate");
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
| **id** | **UUID**| Tax unique identifier (UUID) | |
| **updateTaxDto** | [**UpdateTaxDto**](UpdateTaxDto.md)| Tax update data - only include fields you want to update | |

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
| **200** | Successfully updated tax |  -  |
| **400** | Bad Request - Invalid input data or tax ID format |  -  |
| **401** | Unauthorized - Invalid API credentials |  -  |
| **404** | Not Found - Tax not found |  -  |


## taxControllerUpdateWithoutId

> void taxControllerUpdateWithoutId()

Tax ID required for updates

This endpoint requires a tax ID in the URL path. Use PUT /api/v0/taxes/{id} instead.

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaxesApi;

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

        TaxesApi apiInstance = new TaxesApi(defaultClient);
        try {
            apiInstance.taxControllerUpdateWithoutId();
        } catch (ApiException e) {
            System.err.println("Exception when calling TaxesApi#taxControllerUpdateWithoutId");
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


null (empty response body)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request - Tax ID is required in the URL path |  -  |

## taxControllerUpdateWithoutIdWithHttpInfo

> ApiResponse<Void> taxControllerUpdateWithoutId taxControllerUpdateWithoutIdWithHttpInfo()

Tax ID required for updates

This endpoint requires a tax ID in the URL path. Use PUT /api/v0/taxes/{id} instead.

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaxesApi;

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

        TaxesApi apiInstance = new TaxesApi(defaultClient);
        try {
            ApiResponse<Void> response = apiInstance.taxControllerUpdateWithoutIdWithHttpInfo();
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling TaxesApi#taxControllerUpdateWithoutId");
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


ApiResponse<Void>

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request - Tax ID is required in the URL path |  -  |

