# \TransfersAPI

All URIs are relative to *https://api.devdraft.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**TransferControllerCreateDirectBankTransfer**](TransfersAPI.md#TransferControllerCreateDirectBankTransfer) | **Post** /api/v0/transfers/direct-bank | Create a direct bank transfer
[**TransferControllerCreateDirectWalletTransfer**](TransfersAPI.md#TransferControllerCreateDirectWalletTransfer) | **Post** /api/v0/transfers/direct-wallet | Create a direct wallet transfer
[**TransferControllerCreateExternalBankTransfer**](TransfersAPI.md#TransferControllerCreateExternalBankTransfer) | **Post** /api/v0/transfers/external-bank-transfer | Create an external bank transfer
[**TransferControllerCreateExternalStablecoinTransfer**](TransfersAPI.md#TransferControllerCreateExternalStablecoinTransfer) | **Post** /api/v0/transfers/external-stablecoin-transfer | Create an external stablecoin transfer
[**TransferControllerCreateStablecoinConversion**](TransfersAPI.md#TransferControllerCreateStablecoinConversion) | **Post** /api/v0/transfers/stablecoin-conversion | Create a stablecoin conversion



## TransferControllerCreateDirectBankTransfer

> TransferControllerCreateDirectBankTransfer(ctx).CreateDirectBankTransferDto(createDirectBankTransferDto).Execute()

Create a direct bank transfer

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
	createDirectBankTransferDto := *openapiclient.NewCreateDirectBankTransferDto("WalletId_example", "PaymentRail_example", "DestinationCurrency_example", "SourceCurrency_example", float32(123)) // CreateDirectBankTransferDto | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.TransfersAPI.TransferControllerCreateDirectBankTransfer(context.Background()).CreateDirectBankTransferDto(createDirectBankTransferDto).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TransfersAPI.TransferControllerCreateDirectBankTransfer``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiTransferControllerCreateDirectBankTransferRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createDirectBankTransferDto** | [**CreateDirectBankTransferDto**](CreateDirectBankTransferDto.md) |  | 

### Return type

 (empty response body)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## TransferControllerCreateDirectWalletTransfer

> TransferControllerCreateDirectWalletTransfer(ctx).CreateDirectWalletTransferDto(createDirectWalletTransferDto).Execute()

Create a direct wallet transfer

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
	createDirectWalletTransferDto := *openapiclient.NewCreateDirectWalletTransferDto("WalletId_example", "Network_example", "StableCoinCurrency_example", float32(123)) // CreateDirectWalletTransferDto | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.TransfersAPI.TransferControllerCreateDirectWalletTransfer(context.Background()).CreateDirectWalletTransferDto(createDirectWalletTransferDto).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TransfersAPI.TransferControllerCreateDirectWalletTransfer``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiTransferControllerCreateDirectWalletTransferRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createDirectWalletTransferDto** | [**CreateDirectWalletTransferDto**](CreateDirectWalletTransferDto.md) |  | 

### Return type

 (empty response body)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## TransferControllerCreateExternalBankTransfer

> TransferControllerCreateExternalBankTransfer(ctx).CreateExternalBankTransferDto(createExternalBankTransferDto).Execute()

Create an external bank transfer

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
	createExternalBankTransferDto := *openapiclient.NewCreateExternalBankTransferDto("SourceWalletId_example", "SourceCurrency_example", "DestinationCurrency_example", openapiclient.BridgeFiatPaymentRail("ach"), "ExternalAccountId_example") // CreateExternalBankTransferDto | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.TransfersAPI.TransferControllerCreateExternalBankTransfer(context.Background()).CreateExternalBankTransferDto(createExternalBankTransferDto).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TransfersAPI.TransferControllerCreateExternalBankTransfer``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiTransferControllerCreateExternalBankTransferRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createExternalBankTransferDto** | [**CreateExternalBankTransferDto**](CreateExternalBankTransferDto.md) |  | 

### Return type

 (empty response body)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## TransferControllerCreateExternalStablecoinTransfer

> TransferControllerCreateExternalStablecoinTransfer(ctx).CreateExternalStablecoinTransferDto(createExternalStablecoinTransferDto).Execute()

Create an external stablecoin transfer

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
	createExternalStablecoinTransferDto := *openapiclient.NewCreateExternalStablecoinTransferDto("SourceWalletId_example", "SourceCurrency_example", "DestinationCurrency_example", "beneficiary_12345") // CreateExternalStablecoinTransferDto | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.TransfersAPI.TransferControllerCreateExternalStablecoinTransfer(context.Background()).CreateExternalStablecoinTransferDto(createExternalStablecoinTransferDto).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TransfersAPI.TransferControllerCreateExternalStablecoinTransfer``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiTransferControllerCreateExternalStablecoinTransferRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createExternalStablecoinTransferDto** | [**CreateExternalStablecoinTransferDto**](CreateExternalStablecoinTransferDto.md) |  | 

### Return type

 (empty response body)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## TransferControllerCreateStablecoinConversion

> TransferControllerCreateStablecoinConversion(ctx).CreateStablecoinConversionDto(createStablecoinConversionDto).Execute()

Create a stablecoin conversion

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
	createStablecoinConversionDto := *openapiclient.NewCreateStablecoinConversionDto("WalletId_example", "SourceNetwork_example", "SourceCurrency_example", "DestinationCurrency_example", float32(123)) // CreateStablecoinConversionDto | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.TransfersAPI.TransferControllerCreateStablecoinConversion(context.Background()).CreateStablecoinConversionDto(createStablecoinConversionDto).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TransfersAPI.TransferControllerCreateStablecoinConversion``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiTransferControllerCreateStablecoinConversionRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createStablecoinConversionDto** | [**CreateStablecoinConversionDto**](CreateStablecoinConversionDto.md) |  | 

### Return type

 (empty response body)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

