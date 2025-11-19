# InvoiceProductDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ProductId** | **string** | Product ID | 
**Quantity** | **float32** | Quantity of the product | 

## Methods

### NewInvoiceProductDto

`func NewInvoiceProductDto(productId string, quantity float32, ) *InvoiceProductDto`

NewInvoiceProductDto instantiates a new InvoiceProductDto object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewInvoiceProductDtoWithDefaults

`func NewInvoiceProductDtoWithDefaults() *InvoiceProductDto`

NewInvoiceProductDtoWithDefaults instantiates a new InvoiceProductDto object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetProductId

`func (o *InvoiceProductDto) GetProductId() string`

GetProductId returns the ProductId field if non-nil, zero value otherwise.

### GetProductIdOk

`func (o *InvoiceProductDto) GetProductIdOk() (*string, bool)`

GetProductIdOk returns a tuple with the ProductId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProductId

`func (o *InvoiceProductDto) SetProductId(v string)`

SetProductId sets ProductId field to given value.


### GetQuantity

`func (o *InvoiceProductDto) GetQuantity() float32`

GetQuantity returns the Quantity field if non-nil, zero value otherwise.

### GetQuantityOk

`func (o *InvoiceProductDto) GetQuantityOk() (*float32, bool)`

GetQuantityOk returns a tuple with the Quantity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetQuantity

`func (o *InvoiceProductDto) SetQuantity(v float32)`

SetQuantity sets Quantity field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


