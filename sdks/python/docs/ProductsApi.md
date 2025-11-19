# devdraft.ProductsApi

All URIs are relative to *https://api.devdraft.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**product_controller_create**](ProductsApi.md#product_controller_create) | **POST** /api/v0/products | Create a new product
[**product_controller_find_all**](ProductsApi.md#product_controller_find_all) | **GET** /api/v0/products | Get all products
[**product_controller_find_one**](ProductsApi.md#product_controller_find_one) | **GET** /api/v0/products/{id} | Get a product by ID
[**product_controller_remove**](ProductsApi.md#product_controller_remove) | **DELETE** /api/v0/products/{id} | Delete a product
[**product_controller_update**](ProductsApi.md#product_controller_update) | **PUT** /api/v0/products/{id} | Update a product
[**product_controller_upload_image**](ProductsApi.md#product_controller_upload_image) | **POST** /api/v0/products/{id}/images | Upload images for a product


# **product_controller_create**
> product_controller_create(name, description, price, currency=currency, type=type, weight=weight, unit=unit, quantity=quantity, stock_count=stock_count, status=status, product_type=product_type, images=images)

Create a new product

Creates a new product with optional image uploads.
    
This endpoint allows you to create products with detailed information and multiple images.

## Use Cases
- Add new products to your catalog
- Create products with multiple images
- Set up product pricing and descriptions

## Supported Image Formats
- JPEG/JPG
- PNG
- WebP
- Maximum 10 images per product
- Maximum file size: 5MB per image

## Example Request (multipart/form-data)
```
name: "Premium Widget"
description: "High-quality widget for all your needs"
price: "99.99"
images: [file1.jpg, file2.jpg]  // Optional, up to 10 images
```

## Required Fields
- `name`: Product name
- `price`: Product price (decimal number)

## Optional Fields
- `description`: Detailed product description
- `images`: Product images (up to 10 files)

### Example

* Api Key Authentication (x-client-secret):
* Api Key Authentication (x-client-key):

```python
import devdraft
from devdraft.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.devdraft.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = devdraft.Configuration(
    host = "https://api.devdraft.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x-client-secret
configuration.api_key['x-client-secret'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-client-secret'] = 'Bearer'

# Configure API key authorization: x-client-key
configuration.api_key['x-client-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-client-key'] = 'Bearer'

# Enter a context with an instance of the API client
with devdraft.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = devdraft.ProductsApi(api_client)
    name = 'name_example' # str | Product name as it will appear to customers. Should be clear and descriptive.
    description = 'description_example' # str | Detailed description of the product. Supports markdown formatting for rich text display.
    price = 3.4 # float | Product price in the specified currency. Must be greater than 0.
    currency = USD # str | Currency code for the price. Defaults to USD if not specified. (optional) (default to USD)
    type = 'type_example' # str | Product type (optional)
    weight = 3.4 # float | Weight of the product (optional)
    unit = 'unit_example' # str | Unit of measurement (optional)
    quantity = 3.4 # float | Quantity available (optional)
    stock_count = 3.4 # float | Stock count (optional)
    status = 'status_example' # str | Product status (optional)
    product_type = 'product_type_example' # str | Product type (optional)
    images = ['images_example'] # List[str] | Array of image URLs (optional)

    try:
        # Create a new product
        api_instance.product_controller_create(name, description, price, currency=currency, type=type, weight=weight, unit=unit, quantity=quantity, stock_count=stock_count, status=status, product_type=product_type, images=images)
    except Exception as e:
        print("Exception when calling ProductsApi->product_controller_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Product name as it will appear to customers. Should be clear and descriptive. | 
 **description** | **str**| Detailed description of the product. Supports markdown formatting for rich text display. | 
 **price** | **float**| Product price in the specified currency. Must be greater than 0. | 
 **currency** | **str**| Currency code for the price. Defaults to USD if not specified. | [optional] [default to USD]
 **type** | **str**| Product type | [optional] 
 **weight** | **float**| Weight of the product | [optional] 
 **unit** | **str**| Unit of measurement | [optional] 
 **quantity** | **float**| Quantity available | [optional] 
 **stock_count** | **float**| Stock count | [optional] 
 **status** | **str**| Product status | [optional] 
 **product_type** | **str**| Product type | [optional] 
 **images** | [**List[str]**](str.md)| Array of image URLs | [optional] 

### Return type

void (empty response body)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The product has been successfully created. |  -  |
**400** | Bad Request - Invalid input data or image format |  -  |
**401** | Unauthorized - Invalid API credentials |  -  |
**413** | Payload Too Large - Image files too large |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_controller_find_all**
> product_controller_find_all(skip=skip, take=take)

Get all products

Retrieves a list of products with pagination.
    
This endpoint allows you to fetch products with optional pagination.

## Use Cases
- List all products
- Browse product catalog
- Implement product search

## Query Parameters
- `skip`: Number of records to skip (default: 0)
- `take`: Number of records to take (default: 10)

## Example Response
```json
{
  "data": [
    {
      "id": "prod_123456",
      "name": "Premium Widget",
      "description": "High-quality widget for all your needs",
      "price": "99.99",
      "images": [
        "https://storage.example.com/images/file1.jpg",
        "https://storage.example.com/images/file2.jpg"
      ],
      "createdAt": "2024-03-20T10:00:00Z"
    }
  ],
  "total": 100,
  "skip": 0,
  "take": 10
}
```

### Example

* Api Key Authentication (x-client-secret):
* Api Key Authentication (x-client-key):

```python
import devdraft
from devdraft.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.devdraft.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = devdraft.Configuration(
    host = "https://api.devdraft.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x-client-secret
configuration.api_key['x-client-secret'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-client-secret'] = 'Bearer'

# Configure API key authorization: x-client-key
configuration.api_key['x-client-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-client-key'] = 'Bearer'

# Enter a context with an instance of the API client
with devdraft.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = devdraft.ProductsApi(api_client)
    skip = 3.4 # float | Number of records to skip (optional)
    take = 3.4 # float | Number of records to take (optional)

    try:
        # Get all products
        api_instance.product_controller_find_all(skip=skip, take=take)
    except Exception as e:
        print("Exception when calling ProductsApi->product_controller_find_all: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **float**| Number of records to skip | [optional] 
 **take** | **float**| Number of records to take | [optional] 

### Return type

void (empty response body)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return all products. |  -  |
**401** | Unauthorized - Invalid API credentials |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_controller_find_one**
> product_controller_find_one(id)

Get a product by ID

Retrieves detailed information about a specific product.
    
This endpoint allows you to fetch complete product details including all images.

## Use Cases
- View product details
- Display product information
- Check product availability

## Example Response
```json
{
  "id": "prod_123456",
  "name": "Premium Widget",
  "description": "High-quality widget for all your needs",
  "price": "99.99",
  "images": [
    "https://storage.example.com/images/file1.jpg",
    "https://storage.example.com/images/file2.jpg"
  ],
  "createdAt": "2024-03-20T10:00:00Z",
  "updatedAt": "2024-03-20T10:00:00Z"
}
```

### Example

* Api Key Authentication (x-client-secret):
* Api Key Authentication (x-client-key):

```python
import devdraft
from devdraft.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.devdraft.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = devdraft.Configuration(
    host = "https://api.devdraft.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x-client-secret
configuration.api_key['x-client-secret'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-client-secret'] = 'Bearer'

# Configure API key authorization: x-client-key
configuration.api_key['x-client-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-client-key'] = 'Bearer'

# Enter a context with an instance of the API client
with devdraft.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = devdraft.ProductsApi(api_client)
    id = 'id_example' # str | Product ID

    try:
        # Get a product by ID
        api_instance.product_controller_find_one(id)
    except Exception as e:
        print("Exception when calling ProductsApi->product_controller_find_one: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Product ID | 

### Return type

void (empty response body)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return the product. |  -  |
**401** | Unauthorized - Invalid API credentials |  -  |
**404** | Product not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_controller_remove**
> product_controller_remove(id)

Delete a product

Deletes a product and its associated images.
    
This endpoint allows you to remove a product and all its associated data.

## Use Cases
- Remove discontinued products
- Clean up product catalog
- Delete test products

## Notes
- This action cannot be undone
- All product images will be deleted
- Associated data will be removed

### Example

* Api Key Authentication (x-client-secret):
* Api Key Authentication (x-client-key):

```python
import devdraft
from devdraft.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.devdraft.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = devdraft.Configuration(
    host = "https://api.devdraft.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x-client-secret
configuration.api_key['x-client-secret'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-client-secret'] = 'Bearer'

# Configure API key authorization: x-client-key
configuration.api_key['x-client-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-client-key'] = 'Bearer'

# Enter a context with an instance of the API client
with devdraft.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = devdraft.ProductsApi(api_client)
    id = 'id_example' # str | Product ID

    try:
        # Delete a product
        api_instance.product_controller_remove(id)
    except Exception as e:
        print("Exception when calling ProductsApi->product_controller_remove: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Product ID | 

### Return type

void (empty response body)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The product has been successfully deleted. |  -  |
**401** | Unauthorized - Invalid API credentials |  -  |
**404** | Product not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_controller_update**
> product_controller_update(id, name=name, description=description, price=price, currency=currency, type=type, weight=weight, unit=unit, quantity=quantity, stock_count=stock_count, status=status, product_type=product_type, images=images)

Update a product

Updates an existing product's information and optionally adds new images.
    
This endpoint allows you to modify product details and manage product images.

## Use Cases
- Update product information
- Change product pricing
- Modify product images
- Update product description

## Example Request (multipart/form-data)
```
name: "Updated Premium Widget"
description: "Updated description"
price: "129.99"
images: [file1.jpg, file2.jpg]  // Optional, up to 10 images
```

## Notes
- Only include fields that need to be updated
- New images will replace existing images
- Maximum 10 images per product
- Images are automatically optimized

### Example

* Api Key Authentication (x-client-secret):
* Api Key Authentication (x-client-key):

```python
import devdraft
from devdraft.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.devdraft.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = devdraft.Configuration(
    host = "https://api.devdraft.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x-client-secret
configuration.api_key['x-client-secret'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-client-secret'] = 'Bearer'

# Configure API key authorization: x-client-key
configuration.api_key['x-client-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-client-key'] = 'Bearer'

# Enter a context with an instance of the API client
with devdraft.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = devdraft.ProductsApi(api_client)
    id = 'id_example' # str | Product ID
    name = 'name_example' # str | Product name as it will appear to customers. Should be clear and descriptive. (optional)
    description = 'description_example' # str | Detailed description of the product. Supports markdown formatting for rich text display. (optional)
    price = 3.4 # float | Product price in the specified currency. Must be greater than 0. (optional)
    currency = USD # str | Currency code for the price. Defaults to USD if not specified. (optional) (default to USD)
    type = 'type_example' # str | Product type (optional)
    weight = 3.4 # float | Weight of the product (optional)
    unit = 'unit_example' # str | Unit of measurement (optional)
    quantity = 3.4 # float | Quantity available (optional)
    stock_count = 3.4 # float | Stock count (optional)
    status = 'status_example' # str | Product status (optional)
    product_type = 'product_type_example' # str | Product type (optional)
    images = ['images_example'] # List[str] | Array of image URLs (optional)

    try:
        # Update a product
        api_instance.product_controller_update(id, name=name, description=description, price=price, currency=currency, type=type, weight=weight, unit=unit, quantity=quantity, stock_count=stock_count, status=status, product_type=product_type, images=images)
    except Exception as e:
        print("Exception when calling ProductsApi->product_controller_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Product ID | 
 **name** | **str**| Product name as it will appear to customers. Should be clear and descriptive. | [optional] 
 **description** | **str**| Detailed description of the product. Supports markdown formatting for rich text display. | [optional] 
 **price** | **float**| Product price in the specified currency. Must be greater than 0. | [optional] 
 **currency** | **str**| Currency code for the price. Defaults to USD if not specified. | [optional] [default to USD]
 **type** | **str**| Product type | [optional] 
 **weight** | **float**| Weight of the product | [optional] 
 **unit** | **str**| Unit of measurement | [optional] 
 **quantity** | **float**| Quantity available | [optional] 
 **stock_count** | **float**| Stock count | [optional] 
 **status** | **str**| Product status | [optional] 
 **product_type** | **str**| Product type | [optional] 
 **images** | [**List[str]**](str.md)| Array of image URLs | [optional] 

### Return type

void (empty response body)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The product has been successfully updated. |  -  |
**400** | Bad Request - Invalid input data or image format |  -  |
**401** | Unauthorized - Invalid API credentials |  -  |
**404** | Product not found. |  -  |
**413** | Payload Too Large - Image files too large |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_controller_upload_image**
> product_controller_upload_image(id)

Upload images for a product

Adds new images to an existing product.
    
This endpoint allows you to upload additional images for a product that already exists.

## Use Cases
- Add more product images
- Update product gallery
- Enhance product presentation

## Supported Image Formats
- JPEG/JPG
- PNG
- WebP
- Maximum 10 images per upload
- Maximum file size: 5MB per image

## Example Request (multipart/form-data)
```
images: [file1.jpg, file2.jpg]  // Up to 10 images
```

## Notes
- Images are appended to existing product images
- Total images per product cannot exceed 10
- Images are automatically optimized and resized

### Example

* Api Key Authentication (x-client-secret):
* Api Key Authentication (x-client-key):

```python
import devdraft
from devdraft.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.devdraft.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = devdraft.Configuration(
    host = "https://api.devdraft.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x-client-secret
configuration.api_key['x-client-secret'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-client-secret'] = 'Bearer'

# Configure API key authorization: x-client-key
configuration.api_key['x-client-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-client-key'] = 'Bearer'

# Enter a context with an instance of the API client
with devdraft.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = devdraft.ProductsApi(api_client)
    id = 'id_example' # str | Product ID

    try:
        # Upload images for a product
        api_instance.product_controller_upload_image(id)
    except Exception as e:
        print("Exception when calling ProductsApi->product_controller_upload_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Product ID | 

### Return type

void (empty response body)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The images have been successfully uploaded. |  -  |
**401** | Unauthorized - Invalid API credentials |  -  |
**404** | Product not found. |  -  |
**413** | Payload Too Large - Image files too large |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

