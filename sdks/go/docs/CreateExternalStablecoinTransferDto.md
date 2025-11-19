# CreateExternalStablecoinTransferDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**SourceWalletId** | **string** | The ID of the source bridge wallet | 
**SourceCurrency** | **string** | The source currency | 
**DestinationCurrency** | **string** | The destination currency | 
**BlockchainMemo** | Pointer to **string** | Blockchain memo for the transfer | [optional] 
**BeneficiaryId** | **string** | Beneficiary ID for the stablecoin transfer | 
**Amount** | Pointer to **float32** | The amount to transfer | [optional] 

## Methods

### NewCreateExternalStablecoinTransferDto

`func NewCreateExternalStablecoinTransferDto(sourceWalletId string, sourceCurrency string, destinationCurrency string, beneficiaryId string, ) *CreateExternalStablecoinTransferDto`

NewCreateExternalStablecoinTransferDto instantiates a new CreateExternalStablecoinTransferDto object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateExternalStablecoinTransferDtoWithDefaults

`func NewCreateExternalStablecoinTransferDtoWithDefaults() *CreateExternalStablecoinTransferDto`

NewCreateExternalStablecoinTransferDtoWithDefaults instantiates a new CreateExternalStablecoinTransferDto object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSourceWalletId

`func (o *CreateExternalStablecoinTransferDto) GetSourceWalletId() string`

GetSourceWalletId returns the SourceWalletId field if non-nil, zero value otherwise.

### GetSourceWalletIdOk

`func (o *CreateExternalStablecoinTransferDto) GetSourceWalletIdOk() (*string, bool)`

GetSourceWalletIdOk returns a tuple with the SourceWalletId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSourceWalletId

`func (o *CreateExternalStablecoinTransferDto) SetSourceWalletId(v string)`

SetSourceWalletId sets SourceWalletId field to given value.


### GetSourceCurrency

`func (o *CreateExternalStablecoinTransferDto) GetSourceCurrency() string`

GetSourceCurrency returns the SourceCurrency field if non-nil, zero value otherwise.

### GetSourceCurrencyOk

`func (o *CreateExternalStablecoinTransferDto) GetSourceCurrencyOk() (*string, bool)`

GetSourceCurrencyOk returns a tuple with the SourceCurrency field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSourceCurrency

`func (o *CreateExternalStablecoinTransferDto) SetSourceCurrency(v string)`

SetSourceCurrency sets SourceCurrency field to given value.


### GetDestinationCurrency

`func (o *CreateExternalStablecoinTransferDto) GetDestinationCurrency() string`

GetDestinationCurrency returns the DestinationCurrency field if non-nil, zero value otherwise.

### GetDestinationCurrencyOk

`func (o *CreateExternalStablecoinTransferDto) GetDestinationCurrencyOk() (*string, bool)`

GetDestinationCurrencyOk returns a tuple with the DestinationCurrency field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDestinationCurrency

`func (o *CreateExternalStablecoinTransferDto) SetDestinationCurrency(v string)`

SetDestinationCurrency sets DestinationCurrency field to given value.


### GetBlockchainMemo

`func (o *CreateExternalStablecoinTransferDto) GetBlockchainMemo() string`

GetBlockchainMemo returns the BlockchainMemo field if non-nil, zero value otherwise.

### GetBlockchainMemoOk

`func (o *CreateExternalStablecoinTransferDto) GetBlockchainMemoOk() (*string, bool)`

GetBlockchainMemoOk returns a tuple with the BlockchainMemo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBlockchainMemo

`func (o *CreateExternalStablecoinTransferDto) SetBlockchainMemo(v string)`

SetBlockchainMemo sets BlockchainMemo field to given value.

### HasBlockchainMemo

`func (o *CreateExternalStablecoinTransferDto) HasBlockchainMemo() bool`

HasBlockchainMemo returns a boolean if a field has been set.

### GetBeneficiaryId

`func (o *CreateExternalStablecoinTransferDto) GetBeneficiaryId() string`

GetBeneficiaryId returns the BeneficiaryId field if non-nil, zero value otherwise.

### GetBeneficiaryIdOk

`func (o *CreateExternalStablecoinTransferDto) GetBeneficiaryIdOk() (*string, bool)`

GetBeneficiaryIdOk returns a tuple with the BeneficiaryId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBeneficiaryId

`func (o *CreateExternalStablecoinTransferDto) SetBeneficiaryId(v string)`

SetBeneficiaryId sets BeneficiaryId field to given value.


### GetAmount

`func (o *CreateExternalStablecoinTransferDto) GetAmount() float32`

GetAmount returns the Amount field if non-nil, zero value otherwise.

### GetAmountOk

`func (o *CreateExternalStablecoinTransferDto) GetAmountOk() (*float32, bool)`

GetAmountOk returns a tuple with the Amount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAmount

`func (o *CreateExternalStablecoinTransferDto) SetAmount(v float32)`

SetAmount sets Amount field to given value.

### HasAmount

`func (o *CreateExternalStablecoinTransferDto) HasAmount() bool`

HasAmount returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


