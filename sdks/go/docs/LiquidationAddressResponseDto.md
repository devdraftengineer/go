# LiquidationAddressResponseDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | Unique identifier for the liquidation address | 
**State** | **string** | Current state of the liquidation address | 
**CustomerId** | **string** | Customer ID this liquidation address belongs to | 
**Chain** | **string** | Blockchain chain | 
**Currency** | **string** | Currency | 
**Address** | **string** | Liquidation address | 
**ExternalAccountId** | Pointer to **string** | External account ID | [optional] 
**PrefundedAccountId** | Pointer to **string** | Prefunded account ID | [optional] 
**BridgeWalletId** | Pointer to **string** | Bridge wallet ID | [optional] 
**DestinationPaymentRail** | Pointer to **string** | Destination payment rail | [optional] 
**DestinationCurrency** | Pointer to **string** | Destination currency | [optional] 
**CustomDeveloperFeePercent** | Pointer to **string** | Custom developer fee percent | [optional] 
**CreatedAt** | **string** | Creation timestamp | 
**UpdatedAt** | **string** | Last update timestamp | 

## Methods

### NewLiquidationAddressResponseDto

`func NewLiquidationAddressResponseDto(id string, state string, customerId string, chain string, currency string, address string, createdAt string, updatedAt string, ) *LiquidationAddressResponseDto`

NewLiquidationAddressResponseDto instantiates a new LiquidationAddressResponseDto object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewLiquidationAddressResponseDtoWithDefaults

`func NewLiquidationAddressResponseDtoWithDefaults() *LiquidationAddressResponseDto`

