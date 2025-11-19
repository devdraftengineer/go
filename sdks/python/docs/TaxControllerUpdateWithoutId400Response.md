# TaxControllerUpdateWithoutId400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**error** | **str** |  | [optional] 
**status_code** | **float** |  | [optional] 

## Example

```python
from devdraft.models.tax_controller_update_without_id400_response import TaxControllerUpdateWithoutId400Response

# TODO update the JSON string below
json = "{}"
# create an instance of TaxControllerUpdateWithoutId400Response from a JSON string
tax_controller_update_without_id400_response_instance = TaxControllerUpdateWithoutId400Response.from_json(json)
# print the JSON string representation of the object
print(TaxControllerUpdateWithoutId400Response.to_json())

# convert the object into a dict
tax_controller_update_without_id400_response_dict = tax_controller_update_without_id400_response_instance.to_dict()
# create an instance of TaxControllerUpdateWithoutId400Response from a dict
tax_controller_update_without_id400_response_from_dict = TaxControllerUpdateWithoutId400Response.from_dict(tax_controller_update_without_id400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


