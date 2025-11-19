# CreateExternalBankTransferDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**SourceWalletId** | **string** | The ID of the source bridge wallet | 
**SourceCurrency** | **string** | The source currency | 
**DestinationCurrency** | **string** | The destination currency | 
**DestinationPaymentRail** | [**BridgeFiatPaymentRail**](BridgeFiatPaymentRail.md) | The destination payment rail (fiat payment method) | 
**ExternalAccountId** | **string** | The external account ID for the bank transfer | 
**Amount** | Pointer to **float32** | The amount to transfer | [optional] 
**WireMessage** | Pointer to **string** | Wire transfer message (1-256 characters, only for wire transfers) | [optional] 
**SepaReference** | Pointer to **string** | SEPA reference message (6-140 characters, only for SEPA transfers) | [optional] 
**SwiftReference** | Pointer to **string** | SWIFT reference message (1-190 characters, only for SWIFT transfers) | [optional] 
**SpeiReference** | Pointer to **string** | SPEI reference message (1-40 characters, only for SPEI transfers) | [optional] 
**SwiftCharges** | Pointer to **string** | SWIFT charges bearer (only for SWIFT transfers) | [optional] 
**AchReference** | Pointer to **string** | ACH reference message (1-10 characters, only for ACH transfers) | [optional] 

## Methods

### NewCreateExternalBankTransferDto

`func NewCreateExternalBankTransferDto(sourceWalletId string, sourceCurrency string, destinationCurrency string, destinationPaymentRail BridgeFiatPaymentRail, externalAccountId string, ) *CreateExternalBankTransferDto`

NewCreateExternalBankTransferDto instantiates a new CreateExternalBankTransferDto object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateExternalBankTransferDtoWithDefaults

`func NewCreateExternalBankTransferDtoWithDefaults() *CreateExternalBankTransferDto`

NewCreateExternalBankTransferDtoWithDefaults instantiates a new CreateExternalBankTransferDto object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSourceWalletId

`func (o *CreateExternalBankTransferDto) GetSourceWalletId() string`

GetSourceWalletId returns the SourceWalletId field if non-nil, zero value otherwise.

### GetSourceWalletIdOk

`func (o *CreateExternalBankTransferDto) GetSourceWalletIdOk() (*string, bool)`

GetSourceWalletIdOk returns a tuple with the SourceWalletId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSourceWalletId

`func (o *CreateExternalBankTransferDto) SetSourceWalletId(v string)`

SetSourceWalletId sets SourceWalletId field to given value.


### GetSourceCurrency

`func (o *CreateExternalBankTransferDto) GetSourceCurrency() string`

GetSourceCurrency returns the SourceCurrency field if non-nil, zero value otherwise.

### GetSourceCurrencyOk

`func (o *CreateExternalBankTransferDto) GetSourceCurrencyOk() (*string, bool)`

GetSourceCurrencyOk returns a tuple with the SourceCurrency field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSourceCurrency

`func (o *CreateExternalBankTransferDto) SetSourceCurrency(v string)`

SetSourceCurrency sets SourceCurrency field to given value.


### GetDestinationCurrency

`func (o *CreateExternalBankTransferDto) GetDestinationCurrency() string`

GetDestinationCurrency returns the DestinationCurrency field if non-nil, zero value otherwise.

### GetDestinationCurrencyOk

`func (o *CreateExternalBankTransferDto) GetDestinationCurrencyOk() (*string, bool)`

GetDestinationCurrencyOk returns a tuple with the DestinationCurrency field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDestinationCurrency

`func (o *CreateExternalBankTransferDto) SetDestinationCurrency(v string)`

SetDestinationCurrency sets DestinationCurrency field to given value.


### GetDestinationPaymentRail

`func (o *CreateExternalBankTransferDto) GetDestinationPaymentRail() BridgeFiatPaymentRail`

GetDestinationPaymentRail returns the DestinationPaymentRail field if non-nil, zero value otherwise.

### GetDestinationPaymentRailOk

`func (o *CreateExternalBankTransferDto) GetDestinationPaymentRailOk() (*BridgeFiatPaymentRail, bool)`

GetDestinationPaymentRailOk returns a tuple with the DestinationPaymentRail field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDestinationPaymentRail

`func (o *CreateExternalBankTransferDto) SetDestinationPaymentRail(v BridgeFiatPaymentRail)`

SetDestinationPaymentRail sets DestinationPaymentRail field to given value.


### GetExternalAccountId

`func (o *CreateExternalBankTransferDto) GetExternalAccountId() string`

GetExternalAccountId returns the ExternalAccountId field if non-nil, zero value otherwise.

### GetExternalAccountIdOk

`func (o *CreateExternalBankTransferDto) GetExternalAccountIdOk() (*string, bool)`

GetExternalAccountIdOk returns a tuple with the ExternalAccountId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExternalAccountId

