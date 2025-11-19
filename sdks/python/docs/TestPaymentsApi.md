# devdraft.TestPaymentsApi

All URIs are relative to *https://api.devdraft.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**test_payment_controller_create_payment_v0**](TestPaymentsApi.md#test_payment_controller_create_payment_v0) | **POST** /api/v0/test-payment | Process a test payment
[**test_payment_controller_get_payment_v0**](TestPaymentsApi.md#test_payment_controller_get_payment_v0) | **GET** /api/v0/test-payment/{id} | Get payment details by ID
[**test_payment_controller_refund_payment_v0**](TestPaymentsApi.md#test_payment_controller_refund_payment_v0) | **POST** /api/v0/test-payment/{id}/refund | Refund a payment


# **test_payment_controller_create_payment_v0**
> PaymentResponseDto test_payment_controller_create_payment_v0(idempotency_key, payment_request_dto)

Process a test payment

Creates a new payment. Requires an idempotency key to prevent duplicate payments on retry.
    
## Idempotency Key Best Practices

1. **Generate unique keys**: Use UUIDs or similar unique identifiers, prefixed with a descriptive operation name
2. **Store keys client-side**: Save the key with the original request so you can retry with the same key
3. **Key format**: Between 6-64 alphanumeric characters
4. **Expiration**: Keys expire after 24 hours by default
5. **Use case**: Perfect for ensuring payment operations are never processed twice, even during network failures

## Example Request (curl)

```bash
curl -X POST \
  https://api.example.com/rest-api/v0/test-payment \
  -H 'Content-Type: application/json' \
  -H 'Client-Key: your-api-key' \
  -H 'Client-Secret: your-api-secret' \
  -H 'Idempotency-Key: payment_123456_unique_key' \
  -d '{
    "amount": 100.00,
    "currency": "USD",
    "description": "Test payment for order #12345",
    "customerId": "cus_12345"
  }'
```

## Example Response (First Request)

```json
{
  "id": "pay_abc123xyz456",
  "amount": 100.00,
  "currency": "USD",
  "status": "succeeded",
  "timestamp": "2023-07-01T12:00:00.000Z"
}
```

## Example Response (Duplicate Request)

The exact same response will be returned for any duplicate request with the same idempotency key, without creating a new payment.

## Retry Scenario Example

Network failure during payment submission:
1. Client creates payment request with idempotency key: "payment_123456_unique_key"
2. Request begins processing, but network connection fails before response received
3. Client retries the exact same request with the same idempotency key
4. Server detects duplicate idempotency key and returns the result of the first request
5. No duplicate payment is created

If you retry with same key but different parameters (e.g., different amount), you'll receive a 409 Conflict error.

### Example

* Api Key Authentication (x-client-secret):
* Api Key Authentication (x-client-key):

```python
import devdraft
from devdraft.models.payment_request_dto import PaymentRequestDto
from devdraft.models.payment_response_dto import PaymentResponseDto
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
    api_instance = devdraft.TestPaymentsApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | Unique key to ensure the request is idempotent. If a request with the same key is sent multiple times, only the first will be processed, and subsequent requests will return the same response.
    payment_request_dto = devdraft.PaymentRequestDto() # PaymentRequestDto | 

    try:
        # Process a test payment
        api_response = api_instance.test_payment_controller_create_payment_v0(idempotency_key, payment_request_dto)
        print("The response of TestPaymentsApi->test_payment_controller_create_payment_v0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestPaymentsApi->test_payment_controller_create_payment_v0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique key to ensure the request is idempotent. If a request with the same key is sent multiple times, only the first will be processed, and subsequent requests will return the same response. | 
 **payment_request_dto** | [**PaymentRequestDto**](PaymentRequestDto.md)|  | 

### Return type

[**PaymentResponseDto**](PaymentResponseDto.md)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Payment processed successfully |  -  |
**400** | Bad Request. The idempotency key is missing or invalid.    Sample response: &#x60;&#x60;&#x60;json {   \&quot;statusCode\&quot;: 400,   \&quot;message\&quot;: \&quot;The idempotency-key header is required for POST requests\&quot; } &#x60;&#x60;&#x60; |  -  |
**401** | Unauthorized. Client key or secret is invalid or missing. |  -  |
**409** | Idempotency Conflict. The provided idempotency key was already used with different parameters.    Sample response: &#x60;&#x60;&#x60;json {   \&quot;statusCode\&quot;: 409,   \&quot;message\&quot;: \&quot;Conflict: Idempotency key already used with different request data\&quot; } &#x60;&#x60;&#x60; |  -  |
**429** | Too many requests, rate limit exceeded. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_payment_controller_get_payment_v0**
> PaymentResponseDto test_payment_controller_get_payment_v0(id)

Get payment details by ID

### Example

* Api Key Authentication (x-client-secret):
* Api Key Authentication (x-client-key):

```python
import devdraft
from devdraft.models.payment_response_dto import PaymentResponseDto
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
    api_instance = devdraft.TestPaymentsApi(api_client)
    id = 'id_example' # str | Payment ID

    try:
        # Get payment details by ID
        api_response = api_instance.test_payment_controller_get_payment_v0(id)
        print("The response of TestPaymentsApi->test_payment_controller_get_payment_v0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestPaymentsApi->test_payment_controller_get_payment_v0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Payment ID | 

### Return type

[**PaymentResponseDto**](PaymentResponseDto.md)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Payment details retrieved successfully |  -  |
**400** | Bad Request. The idempotency key is missing or invalid.    Sample response: &#x60;&#x60;&#x60;json {   \&quot;statusCode\&quot;: 400,   \&quot;message\&quot;: \&quot;The idempotency-key header is required for POST requests\&quot; } &#x60;&#x60;&#x60; |  -  |
**401** | Unauthorized. Client key or secret is invalid or missing. |  -  |
**409** | Idempotency Conflict. The provided idempotency key was already used with different parameters.    Sample response: &#x60;&#x60;&#x60;json {   \&quot;statusCode\&quot;: 409,   \&quot;message\&quot;: \&quot;Conflict: Idempotency key already used with different request data\&quot; } &#x60;&#x60;&#x60; |  -  |
**429** | Too many requests, rate limit exceeded. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_payment_controller_refund_payment_v0**
> RefundResponseDto test_payment_controller_refund_payment_v0(id, idempotency_key)

Refund a payment

Refunds an existing payment. Requires an idempotency key to prevent duplicate refunds on retry.
    
## Idempotency Key Benefits for Refunds

Refunds are critical financial operations where duplicates can cause serious issues. Using idempotency keys ensures:

1. **Prevent duplicate refunds**: Even if a request times out or fails, retrying with the same key won't issue multiple refunds
2. **Safe retries**: Network failures or timeouts won't risk creating multiple refunds
3. **Consistent response**: Always get the same response for the same operation

## Example Request (curl)

```bash
curl -X POST \
  https://api.example.com/rest-api/v0/test-payment/pay_abc123xyz456/refund \
  -H 'Content-Type: application/json' \
  -H 'Client-Key: your-api-key' \
  -H 'Client-Secret: your-api-secret' \
  -H 'Idempotency-Key: refund_123456_unique_key'
```

## Example Response (First Request)

```json
{
  "id": "ref_xyz789",
  "paymentId": "pay_abc123xyz456",
  "amount": 100.00,
  "status": "succeeded",
  "timestamp": "2023-07-01T14:30:00.000Z"
}
```

## Example Response (Duplicate Request)

The exact same response will be returned for any duplicate request with the same idempotency key, without creating a new refund.

## Idempotency Key Guidelines

- Use a unique key for each distinct refund operation
- Store keys client-side to ensure you can retry with the same key if needed
- Keys expire after 24 hours by default

### Example

* Api Key Authentication (x-client-secret):
* Api Key Authentication (x-client-key):

```python
import devdraft
from devdraft.models.refund_response_dto import RefundResponseDto
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
    api_instance = devdraft.TestPaymentsApi(api_client)
    id = 'id_example' # str | Payment ID to refund
    idempotency_key = 'idempotency_key_example' # str | Unique key to ensure the refund request is idempotent. If a request with the same key is sent multiple times, only the first will be processed, and subsequent requests will return the same response.

    try:
        # Refund a payment
        api_response = api_instance.test_payment_controller_refund_payment_v0(id, idempotency_key)
        print("The response of TestPaymentsApi->test_payment_controller_refund_payment_v0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestPaymentsApi->test_payment_controller_refund_payment_v0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Payment ID to refund | 
 **idempotency_key** | **str**| Unique key to ensure the refund request is idempotent. If a request with the same key is sent multiple times, only the first will be processed, and subsequent requests will return the same response. | 

### Return type

[**RefundResponseDto**](RefundResponseDto.md)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Payment refunded successfully |  -  |
**400** | Bad Request. The idempotency key is missing or invalid.    Sample response: &#x60;&#x60;&#x60;json {   \&quot;statusCode\&quot;: 400,   \&quot;message\&quot;: \&quot;The idempotency-key header is required for POST requests\&quot; } &#x60;&#x60;&#x60; |  -  |
**401** | Unauthorized. Client key or secret is invalid or missing. |  -  |
**409** | Idempotency Conflict. The provided idempotency key was already used with different parameters.    Sample response: &#x60;&#x60;&#x60;json {   \&quot;statusCode\&quot;: 409,   \&quot;message\&quot;: \&quot;Conflict: Idempotency key already used with different request data\&quot; } &#x60;&#x60;&#x60; |  -  |
**429** | Too many requests, rate limit exceeded. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

