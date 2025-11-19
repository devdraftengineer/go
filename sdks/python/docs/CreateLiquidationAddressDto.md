# CreateLiquidationAddressDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain** | **str** | The blockchain chain for the liquidation address | 
**currency** | **str** | The currency for the liquidation address | 
**address** | **str** | The liquidation address on the blockchain | 
**external_account_id** | **str** | External bank account to send funds to | [optional] 
**prefunded_account_id** | **str** | Developer&#39;s prefunded account id | [optional] 
**bridge_wallet_id** | **str** | Bridge Wallet to send funds to | [optional] 
**destination_payment_rail** | [**BridgePaymentRail**](BridgePaymentRail.md) | Payment rail for sending funds | [optional] 
**destination_currency** | [**DestinationCurrency**](DestinationCurrency.md) | Currency for sending funds | [optional] 
**destination_wire_message** | **str** | Message for wire transfers | [optional] 
**destination_sepa_reference** | **str** | Reference for SEPA transactions | [optional] 
**destination_ach_reference** | **str** | Reference for ACH transactions | [optional] 
**destination_address** | **str** | Crypto wallet address for crypto transfers | [optional] 
**destination_blockchain_memo** | **str** | Memo for blockchain transactions | [optional] 
**return_address** | **str** | Address to return funds on failed transactions (Not supported on Stellar) | [optional] 
**custom_developer_fee_percent** | **str** | Custom developer fee percentage (Base 100 percentage: 10.2% &#x3D; \&quot;10.2\&quot;) | [optional] 

## Example

```python
from devdraft.models.create_liquidation_address_dto import CreateLiquidationAddressDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateLiquidationAddressDto from a JSON string
create_liquidation_address_dto_instance = CreateLiquidationAddressDto.from_json(json)
# print the JSON string representation of the object
print(CreateLiquidationAddressDto.to_json())

# convert the object into a dict
create_liquidation_address_dto_dict = create_liquidation_address_dto_instance.to_dict()
# create an instance of CreateLiquidationAddressDto from a dict
create_liquidation_address_dto_from_dict = CreateLiquidationAddressDto.from_dict(create_liquidation_address_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


