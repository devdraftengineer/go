# \InvoicesAPI

All URIs are relative to *https://api.devdraft.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**InvoiceControllerCreate**](InvoicesAPI.md#InvoiceControllerCreate) | **Post** /api/v0/invoices | Create a new invoice
[**InvoiceControllerFindAll**](InvoicesAPI.md#InvoiceControllerFindAll) | **Get** /api/v0/invoices | Get all invoices
[**InvoiceControllerFindOne**](InvoicesAPI.md#InvoiceControllerFindOne) | **Get** /api/v0/invoices/{id} | Get an invoice by ID
[**InvoiceControllerUpdate**](InvoicesAPI.md#InvoiceControllerUpdate) | **Put** /api/v0/invoices/{id} | Update an invoice



## InvoiceControllerCreate

> InvoiceControllerCreate(ctx).CreateInvoiceDto(createInvoiceDto).Execute()

Create a new invoice

### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
    "time"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	createInvoiceDto := *openapiclient.NewCreateInvoiceDto("Name_example", "Email_example", "CustomerId_example", "Currency_example", map[string]interface{}(123), time.Now(), "Delivery_example", false, []string{"PaymentMethods_example"}, "Status_example", false) // CreateInvoiceDto | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.InvoicesAPI.InvoiceControllerCreate(context.Background()).CreateInvoiceDto(createInvoiceDto).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `InvoicesAPI.InvoiceControllerCreate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiInvoiceControllerCreateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createInvoiceDto** | [**CreateInvoiceDto**](CreateInvoiceDto.md) |  | 

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


## InvoiceControllerFindAll

> InvoiceControllerFindAll(ctx).Skip(skip).Take(take).Execute()

Get all invoices

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
	skip := float32(8.14) // float32 | Number of records to skip (optional)
	take := float32(8.14) // float32 | Number of records to take (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.InvoicesAPI.InvoiceControllerFindAll(context.Background()).Skip(skip).Take(take).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `InvoicesAPI.InvoiceControllerFindAll``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiInvoiceControllerFindAllRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **float32** | Number of records to skip | 
 **take** | **float32** | Number of records to take | 

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


## InvoiceControllerFindOne

> InvoiceControllerFindOne(ctx, id).Execute()

Get an invoice by ID

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
	id := "id_example" // string | Invoice ID

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.InvoicesAPI.InvoiceControllerFindOne(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `InvoicesAPI.InvoiceControllerFindOne``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** | Invoice ID | 

### Other Parameters

Other parameters are passed through a pointer to a apiInvoiceControllerFindOneRequest struct via the builder pattern


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


## InvoiceControllerUpdate

> InvoiceControllerUpdate(ctx, id).CreateInvoiceDto(createInvoiceDto).Execute()

Update an invoice

### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
    "time"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	id := "id_example" // string | Invoice ID
	createInvoiceDto := *openapiclient.NewCreateInvoiceDto("Name_example", "Email_example", "CustomerId_example", "Currency_example", map[string]interface{}(123), time.Now(), "Delivery_example", false, []string{"PaymentMethods_example"}, "Status_example", false) // CreateInvoiceDto | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.InvoicesAPI.InvoiceControllerUpdate(context.Background(), id).CreateInvoiceDto(createInvoiceDto).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `InvoicesAPI.InvoiceControllerUpdate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** | Invoice ID | 

### Other Parameters

Other parameters are passed through a pointer to a apiInvoiceControllerUpdateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **createInvoiceDto** | [**CreateInvoiceDto**](CreateInvoiceDto.md) |  | 

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

