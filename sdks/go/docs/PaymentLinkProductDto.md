# PaymentLinkProductDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ProductId** | **string** | UUID of the product to include in this payment link. Must be a valid product from your catalog. | 
**Quantity** | **int32** | Quantity of this product to include. Must be at least 1. | [default to 1]

## Methods

### NewPaymentLinkProductDto

`func NewPaymentLinkProductDto(productId string, quantity int32, ) *PaymentLinkProductDto`

NewPaymentLinkProductDto instantiates a new PaymentLinkProductDto object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPaymentLinkProductDtoWithDefaults

`func NewPaymentLinkProductDtoWithDefaults() *PaymentLinkProductDto`

NewPaymentLinkProductDtoWithDefaults instantiates a new PaymentLinkProductDto object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetProductId

`func (o *PaymentLinkProductDto) GetProductId() string`

GetProductId returns the ProductId field if non-nil, zero value otherwise.

### GetProductIdOk

`func (o *PaymentLinkProductDto) GetProductIdOk() (*string, bool)`

GetProductIdOk returns a tuple with the ProductId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProductId

`func (o *PaymentLinkProductDto) SetProductId(v string)`

SetProductId sets ProductId field to given value.


### GetQuantity

`func (o *PaymentLinkProductDto) GetQuantity() int32`

GetQuantity returns the Quantity field if non-nil, zero value otherwise.

### GetQuantityOk

`func (o *PaymentLinkProductDto) GetQuantityOk() (*int32, bool)`

GetQuantityOk returns a tuple with the Quantity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetQuantity

`func (o *PaymentLinkProductDto) SetQuantity(v int32)`

SetQuantity sets Quantity field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


