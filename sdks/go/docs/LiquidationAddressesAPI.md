# \LiquidationAddressesAPI

All URIs are relative to *https://api.devdraft.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**LiquidationAddressControllerCreateLiquidationAddress**](LiquidationAddressesAPI.md#LiquidationAddressControllerCreateLiquidationAddress) | **Post** /api/v0/customers/{customerId}/liquidation_addresses | Create a new liquidation address for a customer
[**LiquidationAddressControllerGetLiquidationAddress**](LiquidationAddressesAPI.md#LiquidationAddressControllerGetLiquidationAddress) | **Get** /api/v0/customers/{customerId}/liquidation_addresses/{liquidationAddressId} | Get a specific liquidation address
[**LiquidationAddressControllerGetLiquidationAddresses**](LiquidationAddressesAPI.md#LiquidationAddressControllerGetLiquidationAddresses) | **Get** /api/v0/customers/{customerId}/liquidation_addresses | Get all liquidation addresses for a customer



## LiquidationAddressControllerCreateLiquidationAddress

> LiquidationAddressResponseDto LiquidationAddressControllerCreateLiquidationAddress(ctx, customerId).CreateLiquidationAddressDto(createLiquidationAddressDto).Execute()

Create a new liquidation address for a customer



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
	customerId := "cust_123" // string | Unique identifier for the customer
	createLiquidationAddressDto := *openapiclient.NewCreateLiquidationAddressDto("ethereum", "usdc", "0x4d0280da2f2fDA5103914bCc5aad114743152A9c") // CreateLiquidationAddressDto | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.LiquidationAddressesAPI.LiquidationAddressControllerCreateLiquidationAddress(context.Background(), customerId).CreateLiquidationAddressDto(createLiquidationAddressDto).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LiquidationAddressesAPI.LiquidationAddressControllerCreateLiquidationAddress``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `LiquidationAddressControllerCreateLiquidationAddress`: LiquidationAddressResponseDto
	fmt.Fprintf(os.Stdout, "Response from `LiquidationAddressesAPI.LiquidationAddressControllerCreateLiquidationAddress`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**customerId** | **string** | Unique identifier for the customer | 

### Other Parameters

Other parameters are passed through a pointer to a apiLiquidationAddressControllerCreateLiquidationAddressRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **createLiquidationAddressDto** | [**CreateLiquidationAddressDto**](CreateLiquidationAddressDto.md) |  | 

### Return type

[**LiquidationAddressResponseDto**](LiquidationAddressResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## LiquidationAddressControllerGetLiquidationAddress

> LiquidationAddressResponseDto LiquidationAddressControllerGetLiquidationAddress(ctx, customerId, liquidationAddressId).Execute()

Get a specific liquidation address



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
	customerId := "cust_123" // string | Unique identifier for the customer
	liquidationAddressId := "la_generated_id_123" // string | Unique identifier for the liquidation address

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.LiquidationAddressesAPI.LiquidationAddressControllerGetLiquidationAddress(context.Background(), customerId, liquidationAddressId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LiquidationAddressesAPI.LiquidationAddressControllerGetLiquidationAddress``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `LiquidationAddressControllerGetLiquidationAddress`: LiquidationAddressResponseDto
	fmt.Fprintf(os.Stdout, "Response from `LiquidationAddressesAPI.LiquidationAddressControllerGetLiquidationAddress`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**customerId** | **string** | Unique identifier for the customer | 
**liquidationAddressId** | **string** | Unique identifier for the liquidation address | 

### Other Parameters

Other parameters are passed through a pointer to a apiLiquidationAddressControllerGetLiquidationAddressRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**LiquidationAddressResponseDto**](LiquidationAddressResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## LiquidationAddressControllerGetLiquidationAddresses

> []LiquidationAddressResponseDto LiquidationAddressControllerGetLiquidationAddresses(ctx, customerId).Execute()

Get all liquidation addresses for a customer



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
	customerId := "cust_123" // string | Unique identifier for the customer

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.LiquidationAddressesAPI.LiquidationAddressControllerGetLiquidationAddresses(context.Background(), customerId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `LiquidationAddressesAPI.LiquidationAddressControllerGetLiquidationAddresses``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `LiquidationAddressControllerGetLiquidationAddresses`: []LiquidationAddressResponseDto
	fmt.Fprintf(os.Stdout, "Response from `LiquidationAddressesAPI.LiquidationAddressControllerGetLiquidationAddresses`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**customerId** | **string** | Unique identifier for the customer | 

### Other Parameters

Other parameters are passed through a pointer to a apiLiquidationAddressControllerGetLiquidationAddressesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**[]LiquidationAddressResponseDto**](LiquidationAddressResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

