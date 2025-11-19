# devdraft.PaymentLinksApi

All URIs are relative to *https://api.devdraft.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payment_links_controller_create**](PaymentLinksApi.md#payment_links_controller_create) | **POST** /api/v0/payment-links | Create a new payment link
[**payment_links_controller_find_all**](PaymentLinksApi.md#payment_links_controller_find_all) | **GET** /api/v0/payment-links | Get all payment links
[**payment_links_controller_find_one**](PaymentLinksApi.md#payment_links_controller_find_one) | **GET** /api/v0/payment-links/{id} | Get a payment link by ID
[**payment_links_controller_update**](PaymentLinksApi.md#payment_links_controller_update) | **PUT** /api/v0/payment-links/{id} | Update a payment link


# **payment_links_controller_create**
> payment_links_controller_create(create_payment_link_dto)

Create a new payment link

Creates a new payment link with the provided details. Supports both simple one-time payments and complex product bundles.

### Example

* Api Key Authentication (x-client-secret):
* Api Key Authentication (x-client-key):

```python
import devdraft
from devdraft.models.create_payment_link_dto import CreatePaymentLinkDto
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
    api_instance = devdraft.PaymentLinksApi(api_client)
    create_payment_link_dto = devdraft.CreatePaymentLinkDto() # CreatePaymentLinkDto | Payment link creation data

    try:
        # Create a new payment link
        api_instance.payment_links_controller_create(create_payment_link_dto)
    except Exception as e:
        print("Exception when calling PaymentLinksApi->payment_links_controller_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_payment_link_dto** | [**CreatePaymentLinkDto**](CreatePaymentLinkDto.md)| Payment link creation data | 

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
**201** | The payment link has been successfully created. |  -  |
**400** | Bad Request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_links_controller_find_all**
> payment_links_controller_find_all(skip=skip, take=take)

Get all payment links

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
    api_instance = devdraft.PaymentLinksApi(api_client)
    skip = 'skip_example' # str | Number of records to skip (must be non-negative) (optional)
    take = 'take_example' # str | Number of records to take (must be positive) (optional)

    try:
        # Get all payment links
        api_instance.payment_links_controller_find_all(skip=skip, take=take)
    except Exception as e:
        print("Exception when calling PaymentLinksApi->payment_links_controller_find_all: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **str**| Number of records to skip (must be non-negative) | [optional] 
 **take** | **str**| Number of records to take (must be positive) | [optional] 

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
**200** | Return all payment links. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_links_controller_find_one**
> payment_links_controller_find_one(id)

Get a payment link by ID

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
    api_instance = devdraft.PaymentLinksApi(api_client)
    id = 'id_example' # str | Payment Link ID

    try:
        # Get a payment link by ID
        api_instance.payment_links_controller_find_one(id)
    except Exception as e:
        print("Exception when calling PaymentLinksApi->payment_links_controller_find_one: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Payment Link ID | 

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
**200** | Return the payment link. |  -  |
**404** | Payment link not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_links_controller_update**
> payment_links_controller_update(id, body)

Update a payment link

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
    api_instance = devdraft.PaymentLinksApi(api_client)
    id = 'id_example' # str | Payment Link ID
    body = None # object | 

    try:
        # Update a payment link
        api_instance.payment_links_controller_update(id, body)
    except Exception as e:
        print("Exception when calling PaymentLinksApi->payment_links_controller_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Payment Link ID | 
 **body** | **object**|  | 

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
**200** | The payment link has been successfully updated. |  -  |
**404** | Payment link not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

