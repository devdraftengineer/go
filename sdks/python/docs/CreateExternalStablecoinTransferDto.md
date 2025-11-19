# CreateExternalStablecoinTransferDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_wallet_id** | **str** | The ID of the source bridge wallet | 
**source_currency** | **str** | The source currency | 
**destination_currency** | **str** | The destination currency | 
**blockchain_memo** | **str** | Blockchain memo for the transfer | [optional] 
**beneficiary_id** | **str** | Beneficiary ID for the stablecoin transfer | 
**amount** | **float** | The amount to transfer | [optional] 

## Example

```python
from devdraft.models.create_external_stablecoin_transfer_dto import CreateExternalStablecoinTransferDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateExternalStablecoinTransferDto from a JSON string
create_external_stablecoin_transfer_dto_instance = CreateExternalStablecoinTransferDto.from_json(json)
# print the JSON string representation of the object
print(CreateExternalStablecoinTransferDto.to_json())

# convert the object into a dict
create_external_stablecoin_transfer_dto_dict = create_external_stablecoin_transfer_dto_instance.to_dict()
# create an instance of CreateExternalStablecoinTransferDto from a dict
create_external_stablecoin_transfer_dto_from_dict = CreateExternalStablecoinTransferDto.from_dict(create_external_stablecoin_transfer_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


