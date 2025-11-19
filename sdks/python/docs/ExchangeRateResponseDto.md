# ExchangeRateResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** | Source currency code (USD for USDC) | 
**to** | **str** | Target currency code (EUR for EURC) | 
**midmarket_rate** | **str** | Mid-market exchange rate from source to target currency | 
**buy_rate** | **str** | Rate for buying target currency (what you get when converting from source to target) | 
**sell_rate** | **str** | Rate for selling target currency (what you pay when converting from target to source) | 
**timestamp** | **str** | Timestamp when the exchange rate was last updated | [optional] 

## Example

```python
from devdraft.models.exchange_rate_response_dto import ExchangeRateResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeRateResponseDto from a JSON string
exchange_rate_response_dto_instance = ExchangeRateResponseDto.from_json(json)
# print the JSON string representation of the object
print(ExchangeRateResponseDto.to_json())

# convert the object into a dict
exchange_rate_response_dto_dict = exchange_rate_response_dto_instance.to_dict()
# create an instance of ExchangeRateResponseDto from a dict
exchange_rate_response_dto_from_dict = ExchangeRateResponseDto.from_dict(exchange_rate_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


