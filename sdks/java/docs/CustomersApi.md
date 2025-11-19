# CustomersApi

All URIs are relative to *https://api.devdraft.ai*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**customerControllerCreate**](CustomersApi.md#customerControllerCreate) | **POST** /api/v0/customers | Create a new customer |
| [**customerControllerCreateWithHttpInfo**](CustomersApi.md#customerControllerCreateWithHttpInfo) | **POST** /api/v0/customers | Create a new customer |
| [**customerControllerFindAll**](CustomersApi.md#customerControllerFindAll) | **GET** /api/v0/customers | Get all customers with filters |
| [**customerControllerFindAllWithHttpInfo**](CustomersApi.md#customerControllerFindAllWithHttpInfo) | **GET** /api/v0/customers | Get all customers with filters |
| [**customerControllerFindOne**](CustomersApi.md#customerControllerFindOne) | **GET** /api/v0/customers/{id} | Get a customer by ID |
| [**customerControllerFindOneWithHttpInfo**](CustomersApi.md#customerControllerFindOneWithHttpInfo) | **GET** /api/v0/customers/{id} | Get a customer by ID |
| [**customerControllerUpdate**](CustomersApi.md#customerControllerUpdate) | **PATCH** /api/v0/customers/{id} | Update a customer |
| [**customerControllerUpdateWithHttpInfo**](CustomersApi.md#customerControllerUpdateWithHttpInfo) | **PATCH** /api/v0/customers/{id} | Update a customer |



## customerControllerCreate

> void customerControllerCreate(createCustomerDto)

Create a new customer

Creates a new customer in the system with their personal and contact information.      This endpoint allows you to register new customers and store their details for future transactions.  ## Use Cases - Register new customers for payment processing - Store customer information for recurring payments - Maintain customer profiles for transaction history  ## Example: Create New Customer &#x60;&#x60;&#x60;json {   \&quot;first_name\&quot;: \&quot;John\&quot;,   \&quot;last_name\&quot;: \&quot;Doe\&quot;,   \&quot;email\&quot;: \&quot;john.doe@example.com\&quot;,   \&quot;phone_number\&quot;: \&quot;+1-555-123-4567\&quot;,   \&quot;customer_type\&quot;: \&quot;Startup\&quot;,   \&quot;status\&quot;: \&quot;ACTIVE\&quot; } &#x60;&#x60;&#x60;  ## Required Fields - &#x60;first_name&#x60;: Customer&#39;s first name (1-100 characters) - &#x60;last_name&#x60;: Customer&#39;s last name (1-100 characters) - &#x60;phone_number&#x60;: Customer&#39;s phone number (max 20 characters)  ## Optional Fields - &#x60;email&#x60;: Valid email address (max 255 characters) - &#x60;customer_type&#x60;: Type of customer account (Individual, Startup, Small Business, Medium Business, Enterprise, Non-Profit, Government) - &#x60;status&#x60;: Customer status (ACTIVE, BLACKLISTED, DEACTIVATED)

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersApi;

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

        CustomersApi apiInstance = new CustomersApi(defaultClient);
        CreateCustomerDto createCustomerDto = new CreateCustomerDto(); // CreateCustomerDto | Customer creation data
        try {
            apiInstance.customerControllerCreate(createCustomerDto);
        } catch (ApiException e) {
            System.err.println("Exception when calling CustomersApi#customerControllerCreate");
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
| **createCustomerDto** | [**CreateCustomerDto**](CreateCustomerDto.md)| Customer creation data | |

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
| **201** | Customer created successfully |  -  |
| **400** | Bad Request - Invalid input data |  -  |
| **401** | Unauthorized - Invalid API credentials |  -  |
| **409** | Conflict - Customer with the same email already exists |  -  |

## customerControllerCreateWithHttpInfo

> ApiResponse<Void> customerControllerCreate customerControllerCreateWithHttpInfo(createCustomerDto)

Create a new customer

Creates a new customer in the system with their personal and contact information.      This endpoint allows you to register new customers and store their details for future transactions.  ## Use Cases - Register new customers for payment processing - Store customer information for recurring payments - Maintain customer profiles for transaction history  ## Example: Create New Customer &#x60;&#x60;&#x60;json {   \&quot;first_name\&quot;: \&quot;John\&quot;,   \&quot;last_name\&quot;: \&quot;Doe\&quot;,   \&quot;email\&quot;: \&quot;john.doe@example.com\&quot;,   \&quot;phone_number\&quot;: \&quot;+1-555-123-4567\&quot;,   \&quot;customer_type\&quot;: \&quot;Startup\&quot;,   \&quot;status\&quot;: \&quot;ACTIVE\&quot; } &#x60;&#x60;&#x60;  ## Required Fields - &#x60;first_name&#x60;: Customer&#39;s first name (1-100 characters) - &#x60;last_name&#x60;: Customer&#39;s last name (1-100 characters) - &#x60;phone_number&#x60;: Customer&#39;s phone number (max 20 characters)  ## Optional Fields - &#x60;email&#x60;: Valid email address (max 255 characters) - &#x60;customer_type&#x60;: Type of customer account (Individual, Startup, Small Business, Medium Business, Enterprise, Non-Profit, Government) - &#x60;status&#x60;: Customer status (ACTIVE, BLACKLISTED, DEACTIVATED)

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersApi;

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

        CustomersApi apiInstance = new CustomersApi(defaultClient);
        CreateCustomerDto createCustomerDto = new CreateCustomerDto(); // CreateCustomerDto | Customer creation data
        try {
            ApiResponse<Void> response = apiInstance.customerControllerCreateWithHttpInfo(createCustomerDto);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling CustomersApi#customerControllerCreate");
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
| **createCustomerDto** | [**CreateCustomerDto**](CreateCustomerDto.md)| Customer creation data | |

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
| **201** | Customer created successfully |  -  |
| **400** | Bad Request - Invalid input data |  -  |
| **401** | Unauthorized - Invalid API credentials |  -  |
| **409** | Conflict - Customer with the same email already exists |  -  |


## customerControllerFindAll

> void customerControllerFindAll(skip, take, status, name, email)

Get all customers with filters

Retrieves a list of customers with optional filtering and pagination.      This endpoint allows you to search and filter customers based on various criteria.  ## Use Cases - List all customers with pagination - Search customers by name or email - Filter customers by status - Export customer data  ## Query Parameters - &#x60;skip&#x60;: Number of records to skip (default: 0, min: 0) - &#x60;take&#x60;: Number of records to take (default: 10, min: 1, max: 100) - &#x60;status&#x60;: Filter by customer status (ACTIVE, BLACKLISTED, DEACTIVATED) - &#x60;name&#x60;: Filter by customer name (partial match, case-insensitive) - &#x60;email&#x60;: Filter by customer email (exact match, case-insensitive)  ## Example Request &#x60;GET /api/v0/customers?skip&#x3D;0&amp;take&#x3D;20&amp;status&#x3D;ACTIVE&amp;name&#x3D;John&#x60;  ## Example Response &#x60;&#x60;&#x60;json {   \&quot;data\&quot;: [     {       \&quot;id\&quot;: \&quot;cust_123456\&quot;,       \&quot;first_name\&quot;: \&quot;John\&quot;,       \&quot;last_name\&quot;: \&quot;Doe\&quot;,       \&quot;email\&quot;: \&quot;john.doe@example.com\&quot;,       \&quot;phone_number\&quot;: \&quot;+1-555-123-4567\&quot;,       \&quot;customer_type\&quot;: \&quot;Startup\&quot;,       \&quot;status\&quot;: \&quot;ACTIVE\&quot;,       \&quot;created_at\&quot;: \&quot;2024-03-20T10:00:00Z\&quot;,       \&quot;updated_at\&quot;: \&quot;2024-03-20T10:00:00Z\&quot;     }   ],   \&quot;total\&quot;: 100,   \&quot;skip\&quot;: 0,   \&quot;take\&quot;: 10 } &#x60;&#x60;&#x60;

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersApi;

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

        CustomersApi apiInstance = new CustomersApi(defaultClient);
        BigDecimal skip = new BigDecimal("0"); // BigDecimal | Number of records to skip for pagination
        BigDecimal take = new BigDecimal("10"); // BigDecimal | Number of records to return (max 100)
        CustomerStatus status = CustomerStatus.fromValue("ACTIVE"); // CustomerStatus | Filter customers by status
        String name = "John"; // String | Filter customers by name (partial match, case-insensitive)
        String email = "john.doe@example.com"; // String | Filter customers by email (exact match, case-insensitive)
        try {
            apiInstance.customerControllerFindAll(skip, take, status, name, email);
        } catch (ApiException e) {
            System.err.println("Exception when calling CustomersApi#customerControllerFindAll");
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
| **status** | [**CustomerStatus**](.md)| Filter customers by status | [optional] [enum: ACTIVE, BLACKLISTED, DEACTIVATED, DELETED] |
| **name** | **String**| Filter customers by name (partial match, case-insensitive) | [optional] |
| **email** | **String**| Filter customers by email (exact match, case-insensitive) | [optional] |

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
| **200** | Successfully retrieved customers |  -  |
| **400** | Bad Request - Invalid query parameters |  -  |
| **401** | Unauthorized - Invalid API credentials |  -  |

## customerControllerFindAllWithHttpInfo

> ApiResponse<Void> customerControllerFindAll customerControllerFindAllWithHttpInfo(skip, take, status, name, email)

Get all customers with filters

Retrieves a list of customers with optional filtering and pagination.      This endpoint allows you to search and filter customers based on various criteria.  ## Use Cases - List all customers with pagination - Search customers by name or email - Filter customers by status - Export customer data  ## Query Parameters - &#x60;skip&#x60;: Number of records to skip (default: 0, min: 0) - &#x60;take&#x60;: Number of records to take (default: 10, min: 1, max: 100) - &#x60;status&#x60;: Filter by customer status (ACTIVE, BLACKLISTED, DEACTIVATED) - &#x60;name&#x60;: Filter by customer name (partial match, case-insensitive) - &#x60;email&#x60;: Filter by customer email (exact match, case-insensitive)  ## Example Request &#x60;GET /api/v0/customers?skip&#x3D;0&amp;take&#x3D;20&amp;status&#x3D;ACTIVE&amp;name&#x3D;John&#x60;  ## Example Response &#x60;&#x60;&#x60;json {   \&quot;data\&quot;: [     {       \&quot;id\&quot;: \&quot;cust_123456\&quot;,       \&quot;first_name\&quot;: \&quot;John\&quot;,       \&quot;last_name\&quot;: \&quot;Doe\&quot;,       \&quot;email\&quot;: \&quot;john.doe@example.com\&quot;,       \&quot;phone_number\&quot;: \&quot;+1-555-123-4567\&quot;,       \&quot;customer_type\&quot;: \&quot;Startup\&quot;,       \&quot;status\&quot;: \&quot;ACTIVE\&quot;,       \&quot;created_at\&quot;: \&quot;2024-03-20T10:00:00Z\&quot;,       \&quot;updated_at\&quot;: \&quot;2024-03-20T10:00:00Z\&quot;     }   ],   \&quot;total\&quot;: 100,   \&quot;skip\&quot;: 0,   \&quot;take\&quot;: 10 } &#x60;&#x60;&#x60;

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersApi;

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

        CustomersApi apiInstance = new CustomersApi(defaultClient);
        BigDecimal skip = new BigDecimal("0"); // BigDecimal | Number of records to skip for pagination
        BigDecimal take = new BigDecimal("10"); // BigDecimal | Number of records to return (max 100)
        CustomerStatus status = CustomerStatus.fromValue("ACTIVE"); // CustomerStatus | Filter customers by status
        String name = "John"; // String | Filter customers by name (partial match, case-insensitive)
        String email = "john.doe@example.com"; // String | Filter customers by email (exact match, case-insensitive)
        try {
            ApiResponse<Void> response = apiInstance.customerControllerFindAllWithHttpInfo(skip, take, status, name, email);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling CustomersApi#customerControllerFindAll");
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
| **status** | [**CustomerStatus**](.md)| Filter customers by status | [optional] [enum: ACTIVE, BLACKLISTED, DEACTIVATED, DELETED] |
| **name** | **String**| Filter customers by name (partial match, case-insensitive) | [optional] |
| **email** | **String**| Filter customers by email (exact match, case-insensitive) | [optional] |

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
| **200** | Successfully retrieved customers |  -  |
| **400** | Bad Request - Invalid query parameters |  -  |
| **401** | Unauthorized - Invalid API credentials |  -  |


## customerControllerFindOne

> void customerControllerFindOne(id)

Get a customer by ID

Retrieves detailed information about a specific customer.      This endpoint allows you to fetch complete customer details including their contact information and status.  ## Use Cases - View customer details - Verify customer information - Check customer status before processing payments  ## Path Parameters - &#x60;id&#x60;: Customer UUID (required) - Must be a valid UUID format  ## Example Request &#x60;GET /api/v0/customers/123e4567-e89b-12d3-a456-426614174000&#x60;  ## Example Response &#x60;&#x60;&#x60;json {   \&quot;id\&quot;: \&quot;cust_123456\&quot;,   \&quot;first_name\&quot;: \&quot;John\&quot;,   \&quot;last_name\&quot;: \&quot;Doe\&quot;,   \&quot;email\&quot;: \&quot;john.doe@example.com\&quot;,   \&quot;phone_number\&quot;: \&quot;+1-555-123-4567\&quot;,   \&quot;customer_type\&quot;: \&quot;Enterprise\&quot;,   \&quot;status\&quot;: \&quot;ACTIVE\&quot;,   \&quot;last_spent\&quot;: 1250.50,   \&quot;last_purchase_date\&quot;: \&quot;2024-03-15T14:30:00Z\&quot;,   \&quot;created_at\&quot;: \&quot;2024-03-20T10:00:00Z\&quot;,   \&quot;updated_at\&quot;: \&quot;2024-03-20T10:00:00Z\&quot; } &#x60;&#x60;&#x60;

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersApi;

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

        CustomersApi apiInstance = new CustomersApi(defaultClient);
        UUID id = UUID.randomUUID(); // UUID | Customer unique identifier (UUID)
        try {
            apiInstance.customerControllerFindOne(id);
        } catch (ApiException e) {
            System.err.println("Exception when calling CustomersApi#customerControllerFindOne");
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
| **id** | **UUID**| Customer unique identifier (UUID) | |

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
| **200** | Successfully retrieved customer |  -  |
| **400** | Bad Request - Invalid customer ID format |  -  |
| **401** | Unauthorized - Invalid API credentials |  -  |
| **404** | Not Found - Customer not found |  -  |

## customerControllerFindOneWithHttpInfo

> ApiResponse<Void> customerControllerFindOne customerControllerFindOneWithHttpInfo(id)

Get a customer by ID

Retrieves detailed information about a specific customer.      This endpoint allows you to fetch complete customer details including their contact information and status.  ## Use Cases - View customer details - Verify customer information - Check customer status before processing payments  ## Path Parameters - &#x60;id&#x60;: Customer UUID (required) - Must be a valid UUID format  ## Example Request &#x60;GET /api/v0/customers/123e4567-e89b-12d3-a456-426614174000&#x60;  ## Example Response &#x60;&#x60;&#x60;json {   \&quot;id\&quot;: \&quot;cust_123456\&quot;,   \&quot;first_name\&quot;: \&quot;John\&quot;,   \&quot;last_name\&quot;: \&quot;Doe\&quot;,   \&quot;email\&quot;: \&quot;john.doe@example.com\&quot;,   \&quot;phone_number\&quot;: \&quot;+1-555-123-4567\&quot;,   \&quot;customer_type\&quot;: \&quot;Enterprise\&quot;,   \&quot;status\&quot;: \&quot;ACTIVE\&quot;,   \&quot;last_spent\&quot;: 1250.50,   \&quot;last_purchase_date\&quot;: \&quot;2024-03-15T14:30:00Z\&quot;,   \&quot;created_at\&quot;: \&quot;2024-03-20T10:00:00Z\&quot;,   \&quot;updated_at\&quot;: \&quot;2024-03-20T10:00:00Z\&quot; } &#x60;&#x60;&#x60;

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersApi;

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

        CustomersApi apiInstance = new CustomersApi(defaultClient);
        UUID id = UUID.randomUUID(); // UUID | Customer unique identifier (UUID)
        try {
            ApiResponse<Void> response = apiInstance.customerControllerFindOneWithHttpInfo(id);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling CustomersApi#customerControllerFindOne");
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
| **id** | **UUID**| Customer unique identifier (UUID) | |

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
| **200** | Successfully retrieved customer |  -  |
| **400** | Bad Request - Invalid customer ID format |  -  |
| **401** | Unauthorized - Invalid API credentials |  -  |
| **404** | Not Found - Customer not found |  -  |


## customerControllerUpdate

> void customerControllerUpdate(id, updateCustomerDto)

Update a customer

Updates an existing customer&#39;s information.      This endpoint allows you to modify customer details while preserving their core information.  ## Use Cases - Update customer contact information - Change customer type - Modify customer status  ## Path Parameters - &#x60;id&#x60;: Customer UUID (required) - Must be a valid UUID format  ## Example Request &#x60;PATCH /api/v0/customers/123e4567-e89b-12d3-a456-426614174000&#x60;  ## Example Request Body &#x60;&#x60;&#x60;json {   \&quot;first_name\&quot;: \&quot;John\&quot;,   \&quot;last_name\&quot;: \&quot;Smith\&quot;,   \&quot;phone_number\&quot;: \&quot;+1-987-654-3210\&quot;,   \&quot;customer_type\&quot;: \&quot;Small Business\&quot; } &#x60;&#x60;&#x60;  ## Notes - Only include fields that need to be updated - All fields are optional in updates - Status changes may require additional verification

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersApi;

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

        CustomersApi apiInstance = new CustomersApi(defaultClient);
        UUID id = UUID.randomUUID(); // UUID | Customer unique identifier (UUID)
        UpdateCustomerDto updateCustomerDto = new UpdateCustomerDto(); // UpdateCustomerDto | Customer update data
        try {
            apiInstance.customerControllerUpdate(id, updateCustomerDto);
        } catch (ApiException e) {
            System.err.println("Exception when calling CustomersApi#customerControllerUpdate");
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
| **id** | **UUID**| Customer unique identifier (UUID) | |
| **updateCustomerDto** | [**UpdateCustomerDto**](UpdateCustomerDto.md)| Customer update data | |

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
| **200** | Successfully updated customer |  -  |
| **400** | Bad Request - Invalid input data or customer ID format |  -  |
| **401** | Unauthorized - Invalid API credentials |  -  |
| **404** | Not Found - Customer not found |  -  |

## customerControllerUpdateWithHttpInfo

> ApiResponse<Void> customerControllerUpdate customerControllerUpdateWithHttpInfo(id, updateCustomerDto)

Update a customer

Updates an existing customer&#39;s information.      This endpoint allows you to modify customer details while preserving their core information.  ## Use Cases - Update customer contact information - Change customer type - Modify customer status  ## Path Parameters - &#x60;id&#x60;: Customer UUID (required) - Must be a valid UUID format  ## Example Request &#x60;PATCH /api/v0/customers/123e4567-e89b-12d3-a456-426614174000&#x60;  ## Example Request Body &#x60;&#x60;&#x60;json {   \&quot;first_name\&quot;: \&quot;John\&quot;,   \&quot;last_name\&quot;: \&quot;Smith\&quot;,   \&quot;phone_number\&quot;: \&quot;+1-987-654-3210\&quot;,   \&quot;customer_type\&quot;: \&quot;Small Business\&quot; } &#x60;&#x60;&#x60;  ## Notes - Only include fields that need to be updated - All fields are optional in updates - Status changes may require additional verification

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersApi;

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

        CustomersApi apiInstance = new CustomersApi(defaultClient);
        UUID id = UUID.randomUUID(); // UUID | Customer unique identifier (UUID)
        UpdateCustomerDto updateCustomerDto = new UpdateCustomerDto(); // UpdateCustomerDto | Customer update data
        try {
            ApiResponse<Void> response = apiInstance.customerControllerUpdateWithHttpInfo(id, updateCustomerDto);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling CustomersApi#customerControllerUpdate");
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
| **id** | **UUID**| Customer unique identifier (UUID) | |
| **updateCustomerDto** | [**UpdateCustomerDto**](UpdateCustomerDto.md)| Customer update data | |

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
| **200** | Successfully updated customer |  -  |
| **400** | Bad Request - Invalid input data or customer ID format |  -  |
| **401** | Unauthorized - Invalid API credentials |  -  |
| **404** | Not Found - Customer not found |  -  |

