# CreateExternalBankTransferDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_wallet_id** | **str** | The ID of the source bridge wallet | 
**source_currency** | **str** | The source currency | 
**destination_currency** | **str** | The destination currency | 
**destination_payment_rail** | [**BridgeFiatPaymentRail**](BridgeFiatPaymentRail.md) | The destination payment rail (fiat payment method) | 
**external_account_id** | **str** | The external account ID for the bank transfer | 
**amount** | **float** | The amount to transfer | [optional] 
**wire_message** | **str** | Wire transfer message (1-256 characters, only for wire transfers) | [optional] 
**sepa_reference** | **str** | SEPA reference message (6-140 characters, only for SEPA transfers) | [optional] 
**swift_reference** | **str** | SWIFT reference message (1-190 characters, only for SWIFT transfers) | [optional] 
**spei_reference** | **str** | SPEI reference message (1-40 characters, only for SPEI transfers) | [optional] 
**swift_charges** | **str** | SWIFT charges bearer (only for SWIFT transfers) | [optional] 
**ach_reference** | **str** | ACH reference message (1-10 characters, only for ACH transfers) | [optional] 

## Example

```python
from devdraft.models.create_external_bank_transfer_dto import CreateExternalBankTransferDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateExternalBankTransferDto from a JSON string
create_external_bank_transfer_dto_instance = CreateExternalBankTransferDto.from_json(json)
# print the JSON string representation of the object
print(CreateExternalBankTransferDto.to_json())

# convert the object into a dict
create_external_bank_transfer_dto_dict = create_external_bank_transfer_dto_instance.to_dict()
# create an instance of CreateExternalBankTransferDto from a dict
create_external_bank_transfer_dto_from_dict = CreateExternalBankTransferDto.from_dict(create_external_bank_transfer_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


