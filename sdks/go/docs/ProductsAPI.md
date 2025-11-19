# \ProductsAPI

All URIs are relative to *https://api.devdraft.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ProductControllerCreate**](ProductsAPI.md#ProductControllerCreate) | **Post** /api/v0/products | Create a new product
[**ProductControllerFindAll**](ProductsAPI.md#ProductControllerFindAll) | **Get** /api/v0/products | Get all products
[**ProductControllerFindOne**](ProductsAPI.md#ProductControllerFindOne) | **Get** /api/v0/products/{id} | Get a product by ID
[**ProductControllerRemove**](ProductsAPI.md#ProductControllerRemove) | **Delete** /api/v0/products/{id} | Delete a product
[**ProductControllerUpdate**](ProductsAPI.md#ProductControllerUpdate) | **Put** /api/v0/products/{id} | Update a product
[**ProductControllerUploadImage**](ProductsAPI.md#ProductControllerUploadImage) | **Post** /api/v0/products/{id}/images | Upload images for a product



## ProductControllerCreate

> ProductControllerCreate(ctx).Name(name).Description(description).Price(price).Currency(currency).Type_(type_).Weight(weight).Unit(unit).Quantity(quantity).StockCount(stockCount).Status(status).ProductType(productType).Images(images).Execute()

Create a new product



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
	name := "name_example" // string | Product name as it will appear to customers. Should be clear and descriptive.
	description := "description_example" // string | Detailed description of the product. Supports markdown formatting for rich text display.
	price := float32(8.14) // float32 | Product price in the specified currency. Must be greater than 0.
	currency := "currency_example" // string | Currency code for the price. Defaults to USD if not specified. (optional) (default to "USD")
	type_ := "type__example" // string | Product type (optional)
	weight := float32(8.14) // float32 | Weight of the product (optional)
	unit := "unit_example" // string | Unit of measurement (optional)
	quantity := float32(8.14) // float32 | Quantity available (optional)
	stockCount := float32(8.14) // float32 | Stock count (optional)
	status := "status_example" // string | Product status (optional)
	productType := "productType_example" // string | Product type (optional)
	images := []string{"Inner_example"} // []string | Array of image URLs (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.ProductsAPI.ProductControllerCreate(context.Background()).Name(name).Description(description).Price(price).Currency(currency).Type_(type_).Weight(weight).Unit(unit).Quantity(quantity).StockCount(stockCount).Status(status).ProductType(productType).Images(images).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ProductsAPI.ProductControllerCreate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiProductControllerCreateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **string** | Product name as it will appear to customers. Should be clear and descriptive. | 
 **description** | **string** | Detailed description of the product. Supports markdown formatting for rich text display. | 
 **price** | **float32** | Product price in the specified currency. Must be greater than 0. | 
 **currency** | **string** | Currency code for the price. Defaults to USD if not specified. | [default to &quot;USD&quot;]
 **type_** | **string** | Product type | 
 **weight** | **float32** | Weight of the product | 
 **unit** | **string** | Unit of measurement | 
 **quantity** | **float32** | Quantity available | 
 **stockCount** | **float32** | Stock count | 
 **status** | **string** | Product status | 
 **productType** | **string** | Product type | 
 **images** | **[]string** | Array of image URLs | 

### Return type

 (empty response body)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ProductControllerFindAll

> ProductControllerFindAll(ctx).Skip(skip).Take(take).Execute()

Get all products



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
	r, err := apiClient.ProductsAPI.ProductControllerFindAll(context.Background()).Skip(skip).Take(take).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ProductsAPI.ProductControllerFindAll``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiProductControllerFindAllRequest struct via the builder pattern


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


## ProductControllerFindOne

> ProductControllerFindOne(ctx, id).Execute()

Get a product by ID



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
	id := "id_example" // string | Product ID

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.ProductsAPI.ProductControllerFindOne(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ProductsAPI.ProductControllerFindOne``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** | Product ID | 

### Other Parameters

Other parameters are passed through a pointer to a apiProductControllerFindOneRequest struct via the builder pattern


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


## ProductControllerRemove

> ProductControllerRemove(ctx, id).Execute()

Delete a product



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
	id := "id_example" // string | Product ID

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.ProductsAPI.ProductControllerRemove(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ProductsAPI.ProductControllerRemove``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** | Product ID | 

### Other Parameters

Other parameters are passed through a pointer to a apiProductControllerRemoveRequest struct via the builder pattern


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


## ProductControllerUpdate

> ProductControllerUpdate(ctx, id).Name(name).Description(description).Price(price).Currency(currency).Type_(type_).Weight(weight).Unit(unit).Quantity(quantity).StockCount(stockCount).Status(status).ProductType(productType).Images(images).Execute()

Update a product



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
	id := "id_example" // string | Product ID
	name := "name_example" // string | Product name as it will appear to customers. Should be clear and descriptive. (optional)
	description := "description_example" // string | Detailed description of the product. Supports markdown formatting for rich text display. (optional)
	price := float32(8.14) // float32 | Product price in the specified currency. Must be greater than 0. (optional)
	currency := "currency_example" // string | Currency code for the price. Defaults to USD if not specified. (optional) (default to "USD")
	type_ := "type__example" // string | Product type (optional)
	weight := float32(8.14) // float32 | Weight of the product (optional)
	unit := "unit_example" // string | Unit of measurement (optional)
	quantity := float32(8.14) // float32 | Quantity available (optional)
	stockCount := float32(8.14) // float32 | Stock count (optional)
	status := "status_example" // string | Product status (optional)
	productType := "productType_example" // string | Product type (optional)
	images := []string{"Inner_example"} // []string | Array of image URLs (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.ProductsAPI.ProductControllerUpdate(context.Background(), id).Name(name).Description(description).Price(price).Currency(currency).Type_(type_).Weight(weight).Unit(unit).Quantity(quantity).StockCount(stockCount).Status(status).ProductType(productType).Images(images).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ProductsAPI.ProductControllerUpdate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** | Product ID | 

### Other Parameters

Other parameters are passed through a pointer to a apiProductControllerUpdateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **name** | **string** | Product name as it will appear to customers. Should be clear and descriptive. | 
 **description** | **string** | Detailed description of the product. Supports markdown formatting for rich text display. | 
 **price** | **float32** | Product price in the specified currency. Must be greater than 0. | 
 **currency** | **string** | Currency code for the price. Defaults to USD if not specified. | [default to &quot;USD&quot;]
 **type_** | **string** | Product type | 
 **weight** | **float32** | Weight of the product | 
 **unit** | **string** | Unit of measurement | 
 **quantity** | **float32** | Quantity available | 
 **stockCount** | **float32** | Stock count | 
 **status** | **string** | Product status | 
 **productType** | **string** | Product type | 
 **images** | **[]string** | Array of image URLs | 

### Return type

 (empty response body)

### Authorization

[x-client-secret](../README.md#x-client-secret), [x-client-key](../README.md#x-client-key)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ProductControllerUploadImage

> ProductControllerUploadImage(ctx, id).Execute()

Upload images for a product



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
	id := "id_example" // string | Product ID

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.ProductsAPI.ProductControllerUploadImage(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ProductsAPI.ProductControllerUploadImage``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** | Product ID | 

### Other Parameters

Other parameters are passed through a pointer to a apiProductControllerUploadImageRequest struct via the builder pattern


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

