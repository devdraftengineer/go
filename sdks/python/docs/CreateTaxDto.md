# CreateTaxDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Tax name. Used to identify and reference this tax rate. | 
**description** | **str** | Optional description explaining what this tax covers. | [optional] 
**percentage** | **float** | Tax percentage rate. Must be between 0 and 100. | 
**active** | **bool** | Whether this tax is currently active and can be applied. | [optional] [default to True]
**app_ids** | **List[str]** | Array of app IDs where this tax should be available. If not provided, tax will be available for the current app. | [optional] 

## Example

```python
from devdraft.models.create_tax_dto import CreateTaxDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTaxDto from a JSON string
create_tax_dto_instance = CreateTaxDto.from_json(json)
# print the JSON string representation of the object
print(CreateTaxDto.to_json())

# convert the object into a dict
create_tax_dto_dict = create_tax_dto_instance.to_dict()
# create an instance of CreateTaxDto from a dict
create_tax_dto_from_dict = CreateTaxDto.from_dict(create_tax_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


