# UpdateTaxDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Tax name for identification and display purposes | [optional] 
**description** | **str** | Detailed description of what this tax covers | [optional] 
**percentage** | **float** | Tax rate as a percentage (0-100) | [optional] 
**active** | **bool** | Whether this tax is currently active and can be applied | [optional] 
**app_ids** | **List[str]** | Array of app IDs where this tax should be available | [optional] 

## Example

```python
from devdraft.models.update_tax_dto import UpdateTaxDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTaxDto from a JSON string
update_tax_dto_instance = UpdateTaxDto.from_json(json)
# print the JSON string representation of the object
print(UpdateTaxDto.to_json())

# convert the object into a dict
update_tax_dto_dict = update_tax_dto_instance.to_dict()
# create an instance of UpdateTaxDto from a dict
update_tax_dto_from_dict = UpdateTaxDto.from_dict(update_tax_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


