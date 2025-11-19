# CreateStablecoinConversionDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**WalletId** | **string** | The ID of the bridge wallet to use | 
**SourceNetwork** | **string** | The source network | 
**SourceCurrency** | **string** | The source currency | 
**DestinationCurrency** | **string** | The destination currency | 
**Amount** | **float32** | The amount to convert | 

## Methods

### NewCreateStablecoinConversionDto

`func NewCreateStablecoinConversionDto(walletId string, sourceNetwork string, sourceCurrency string, destinationCurrency string, amount float32, ) *CreateStablecoinConversionDto`

NewCreateStablecoinConversionDto instantiates a new CreateStablecoinConversionDto object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateStablecoinConversionDtoWithDefaults

`func NewCreateStablecoinConversionDtoWithDefaults() *CreateStablecoinConversionDto`

NewCreateStablecoinConversionDtoWithDefaults instantiates a new CreateStablecoinConversionDto object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetWalletId

`func (o *CreateStablecoinConversionDto) GetWalletId() string`

GetWalletId returns the WalletId field if non-nil, zero value otherwise.

### GetWalletIdOk

`func (o *CreateStablecoinConversionDto) GetWalletIdOk() (*string, bool)`

GetWalletIdOk returns a tuple with the WalletId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWalletId

`func (o *CreateStablecoinConversionDto) SetWalletId(v string)`

SetWalletId sets WalletId field to given value.


### GetSourceNetwork

`func (o *CreateStablecoinConversionDto) GetSourceNetwork() string`

GetSourceNetwork returns the SourceNetwork field if non-nil, zero value otherwise.

### GetSourceNetworkOk

`func (o *CreateStablecoinConversionDto) GetSourceNetworkOk() (*string, bool)`

GetSourceNetworkOk returns a tuple with the SourceNetwork field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSourceNetwork

`func (o *CreateStablecoinConversionDto) SetSourceNetwork(v string)`

SetSourceNetwork sets SourceNetwork field to given value.


### GetSourceCurrency

`func (o *CreateStablecoinConversionDto) GetSourceCurrency() string`

GetSourceCurrency returns the SourceCurrency field if non-nil, zero value otherwise.

### GetSourceCurrencyOk

`func (o *CreateStablecoinConversionDto) GetSourceCurrencyOk() (*string, bool)`

GetSourceCurrencyOk returns a tuple with the SourceCurrency field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSourceCurrency

`func (o *CreateStablecoinConversionDto) SetSourceCurrency(v string)`

SetSourceCurrency sets SourceCurrency field to given value.


### GetDestinationCurrency

`func (o *CreateStablecoinConversionDto) GetDestinationCurrency() string`

GetDestinationCurrency returns the DestinationCurrency field if non-nil, zero value otherwise.

### GetDestinationCurrencyOk

`func (o *CreateStablecoinConversionDto) GetDestinationCurrencyOk() (*string, bool)`

GetDestinationCurrencyOk returns a tuple with the DestinationCurrency field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDestinationCurrency

`func (o *CreateStablecoinConversionDto) SetDestinationCurrency(v string)`

SetDestinationCurrency sets DestinationCurrency field to given value.


### GetAmount

`func (o *CreateStablecoinConversionDto) GetAmount() float32`

GetAmount returns the Amount field if non-nil, zero value otherwise.

### GetAmountOk

`func (o *CreateStablecoinConversionDto) GetAmountOk() (*float32, bool)`

GetAmountOk returns a tuple with the Amount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAmount

`func (o *CreateStablecoinConversionDto) SetAmount(v float32)`

SetAmount sets Amount field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


