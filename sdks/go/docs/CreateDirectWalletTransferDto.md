# CreateDirectWalletTransferDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**WalletId** | **string** | The ID of the bridge wallet to transfer from | 
**Network** | **string** | The network to use for the transfer | 
**StableCoinCurrency** | **string** | The stablecoin currency to use | 
**Amount** | **float32** | The amount to transfer | 

## Methods

### NewCreateDirectWalletTransferDto

`func NewCreateDirectWalletTransferDto(walletId string, network string, stableCoinCurrency string, amount float32, ) *CreateDirectWalletTransferDto`

NewCreateDirectWalletTransferDto instantiates a new CreateDirectWalletTransferDto object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateDirectWalletTransferDtoWithDefaults

`func NewCreateDirectWalletTransferDtoWithDefaults() *CreateDirectWalletTransferDto`

NewCreateDirectWalletTransferDtoWithDefaults instantiates a new CreateDirectWalletTransferDto object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetWalletId

`func (o *CreateDirectWalletTransferDto) GetWalletId() string`

GetWalletId returns the WalletId field if non-nil, zero value otherwise.

### GetWalletIdOk

`func (o *CreateDirectWalletTransferDto) GetWalletIdOk() (*string, bool)`

GetWalletIdOk returns a tuple with the WalletId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWalletId

`func (o *CreateDirectWalletTransferDto) SetWalletId(v string)`

SetWalletId sets WalletId field to given value.


### GetNetwork

`func (o *CreateDirectWalletTransferDto) GetNetwork() string`

GetNetwork returns the Network field if non-nil, zero value otherwise.

### GetNetworkOk

`func (o *CreateDirectWalletTransferDto) GetNetworkOk() (*string, bool)`

GetNetworkOk returns a tuple with the Network field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNetwork

`func (o *CreateDirectWalletTransferDto) SetNetwork(v string)`

SetNetwork sets Network field to given value.


### GetStableCoinCurrency

`func (o *CreateDirectWalletTransferDto) GetStableCoinCurrency() string`

GetStableCoinCurrency returns the StableCoinCurrency field if non-nil, zero value otherwise.

### GetStableCoinCurrencyOk

`func (o *CreateDirectWalletTransferDto) GetStableCoinCurrencyOk() (*string, bool)`

GetStableCoinCurrencyOk returns a tuple with the StableCoinCurrency field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStableCoinCurrency

`func (o *CreateDirectWalletTransferDto) SetStableCoinCurrency(v string)`

SetStableCoinCurrency sets StableCoinCurrency field to given value.


### GetAmount

`func (o *CreateDirectWalletTransferDto) GetAmount() float32`

GetAmount returns the Amount field if non-nil, zero value otherwise.

### GetAmountOk

`func (o *CreateDirectWalletTransferDto) GetAmountOk() (*float32, bool)`

GetAmountOk returns a tuple with the Amount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAmount

`func (o *CreateDirectWalletTransferDto) SetAmount(v float32)`

SetAmount sets Amount field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


