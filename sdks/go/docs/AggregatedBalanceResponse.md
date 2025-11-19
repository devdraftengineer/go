# AggregatedBalanceResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Currency** | **string** | The stablecoin currency | 
**TotalBalance** | **string** | The total aggregated balance across all wallets and chains | 
**Balances** | **[]map[string]interface{}** | Detailed breakdown of balances by wallet and chain | 

## Methods

### NewAggregatedBalanceResponse

`func NewAggregatedBalanceResponse(currency string, totalBalance string, balances []map[string]interface{}, ) *AggregatedBalanceResponse`

NewAggregatedBalanceResponse instantiates a new AggregatedBalanceResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAggregatedBalanceResponseWithDefaults

`func NewAggregatedBalanceResponseWithDefaults() *AggregatedBalanceResponse`

NewAggregatedBalanceResponseWithDefaults instantiates a new AggregatedBalanceResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCurrency

`func (o *AggregatedBalanceResponse) GetCurrency() string`

GetCurrency returns the Currency field if non-nil, zero value otherwise.

### GetCurrencyOk

`func (o *AggregatedBalanceResponse) GetCurrencyOk() (*string, bool)`

GetCurrencyOk returns a tuple with the Currency field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCurrency

`func (o *AggregatedBalanceResponse) SetCurrency(v string)`

SetCurrency sets Currency field to given value.


### GetTotalBalance

`func (o *AggregatedBalanceResponse) GetTotalBalance() string`

GetTotalBalance returns the TotalBalance field if non-nil, zero value otherwise.

### GetTotalBalanceOk

`func (o *AggregatedBalanceResponse) GetTotalBalanceOk() (*string, bool)`

GetTotalBalanceOk returns a tuple with the TotalBalance field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalBalance

`func (o *AggregatedBalanceResponse) SetTotalBalance(v string)`

SetTotalBalance sets TotalBalance field to given value.


### GetBalances

`func (o *AggregatedBalanceResponse) GetBalances() []map[string]interface{}`

GetBalances returns the Balances field if non-nil, zero value otherwise.

### GetBalancesOk

`func (o *AggregatedBalanceResponse) GetBalancesOk() (*[]map[string]interface{}, bool)`

GetBalancesOk returns a tuple with the Balances field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBalances

`func (o *AggregatedBalanceResponse) SetBalances(v []map[string]interface{})`

SetBalances sets Balances field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


