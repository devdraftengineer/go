# RefundResponseDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | Refund ID | 
**PaymentId** | **string** | Original payment ID | 
**Amount** | **float32** | The amount refunded | 
**Status** | **string** | Refund status | 
**Timestamp** | **string** | Timestamp of the refund | 

## Methods

### NewRefundResponseDto

`func NewRefundResponseDto(id string, paymentId string, amount float32, status string, timestamp string, ) *RefundResponseDto`

NewRefundResponseDto instantiates a new RefundResponseDto object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRefundResponseDtoWithDefaults

`func NewRefundResponseDtoWithDefaults() *RefundResponseDto`

NewRefundResponseDtoWithDefaults instantiates a new RefundResponseDto object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *RefundResponseDto) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *RefundResponseDto) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *RefundResponseDto) SetId(v string)`

SetId sets Id field to given value.


### GetPaymentId

`func (o *RefundResponseDto) GetPaymentId() string`

GetPaymentId returns the PaymentId field if non-nil, zero value otherwise.

### GetPaymentIdOk

`func (o *RefundResponseDto) GetPaymentIdOk() (*string, bool)`

GetPaymentIdOk returns a tuple with the PaymentId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPaymentId

`func (o *RefundResponseDto) SetPaymentId(v string)`

SetPaymentId sets PaymentId field to given value.


### GetAmount

`func (o *RefundResponseDto) GetAmount() float32`

GetAmount returns the Amount field if non-nil, zero value otherwise.

### GetAmountOk

`func (o *RefundResponseDto) GetAmountOk() (*float32, bool)`

GetAmountOk returns a tuple with the Amount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAmount

`func (o *RefundResponseDto) SetAmount(v float32)`

SetAmount sets Amount field to given value.


### GetStatus

`func (o *RefundResponseDto) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *RefundResponseDto) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *RefundResponseDto) SetStatus(v string)`

SetStatus sets Status field to given value.


### GetTimestamp

`func (o *RefundResponseDto) GetTimestamp() string`

GetTimestamp returns the Timestamp field if non-nil, zero value otherwise.

### GetTimestampOk

`func (o *RefundResponseDto) GetTimestampOk() (*string, bool)`

GetTimestampOk returns a tuple with the Timestamp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTimestamp

`func (o *RefundResponseDto) SetTimestamp(v string)`

SetTimestamp sets Timestamp field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


