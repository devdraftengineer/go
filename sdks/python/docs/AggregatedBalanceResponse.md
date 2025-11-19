# AggregatedBalanceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | The stablecoin currency | 
**total_balance** | **str** | The total aggregated balance across all wallets and chains | 
**balances** | **List[object]** | Detailed breakdown of balances by wallet and chain | 

## Example

```python
from devdraft.models.aggregated_balance_response import AggregatedBalanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AggregatedBalanceResponse from a JSON string
aggregated_balance_response_instance = AggregatedBalanceResponse.from_json(json)
# print the JSON string representation of the object
print(AggregatedBalanceResponse.to_json())

# convert the object into a dict
aggregated_balance_response_dict = aggregated_balance_response_instance.to_dict()
# create an instance of AggregatedBalanceResponse from a dict
aggregated_balance_response_from_dict = AggregatedBalanceResponse.from_dict(aggregated_balance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


