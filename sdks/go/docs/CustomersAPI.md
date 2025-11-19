# \CustomersAPI

All URIs are relative to *https://api.devdraft.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CustomerControllerCreate**](CustomersAPI.md#CustomerControllerCreate) | **Post** /api/v0/customers | Create a new customer
[**CustomerControllerFindAll**](CustomersAPI.md#CustomerControllerFindAll) | **Get** /api/v0/customers | Get all customers with filters
[**CustomerControllerFindOne**](CustomersAPI.md#CustomerControllerFindOne) | **Get** /api/v0/customers/{id} | Get a customer by ID
[**CustomerControllerUpdate**](CustomersAPI.md#CustomerControllerUpdate) | **Patch** /api/v0/customers/{id} | Update a customer



## CustomerControllerCreate

> CustomerControllerCreate(ctx).CreateCustomerDto(createCustomerDto).Execute()

Create a new customer



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
	createCustomerDto := *openapiclient.NewCreateCustomerDto("John", "Doe", "+1-555-123-4567") // CreateCustomerDto | Customer creation data

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.CustomersAPI.CustomerControllerCreate(context.Background()).CreateCustomerDto(createCustomerDto).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CustomersAPI.CustomerControllerCreate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCustomerControllerCreateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createCustomerDto** | [**CreateCustomerDto**](CreateCustomerDto.md) | Customer creation data | 

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


## CustomerControllerFindAll

> CustomerControllerFindAll(ctx).Skip(skip).Take(take).Status(status).Name(name).Email(email).Execute()

Get all customers with filters



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
	status := openapiclient.CustomerStatus("ACTIVE") // CustomerStatus | Filter customers by status (optional)
	name := "John" // string | Filter customers by name (partial match, case-insensitive) (optional)
	email := "john.doe@example.com" // string | Filter customers by email (exact match, case-insensitive) (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.CustomersAPI.CustomerControllerFindAll(context.Background()).Skip(skip).Take(take).Status(status).Name(name).Email(email).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CustomersAPI.CustomerControllerFindAll``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCustomerControllerFindAllRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **float32** | Number of records to skip for pagination | [default to 0]
 **take** | **float32** | Number of records to return (max 100) | [default to 10]
 **status** | [**CustomerStatus**](CustomerStatus.md) | Filter customers by status | 
 **name** | **string** | Filter customers by name (partial match, case-insensitive) | 
 **email** | **string** | Filter customers by email (exact match, case-insensitive) | 

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


## CustomerControllerFindOne

> CustomerControllerFindOne(ctx, id).Execute()

Get a customer by ID



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
	id := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Customer unique identifier (UUID)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.CustomersAPI.CustomerControllerFindOne(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CustomersAPI.CustomerControllerFindOne``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** | Customer unique identifier (UUID) | 

### Other Parameters

Other parameters are passed through a pointer to a apiCustomerControllerFindOneRequest struct via the builder pattern


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


## CustomerControllerUpdate

> CustomerControllerUpdate(ctx, id).UpdateCustomerDto(updateCustomerDto).Execute()

Update a customer



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
	id := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Customer unique identifier (UUID)
	updateCustomerDto := *openapiclient.NewUpdateCustomerDto() // UpdateCustomerDto | Customer update data

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.CustomersAPI.CustomerControllerUpdate(context.Background(), id).UpdateCustomerDto(updateCustomerDto).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CustomersAPI.CustomerControllerUpdate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** | Customer unique identifier (UUID) | 

### Other Parameters

Other parameters are passed through a pointer to a apiCustomerControllerUpdateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **updateCustomerDto** | [**UpdateCustomerDto**](UpdateCustomerDto.md) | Customer update data | 

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

