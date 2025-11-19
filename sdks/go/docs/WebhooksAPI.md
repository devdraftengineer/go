# \WebhooksAPI

All URIs are relative to *https://api.devdraft.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**WebhookControllerCreate**](WebhooksAPI.md#WebhookControllerCreate) | **Post** /api/v0/webhooks | Create a new webhook
[**WebhookControllerFindAll**](WebhooksAPI.md#WebhookControllerFindAll) | **Get** /api/v0/webhooks | Get all webhooks
[**WebhookControllerFindOne**](WebhooksAPI.md#WebhookControllerFindOne) | **Get** /api/v0/webhooks/{id} | Get a webhook by id
[**WebhookControllerRemove**](WebhooksAPI.md#WebhookControllerRemove) | **Delete** /api/v0/webhooks/{id} | Delete a webhook
[**WebhookControllerUpdate**](WebhooksAPI.md#WebhookControllerUpdate) | **Patch** /api/v0/webhooks/{id} | Update a webhook



## WebhookControllerCreate

> WebhookResponseDto WebhookControllerCreate(ctx).CreateWebhookDto(createWebhookDto).Execute()

Create a new webhook



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
	createWebhookDto := *openapiclient.NewCreateWebhookDto("Payment Notifications", "https://api.example.com/webhooks/payments", true, false) // CreateWebhookDto | Webhook configuration details

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.WebhooksAPI.WebhookControllerCreate(context.Background()).CreateWebhookDto(createWebhookDto).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `WebhooksAPI.WebhookControllerCreate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `WebhookControllerCreate`: WebhookResponseDto
	fmt.Fprintf(os.Stdout, "Response from `WebhooksAPI.WebhookControllerCreate`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiWebhookControllerCreateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createWebhookDto** | [**CreateWebhookDto**](CreateWebhookDto.md) | Webhook configuration details | 

### Return type

[**WebhookResponseDto**](WebhookResponseDto.md)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## WebhookControllerFindAll

> []WebhookResponseDto WebhookControllerFindAll(ctx).Skip(skip).Take(take).Execute()

Get all webhooks



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
	skip := float32(8.14) // float32 | Number of records to skip (default: 0) (optional)
	take := float32(8.14) // float32 | Number of records to return (default: 10) (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.WebhooksAPI.WebhookControllerFindAll(context.Background()).Skip(skip).Take(take).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `WebhooksAPI.WebhookControllerFindAll``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `WebhookControllerFindAll`: []WebhookResponseDto
	fmt.Fprintf(os.Stdout, "Response from `WebhooksAPI.WebhookControllerFindAll`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiWebhookControllerFindAllRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **float32** | Number of records to skip (default: 0) | 
 **take** | **float32** | Number of records to return (default: 10) | 

### Return type

[**[]WebhookResponseDto**](WebhookResponseDto.md)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## WebhookControllerFindOne

> WebhookResponseDto WebhookControllerFindOne(ctx, id).Execute()

Get a webhook by id



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
	id := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Webhook unique identifier (UUID)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.WebhooksAPI.WebhookControllerFindOne(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `WebhooksAPI.WebhookControllerFindOne``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `WebhookControllerFindOne`: WebhookResponseDto
	fmt.Fprintf(os.Stdout, "Response from `WebhooksAPI.WebhookControllerFindOne`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** | Webhook unique identifier (UUID) | 

### Other Parameters

Other parameters are passed through a pointer to a apiWebhookControllerFindOneRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**WebhookResponseDto**](WebhookResponseDto.md)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## WebhookControllerRemove

> WebhookResponseDto WebhookControllerRemove(ctx, id).Execute()

Delete a webhook



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
	id := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Webhook unique identifier (UUID)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.WebhooksAPI.WebhookControllerRemove(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `WebhooksAPI.WebhookControllerRemove``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `WebhookControllerRemove`: WebhookResponseDto
	fmt.Fprintf(os.Stdout, "Response from `WebhooksAPI.WebhookControllerRemove`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** | Webhook unique identifier (UUID) | 

### Other Parameters

Other parameters are passed through a pointer to a apiWebhookControllerRemoveRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**WebhookResponseDto**](WebhookResponseDto.md)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## WebhookControllerUpdate

> WebhookResponseDto WebhookControllerUpdate(ctx, id).UpdateWebhookDto(updateWebhookDto).Execute()

Update a webhook



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
	id := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Webhook unique identifier (UUID)
	updateWebhookDto := *openapiclient.NewUpdateWebhookDto() // UpdateWebhookDto | Webhook update details

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.WebhooksAPI.WebhookControllerUpdate(context.Background(), id).UpdateWebhookDto(updateWebhookDto).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `WebhooksAPI.WebhookControllerUpdate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `WebhookControllerUpdate`: WebhookResponseDto
	fmt.Fprintf(os.Stdout, "Response from `WebhooksAPI.WebhookControllerUpdate`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** | Webhook unique identifier (UUID) | 

### Other Parameters

Other parameters are passed through a pointer to a apiWebhookControllerUpdateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **updateWebhookDto** | [**UpdateWebhookDto**](UpdateWebhookDto.md) | Webhook update details | 

### Return type

[**WebhookResponseDto**](WebhookResponseDto.md)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

