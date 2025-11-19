# \TaxesAPI

All URIs are relative to *https://api.devdraft.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**TaxControllerCreate**](TaxesAPI.md#TaxControllerCreate) | **Post** /api/v0/taxes | Create a new tax
[**TaxControllerDeleteWithoutId**](TaxesAPI.md#TaxControllerDeleteWithoutId) | **Delete** /api/v0/taxes | Tax ID required for deletion
[**TaxControllerFindAll**](TaxesAPI.md#TaxControllerFindAll) | **Get** /api/v0/taxes | Get all taxes with filters
[**TaxControllerFindOne**](TaxesAPI.md#TaxControllerFindOne) | **Get** /api/v0/taxes/{id} | Get a tax by ID
[**TaxControllerRemove**](TaxesAPI.md#TaxControllerRemove) | **Delete** /api/v0/taxes/{id} | Delete a tax
[**TaxControllerUpdate**](TaxesAPI.md#TaxControllerUpdate) | **Put** /api/v0/taxes/{id} | Update a tax
[**TaxControllerUpdateWithoutId**](TaxesAPI.md#TaxControllerUpdateWithoutId) | **Put** /api/v0/taxes | Tax ID required for updates



## TaxControllerCreate

> TaxControllerCreate201Response TaxControllerCreate(ctx).CreateTaxDto(createTaxDto).Execute()

Create a new tax



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
	createTaxDto := *openapiclient.NewCreateTaxDto("Sales Tax", float32(8.5)) // CreateTaxDto | Tax creation data

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TaxesAPI.TaxControllerCreate(context.Background()).CreateTaxDto(createTaxDto).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TaxesAPI.TaxControllerCreate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `TaxControllerCreate`: TaxControllerCreate201Response
	fmt.Fprintf(os.Stdout, "Response from `TaxesAPI.TaxControllerCreate`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiTaxControllerCreateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createTaxDto** | [**CreateTaxDto**](CreateTaxDto.md) | Tax creation data | 

### Return type

[**TaxControllerCreate201Response**](TaxControllerCreate201Response.md)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## TaxControllerDeleteWithoutId

> TaxControllerDeleteWithoutId(ctx).Execute()

Tax ID required for deletion



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
	r, err := apiClient.TaxesAPI.TaxControllerDeleteWithoutId(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TaxesAPI.TaxControllerDeleteWithoutId``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiTaxControllerDeleteWithoutIdRequest struct via the builder pattern


### Return type

 (empty response body)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## TaxControllerFindAll

> TaxControllerFindAll(ctx).Skip(skip).Take(take).Name(name).Active(active).Execute()

Get all taxes with filters



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
	skip := float32(0) // float32 | Number of records to skip for pagination (optional) (default to 0)
	take := float32(10) // float32 | Number of records to return (max 100) (optional) (default to 10)
	name := "Sales" // string | Filter taxes by name (partial match, case-insensitive) (optional)
	active := true // bool | Filter by active status (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.TaxesAPI.TaxControllerFindAll(context.Background()).Skip(skip).Take(take).Name(name).Active(active).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TaxesAPI.TaxControllerFindAll``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiTaxControllerFindAllRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **float32** | Number of records to skip for pagination | [default to 0]
 **take** | **float32** | Number of records to return (max 100) | [default to 10]
 **name** | **string** | Filter taxes by name (partial match, case-insensitive) | 
 **active** | **bool** | Filter by active status | 

### Return type

 (empty response body)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## TaxControllerFindOne

> TaxControllerFindOne(ctx, id).Execute()

Get a tax by ID



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
	id := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Tax unique identifier (UUID)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.TaxesAPI.TaxControllerFindOne(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TaxesAPI.TaxControllerFindOne``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** | Tax unique identifier (UUID) | 

### Other Parameters

Other parameters are passed through a pointer to a apiTaxControllerFindOneRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

 (empty response body)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## TaxControllerRemove

> TaxControllerRemove(ctx, id).Execute()

Delete a tax



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
	id := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Tax unique identifier (UUID)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.TaxesAPI.TaxControllerRemove(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TaxesAPI.TaxControllerRemove``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** | Tax unique identifier (UUID) | 

### Other Parameters

Other parameters are passed through a pointer to a apiTaxControllerRemoveRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

 (empty response body)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## TaxControllerUpdate

> TaxControllerUpdate(ctx, id).UpdateTaxDto(updateTaxDto).Execute()

Update a tax



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
	id := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Tax unique identifier (UUID)
	updateTaxDto := *openapiclient.NewUpdateTaxDto() // UpdateTaxDto | Tax update data - only include fields you want to update

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.TaxesAPI.TaxControllerUpdate(context.Background(), id).UpdateTaxDto(updateTaxDto).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TaxesAPI.TaxControllerUpdate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** | Tax unique identifier (UUID) | 

### Other Parameters

Other parameters are passed through a pointer to a apiTaxControllerUpdateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **updateTaxDto** | [**UpdateTaxDto**](UpdateTaxDto.md) | Tax update data - only include fields you want to update | 

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


## TaxControllerUpdateWithoutId

> TaxControllerUpdateWithoutId(ctx).Execute()

Tax ID required for updates



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
	r, err := apiClient.TaxesAPI.TaxControllerUpdateWithoutId(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TaxesAPI.TaxControllerUpdateWithoutId``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiTaxControllerUpdateWithoutIdRequest struct via the builder pattern


### Return type

 (empty response body)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

