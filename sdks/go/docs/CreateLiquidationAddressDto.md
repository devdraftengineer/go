# CreateLiquidationAddressDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Chain** | **string** | The blockchain chain for the liquidation address | 
**Currency** | **string** | The currency for the liquidation address | 
**Address** | **string** | The liquidation address on the blockchain | 
**ExternalAccountId** | Pointer to **string** | External bank account to send funds to | [optional] 
**PrefundedAccountId** | Pointer to **string** | Developer&#39;s prefunded account id | [optional] 
**BridgeWalletId** | Pointer to **string** | Bridge Wallet to send funds to | [optional] 
**DestinationPaymentRail** | Pointer to [**BridgePaymentRail**](BridgePaymentRail.md) | Payment rail for sending funds | [optional] [default to ACH]
**DestinationCurrency** | Pointer to [**DestinationCurrency**](DestinationCurrency.md) | Currency for sending funds | [optional] [default to USD]
**DestinationWireMessage** | Pointer to **string** | Message for wire transfers | [optional] 
**DestinationSepaReference** | Pointer to **string** | Reference for SEPA transactions | [optional] 
**DestinationAchReference** | Pointer to **string** | Reference for ACH transactions | [optional] 
**DestinationAddress** | Pointer to **string** | Crypto wallet address for crypto transfers | [optional] 
**DestinationBlockchainMemo** | Pointer to **string** | Memo for blockchain transactions | [optional] 
**ReturnAddress** | Pointer to **string** | Address to return funds on failed transactions (Not supported on Stellar) | [optional] 
**CustomDeveloperFeePercent** | Pointer to **string** | Custom developer fee percentage (Base 100 percentage: 10.2% &#x3D; \&quot;10.2\&quot;) | [optional] 

## Methods

### NewCreateLiquidationAddressDto

`func NewCreateLiquidationAddressDto(chain string, currency string, address string, ) *CreateLiquidationAddressDto`

NewCreateLiquidationAddressDto instantiates a new CreateLiquidationAddressDto object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateLiquidationAddressDtoWithDefaults

`func NewCreateLiquidationAddressDtoWithDefaults() *CreateLiquidationAddressDto`

NewCreateLiquidationAddressDtoWithDefaults instantiates a new CreateLiquidationAddressDto object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetChain

`func (o *CreateLiquidationAddressDto) GetChain() string`

GetChain returns the Chain field if non-nil, zero value otherwise.

### GetChainOk

`func (o *CreateLiquidationAddressDto) GetChainOk() (*string, bool)`

GetChainOk returns a tuple with the Chain field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChain

`func (o *CreateLiquidationAddressDto) SetChain(v string)`

SetChain sets Chain field to given value.


### GetCurrency

`func (o *CreateLiquidationAddressDto) GetCurrency() string`

GetCurrency returns the Currency field if non-nil, zero value otherwise.

### GetCurrencyOk

`func (o *CreateLiquidationAddressDto) GetCurrencyOk() (*string, bool)`

GetCurrencyOk returns a tuple with the Currency field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCurrency

`func (o *CreateLiquidationAddressDto) SetCurrency(v string)`

SetCurrency sets Currency field to given value.


### GetAddress

`func (o *CreateLiquidationAddressDto) GetAddress() string`

GetAddress returns the Address field if non-nil, zero value otherwise.

### GetAddressOk

`func (o *CreateLiquidationAddressDto) GetAddressOk() (*string, bool)`

GetAddressOk returns a tuple with the Address field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAddress

`func (o *CreateLiquidationAddressDto) SetAddress(v string)`

SetAddress sets Address field to given value.


### GetExternalAccountId

`func (o *CreateLiquidationAddressDto) GetExternalAccountId() string`

GetExternalAccountId returns the ExternalAccountId field if non-nil, zero value otherwise.

### GetExternalAccountIdOk

`func (o *CreateLiquidationAddressDto) GetExternalAccountIdOk() (*string, bool)`

GetExternalAccountIdOk returns a tuple with the ExternalAccountId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExternalAccountId

`func (o *CreateLiquidationAddressDto) SetExternalAccountId(v string)`

SetExternalAccountId sets ExternalAccountId field to given value.

### HasExternalAccountId

`func (o *CreateLiquidationAddressDto) HasExternalAccountId() bool`

HasExternalAccountId returns a boolean if a field has been set.

### GetPrefundedAccountId

`func (o *CreateLiquidationAddressDto) GetPrefundedAccountId() string`

GetPrefundedAccountId returns the PrefundedAccountId field if non-nil, zero value otherwise.

### GetPrefundedAccountIdOk

`func (o *CreateLiquidationAddressDto) GetPrefundedAccountIdOk() (*string, bool)`

GetPrefundedAccountIdOk returns a tuple with the PrefundedAccountId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrefundedAccountId

`func (o *CreateLiquidationAddressDto) SetPrefundedAccountId(v string)`

SetPrefundedAccountId sets PrefundedAccountId field to given value.

### HasPrefundedAccountId

`func (o *CreateLiquidationAddressDto) HasPrefundedAccountId() bool`

HasPrefundedAccountId returns a boolean if a field has been set.

### GetBridgeWalletId

`func (o *CreateLiquidationAddressDto) GetBridgeWalletId() string`

GetBridgeWalletId returns the BridgeWalletId field if non-nil, zero value otherwise.

### GetBridgeWalletIdOk

`func (o *CreateLiquidationAddressDto) GetBridgeWalletIdOk() (*string, bool)`

GetBridgeWalletIdOk returns a tuple with the BridgeWalletId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBridgeWalletId

`func (o *CreateLiquidationAddressDto) SetBridgeWalletId(v string)`

SetBridgeWalletId sets BridgeWalletId field to given value.

### HasBridgeWalletId

`func (o *CreateLiquidationAddressDto) HasBridgeWalletId() bool`

HasBridgeWalletId returns a boolean if a field has been set.

### GetDestinationPaymentRail

`func (o *CreateLiquidationAddressDto) GetDestinationPaymentRail() BridgePaymentRail`

GetDestinationPaymentRail returns the DestinationPaymentRail field if non-nil, zero value otherwise.

### GetDestinationPaymentRailOk

`func (o *CreateLiquidationAddressDto) GetDestinationPaymentRailOk() (*BridgePaymentRail, bool)`

GetDestinationPaymentRailOk returns a tuple with the DestinationPaymentRail field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDestinationPaymentRail

`func (o *CreateLiquidationAddressDto) SetDestinationPaymentRail(v BridgePaymentRail)`

SetDestinationPaymentRail sets DestinationPaymentRail field to given value.

### HasDestinationPaymentRail

`func (o *CreateLiquidationAddressDto) HasDestinationPaymentRail() bool`

HasDestinationPaymentRail returns a boolean if a field has been set.

### GetDestinationCurrency

`func (o *CreateLiquidationAddressDto) GetDestinationCurrency() DestinationCurrency`

GetDestinationCurrency returns the DestinationCurrency field if non-nil, zero value otherwise.

### GetDestinationCurrencyOk

`func (o *CreateLiquidationAddressDto) GetDestinationCurrencyOk() (*DestinationCurrency, bool)`

GetDestinationCurrencyOk returns a tuple with the DestinationCurrency field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDestinationCurrency

`func (o *CreateLiquidationAddressDto) SetDestinationCurrency(v DestinationCurrency)`

SetDestinationCurrency sets DestinationCurrency field to given value.

### HasDestinationCurrency

`func (o *CreateLiquidationAddressDto) HasDestinationCurrency() bool`

HasDestinationCurrency returns a boolean if a field has been set.

### GetDestinationWireMessage

`func (o *CreateLiquidationAddressDto) GetDestinationWireMessage() string`

GetDestinationWireMessage returns the DestinationWireMessage field if non-nil, zero value otherwise.

### GetDestinationWireMessageOk

`func (o *CreateLiquidationAddressDto) GetDestinationWireMessageOk() (*string, bool)`

GetDestinationWireMessageOk returns a tuple with the DestinationWireMessage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDestinationWireMessage

`func (o *CreateLiquidationAddressDto) SetDestinationWireMessage(v string)`

SetDestinationWireMessage sets DestinationWireMessage field to given value.

### HasDestinationWireMessage

`func (o *CreateLiquidationAddressDto) HasDestinationWireMessage() bool`

HasDestinationWireMessage returns a boolean if a field has been set.

### GetDestinationSepaReference

`func (o *CreateLiquidationAddressDto) GetDestinationSepaReference() string`

GetDestinationSepaReference returns the DestinationSepaReference field if non-nil, zero value otherwise.

### GetDestinationSepaReferenceOk

`func (o *CreateLiquidationAddressDto) GetDestinationSepaReferenceOk() (*string, bool)`

GetDestinationSepaReferenceOk returns a tuple with the DestinationSepaReference field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDestinationSepaReference

`func (o *CreateLiquidationAddressDto) SetDestinationSepaReference(v string)`

SetDestinationSepaReference sets DestinationSepaReference field to given value.

### HasDestinationSepaReference

`func (o *CreateLiquidationAddressDto) HasDestinationSepaReference() bool`

HasDestinationSepaReference returns a boolean if a field has been set.

### GetDestinationAchReference

`func (o *CreateLiquidationAddressDto) GetDestinationAchReference() string`

GetDestinationAchReference returns the DestinationAchReference field if non-nil, zero value otherwise.

### GetDestinationAchReferenceOk

`func (o *CreateLiquidationAddressDto) GetDestinationAchReferenceOk() (*string, bool)`

GetDestinationAchReferenceOk returns a tuple with the DestinationAchReference field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDestinationAchReference

`func (o *CreateLiquidationAddressDto) SetDestinationAchReference(v string)`

SetDestinationAchReference sets DestinationAchReference field to given value.

### HasDestinationAchReference

`func (o *CreateLiquidationAddressDto) HasDestinationAchReference() bool`

HasDestinationAchReference returns a boolean if a field has been set.

### GetDestinationAddress

`func (o *CreateLiquidationAddressDto) GetDestinationAddress() string`

GetDestinationAddress returns the DestinationAddress field if non-nil, zero value otherwise.

### GetDestinationAddressOk

`func (o *CreateLiquidationAddressDto) GetDestinationAddressOk() (*string, bool)`

GetDestinationAddressOk returns a tuple with the DestinationAddress field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDestinationAddress

`func (o *CreateLiquidationAddressDto) SetDestinationAddress(v string)`

SetDestinationAddress sets DestinationAddress field to given value.

### HasDestinationAddress

`func (o *CreateLiquidationAddressDto) HasDestinationAddress() bool`

HasDestinationAddress returns a boolean if a field has been set.

### GetDestinationBlockchainMemo

`func (o *CreateLiquidationAddressDto) GetDestinationBlockchainMemo() string`

GetDestinationBlockchainMemo returns the DestinationBlockchainMemo field if non-nil, zero value otherwise.

### GetDestinationBlockchainMemoOk

`func (o *CreateLiquidationAddressDto) GetDestinationBlockchainMemoOk() (*string, bool)`

GetDestinationBlockchainMemoOk returns a tuple with the DestinationBlockchainMemo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDestinationBlockchainMemo

`func (o *CreateLiquidationAddressDto) SetDestinationBlockchainMemo(v string)`

SetDestinationBlockchainMemo sets DestinationBlockchainMemo field to given value.

### HasDestinationBlockchainMemo

`func (o *CreateLiquidationAddressDto) HasDestinationBlockchainMemo() bool`

HasDestinationBlockchainMemo returns a boolean if a field has been set.

### GetReturnAddress

`func (o *CreateLiquidationAddressDto) GetReturnAddress() string`

GetReturnAddress returns the ReturnAddress field if non-nil, zero value otherwise.

### GetReturnAddressOk

`func (o *CreateLiquidationAddressDto) GetReturnAddressOk() (*string, bool)`

GetReturnAddressOk returns a tuple with the ReturnAddress field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReturnAddress

`func (o *CreateLiquidationAddressDto) SetReturnAddress(v string)`

SetReturnAddress sets ReturnAddress field to given value.

### HasReturnAddress

`func (o *CreateLiquidationAddressDto) HasReturnAddress() bool`

HasReturnAddress returns a boolean if a field has been set.

### GetCustomDeveloperFeePercent

`func (o *CreateLiquidationAddressDto) GetCustomDeveloperFeePercent() string`

GetCustomDeveloperFeePercent returns the CustomDeveloperFeePercent field if non-nil, zero value otherwise.

### GetCustomDeveloperFeePercentOk

`func (o *CreateLiquidationAddressDto) GetCustomDeveloperFeePercentOk() (*string, bool)`

GetCustomDeveloperFeePercentOk returns a tuple with the CustomDeveloperFeePercent field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomDeveloperFeePercent

`func (o *CreateLiquidationAddressDto) SetCustomDeveloperFeePercent(v string)`

SetCustomDeveloperFeePercent sets CustomDeveloperFeePercent field to given value.

### HasCustomDeveloperFeePercent

`func (o *CreateLiquidationAddressDto) HasCustomDeveloperFeePercent() bool`

HasCustomDeveloperFeePercent returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


