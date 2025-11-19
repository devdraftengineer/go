# CreateDirectWalletTransferDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_id** | **str** | The ID of the bridge wallet to transfer from | 
**network** | **str** | The network to use for the transfer | 
**stable_coin_currency** | **str** | The stablecoin currency to use | 
**amount** | **float** | The amount to transfer | 

## Example

```python
from devdraft.models.create_direct_wallet_transfer_dto import CreateDirectWalletTransferDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDirectWalletTransferDto from a JSON string
create_direct_wallet_transfer_dto_instance = CreateDirectWalletTransferDto.from_json(json)
# print the JSON string representation of the object
print(CreateDirectWalletTransferDto.to_json())

# convert the object into a dict
create_direct_wallet_transfer_dto_dict = create_direct_wallet_transfer_dto_instance.to_dict()
# create an instance of CreateDirectWalletTransferDto from a dict
create_direct_wallet_transfer_dto_from_dict = CreateDirectWalletTransferDto.from_dict(create_direct_wallet_transfer_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


