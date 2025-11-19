# ExchangeRateResponseDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**From** | **string** | Source currency code (USD for USDC) | 
**To** | **string** | Target currency code (EUR for EURC) | 
**MidmarketRate** | **string** | Mid-market exchange rate from source to target currency | 
**BuyRate** | **string** | Rate for buying target currency (what you get when converting from source to target) | 
**SellRate** | **string** | Rate for selling target currency (what you pay when converting from target to source) | 
**Timestamp** | Pointer to **string** | Timestamp when the exchange rate was last updated | [optional] 

## Methods

### NewExchangeRateResponseDto

`func NewExchangeRateResponseDto(from string, to string, midmarketRate string, buyRate string, sellRate string, ) *ExchangeRateResponseDto`

NewExchangeRateResponseDto instantiates a new ExchangeRateResponseDto object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewExchangeRateResponseDtoWithDefaults

`func NewExchangeRateResponseDtoWithDefaults() *ExchangeRateResponseDto`

NewExchangeRateResponseDtoWithDefaults instantiates a new ExchangeRateResponseDto object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetFrom

`func (o *ExchangeRateResponseDto) GetFrom() string`

GetFrom returns the From field if non-nil, zero value otherwise.

### GetFromOk

`func (o *ExchangeRateResponseDto) GetFromOk() (*string, bool)`

GetFromOk returns a tuple with the From field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFrom

`func (o *ExchangeRateResponseDto) SetFrom(v string)`

SetFrom sets From field to given value.


### GetTo

`func (o *ExchangeRateResponseDto) GetTo() string`

GetTo returns the To field if non-nil, zero value otherwise.

### GetToOk

`func (o *ExchangeRateResponseDto) GetToOk() (*string, bool)`

GetToOk returns a tuple with the To field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTo

`func (o *ExchangeRateResponseDto) SetTo(v string)`

SetTo sets To field to given value.


### GetMidmarketRate

`func (o *ExchangeRateResponseDto) GetMidmarketRate() string`

GetMidmarketRate returns the MidmarketRate field if non-nil, zero value otherwise.

### GetMidmarketRateOk

`func (o *ExchangeRateResponseDto) GetMidmarketRateOk() (*string, bool)`

GetMidmarketRateOk returns a tuple with the MidmarketRate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMidmarketRate

`func (o *ExchangeRateResponseDto) SetMidmarketRate(v string)`

SetMidmarketRate sets MidmarketRate field to given value.


### GetBuyRate

`func (o *ExchangeRateResponseDto) GetBuyRate() string`

GetBuyRate returns the BuyRate field if non-nil, zero value otherwise.

### GetBuyRateOk

`func (o *ExchangeRateResponseDto) GetBuyRateOk() (*string, bool)`

GetBuyRateOk returns a tuple with the BuyRate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBuyRate

`func (o *ExchangeRateResponseDto) SetBuyRate(v string)`

SetBuyRate sets BuyRate field to given value.


### GetSellRate

`func (o *ExchangeRateResponseDto) GetSellRate() string`

GetSellRate returns the SellRate field if non-nil, zero value otherwise.

### GetSellRateOk

`func (o *ExchangeRateResponseDto) GetSellRateOk() (*string, bool)`

GetSellRateOk returns a tuple with the SellRate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSellRate

`func (o *ExchangeRateResponseDto) SetSellRate(v string)`

SetSellRate sets SellRate field to given value.


### GetTimestamp

`func (o *ExchangeRateResponseDto) GetTimestamp() string`

GetTimestamp returns the Timestamp field if non-nil, zero value otherwise.

### GetTimestampOk

`func (o *ExchangeRateResponseDto) GetTimestampOk() (*string, bool)`

GetTimestampOk returns a tuple with the Timestamp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTimestamp

`func (o *ExchangeRateResponseDto) SetTimestamp(v string)`

SetTimestamp sets Timestamp field to given value.

### HasTimestamp

`func (o *ExchangeRateResponseDto) HasTimestamp() bool`

HasTimestamp returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


