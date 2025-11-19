# TaxControllerCreate201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**percentage** | **float** |  | [optional] 
**active** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from devdraft.models.tax_controller_create201_response import TaxControllerCreate201Response

# TODO update the JSON string below
json = "{}"
# create an instance of TaxControllerCreate201Response from a JSON string
tax_controller_create201_response_instance = TaxControllerCreate201Response.from_json(json)
# print the JSON string representation of the object
print(TaxControllerCreate201Response.to_json())

# convert the object into a dict
tax_controller_create201_response_dict = tax_controller_create201_response_instance.to_dict()
# create an instance of TaxControllerCreate201Response from a dict
tax_controller_create201_response_from_dict = TaxControllerCreate201Response.from_dict(tax_controller_create201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


