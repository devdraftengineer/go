# \AppBalancesAPI

All URIs are relative to *https://api.devdraft.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**BalanceControllerGetAllBalances**](AppBalancesAPI.md#BalanceControllerGetAllBalances) | **Get** /api/v0/balance | Get all stablecoin balances for an app
[**BalanceControllerGetEURCBalance**](AppBalancesAPI.md#BalanceControllerGetEURCBalance) | **Get** /api/v0/balance/eurc | Get EURC balance for an app
[**BalanceControllerGetUSDCBalance**](AppBalancesAPI.md#BalanceControllerGetUSDCBalance) | **Get** /api/v0/balance/usdc | Get USDC balance for an app



## BalanceControllerGetAllBalances

> AllBalancesResponse BalanceControllerGetAllBalances(ctx).Execute()

Get all stablecoin balances for an app



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

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AppBalancesAPI.BalanceControllerGetAllBalances(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AppBalancesAPI.BalanceControllerGetAllBalances``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `BalanceControllerGetAllBalances`: AllBalancesResponse
	fmt.Fprintf(os.Stdout, "Response from `AppBalancesAPI.BalanceControllerGetAllBalances`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiBalanceControllerGetAllBalancesRequest struct via the builder pattern


### Return type

[**AllBalancesResponse**](AllBalancesResponse.md)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## BalanceControllerGetEURCBalance

> AggregatedBalanceResponse BalanceControllerGetEURCBalance(ctx).Execute()

Get EURC balance for an app



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

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AppBalancesAPI.BalanceControllerGetEURCBalance(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AppBalancesAPI.BalanceControllerGetEURCBalance``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `BalanceControllerGetEURCBalance`: AggregatedBalanceResponse
	fmt.Fprintf(os.Stdout, "Response from `AppBalancesAPI.BalanceControllerGetEURCBalance`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiBalanceControllerGetEURCBalanceRequest struct via the builder pattern


### Return type

[**AggregatedBalanceResponse**](AggregatedBalanceResponse.md)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## BalanceControllerGetUSDCBalance

> AggregatedBalanceResponse BalanceControllerGetUSDCBalance(ctx).Execute()

Get USDC balance for an app



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

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AppBalancesAPI.BalanceControllerGetUSDCBalance(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AppBalancesAPI.BalanceControllerGetUSDCBalance``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `BalanceControllerGetUSDCBalance`: AggregatedBalanceResponse
	fmt.Fprintf(os.Stdout, "Response from `AppBalancesAPI.BalanceControllerGetUSDCBalance`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiBalanceControllerGetUSDCBalanceRequest struct via the builder pattern


### Return type

[**AggregatedBalanceResponse**](AggregatedBalanceResponse.md)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