NewLiquidationAddressResponseDtoWithDefaults instantiates a new LiquidationAddressResponseDto object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *LiquidationAddressResponseDto) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *LiquidationAddressResponseDto) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *LiquidationAddressResponseDto) SetId(v string)`

SetId sets Id field to given value.


### GetState

`func (o *LiquidationAddressResponseDto) GetState() string`

GetState returns the State field if non-nil, zero value otherwise.

### GetStateOk

`func (o *LiquidationAddressResponseDto) GetStateOk() (*string, bool)`

GetStateOk returns a tuple with the State field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetState

`func (o *LiquidationAddressResponseDto) SetState(v string)`

SetState sets State field to given value.


### GetCustomerId

`func (o *LiquidationAddressResponseDto) GetCustomerId() string`

GetCustomerId returns the CustomerId field if non-nil, zero value otherwise.

### GetCustomerIdOk

`func (o *LiquidationAddressResponseDto) GetCustomerIdOk() (*string, bool)`

GetCustomerIdOk returns a tuple with the CustomerId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomerId

`func (o *LiquidationAddressResponseDto) SetCustomerId(v string)`

SetCustomerId sets CustomerId field to given value.


### GetChain

`func (o *LiquidationAddressResponseDto) GetChain() string`

GetChain returns the Chain field if non-nil, zero value otherwise.

### GetChainOk

`func (o *LiquidationAddressResponseDto) GetChainOk() (*string, bool)`

GetChainOk returns a tuple with the Chain field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChain

`func (o *LiquidationAddressResponseDto) SetChain(v string)`

SetChain sets Chain field to given value.


### GetCurrency

`func (o *LiquidationAddressResponseDto) GetCurrency() string`

GetCurrency returns the Currency field if non-nil, zero value otherwise.

### GetCurrencyOk

`func (o *LiquidationAddressResponseDto) GetCurrencyOk() (*string, bool)`

GetCurrencyOk returns a tuple with the Currency field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCurrency

`func (o *LiquidationAddressResponseDto) SetCurrency(v string)`

SetCurrency sets Currency field to given value.


### GetAddress

`func (o *LiquidationAddressResponseDto) GetAddress() string`

GetAddress returns the Address field if non-nil, zero value otherwise.

### GetAddressOk

`func (o *LiquidationAddressResponseDto) GetAddressOk() (*string, bool)`

GetAddressOk returns a tuple with the Address field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAddress

`func (o *LiquidationAddressResponseDto) SetAddress(v string)`

SetAddress sets Address field to given value.


### GetExternalAccountId

`func (o *LiquidationAddressResponseDto) GetExternalAccountId() string`

GetExternalAccountId returns the ExternalAccountId field if non-nil, zero value otherwise.

### GetExternalAccountIdOk

`func (o *LiquidationAddressResponseDto) GetExternalAccountIdOk() (*string, bool)`

GetExternalAccountIdOk returns a tuple with the ExternalAccountId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExternalAccountId

`func (o *LiquidationAddressResponseDto) SetExternalAccountId(v string)`

SetExternalAccountId sets ExternalAccountId field to given value.

### HasExternalAccountId

`func (o *LiquidationAddressResponseDto) HasExternalAccountId() bool`

HasExternalAccountId returns a boolean if a field has been set.

### GetPrefundedAccountId

`func (o *LiquidationAddressResponseDto) GetPrefundedAccountId() string`

GetPrefundedAccountId returns the PrefundedAccountId field if non-nil, zero value otherwise.

### GetPrefundedAccountIdOk

`func (o *LiquidationAddressResponseDto) GetPrefundedAccountIdOk() (*string, bool)`

GetPrefundedAccountIdOk returns a tuple with the PrefundedAccountId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrefundedAccountId

`func (o *LiquidationAddressResponseDto) SetPrefundedAccountId(v string)`

SetPrefundedAccountId sets PrefundedAccountId field to given value.

### HasPrefundedAccountId

`func (o *LiquidationAddressResponseDto) HasPrefundedAccountId() bool`

HasPrefundedAccountId returns a boolean if a field has been set.

### GetBridgeWalletId

`func (o *LiquidationAddressResponseDto) GetBridgeWalletId() string`

GetBridgeWalletId returns the BridgeWalletId field if non-nil, zero value otherwise.

### GetBridgeWalletIdOk

`func (o *LiquidationAddressResponseDto) GetBridgeWalletIdOk() (*string, bool)`

GetBridgeWalletIdOk returns a tuple with the BridgeWalletId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBridgeWalletId

`func (o *LiquidationAddressResponseDto) SetBridgeWalletId(v string)`

SetBridgeWalletId sets BridgeWalletId field to given value.

### HasBridgeWalletId

`func (o *LiquidationAddressResponseDto) HasBridgeWalletId() bool`

HasBridgeWalletId returns a boolean if a field has been set.

### GetDestinationPaymentRail

`func (o *LiquidationAddressResponseDto) GetDestinationPaymentRail() string`

GetDestinationPaymentRail returns the DestinationPaymentRail field if non-nil, zero value otherwise.

### GetDestinationPaymentRailOk

`func (o *LiquidationAddressResponseDto) GetDestinationPaymentRailOk() (*string, bool)`

GetDestinationPaymentRailOk returns a tuple with the DestinationPaymentRail field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDestinationPaymentRail

`func (o *LiquidationAddressResponseDto) SetDestinationPaymentRail(v string)`

SetDestinationPaymentRail sets DestinationPaymentRail field to given value.

### HasDestinationPaymentRail

`func (o *LiquidationAddressResponseDto) HasDestinationPaymentRail() bool`

HasDestinationPaymentRail returns a boolean if a field has been set.

### GetDestinationCurrency

`func (o *LiquidationAddressResponseDto) GetDestinationCurrency() string`

GetDestinationCurrency returns the DestinationCurrency field if non-nil, zero value otherwise.

### GetDestinationCurrencyOk

`func (o *LiquidationAddressResponseDto) GetDestinationCurrencyOk() (*string, bool)`

GetDestinationCurrencyOk returns a tuple with the DestinationCurrency field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDestinationCurrency

`func (o *LiquidationAddressResponseDto) SetDestinationCurrency(v string)`

SetDestinationCurrency sets DestinationCurrency field to given value.

### HasDestinationCurrency

`func (o *LiquidationAddressResponseDto) HasDestinationCurrency() bool`

HasDestinationCurrency returns a boolean if a field has been set.

### GetCustomDeveloperFeePercent

`func (o *LiquidationAddressResponseDto) GetCustomDeveloperFeePercent() string`

GetCustomDeveloperFeePercent returns the CustomDeveloperFeePercent field if non-nil, zero value otherwise.

### GetCustomDeveloperFeePercentOk

`func (o *LiquidationAddressResponseDto) GetCustomDeveloperFeePercentOk() (*string, bool)`

GetCustomDeveloperFeePercentOk returns a tuple with the CustomDeveloperFeePercent field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomDeveloperFeePercent

`func (o *LiquidationAddressResponseDto) SetCustomDeveloperFeePercent(v string)`

SetCustomDeveloperFeePercent sets CustomDeveloperFeePercent field to given value.

### HasCustomDeveloperFeePercent

`func (o *LiquidationAddressResponseDto) HasCustomDeveloperFeePercent() bool`

HasCustomDeveloperFeePercent returns a boolean if a field has been set.

### GetCreatedAt

`func (o *LiquidationAddressResponseDto) GetCreatedAt() string`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *LiquidationAddressResponseDto) GetCreatedAtOk() (*string, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *LiquidationAddressResponseDto) SetCreatedAt(v string)`

SetCreatedAt sets CreatedAt field to given value.


### GetUpdatedAt

`func (o *LiquidationAddressResponseDto) GetUpdatedAt() string`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *LiquidationAddressResponseDto) GetUpdatedAtOk() (*string, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *LiquidationAddressResponseDto) SetUpdatedAt(v string)`

SetUpdatedAt sets UpdatedAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


