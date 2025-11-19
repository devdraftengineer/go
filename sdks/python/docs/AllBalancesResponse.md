# AllBalancesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**usdc** | [**AggregatedBalanceResponse**](AggregatedBalanceResponse.md) | USDC balance aggregation | 
**eurc** | [**AggregatedBalanceResponse**](AggregatedBalanceResponse.md) | EURC balance aggregation | 
**total_usd_value** | **str** | Total value in USD equivalent | 

## Example

```python
from devdraft.models.all_balances_response import AllBalancesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AllBalancesResponse from a JSON string
all_balances_response_instance = AllBalancesResponse.from_json(json)
# print the JSON string representation of the object
print(AllBalancesResponse.to_json())

# convert the object into a dict
all_balances_response_dict = all_balances_response_instance.to_dict()
# create an instance of AllBalancesResponse from a dict
all_balances_response_from_dict = AllBalancesResponse.from_dict(all_balances_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


