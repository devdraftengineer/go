# CreateDirectBankTransferDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**WalletId** | **string** | The ID of the bridge wallet to transfer from | 
**PaymentRail** | **string** | The payment rail to use | 
**DestinationCurrency** | **string** | The destination currency | 
**SourceCurrency** | **string** | The source currency | 
**Amount** | **float32** | The amount to transfer | 
**WireMessage** | Pointer to **string** | Wire transfer message | [optional] 
**SepaReference** | Pointer to **string** | SEPA transfer reference | [optional] 
**AchReference** | Pointer to **string** | ACH transfer reference | [optional] 

## Methods

### NewCreateDirectBankTransferDto

`func NewCreateDirectBankTransferDto(walletId string, paymentRail string, destinationCurrency string, sourceCurrency string, amount float32, ) *CreateDirectBankTransferDto`

NewCreateDirectBankTransferDto instantiates a new CreateDirectBankTransferDto object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateDirectBankTransferDtoWithDefaults

`func NewCreateDirectBankTransferDtoWithDefaults() *CreateDirectBankTransferDto`

NewCreateDirectBankTransferDtoWithDefaults instantiates a new CreateDirectBankTransferDto object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetWalletId

`func (o *CreateDirectBankTransferDto) GetWalletId() string`

GetWalletId returns the WalletId field if non-nil, zero value otherwise.

### GetWalletIdOk

`func (o *CreateDirectBankTransferDto) GetWalletIdOk() (*string, bool)`

GetWalletIdOk returns a tuple with the WalletId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWalletId

`func (o *CreateDirectBankTransferDto) SetWalletId(v string)`

SetWalletId sets WalletId field to given value.


### GetPaymentRail

`func (o *CreateDirectBankTransferDto) GetPaymentRail() string`

GetPaymentRail returns the PaymentRail field if non-nil, zero value otherwise.

### GetPaymentRailOk

`func (o *CreateDirectBankTransferDto) GetPaymentRailOk() (*string, bool)`

GetPaymentRailOk returns a tuple with the PaymentRail field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPaymentRail

`func (o *CreateDirectBankTransferDto) SetPaymentRail(v string)`

SetPaymentRail sets PaymentRail field to given value.


### GetDestinationCurrency

`func (o *CreateDirectBankTransferDto) GetDestinationCurrency() string`

GetDestinationCurrency returns the DestinationCurrency field if non-nil, zero value otherwise.

### GetDestinationCurrencyOk

`func (o *CreateDirectBankTransferDto) GetDestinationCurrencyOk() (*string, bool)`

GetDestinationCurrencyOk returns a tuple with the DestinationCurrency field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDestinationCurrency

`func (o *CreateDirectBankTransferDto) SetDestinationCurrency(v string)`

SetDestinationCurrency sets DestinationCurrency field to given value.


### GetSourceCurrency

`func (o *CreateDirectBankTransferDto) GetSourceCurrency() string`

GetSourceCurrency returns the SourceCurrency field if non-nil, zero value otherwise.

### GetSourceCurrencyOk

`func (o *CreateDirectBankTransferDto) GetSourceCurrencyOk() (*string, bool)`

GetSourceCurrencyOk returns a tuple with the SourceCurrency field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSourceCurrency

`func (o *CreateDirectBankTransferDto) SetSourceCurrency(v string)`

SetSourceCurrency sets SourceCurrency field to given value.


### GetAmount

`func (o *CreateDirectBankTransferDto) GetAmount() float32`

GetAmount returns the Amount field if non-nil, zero value otherwise.

### GetAmountOk

`func (o *CreateDirectBankTransferDto) GetAmountOk() (*float32, bool)`

GetAmountOk returns a tuple with the Amount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAmount

`func (o *CreateDirectBankTransferDto) SetAmount(v float32)`

SetAmount sets Amount field to given value.


### GetWireMessage

`func (o *CreateDirectBankTransferDto) GetWireMessage() string`

GetWireMessage returns the WireMessage field if non-nil, zero value otherwise.

### GetWireMessageOk

`func (o *CreateDirectBankTransferDto) GetWireMessageOk() (*string, bool)`

GetWireMessageOk returns a tuple with the WireMessage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWireMessage

`func (o *CreateDirectBankTransferDto) SetWireMessage(v string)`

SetWireMessage sets WireMessage field to given value.

### HasWireMessage

`func (o *CreateDirectBankTransferDto) HasWireMessage() bool`

HasWireMessage returns a boolean if a field has been set.

### GetSepaReference

`func (o *CreateDirectBankTransferDto) GetSepaReference() string`

GetSepaReference returns the SepaReference field if non-nil, zero value otherwise.

### GetSepaReferenceOk

`func (o *CreateDirectBankTransferDto) GetSepaReferenceOk() (*string, bool)`

GetSepaReferenceOk returns a tuple with the SepaReference field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSepaReference

`func (o *CreateDirectBankTransferDto) SetSepaReference(v string)`

SetSepaReference sets SepaReference field to given value.

### HasSepaReference

`func (o *CreateDirectBankTransferDto) HasSepaReference() bool`

HasSepaReference returns a boolean if a field has been set.

### GetAchReference

`func (o *CreateDirectBankTransferDto) GetAchReference() string`

GetAchReference returns the AchReference field if non-nil, zero value otherwise.

### GetAchReferenceOk

`func (o *CreateDirectBankTransferDto) GetAchReferenceOk() (*string, bool)`

GetAchReferenceOk returns a tuple with the AchReference field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAchReference

`func (o *CreateDirectBankTransferDto) SetAchReference(v string)`

SetAchReference sets AchReference field to given value.

### HasAchReference

`func (o *CreateDirectBankTransferDto) HasAchReference() bool`

HasAchReference returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


