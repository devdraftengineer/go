# AllBalancesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Usdc** | [**AggregatedBalanceResponse**](AggregatedBalanceResponse.md) | USDC balance aggregation | 
**Eurc** | [**AggregatedBalanceResponse**](AggregatedBalanceResponse.md) | EURC balance aggregation | 
**TotalUsdValue** | **string** | Total value in USD equivalent | 

## Methods

### NewAllBalancesResponse

`func NewAllBalancesResponse(usdc AggregatedBalanceResponse, eurc AggregatedBalanceResponse, totalUsdValue string, ) *AllBalancesResponse`

NewAllBalancesResponse instantiates a new AllBalancesResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAllBalancesResponseWithDefaults

`func NewAllBalancesResponseWithDefaults() *AllBalancesResponse`

NewAllBalancesResponseWithDefaults instantiates a new AllBalancesResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetUsdc

`func (o *AllBalancesResponse) GetUsdc() AggregatedBalanceResponse`

GetUsdc returns the Usdc field if non-nil, zero value otherwise.

### GetUsdcOk

`func (o *AllBalancesResponse) GetUsdcOk() (*AggregatedBalanceResponse, bool)`

GetUsdcOk returns a tuple with the Usdc field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUsdc

`func (o *AllBalancesResponse) SetUsdc(v AggregatedBalanceResponse)`

SetUsdc sets Usdc field to given value.


### GetEurc

`func (o *AllBalancesResponse) GetEurc() AggregatedBalanceResponse`

GetEurc returns the Eurc field if non-nil, zero value otherwise.

### GetEurcOk

`func (o *AllBalancesResponse) GetEurcOk() (*AggregatedBalanceResponse, bool)`

GetEurcOk returns a tuple with the Eurc field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEurc

`func (o *AllBalancesResponse) SetEurc(v AggregatedBalanceResponse)`

SetEurc sets Eurc field to given value.


### GetTotalUsdValue

`func (o *AllBalancesResponse) GetTotalUsdValue() string`

GetTotalUsdValue returns the TotalUsdValue field if non-nil, zero value otherwise.

### GetTotalUsdValueOk

`func (o *AllBalancesResponse) GetTotalUsdValueOk() (*string, bool)`

GetTotalUsdValueOk returns a tuple with the TotalUsdValue field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalUsdValue

`func (o *AllBalancesResponse) SetTotalUsdValue(v string)`

SetTotalUsdValue sets TotalUsdValue field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


