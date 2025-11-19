# InvoiceProductDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **str** | Product ID | 
**quantity** | **float** | Quantity of the product | 

## Example

```python
from devdraft.models.invoice_product_dto import InvoiceProductDto

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceProductDto from a JSON string
invoice_product_dto_instance = InvoiceProductDto.from_json(json)
# print the JSON string representation of the object
print(InvoiceProductDto.to_json())

# convert the object into a dict
invoice_product_dto_dict = invoice_product_dto_instance.to_dict()
# create an instance of InvoiceProductDto from a dict
invoice_product_dto_from_dict = InvoiceProductDto.from_dict(invoice_product_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


