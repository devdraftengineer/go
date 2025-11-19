# \ExchangeRatesAPI

All URIs are relative to *https://api.devdraft.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ExchangeRateControllerGetEURToUSDRate**](ExchangeRatesAPI.md#ExchangeRateControllerGetEURToUSDRate) | **Get** /api/v0/exchange-rate/eur-to-usd | Get EUR to USD exchange rate
[**ExchangeRateControllerGetExchangeRate**](ExchangeRatesAPI.md#ExchangeRateControllerGetExchangeRate) | **Get** /api/v0/exchange-rate | Get exchange rate between specified currencies
[**ExchangeRateControllerGetUSDToEURRate**](ExchangeRatesAPI.md#ExchangeRateControllerGetUSDToEURRate) | **Get** /api/v0/exchange-rate/usd-to-eur | Get USD to EUR exchange rate



## ExchangeRateControllerGetEURToUSDRate

> ExchangeRateResponseDto ExchangeRateControllerGetEURToUSDRate(ctx).Execute()

Get EUR to USD exchange rate



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
	resp, r, err := apiClient.ExchangeRatesAPI.ExchangeRateControllerGetEURToUSDRate(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ExchangeRatesAPI.ExchangeRateControllerGetEURToUSDRate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ExchangeRateControllerGetEURToUSDRate`: ExchangeRateResponseDto
	fmt.Fprintf(os.Stdout, "Response from `ExchangeRatesAPI.ExchangeRateControllerGetEURToUSDRate`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiExchangeRateControllerGetEURToUSDRateRequest struct via the builder pattern


### Return type

[**ExchangeRateResponseDto**](ExchangeRateResponseDto.md)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ExchangeRateControllerGetExchangeRate

> ExchangeRateResponseDto ExchangeRateControllerGetExchangeRate(ctx).From(from).To(to).Execute()

Get exchange rate between specified currencies



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
	from := "usd" // string | Source currency code (e.g., usd)
	to := "eur" // string | Target currency code (e.g., eur)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ExchangeRatesAPI.ExchangeRateControllerGetExchangeRate(context.Background()).From(from).To(to).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ExchangeRatesAPI.ExchangeRateControllerGetExchangeRate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ExchangeRateControllerGetExchangeRate`: ExchangeRateResponseDto
	fmt.Fprintf(os.Stdout, "Response from `ExchangeRatesAPI.ExchangeRateControllerGetExchangeRate`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiExchangeRateControllerGetExchangeRateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from** | **string** | Source currency code (e.g., usd) | 
 **to** | **string** | Target currency code (e.g., eur) | 

### Return type

[**ExchangeRateResponseDto**](ExchangeRateResponseDto.md)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ExchangeRateControllerGetUSDToEURRate

> ExchangeRateResponseDto ExchangeRateControllerGetUSDToEURRate(ctx).Execute()

Get USD to EUR exchange rate



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
	resp, r, err := apiClient.ExchangeRatesAPI.ExchangeRateControllerGetUSDToEURRate(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ExchangeRatesAPI.ExchangeRateControllerGetUSDToEURRate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ExchangeRateControllerGetUSDToEURRate`: ExchangeRateResponseDto
	fmt.Fprintf(os.Stdout, "Response from `ExchangeRatesAPI.ExchangeRateControllerGetUSDToEURRate`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiExchangeRateControllerGetUSDToEURRateRequest struct via the builder pattern


### Return type

[**ExchangeRateResponseDto**](ExchangeRateResponseDto.md)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

