# ProductsApi

All URIs are relative to *https://api.devdraft.ai*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**productControllerCreate**](ProductsApi.md#productControllerCreate) | **POST** /api/v0/products | Create a new product |
| [**productControllerCreateWithHttpInfo**](ProductsApi.md#productControllerCreateWithHttpInfo) | **POST** /api/v0/products | Create a new product |
| [**productControllerFindAll**](ProductsApi.md#productControllerFindAll) | **GET** /api/v0/products | Get all products |
| [**productControllerFindAllWithHttpInfo**](ProductsApi.md#productControllerFindAllWithHttpInfo) | **GET** /api/v0/products | Get all products |
| [**productControllerFindOne**](ProductsApi.md#productControllerFindOne) | **GET** /api/v0/products/{id} | Get a product by ID |
| [**productControllerFindOneWithHttpInfo**](ProductsApi.md#productControllerFindOneWithHttpInfo) | **GET** /api/v0/products/{id} | Get a product by ID |
| [**productControllerRemove**](ProductsApi.md#productControllerRemove) | **DELETE** /api/v0/products/{id} | Delete a product |
| [**productControllerRemoveWithHttpInfo**](ProductsApi.md#productControllerRemoveWithHttpInfo) | **DELETE** /api/v0/products/{id} | Delete a product |
| [**productControllerUpdate**](ProductsApi.md#productControllerUpdate) | **PUT** /api/v0/products/{id} | Update a product |
| [**productControllerUpdateWithHttpInfo**](ProductsApi.md#productControllerUpdateWithHttpInfo) | **PUT** /api/v0/products/{id} | Update a product |
| [**productControllerUploadImage**](ProductsApi.md#productControllerUploadImage) | **POST** /api/v0/products/{id}/images | Upload images for a product |
| [**productControllerUploadImageWithHttpInfo**](ProductsApi.md#productControllerUploadImageWithHttpInfo) | **POST** /api/v0/products/{id}/images | Upload images for a product |



## productControllerCreate

> void productControllerCreate(name, description, price, currency, type, weight, unit, quantity, stockCount, status, productType, images)

Create a new product

Creates a new product with optional image uploads.      This endpoint allows you to create products with detailed information and multiple images.  ## Use Cases - Add new products to your catalog - Create products with multiple images - Set up product pricing and descriptions  ## Supported Image Formats - JPEG/JPG - PNG - WebP - Maximum 10 images per product - Maximum file size: 5MB per image  ## Example Request (multipart/form-data) &#x60;&#x60;&#x60; name: \&quot;Premium Widget\&quot; description: \&quot;High-quality widget for all your needs\&quot; price: \&quot;99.99\&quot; images: [file1.jpg, file2.jpg]  // Optional, up to 10 images &#x60;&#x60;&#x60;  ## Required Fields - &#x60;name&#x60;: Product name - &#x60;price&#x60;: Product price (decimal number)  ## Optional Fields - &#x60;description&#x60;: Detailed product description - &#x60;images&#x60;: Product images (up to 10 files)

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

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

        ProductsApi apiInstance = new ProductsApi(defaultClient);
        String name = "name_example"; // String | Product name as it will appear to customers. Should be clear and descriptive.
        String description = "description_example"; // String | Detailed description of the product. Supports markdown formatting for rich text display.
        BigDecimal price = new BigDecimal(78); // BigDecimal | Product price in the specified currency. Must be greater than 0.
        String currency = "USD"; // String | Currency code for the price. Defaults to USD if not specified.
        String type = "type_example"; // String | Product type
        BigDecimal weight = new BigDecimal(78); // BigDecimal | Weight of the product
        String unit = "unit_example"; // String | Unit of measurement
        BigDecimal quantity = new BigDecimal(78); // BigDecimal | Quantity available
        BigDecimal stockCount = new BigDecimal(78); // BigDecimal | Stock count
        String status = "status_example"; // String | Product status
        String productType = "productType_example"; // String | Product type
        List<String> images = Arrays.asList(); // List<String> | Array of image URLs
        try {
            apiInstance.productControllerCreate(name, description, price, currency, type, weight, unit, quantity, stockCount, status, productType, images);
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductsApi#productControllerCreate");
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
| **name** | **String**| Product name as it will appear to customers. Should be clear and descriptive. | |
| **description** | **String**| Detailed description of the product. Supports markdown formatting for rich text display. | |
| **price** | **BigDecimal**| Product price in the specified currency. Must be greater than 0. | |
| **currency** | **String**| Currency code for the price. Defaults to USD if not specified. | [optional] [default to USD] [enum: USD, EUR, GBP, CAD, AUD, JPY] |
| **type** | **String**| Product type | [optional] |
| **weight** | **BigDecimal**| Weight of the product | [optional] |
| **unit** | **String**| Unit of measurement | [optional] |
| **quantity** | **BigDecimal**| Quantity available | [optional] |
| **stockCount** | **BigDecimal**| Stock count | [optional] |
| **status** | **String**| Product status | [optional] |
| **productType** | **String**| Product type | [optional] |
| **images** | [**List&lt;String&gt;**](String.md)| Array of image URLs | [optional] |

### Return type


null (empty response body)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The product has been successfully created. |  -  |
| **400** | Bad Request - Invalid input data or image format |  -  |
| **401** | Unauthorized - Invalid API credentials |  -  |
| **413** | Payload Too Large - Image files too large |  -  |

## productControllerCreateWithHttpInfo

> ApiResponse<Void> productControllerCreate productControllerCreateWithHttpInfo(name, description, price, currency, type, weight, unit, quantity, stockCount, status, productType, images)

Create a new product

Creates a new product with optional image uploads.      This endpoint allows you to create products with detailed information and multiple images.  ## Use Cases - Add new products to your catalog - Create products with multiple images - Set up product pricing and descriptions  ## Supported Image Formats - JPEG/JPG - PNG - WebP - Maximum 10 images per product - Maximum file size: 5MB per image  ## Example Request (multipart/form-data) &#x60;&#x60;&#x60; name: \&quot;Premium Widget\&quot; description: \&quot;High-quality widget for all your needs\&quot; price: \&quot;99.99\&quot; images: [file1.jpg, file2.jpg]  // Optional, up to 10 images &#x60;&#x60;&#x60;  ## Required Fields - &#x60;name&#x60;: Product name - &#x60;price&#x60;: Product price (decimal number)  ## Optional Fields - &#x60;description&#x60;: Detailed product description - &#x60;images&#x60;: Product images (up to 10 files)

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

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

        ProductsApi apiInstance = new ProductsApi(defaultClient);
        String name = "name_example"; // String | Product name as it will appear to customers. Should be clear and descriptive.
        String description = "description_example"; // String | Detailed description of the product. Supports markdown formatting for rich text display.
        BigDecimal price = new BigDecimal(78); // BigDecimal | Product price in the specified currency. Must be greater than 0.
        String currency = "USD"; // String | Currency code for the price. Defaults to USD if not specified.
        String type = "type_example"; // String | Product type
        BigDecimal weight = new BigDecimal(78); // BigDecimal | Weight of the product
        String unit = "unit_example"; // String | Unit of measurement
        BigDecimal quantity = new BigDecimal(78); // BigDecimal | Quantity available
        BigDecimal stockCount = new BigDecimal(78); // BigDecimal | Stock count
        String status = "status_example"; // String | Product status
        String productType = "productType_example"; // String | Product type
        List<String> images = Arrays.asList(); // List<String> | Array of image URLs
        try {
            ApiResponse<Void> response = apiInstance.productControllerCreateWithHttpInfo(name, description, price, currency, type, weight, unit, quantity, stockCount, status, productType, images);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductsApi#productControllerCreate");
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
| **name** | **String**| Product name as it will appear to customers. Should be clear and descriptive. | |
| **description** | **String**| Detailed description of the product. Supports markdown formatting for rich text display. | |
| **price** | **BigDecimal**| Product price in the specified currency. Must be greater than 0. | |
| **currency** | **String**| Currency code for the price. Defaults to USD if not specified. | [optional] [default to USD] [enum: USD, EUR, GBP, CAD, AUD, JPY] |
| **type** | **String**| Product type | [optional] |
| **weight** | **BigDecimal**| Weight of the product | [optional] |
| **unit** | **String**| Unit of measurement | [optional] |
| **quantity** | **BigDecimal**| Quantity available | [optional] |
| **stockCount** | **BigDecimal**| Stock count | [optional] |
| **status** | **String**| Product status | [optional] |
| **productType** | **String**| Product type | [optional] |
| **images** | [**List&lt;String&gt;**](String.md)| Array of image URLs | [optional] |

### Return type


ApiResponse<Void>

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The product has been successfully created. |  -  |
| **400** | Bad Request - Invalid input data or image format |  -  |
| **401** | Unauthorized - Invalid API credentials |  -  |
| **413** | Payload Too Large - Image files too large |  -  |


## productControllerFindAll

> void productControllerFindAll(skip, take)

Get all products

Retrieves a list of products with pagination.      This endpoint allows you to fetch products with optional pagination.  ## Use Cases - List all products - Browse product catalog - Implement product search  ## Query Parameters - &#x60;skip&#x60;: Number of records to skip (default: 0) - &#x60;take&#x60;: Number of records to take (default: 10)  ## Example Response &#x60;&#x60;&#x60;json {   \&quot;data\&quot;: [     {       \&quot;id\&quot;: \&quot;prod_123456\&quot;,       \&quot;name\&quot;: \&quot;Premium Widget\&quot;,       \&quot;description\&quot;: \&quot;High-quality widget for all your needs\&quot;,       \&quot;price\&quot;: \&quot;99.99\&quot;,       \&quot;images\&quot;: [         \&quot;https://storage.example.com/images/file1.jpg\&quot;,         \&quot;https://storage.example.com/images/file2.jpg\&quot;       ],       \&quot;createdAt\&quot;: \&quot;2024-03-20T10:00:00Z\&quot;     }   ],   \&quot;total\&quot;: 100,   \&quot;skip\&quot;: 0,   \&quot;take\&quot;: 10 } &#x60;&#x60;&#x60;

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

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

        ProductsApi apiInstance = new ProductsApi(defaultClient);
        BigDecimal skip = new BigDecimal(78); // BigDecimal | Number of records to skip
        BigDecimal take = new BigDecimal(78); // BigDecimal | Number of records to take
        try {
            apiInstance.productControllerFindAll(skip, take);
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductsApi#productControllerFindAll");
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
| **200** | Return all products. |  -  |
| **401** | Unauthorized - Invalid API credentials |  -  |

## productControllerFindAllWithHttpInfo

> ApiResponse<Void> productControllerFindAll productControllerFindAllWithHttpInfo(skip, take)

Get all products

Retrieves a list of products with pagination.      This endpoint allows you to fetch products with optional pagination.  ## Use Cases - List all products - Browse product catalog - Implement product search  ## Query Parameters - &#x60;skip&#x60;: Number of records to skip (default: 0) - &#x60;take&#x60;: Number of records to take (default: 10)  ## Example Response &#x60;&#x60;&#x60;json {   \&quot;data\&quot;: [     {       \&quot;id\&quot;: \&quot;prod_123456\&quot;,       \&quot;name\&quot;: \&quot;Premium Widget\&quot;,       \&quot;description\&quot;: \&quot;High-quality widget for all your needs\&quot;,       \&quot;price\&quot;: \&quot;99.99\&quot;,       \&quot;images\&quot;: [         \&quot;https://storage.example.com/images/file1.jpg\&quot;,         \&quot;https://storage.example.com/images/file2.jpg\&quot;       ],       \&quot;createdAt\&quot;: \&quot;2024-03-20T10:00:00Z\&quot;     }   ],   \&quot;total\&quot;: 100,   \&quot;skip\&quot;: 0,   \&quot;take\&quot;: 10 } &#x60;&#x60;&#x60;

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

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

        ProductsApi apiInstance = new ProductsApi(defaultClient);
        BigDecimal skip = new BigDecimal(78); // BigDecimal | Number of records to skip
        BigDecimal take = new BigDecimal(78); // BigDecimal | Number of records to take
        try {
            ApiResponse<Void> response = apiInstance.productControllerFindAllWithHttpInfo(skip, take);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductsApi#productControllerFindAll");
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
| **200** | Return all products. |  -  |
| **401** | Unauthorized - Invalid API credentials |  -  |


## productControllerFindOne

> void productControllerFindOne(id)

Get a product by ID

Retrieves detailed information about a specific product.      This endpoint allows you to fetch complete product details including all images.  ## Use Cases - View product details - Display product information - Check product availability  ## Example Response &#x60;&#x60;&#x60;json {   \&quot;id\&quot;: \&quot;prod_123456\&quot;,   \&quot;name\&quot;: \&quot;Premium Widget\&quot;,   \&quot;description\&quot;: \&quot;High-quality widget for all your needs\&quot;,   \&quot;price\&quot;: \&quot;99.99\&quot;,   \&quot;images\&quot;: [     \&quot;https://storage.example.com/images/file1.jpg\&quot;,     \&quot;https://storage.example.com/images/file2.jpg\&quot;   ],   \&quot;createdAt\&quot;: \&quot;2024-03-20T10:00:00Z\&quot;,   \&quot;updatedAt\&quot;: \&quot;2024-03-20T10:00:00Z\&quot; } &#x60;&#x60;&#x60;

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

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

        ProductsApi apiInstance = new ProductsApi(defaultClient);
        String id = "id_example"; // String | Product ID
        try {
            apiInstance.productControllerFindOne(id);
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductsApi#productControllerFindOne");
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
| **id** | **String**| Product ID | |

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
| **200** | Return the product. |  -  |
| **401** | Unauthorized - Invalid API credentials |  -  |
| **404** | Product not found. |  -  |

## productControllerFindOneWithHttpInfo

> ApiResponse<Void> productControllerFindOne productControllerFindOneWithHttpInfo(id)

Get a product by ID

Retrieves detailed information about a specific product.      This endpoint allows you to fetch complete product details including all images.  ## Use Cases - View product details - Display product information - Check product availability  ## Example Response &#x60;&#x60;&#x60;json {   \&quot;id\&quot;: \&quot;prod_123456\&quot;,   \&quot;name\&quot;: \&quot;Premium Widget\&quot;,   \&quot;description\&quot;: \&quot;High-quality widget for all your needs\&quot;,   \&quot;price\&quot;: \&quot;99.99\&quot;,   \&quot;images\&quot;: [     \&quot;https://storage.example.com/images/file1.jpg\&quot;,     \&quot;https://storage.example.com/images/file2.jpg\&quot;   ],   \&quot;createdAt\&quot;: \&quot;2024-03-20T10:00:00Z\&quot;,   \&quot;updatedAt\&quot;: \&quot;2024-03-20T10:00:00Z\&quot; } &#x60;&#x60;&#x60;

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

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

        ProductsApi apiInstance = new ProductsApi(defaultClient);
        String id = "id_example"; // String | Product ID
        try {
            ApiResponse<Void> response = apiInstance.productControllerFindOneWithHttpInfo(id);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductsApi#productControllerFindOne");
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
| **id** | **String**| Product ID | |

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
| **200** | Return the product. |  -  |
| **401** | Unauthorized - Invalid API credentials |  -  |
| **404** | Product not found. |  -  |


## productControllerRemove

> void productControllerRemove(id)

Delete a product

Deletes a product and its associated images.      This endpoint allows you to remove a product and all its associated data.  ## Use Cases - Remove discontinued products - Clean up product catalog - Delete test products  ## Notes - This action cannot be undone - All product images will be deleted - Associated data will be removed

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

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

        ProductsApi apiInstance = new ProductsApi(defaultClient);
        String id = "id_example"; // String | Product ID
        try {
            apiInstance.productControllerRemove(id);
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductsApi#productControllerRemove");
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
| **id** | **String**| Product ID | |

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
| **200** | The product has been successfully deleted. |  -  |
| **401** | Unauthorized - Invalid API credentials |  -  |
| **404** | Product not found. |  -  |

## productControllerRemoveWithHttpInfo

> ApiResponse<Void> productControllerRemove productControllerRemoveWithHttpInfo(id)

Delete a product

Deletes a product and its associated images.      This endpoint allows you to remove a product and all its associated data.  ## Use Cases - Remove discontinued products - Clean up product catalog - Delete test products  ## Notes - This action cannot be undone - All product images will be deleted - Associated data will be removed

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

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

        ProductsApi apiInstance = new ProductsApi(defaultClient);
        String id = "id_example"; // String | Product ID
        try {
            ApiResponse<Void> response = apiInstance.productControllerRemoveWithHttpInfo(id);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductsApi#productControllerRemove");
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
| **id** | **String**| Product ID | |

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
| **200** | The product has been successfully deleted. |  -  |
| **401** | Unauthorized - Invalid API credentials |  -  |
| **404** | Product not found. |  -  |


## productControllerUpdate

> void productControllerUpdate(id, name, description, price, currency, type, weight, unit, quantity, stockCount, status, productType, images)

Update a product

Updates an existing product&#39;s information and optionally adds new images.      This endpoint allows you to modify product details and manage product images.  ## Use Cases - Update product information - Change product pricing - Modify product images - Update product description  ## Example Request (multipart/form-data) &#x60;&#x60;&#x60; name: \&quot;Updated Premium Widget\&quot; description: \&quot;Updated description\&quot; price: \&quot;129.99\&quot; images: [file1.jpg, file2.jpg]  // Optional, up to 10 images &#x60;&#x60;&#x60;  ## Notes - Only include fields that need to be updated - New images will replace existing images - Maximum 10 images per product - Images are automatically optimized

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

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

        ProductsApi apiInstance = new ProductsApi(defaultClient);
        String id = "id_example"; // String | Product ID
        String name = "name_example"; // String | Product name as it will appear to customers. Should be clear and descriptive.
        String description = "description_example"; // String | Detailed description of the product. Supports markdown formatting for rich text display.
        BigDecimal price = new BigDecimal(78); // BigDecimal | Product price in the specified currency. Must be greater than 0.
        String currency = "USD"; // String | Currency code for the price. Defaults to USD if not specified.
        String type = "type_example"; // String | Product type
        BigDecimal weight = new BigDecimal(78); // BigDecimal | Weight of the product
        String unit = "unit_example"; // String | Unit of measurement
        BigDecimal quantity = new BigDecimal(78); // BigDecimal | Quantity available
        BigDecimal stockCount = new BigDecimal(78); // BigDecimal | Stock count
        String status = "status_example"; // String | Product status
        String productType = "productType_example"; // String | Product type
        List<String> images = Arrays.asList(); // List<String> | Array of image URLs
        try {
            apiInstance.productControllerUpdate(id, name, description, price, currency, type, weight, unit, quantity, stockCount, status, productType, images);
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductsApi#productControllerUpdate");
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
| **id** | **String**| Product ID | |
| **name** | **String**| Product name as it will appear to customers. Should be clear and descriptive. | [optional] |
| **description** | **String**| Detailed description of the product. Supports markdown formatting for rich text display. | [optional] |
| **price** | **BigDecimal**| Product price in the specified currency. Must be greater than 0. | [optional] |
| **currency** | **String**| Currency code for the price. Defaults to USD if not specified. | [optional] [default to USD] [enum: USD, EUR, GBP, CAD, AUD, JPY] |
| **type** | **String**| Product type | [optional] |
| **weight** | **BigDecimal**| Weight of the product | [optional] |
| **unit** | **String**| Unit of measurement | [optional] |
| **quantity** | **BigDecimal**| Quantity available | [optional] |
| **stockCount** | **BigDecimal**| Stock count | [optional] |
| **status** | **String**| Product status | [optional] |
| **productType** | **String**| Product type | [optional] |
| **images** | [**List&lt;String&gt;**](String.md)| Array of image URLs | [optional] |

### Return type


null (empty response body)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The product has been successfully updated. |  -  |
| **400** | Bad Request - Invalid input data or image format |  -  |
| **401** | Unauthorized - Invalid API credentials |  -  |
| **404** | Product not found. |  -  |
| **413** | Payload Too Large - Image files too large |  -  |

## productControllerUpdateWithHttpInfo

> ApiResponse<Void> productControllerUpdate productControllerUpdateWithHttpInfo(id, name, description, price, currency, type, weight, unit, quantity, stockCount, status, productType, images)

Update a product

Updates an existing product&#39;s information and optionally adds new images.      This endpoint allows you to modify product details and manage product images.  ## Use Cases - Update product information - Change product pricing - Modify product images - Update product description  ## Example Request (multipart/form-data) &#x60;&#x60;&#x60; name: \&quot;Updated Premium Widget\&quot; description: \&quot;Updated description\&quot; price: \&quot;129.99\&quot; images: [file1.jpg, file2.jpg]  // Optional, up to 10 images &#x60;&#x60;&#x60;  ## Notes - Only include fields that need to be updated - New images will replace existing images - Maximum 10 images per product - Images are automatically optimized

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

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

        ProductsApi apiInstance = new ProductsApi(defaultClient);
        String id = "id_example"; // String | Product ID
        String name = "name_example"; // String | Product name as it will appear to customers. Should be clear and descriptive.
        String description = "description_example"; // String | Detailed description of the product. Supports markdown formatting for rich text display.
        BigDecimal price = new BigDecimal(78); // BigDecimal | Product price in the specified currency. Must be greater than 0.
        String currency = "USD"; // String | Currency code for the price. Defaults to USD if not specified.
        String type = "type_example"; // String | Product type
        BigDecimal weight = new BigDecimal(78); // BigDecimal | Weight of the product
        String unit = "unit_example"; // String | Unit of measurement
        BigDecimal quantity = new BigDecimal(78); // BigDecimal | Quantity available
        BigDecimal stockCount = new BigDecimal(78); // BigDecimal | Stock count
        String status = "status_example"; // String | Product status
        String productType = "productType_example"; // String | Product type
        List<String> images = Arrays.asList(); // List<String> | Array of image URLs
        try {
            ApiResponse<Void> response = apiInstance.productControllerUpdateWithHttpInfo(id, name, description, price, currency, type, weight, unit, quantity, stockCount, status, productType, images);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductsApi#productControllerUpdate");
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
| **id** | **String**| Product ID | |
| **name** | **String**| Product name as it will appear to customers. Should be clear and descriptive. | [optional] |
| **description** | **String**| Detailed description of the product. Supports markdown formatting for rich text display. | [optional] |
| **price** | **BigDecimal**| Product price in the specified currency. Must be greater than 0. | [optional] |
| **currency** | **String**| Currency code for the price. Defaults to USD if not specified. | [optional] [default to USD] [enum: USD, EUR, GBP, CAD, AUD, JPY] |
| **type** | **String**| Product type | [optional] |
| **weight** | **BigDecimal**| Weight of the product | [optional] |
| **unit** | **String**| Unit of measurement | [optional] |
| **quantity** | **BigDecimal**| Quantity available | [optional] |
| **stockCount** | **BigDecimal**| Stock count | [optional] |
| **status** | **String**| Product status | [optional] |
| **productType** | **String**| Product type | [optional] |
| **images** | [**List&lt;String&gt;**](String.md)| Array of image URLs | [optional] |

### Return type


ApiResponse<Void>

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The product has been successfully updated. |  -  |
| **400** | Bad Request - Invalid input data or image format |  -  |
| **401** | Unauthorized - Invalid API credentials |  -  |
| **404** | Product not found. |  -  |
| **413** | Payload Too Large - Image files too large |  -  |


## productControllerUploadImage

> void productControllerUploadImage(id)

Upload images for a product

Adds new images to an existing product.      This endpoint allows you to upload additional images for a product that already exists.  ## Use Cases - Add more product images - Update product gallery - Enhance product presentation  ## Supported Image Formats - JPEG/JPG - PNG - WebP - Maximum 10 images per upload - Maximum file size: 5MB per image  ## Example Request (multipart/form-data) &#x60;&#x60;&#x60; images: [file1.jpg, file2.jpg]  // Up to 10 images &#x60;&#x60;&#x60;  ## Notes - Images are appended to existing product images - Total images per product cannot exceed 10 - Images are automatically optimized and resized

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

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

        ProductsApi apiInstance = new ProductsApi(defaultClient);
        String id = "id_example"; // String | Product ID
        try {
            apiInstance.productControllerUploadImage(id);
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductsApi#productControllerUploadImage");
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
| **id** | **String**| Product ID | |

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
| **201** | The images have been successfully uploaded. |  -  |
| **401** | Unauthorized - Invalid API credentials |  -  |
| **404** | Product not found. |  -  |
| **413** | Payload Too Large - Image files too large |  -  |

## productControllerUploadImageWithHttpInfo

> ApiResponse<Void> productControllerUploadImage productControllerUploadImageWithHttpInfo(id)

Upload images for a product

Adds new images to an existing product.      This endpoint allows you to upload additional images for a product that already exists.  ## Use Cases - Add more product images - Update product gallery - Enhance product presentation  ## Supported Image Formats - JPEG/JPG - PNG - WebP - Maximum 10 images per upload - Maximum file size: 5MB per image  ## Example Request (multipart/form-data) &#x60;&#x60;&#x60; images: [file1.jpg, file2.jpg]  // Up to 10 images &#x60;&#x60;&#x60;  ## Notes - Images are appended to existing product images - Total images per product cannot exceed 10 - Images are automatically optimized and resized

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

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

        ProductsApi apiInstance = new ProductsApi(defaultClient);
        String id = "id_example"; // String | Product ID
        try {
            ApiResponse<Void> response = apiInstance.productControllerUploadImageWithHttpInfo(id);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductsApi#productControllerUploadImage");
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
| **id** | **String**| Product ID | |

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
| **201** | The images have been successfully uploaded. |  -  |
| **401** | Unauthorized - Invalid API credentials |  -  |
| **404** | Product not found. |  -  |
| **413** | Payload Too Large - Image files too large |  -  |

