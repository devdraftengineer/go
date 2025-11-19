# CreateBankPaymentIntentDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_payment_rail** | [**BridgePaymentRail**](BridgePaymentRail.md) | The banking payment method to use for the transfer. Determines processing time and fees. | 
**source_currency** | [**FiatCurrency**](FiatCurrency.md) | The fiat currency to convert FROM. Must match the currency of the source payment rail. | 
**destination_currency** | [**StableCoinCurrency**](StableCoinCurrency.md) | The stablecoin currency to convert TO. The customer will receive this currency. | 
**destination_network** | [**BridgePaymentRail**](BridgePaymentRail.md) | The blockchain network where the stablecoin will be delivered. Must support the destination currency. | 
**destination_address** | **str** | Destination wallet address. Supports Ethereum (0x...) and Solana address formats. | [optional] 
**amount** | **str** | Payment amount (optional for flexible amount) | [optional] 
**customer_first_name** | **str** | Customer first name | [optional] 
**customer_last_name** | **str** | Customer last name | [optional] 
**customer_email** | **str** | Customer email address | [optional] 
**customer_address** | **str** | Customer address | [optional] 
**customer_country** | **str** | Customer country | [optional] 
**customer_country_iso** | **str** | Customer country ISO code | [optional] 
**customer_province** | **str** | Customer province/state | [optional] 
**customer_province_iso** | **str** | Customer province/state ISO code | [optional] 
**phone_number** | **str** | Customer phone number | [optional] 
**wire_message** | **str** | Wire transfer message (for WIRE transfers) | [optional] 
**sepa_reference** | **str** | SEPA reference (for SEPA transfers) | [optional] 
**ach_reference** | **str** | ACH reference (for ACH transfers) | [optional] 

## Example

```python
from devdraft.models.create_bank_payment_intent_dto import CreateBankPaymentIntentDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBankPaymentIntentDto from a JSON string
create_bank_payment_intent_dto_instance = CreateBankPaymentIntentDto.from_json(json)
# print the JSON string representation of the object
print(CreateBankPaymentIntentDto.to_json())

# convert the object into a dict
create_bank_payment_intent_dto_dict = create_bank_payment_intent_dto_instance.to_dict()
# create an instance of CreateBankPaymentIntentDto from a dict
create_bank_payment_intent_dto_from_dict = CreateBankPaymentIntentDto.from_dict(create_bank_payment_intent_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


