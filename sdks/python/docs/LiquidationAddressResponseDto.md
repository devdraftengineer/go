# LiquidationAddressResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the liquidation address | 
**state** | **str** | Current state of the liquidation address | 
**customer_id** | **str** | Customer ID this liquidation address belongs to | 
**chain** | **str** | Blockchain chain | 
**currency** | **str** | Currency | 
**address** | **str** | Liquidation address | 
**external_account_id** | **str** | External account ID | [optional] 
**prefunded_account_id** | **str** | Prefunded account ID | [optional] 
**bridge_wallet_id** | **str** | Bridge wallet ID | [optional] 
**destination_payment_rail** | **str** | Destination payment rail | [optional] 
**destination_currency** | **str** | Destination currency | [optional] 
**custom_developer_fee_percent** | **str** | Custom developer fee percent | [optional] 
**created_at** | **str** | Creation timestamp | 
**updated_at** | **str** | Last update timestamp | 

## Example

```python
from devdraft.models.liquidation_address_response_dto import LiquidationAddressResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of LiquidationAddressResponseDto from a JSON string
liquidation_address_response_dto_instance = LiquidationAddressResponseDto.from_json(json)
# print the JSON string representation of the object
print(LiquidationAddressResponseDto.to_json())

# convert the object into a dict
liquidation_address_response_dto_dict = liquidation_address_response_dto_instance.to_dict()
# create an instance of LiquidationAddressResponseDto from a dict
liquidation_address_response_dto_from_dict = LiquidationAddressResponseDto.from_dict(liquidation_address_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


