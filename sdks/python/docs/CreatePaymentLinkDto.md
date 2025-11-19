# CreatePaymentLinkDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Display title for the payment link. This appears on the checkout page and in customer communications. | 
**url** | **str** | Unique URL slug for the payment link. Can be a full URL or just the path segment. Must be unique within your account. | 
**description** | **str** | Detailed description of what the customer is purchasing. Supports markdown formatting. | [optional] 
**cover_image** | **str** | Cover image URL | [optional] 
**link_type** | **str** | Type of the payment link | 
**amount** | **float** | Amount for the payment link | [optional] 
**payment_for_id** | **str** | Payment for ID | [optional] 
**customer_id** | **str** | Customer ID | [optional] 
**payment_link_products** | [**List[PaymentLinkProductDto]**](PaymentLinkProductDto.md) | Array of products in the payment link | [optional] 
**is_for_all_product** | **bool** | Whether the payment link is for all products | [optional] [default to False]
**allow_quantity_adjustment** | **bool** | Whether to allow quantity adjustment | [default to True]
**collect_tax** | **bool** | Whether to collect tax | [default to False]
**tax_id** | **str** | Tax ID | [optional] 
**collect_address** | **bool** | Whether to collect address | [default to False]
**limit_payments** | **bool** | Whether to limit payments | [optional] [default to False]
**max_payments** | **float** | Maximum number of payments | [optional] 
**custom_fields** | **object** | Custom fields | [optional] 
**allow_mobile_payment** | **bool** | Whether to allow mobile payment | [default to False]
**currency** | **str** | Currency | [default to 'usdc']
**expiration_date** | **datetime** | Expiration date | [optional] 

## Example

```python
from devdraft.models.create_payment_link_dto import CreatePaymentLinkDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePaymentLinkDto from a JSON string
create_payment_link_dto_instance = CreatePaymentLinkDto.from_json(json)
# print the JSON string representation of the object
print(CreatePaymentLinkDto.to_json())

# convert the object into a dict
create_payment_link_dto_dict = create_payment_link_dto_instance.to_dict()
# create an instance of CreatePaymentLinkDto from a dict
create_payment_link_dto_from_dict = CreatePaymentLinkDto.from_dict(create_payment_link_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


