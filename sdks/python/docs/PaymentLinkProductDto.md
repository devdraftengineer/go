# PaymentLinkProductDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **str** | UUID of the product to include in this payment link. Must be a valid product from your catalog. | 
**quantity** | **int** | Quantity of this product to include. Must be at least 1. | [default to 1]

## Example

```python
from devdraft.models.payment_link_product_dto import PaymentLinkProductDto

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentLinkProductDto from a JSON string
payment_link_product_dto_instance = PaymentLinkProductDto.from_json(json)
# print the JSON string representation of the object
print(PaymentLinkProductDto.to_json())

# convert the object into a dict
payment_link_product_dto_dict = payment_link_product_dto_instance.to_dict()
# create an instance of PaymentLinkProductDto from a dict
payment_link_product_dto_from_dict = PaymentLinkProductDto.from_dict(payment_link_product_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


