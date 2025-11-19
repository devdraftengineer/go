# PaymentResponseDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | Payment ID | 
**Amount** | **float32** | The amount charged | 
**Currency** | **string** | The currency code | 
**Status** | **string** | Payment status | 
**Timestamp** | **string** | Timestamp of the payment | 

## Methods

### NewPaymentResponseDto

`func NewPaymentResponseDto(id string, amount float32, currency string, status string, timestamp string, ) *PaymentResponseDto`

NewPaymentResponseDto instantiates a new PaymentResponseDto object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPaymentResponseDtoWithDefaults

`func NewPaymentResponseDtoWithDefaults() *PaymentResponseDto`

NewPaymentResponseDtoWithDefaults instantiates a new PaymentResponseDto object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *PaymentResponseDto) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *PaymentResponseDto) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *PaymentResponseDto) SetId(v string)`

SetId sets Id field to given value.


### GetAmount

`func (o *PaymentResponseDto) GetAmount() float32`

GetAmount returns the Amount field if non-nil, zero value otherwise.

### GetAmountOk

`func (o *PaymentResponseDto) GetAmountOk() (*float32, bool)`

GetAmountOk returns a tuple with the Amount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAmount

`func (o *PaymentResponseDto) SetAmount(v float32)`

SetAmount sets Amount field to given value.


### GetCurrency

`func (o *PaymentResponseDto) GetCurrency() string`

GetCurrency returns the Currency field if non-nil, zero value otherwise.

### GetCurrencyOk

`func (o *PaymentResponseDto) GetCurrencyOk() (*string, bool)`

GetCurrencyOk returns a tuple with the Currency field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCurrency

`func (o *PaymentResponseDto) SetCurrency(v string)`

SetCurrency sets Currency field to given value.


### GetStatus

`func (o *PaymentResponseDto) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *PaymentResponseDto) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *PaymentResponseDto) SetStatus(v string)`

SetStatus sets Status field to given value.


### GetTimestamp

`func (o *PaymentResponseDto) GetTimestamp() string`

GetTimestamp returns the Timestamp field if non-nil, zero value otherwise.

### GetTimestampOk

`func (o *PaymentResponseDto) GetTimestampOk() (*string, bool)`

GetTimestampOk returns a tuple with the Timestamp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTimestamp

`func (o *PaymentResponseDto) SetTimestamp(v string)`

SetTimestamp sets Timestamp field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


