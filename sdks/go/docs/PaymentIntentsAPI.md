# \PaymentIntentsAPI

All URIs are relative to *https://api.devdraft.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**PaymentIntentControllerCreateBankPaymentIntent**](PaymentIntentsAPI.md#PaymentIntentControllerCreateBankPaymentIntent) | **Post** /api/v0/payment-intents/bank | Create a bank payment intent
[**PaymentIntentControllerCreateStablePaymentIntent**](PaymentIntentsAPI.md#PaymentIntentControllerCreateStablePaymentIntent) | **Post** /api/v0/payment-intents/stablecoin | Create a stable payment intent



## PaymentIntentControllerCreateBankPaymentIntent

> PaymentIntentControllerCreateBankPaymentIntent(ctx).IdempotencyKey(idempotencyKey).CreateBankPaymentIntentDto(createBankPaymentIntentDto).Execute()

Create a bank payment intent



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
	idempotencyKey := "idempotencyKey_example" // string | Unique UUID v4 for idempotent requests. Prevents duplicate payments.
	createBankPaymentIntentDto := *openapiclient.NewCreateBankPaymentIntentDto(openapiclient.BridgePaymentRail("ethereum"), openapiclient.FiatCurrency("usd"), openapiclient.StableCoinCurrency("usdc"), openapiclient.BridgePaymentRail("ethereum")) // CreateBankPaymentIntentDto | Bank payment intent creation data

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.PaymentIntentsAPI.PaymentIntentControllerCreateBankPaymentIntent(context.Background()).IdempotencyKey(idempotencyKey).CreateBankPaymentIntentDto(createBankPaymentIntentDto).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `PaymentIntentsAPI.PaymentIntentControllerCreateBankPaymentIntent``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiPaymentIntentControllerCreateBankPaymentIntentRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotencyKey** | **string** | Unique UUID v4 for idempotent requests. Prevents duplicate payments. | 
 **createBankPaymentIntentDto** | [**CreateBankPaymentIntentDto**](CreateBankPaymentIntentDto.md) | Bank payment intent creation data | 

### Return type

 (empty response body)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## PaymentIntentControllerCreateStablePaymentIntent

> PaymentIntentControllerCreateStablePaymentIntent(ctx).IdempotencyKey(idempotencyKey).CreateStablePaymentIntentDto(createStablePaymentIntentDto).Execute()

Create a stable payment intent



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
	idempotencyKey := "idempotencyKey_example" // string | Unique UUID v4 for idempotent requests. Prevents duplicate payments.
	createStablePaymentIntentDto := *openapiclient.NewCreateStablePaymentIntentDto(openapiclient.StableCoinCurrency("usdc"), openapiclient.BridgePaymentRail("ethereum"), openapiclient.BridgePaymentRail("ethereum")) // CreateStablePaymentIntentDto | Stable payment intent creation data

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.PaymentIntentsAPI.PaymentIntentControllerCreateStablePaymentIntent(context.Background()).IdempotencyKey(idempotencyKey).CreateStablePaymentIntentDto(createStablePaymentIntentDto).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `PaymentIntentsAPI.PaymentIntentControllerCreateStablePaymentIntent``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiPaymentIntentControllerCreateStablePaymentIntentRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotencyKey** | **string** | Unique UUID v4 for idempotent requests. Prevents duplicate payments. | 
 **createStablePaymentIntentDto** | [**CreateStablePaymentIntentDto**](CreateStablePaymentIntentDto.md) | Stable payment intent creation data | 

### Return type

 (empty response body)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

