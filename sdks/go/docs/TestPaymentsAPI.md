# \TestPaymentsAPI

All URIs are relative to *https://api.devdraft.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**TestPaymentControllerCreatePaymentV0**](TestPaymentsAPI.md#TestPaymentControllerCreatePaymentV0) | **Post** /api/v0/test-payment | Process a test payment
[**TestPaymentControllerGetPaymentV0**](TestPaymentsAPI.md#TestPaymentControllerGetPaymentV0) | **Get** /api/v0/test-payment/{id} | Get payment details by ID
[**TestPaymentControllerRefundPaymentV0**](TestPaymentsAPI.md#TestPaymentControllerRefundPaymentV0) | **Post** /api/v0/test-payment/{id}/refund | Refund a payment



## TestPaymentControllerCreatePaymentV0

> PaymentResponseDto TestPaymentControllerCreatePaymentV0(ctx).IdempotencyKey(idempotencyKey).PaymentRequestDto(paymentRequestDto).Execute()

Process a test payment



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	idempotencyKey := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Unique key to ensure the request is idempotent. If a request with the same key is sent multiple times, only the first will be processed, and subsequent requests will return the same response.
	paymentRequestDto := *openapiclient.NewPaymentRequestDto(float32(100.5), "USD", "Test payment for API") // PaymentRequestDto | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TestPaymentsAPI.TestPaymentControllerCreatePaymentV0(context.Background()).IdempotencyKey(idempotencyKey).PaymentRequestDto(paymentRequestDto).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TestPaymentsAPI.TestPaymentControllerCreatePaymentV0``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `TestPaymentControllerCreatePaymentV0`: PaymentResponseDto
	fmt.Fprintf(os.Stdout, "Response from `TestPaymentsAPI.TestPaymentControllerCreatePaymentV0`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiTestPaymentControllerCreatePaymentV0Request struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotencyKey** | **string** | Unique key to ensure the request is idempotent. If a request with the same key is sent multiple times, only the first will be processed, and subsequent requests will return the same response. | 
 **paymentRequestDto** | [**PaymentRequestDto**](PaymentRequestDto.md) |  | 

### Return type

[**PaymentResponseDto**](PaymentResponseDto.md)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## TestPaymentControllerGetPaymentV0

> PaymentResponseDto TestPaymentControllerGetPaymentV0(ctx, id).Execute()

Get payment details by ID

### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	id := "id_example" // string | Payment ID

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TestPaymentsAPI.TestPaymentControllerGetPaymentV0(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TestPaymentsAPI.TestPaymentControllerGetPaymentV0``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `TestPaymentControllerGetPaymentV0`: PaymentResponseDto
	fmt.Fprintf(os.Stdout, "Response from `TestPaymentsAPI.TestPaymentControllerGetPaymentV0`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** | Payment ID | 

### Other Parameters

Other parameters are passed through a pointer to a apiTestPaymentControllerGetPaymentV0Request struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**PaymentResponseDto**](PaymentResponseDto.md)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## TestPaymentControllerRefundPaymentV0

> RefundResponseDto TestPaymentControllerRefundPaymentV0(ctx, id).IdempotencyKey(idempotencyKey).Execute()

Refund a payment



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	id := "id_example" // string | Payment ID to refund
	idempotencyKey := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Unique key to ensure the refund request is idempotent. If a request with the same key is sent multiple times, only the first will be processed, and subsequent requests will return the same response.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TestPaymentsAPI.TestPaymentControllerRefundPaymentV0(context.Background(), id).IdempotencyKey(idempotencyKey).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TestPaymentsAPI.TestPaymentControllerRefundPaymentV0``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `TestPaymentControllerRefundPaymentV0`: RefundResponseDto
	fmt.Fprintf(os.Stdout, "Response from `TestPaymentsAPI.TestPaymentControllerRefundPaymentV0`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** | Payment ID to refund | 

### Other Parameters

Other parameters are passed through a pointer to a apiTestPaymentControllerRefundPaymentV0Request struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **idempotencyKey** | **string** | Unique key to ensure the refund request is idempotent. If a request with the same key is sent multiple times, only the first will be processed, and subsequent requests will return the same response. | 

### Return type

[**RefundResponseDto**](RefundResponseDto.md)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

