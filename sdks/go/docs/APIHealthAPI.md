# \APIHealthAPI

All URIs are relative to *https://api.devdraft.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**HealthControllerCheckV0**](APIHealthAPI.md#HealthControllerCheckV0) | **Get** /api/v0/health | Authenticated health check endpoint
[**HealthControllerPublicHealthCheckV0**](APIHealthAPI.md#HealthControllerPublicHealthCheckV0) | **Get** /api/v0/health/public | Public health check endpoint



## HealthControllerCheckV0

> HealthResponseDto HealthControllerCheckV0(ctx).Execute()

Authenticated health check endpoint

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
	resp, r, err := apiClient.APIHealthAPI.HealthControllerCheckV0(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `APIHealthAPI.HealthControllerCheckV0``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `HealthControllerCheckV0`: HealthResponseDto
	fmt.Fprintf(os.Stdout, "Response from `APIHealthAPI.HealthControllerCheckV0`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiHealthControllerCheckV0Request struct via the builder pattern


### Return type

[**HealthResponseDto**](HealthResponseDto.md)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## HealthControllerPublicHealthCheckV0

> PublicHealthResponseDto HealthControllerPublicHealthCheckV0(ctx).Execute()

Public health check endpoint

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
	resp, r, err := apiClient.APIHealthAPI.HealthControllerPublicHealthCheckV0(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `APIHealthAPI.HealthControllerPublicHealthCheckV0``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `HealthControllerPublicHealthCheckV0`: PublicHealthResponseDto
	fmt.Fprintf(os.Stdout, "Response from `APIHealthAPI.HealthControllerPublicHealthCheckV0`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiHealthControllerPublicHealthCheckV0Request struct via the builder pattern


### Return type

[**PublicHealthResponseDto**](PublicHealthResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