`func (o *CreateExternalBankTransferDto) SetExternalAccountId(v string)`

SetExternalAccountId sets ExternalAccountId field to given value.


### GetAmount

`func (o *CreateExternalBankTransferDto) GetAmount() float32`

GetAmount returns the Amount field if non-nil, zero value otherwise.

### GetAmountOk

`func (o *CreateExternalBankTransferDto) GetAmountOk() (*float32, bool)`

GetAmountOk returns a tuple with the Amount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAmount

`func (o *CreateExternalBankTransferDto) SetAmount(v float32)`

SetAmount sets Amount field to given value.

### HasAmount

`func (o *CreateExternalBankTransferDto) HasAmount() bool`

HasAmount returns a boolean if a field has been set.

### GetWireMessage

`func (o *CreateExternalBankTransferDto) GetWireMessage() string`

GetWireMessage returns the WireMessage field if non-nil, zero value otherwise.

### GetWireMessageOk

`func (o *CreateExternalBankTransferDto) GetWireMessageOk() (*string, bool)`

GetWireMessageOk returns a tuple with the WireMessage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWireMessage

`func (o *CreateExternalBankTransferDto) SetWireMessage(v string)`

SetWireMessage sets WireMessage field to given value.

### HasWireMessage

`func (o *CreateExternalBankTransferDto) HasWireMessage() bool`

HasWireMessage returns a boolean if a field has been set.

### GetSepaReference

`func (o *CreateExternalBankTransferDto) GetSepaReference() string`

GetSepaReference returns the SepaReference field if non-nil, zero value otherwise.

### GetSepaReferenceOk

`func (o *CreateExternalBankTransferDto) GetSepaReferenceOk() (*string, bool)`

GetSepaReferenceOk returns a tuple with the SepaReference field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSepaReference

`func (o *CreateExternalBankTransferDto) SetSepaReference(v string)`

SetSepaReference sets SepaReference field to given value.

### HasSepaReference

`func (o *CreateExternalBankTransferDto) HasSepaReference() bool`

HasSepaReference returns a boolean if a field has been set.

### GetSwiftReference

`func (o *CreateExternalBankTransferDto) GetSwiftReference() string`

GetSwiftReference returns the SwiftReference field if non-nil, zero value otherwise.

### GetSwiftReferenceOk

`func (o *CreateExternalBankTransferDto) GetSwiftReferenceOk() (*string, bool)`

GetSwiftReferenceOk returns a tuple with the SwiftReference field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSwiftReference

`func (o *CreateExternalBankTransferDto) SetSwiftReference(v string)`

SetSwiftReference sets SwiftReference field to given value.

### HasSwiftReference

`func (o *CreateExternalBankTransferDto) HasSwiftReference() bool`

HasSwiftReference returns a boolean if a field has been set.

### GetSpeiReference

`func (o *CreateExternalBankTransferDto) GetSpeiReference() string`

GetSpeiReference returns the SpeiReference field if non-nil, zero value otherwise.

### GetSpeiReferenceOk

`func (o *CreateExternalBankTransferDto) GetSpeiReferenceOk() (*string, bool)`

GetSpeiReferenceOk returns a tuple with the SpeiReference field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpeiReference

`func (o *CreateExternalBankTransferDto) SetSpeiReference(v string)`

SetSpeiReference sets SpeiReference field to given value.

### HasSpeiReference

`func (o *CreateExternalBankTransferDto) HasSpeiReference() bool`

HasSpeiReference returns a boolean if a field has been set.

### GetSwiftCharges

`func (o *CreateExternalBankTransferDto) GetSwiftCharges() string`

GetSwiftCharges returns the SwiftCharges field if non-nil, zero value otherwise.

### GetSwiftChargesOk

`func (o *CreateExternalBankTransferDto) GetSwiftChargesOk() (*string, bool)`

GetSwiftChargesOk returns a tuple with the SwiftCharges field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSwiftCharges

`func (o *CreateExternalBankTransferDto) SetSwiftCharges(v string)`

SetSwiftCharges sets SwiftCharges field to given value.

### HasSwiftCharges

`func (o *CreateExternalBankTransferDto) HasSwiftCharges() bool`

HasSwiftCharges returns a boolean if a field has been set.

### GetAchReference

`func (o *CreateExternalBankTransferDto) GetAchReference() string`

GetAchReference returns the AchReference field if non-nil, zero value otherwise.

### GetAchReferenceOk

`func (o *CreateExternalBankTransferDto) GetAchReferenceOk() (*string, bool)`

GetAchReferenceOk returns a tuple with the AchReference field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAchReference

`func (o *CreateExternalBankTransferDto) SetAchReference(v string)`

SetAchReference sets AchReference field to given value.

### HasAchReference

`func (o *CreateExternalBankTransferDto) HasAchReference() bool`

HasAchReference returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


