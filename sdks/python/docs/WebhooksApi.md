# devdraft.WebhooksApi

All URIs are relative to *https://api.devdraft.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**webhook_controller_create**](WebhooksApi.md#webhook_controller_create) | **POST** /api/v0/webhooks | Create a new webhook
[**webhook_controller_find_all**](WebhooksApi.md#webhook_controller_find_all) | **GET** /api/v0/webhooks | Get all webhooks
[**webhook_controller_find_one**](WebhooksApi.md#webhook_controller_find_one) | **GET** /api/v0/webhooks/{id} | Get a webhook by id
[**webhook_controller_remove**](WebhooksApi.md#webhook_controller_remove) | **DELETE** /api/v0/webhooks/{id} | Delete a webhook
[**webhook_controller_update**](WebhooksApi.md#webhook_controller_update) | **PATCH** /api/v0/webhooks/{id} | Update a webhook


# **webhook_controller_create**
> WebhookResponseDto webhook_controller_create(create_webhook_dto)

Create a new webhook

Creates a new webhook endpoint for receiving event notifications. Requires webhook:create scope.

### Example

* Api Key Authentication (x-client-secret):
* Api Key Authentication (x-client-key):

```python
import devdraft
from devdraft.models.create_webhook_dto import CreateWebhookDto
from devdraft.models.webhook_response_dto import WebhookResponseDto
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
    api_instance = devdraft.WebhooksApi(api_client)
    create_webhook_dto = devdraft.CreateWebhookDto() # CreateWebhookDto | Webhook configuration details

    try:
        # Create a new webhook
        api_response = api_instance.webhook_controller_create(create_webhook_dto)
        print("The response of WebhooksApi->webhook_controller_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->webhook_controller_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_webhook_dto** | [**CreateWebhookDto**](CreateWebhookDto.md)| Webhook configuration details | 

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
**201** | The webhook has been successfully created. |  -  |
**400** | Invalid input data. |  -  |
**401** | Unauthorized - Missing or invalid API key. |  -  |
**403** | Forbidden - Missing required scope or API key not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhook_controller_find_all**
> List[WebhookResponseDto] webhook_controller_find_all(skip=skip, take=take)

Get all webhooks

Retrieves a list of all webhooks for your application. Requires webhook:read scope.

### Example

* Api Key Authentication (x-client-secret):
* Api Key Authentication (x-client-key):

```python
import devdraft
from devdraft.models.webhook_response_dto import WebhookResponseDto
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
    api_instance = devdraft.WebhooksApi(api_client)
    skip = 3.4 # float | Number of records to skip (default: 0) (optional)
    take = 3.4 # float | Number of records to return (default: 10) (optional)

    try:
        # Get all webhooks
        api_response = api_instance.webhook_controller_find_all(skip=skip, take=take)
        print("The response of WebhooksApi->webhook_controller_find_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->webhook_controller_find_all: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **float**| Number of records to skip (default: 0) | [optional] 
 **take** | **float**| Number of records to return (default: 10) | [optional] 

### Return type

[**List[WebhookResponseDto]**](WebhookResponseDto.md)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return all webhooks. |  -  |
**401** | Unauthorized - Missing or invalid API key. |  -  |
**403** | Forbidden - Missing required scope or API key not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhook_controller_find_one**
> WebhookResponseDto webhook_controller_find_one(id)

Get a webhook by id

Retrieves details for a specific webhook. Requires webhook:read scope.

### Example

* Api Key Authentication (x-client-secret):
* Api Key Authentication (x-client-key):

```python
import devdraft
from devdraft.models.webhook_response_dto import WebhookResponseDto
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
    api_instance = devdraft.WebhooksApi(api_client)
    id = 'id_example' # str | Webhook unique identifier (UUID)

    try:
        # Get a webhook by id
        api_response = api_instance.webhook_controller_find_one(id)
        print("The response of WebhooksApi->webhook_controller_find_one:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->webhook_controller_find_one: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Webhook unique identifier (UUID) | 

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
**200** | Return the webhook. |  -  |
**401** | Unauthorized - Missing or invalid API key. |  -  |
**403** | Forbidden - Missing required scope or API key not found. |  -  |
**404** | Webhook not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhook_controller_remove**
> WebhookResponseDto webhook_controller_remove(id)

Delete a webhook

Deletes a webhook configuration. Requires webhook:delete scope.

### Example

* Api Key Authentication (x-client-secret):
* Api Key Authentication (x-client-key):

```python
import devdraft
from devdraft.models.webhook_response_dto import WebhookResponseDto
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
    api_instance = devdraft.WebhooksApi(api_client)
    id = 'id_example' # str | Webhook unique identifier (UUID)

    try:
        # Delete a webhook
        api_response = api_instance.webhook_controller_remove(id)
        print("The response of WebhooksApi->webhook_controller_remove:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->webhook_controller_remove: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Webhook unique identifier (UUID) | 

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
**200** | The webhook has been successfully deleted. |  -  |
**401** | Unauthorized - Missing or invalid API key. |  -  |
**403** | Forbidden - Missing required scope or API key not found. |  -  |
**404** | Webhook not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhook_controller_update**
> WebhookResponseDto webhook_controller_update(id, update_webhook_dto)

Update a webhook

Updates an existing webhook configuration. Requires webhook:update scope.

### Example

* Api Key Authentication (x-client-secret):
* Api Key Authentication (x-client-key):

```python
import devdraft
from devdraft.models.update_webhook_dto import UpdateWebhookDto
from devdraft.models.webhook_response_dto import WebhookResponseDto
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
    api_instance = devdraft.WebhooksApi(api_client)
    id = 'id_example' # str | Webhook unique identifier (UUID)
    update_webhook_dto = devdraft.UpdateWebhookDto() # UpdateWebhookDto | Webhook update details

    try:
        # Update a webhook
        api_response = api_instance.webhook_controller_update(id, update_webhook_dto)
        print("The response of WebhooksApi->webhook_controller_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->webhook_controller_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Webhook unique identifier (UUID) | 
 **update_webhook_dto** | [**UpdateWebhookDto**](UpdateWebhookDto.md)| Webhook update details | 

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
**200** | The webhook has been successfully updated. |  -  |
**400** | Invalid input data. |  -  |
**401** | Unauthorized - Missing or invalid API key. |  -  |
**403** | Forbidden - Missing required scope or API key not found. |  -  |
**404** | Webhook not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

