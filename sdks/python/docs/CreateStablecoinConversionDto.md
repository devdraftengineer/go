# CreateStablecoinConversionDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_id** | **str** | The ID of the bridge wallet to use | 
**source_network** | **str** | The source network | 
**source_currency** | **str** | The source currency | 
**destination_currency** | **str** | The destination currency | 
**amount** | **float** | The amount to convert | 

## Example

```python
from devdraft.models.create_stablecoin_conversion_dto import CreateStablecoinConversionDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateStablecoinConversionDto from a JSON string
create_stablecoin_conversion_dto_instance = CreateStablecoinConversionDto.from_json(json)
# print the JSON string representation of the object
print(CreateStablecoinConversionDto.to_json())

# convert the object into a dict
create_stablecoin_conversion_dto_dict = create_stablecoin_conversion_dto_instance.to_dict()
# create an instance of CreateStablecoinConversionDto from a dict
create_stablecoin_conversion_dto_from_dict = CreateStablecoinConversionDto.from_dict(create_stablecoin_conversion_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


