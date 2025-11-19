# devdraft.TaxesApi

All URIs are relative to *https://api.devdraft.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tax_controller_create**](TaxesApi.md#tax_controller_create) | **POST** /api/v0/taxes | Create a new tax
[**tax_controller_delete_without_id**](TaxesApi.md#tax_controller_delete_without_id) | **DELETE** /api/v0/taxes | Tax ID required for deletion
[**tax_controller_find_all**](TaxesApi.md#tax_controller_find_all) | **GET** /api/v0/taxes | Get all taxes with filters
[**tax_controller_find_one**](TaxesApi.md#tax_controller_find_one) | **GET** /api/v0/taxes/{id} | Get a tax by ID
[**tax_controller_remove**](TaxesApi.md#tax_controller_remove) | **DELETE** /api/v0/taxes/{id} | Delete a tax
[**tax_controller_update**](TaxesApi.md#tax_controller_update) | **PUT** /api/v0/taxes/{id} | Update a tax
[**tax_controller_update_without_id**](TaxesApi.md#tax_controller_update_without_id) | **PUT** /api/v0/taxes | Tax ID required for updates


# **tax_controller_create**
> TaxControllerCreate201Response tax_controller_create(create_tax_dto)

Create a new tax

Creates a new tax rate that can be applied to products, invoices, and payment links.

## Use Cases
- Set up sales tax for different regions
- Create VAT rates for international customers
- Configure state and local tax rates
- Manage tax compliance requirements

## Example: Create Basic Sales Tax
```json
{
  "name": "Sales Tax",
  "description": "Standard sales tax for retail transactions",
  "percentage": 8.5,
  "active": true
}
```

## Required Fields
- `name`: Tax name for identification (1-100 characters)
- `percentage`: Tax rate percentage (0-100)

## Optional Fields
- `description`: Explanation of what this tax covers (max 255 characters)
- `active`: Whether this tax is currently active (default: true)
- `appIds`: Array of app IDs where this tax should be available

### Example

* Api Key Authentication (x-client-secret):
* Api Key Authentication (x-client-key):

```python
import devdraft
from devdraft.models.create_tax_dto import CreateTaxDto
from devdraft.models.tax_controller_create201_response import TaxControllerCreate201Response
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
    api_instance = devdraft.TaxesApi(api_client)
    create_tax_dto = devdraft.CreateTaxDto() # CreateTaxDto | Tax creation data

    try:
        # Create a new tax
        api_response = api_instance.tax_controller_create(create_tax_dto)
        print("The response of TaxesApi->tax_controller_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxesApi->tax_controller_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_tax_dto** | [**CreateTaxDto**](CreateTaxDto.md)| Tax creation data | 

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
**201** | Tax created successfully |  -  |
**400** | Bad Request - Invalid input data |  -  |
**401** | Unauthorized - Invalid API credentials |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tax_controller_delete_without_id**
> tax_controller_delete_without_id()

Tax ID required for deletion

This endpoint requires a tax ID in the URL path. Use DELETE /api/v0/taxes/{id} instead.

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
    api_instance = devdraft.TaxesApi(api_client)

    try:
        # Tax ID required for deletion
        api_instance.tax_controller_delete_without_id()
    except Exception as e:
        print("Exception when calling TaxesApi->tax_controller_delete_without_id: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request - Tax ID is required in the URL path |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tax_controller_find_all**
> tax_controller_find_all(skip=skip, take=take, name=name, active=active)

Get all taxes with filters

Retrieves a list of taxes with optional filtering and pagination.

## Use Cases
- List all available tax rates
- Search taxes by name
- Filter active/inactive taxes
- Export tax configuration

## Query Parameters
- `skip`: Number of records to skip (default: 0, min: 0)
- `take`: Number of records to return (default: 10, min: 1, max: 100)
- `name`: Filter taxes by name (partial match, case-insensitive)
- `active`: Filter by active status (true/false)

## Example Request
`GET /api/v0/taxes?skip=0&take=20&active=true&name=Sales`

## Example Response
```json
[
  {
    "id": "tax_123456",
    "name": "Sales Tax",
    "description": "Standard sales tax for retail transactions",
    "percentage": 8.5,
    "active": true,
    "created_at": "2024-03-20T10:00:00Z",
    "updated_at": "2024-03-20T10:00:00Z"
  }
]
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
    api_instance = devdraft.TaxesApi(api_client)
    skip = 0 # float | Number of records to skip for pagination (optional) (default to 0)
    take = 10 # float | Number of records to return (max 100) (optional) (default to 10)
    name = 'Sales' # str | Filter taxes by name (partial match, case-insensitive) (optional)
    active = true # bool | Filter by active status (optional)

    try:
        # Get all taxes with filters
        api_instance.tax_controller_find_all(skip=skip, take=take, name=name, active=active)
    except Exception as e:
        print("Exception when calling TaxesApi->tax_controller_find_all: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **float**| Number of records to skip for pagination | [optional] [default to 0]
 **take** | **float**| Number of records to return (max 100) | [optional] [default to 10]
 **name** | **str**| Filter taxes by name (partial match, case-insensitive) | [optional] 
 **active** | **bool**| Filter by active status | [optional] 

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
**200** | Successfully retrieved taxes |  -  |
**400** | Bad Request - Invalid query parameters |  -  |
**401** | Unauthorized - Invalid API credentials |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tax_controller_find_one**
> tax_controller_find_one(id)

Get a tax by ID

Retrieves detailed information about a specific tax.

## Use Cases
- View tax details
- Verify tax configuration
- Check tax status before applying to products

## Path Parameters
- `id`: Tax UUID (required) - Must be a valid UUID format

## Example Request
`GET /api/v0/taxes/123e4567-e89b-12d3-a456-426614174000`

## Example Response
```json
{
  "id": "tax_123456",
  "name": "Sales Tax",
  "description": "Standard sales tax for retail transactions",
  "percentage": 8.5,
  "active": true,
  "created_at": "2024-03-20T10:00:00Z",
  "updated_at": "2024-03-20T10:00:00Z"
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
    api_instance = devdraft.TaxesApi(api_client)
    id = 'id_example' # str | Tax unique identifier (UUID)

    try:
        # Get a tax by ID
        api_instance.tax_controller_find_one(id)
    except Exception as e:
        print("Exception when calling TaxesApi->tax_controller_find_one: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tax unique identifier (UUID) | 

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
**200** | Successfully retrieved tax |  -  |
**400** | Bad Request - Invalid tax ID format |  -  |
**401** | Unauthorized - Invalid API credentials |  -  |
**404** | Not Found - Tax not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tax_controller_remove**
> tax_controller_remove(id)

Delete a tax

Deletes an existing tax.

## Use Cases
- Remove obsolete tax rates
- Clean up unused taxes
- Comply with regulatory changes

## Path Parameters
- `id`: Tax UUID (required) - Must be a valid UUID format

## Example Request
`DELETE /api/v0/taxes/123e4567-e89b-12d3-a456-426614174000`

## Warning
This action cannot be undone. Consider deactivating the tax instead of deleting it if it has been used in transactions.

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
    api_instance = devdraft.TaxesApi(api_client)
    id = 'id_example' # str | Tax unique identifier (UUID)

    try:
        # Delete a tax
        api_instance.tax_controller_remove(id)
    except Exception as e:
        print("Exception when calling TaxesApi->tax_controller_remove: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tax unique identifier (UUID) | 

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
**200** | Successfully deleted tax |  -  |
**400** | Bad Request - Invalid tax ID format |  -  |
**401** | Unauthorized - Invalid API credentials |  -  |
**404** | Not Found - Tax not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tax_controller_update**
> tax_controller_update(id, update_tax_dto)

Update a tax

Updates an existing tax's information.

## Use Cases
- Modify tax percentage rates
- Update tax descriptions
- Activate/deactivate taxes
- Change tax names

## Path Parameters
- `id`: Tax UUID (required) - Must be a valid UUID format

## Example Request
`PUT /api/v0/taxes/123e4567-e89b-12d3-a456-426614174000`

## Example Request Body
```json
{
  "name": "Updated Sales Tax",
  "description": "Updated sales tax rate",
  "percentage": 9.0,
  "active": true
}
```

## Notes
- Only include fields that need to be updated
- All fields are optional in updates
- Percentage changes affect future calculations only

### Example

* Api Key Authentication (x-client-secret):
* Api Key Authentication (x-client-key):

```python
import devdraft
from devdraft.models.update_tax_dto import UpdateTaxDto
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
    api_instance = devdraft.TaxesApi(api_client)
    id = 'id_example' # str | Tax unique identifier (UUID)
    update_tax_dto = devdraft.UpdateTaxDto() # UpdateTaxDto | Tax update data - only include fields you want to update

    try:
        # Update a tax
        api_instance.tax_controller_update(id, update_tax_dto)
    except Exception as e:
        print("Exception when calling TaxesApi->tax_controller_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tax unique identifier (UUID) | 
 **update_tax_dto** | [**UpdateTaxDto**](UpdateTaxDto.md)| Tax update data - only include fields you want to update | 

### Return type

void (empty response body)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated tax |  -  |
**400** | Bad Request - Invalid input data or tax ID format |  -  |
**401** | Unauthorized - Invalid API credentials |  -  |
**404** | Not Found - Tax not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tax_controller_update_without_id**
> tax_controller_update_without_id()

Tax ID required for updates

This endpoint requires a tax ID in the URL path. Use PUT /api/v0/taxes/{id} instead.

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
    api_instance = devdraft.TaxesApi(api_client)

    try:
        # Tax ID required for updates
        api_instance.tax_controller_update_without_id()
    except Exception as e:
        print("Exception when calling TaxesApi->tax_controller_update_without_id: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request - Tax ID is required in the URL path |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

