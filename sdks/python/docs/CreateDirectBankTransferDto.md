# CreateDirectBankTransferDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_id** | **str** | The ID of the bridge wallet to transfer from | 
**payment_rail** | **str** | The payment rail to use | 
**destination_currency** | **str** | The destination currency | 
**source_currency** | **str** | The source currency | 
**amount** | **float** | The amount to transfer | 
**wire_message** | **str** | Wire transfer message | [optional] 
**sepa_reference** | **str** | SEPA transfer reference | [optional] 
**ach_reference** | **str** | ACH transfer reference | [optional] 

## Example

```python
from devdraft.models.create_direct_bank_transfer_dto import CreateDirectBankTransferDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDirectBankTransferDto from a JSON string
create_direct_bank_transfer_dto_instance = CreateDirectBankTransferDto.from_json(json)
# print the JSON string representation of the object
print(CreateDirectBankTransferDto.to_json())

# convert the object into a dict
create_direct_bank_transfer_dto_dict = create_direct_bank_transfer_dto_instance.to_dict()
# create an instance of CreateDirectBankTransferDto from a dict
create_direct_bank_transfer_dto_from_dict = CreateDirectBankTransferDto.from_dict(create_direct_bank_transfer_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


