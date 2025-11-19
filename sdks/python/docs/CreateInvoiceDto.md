# CreateInvoiceDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the invoice | 
**email** | **str** | Email address | 
**customer_id** | **str** | Customer ID | 
**currency** | **str** | Currency for the invoice | 
**items** | **object** |  | 
**due_date** | **datetime** | Due date of the invoice | 
**delivery** | **str** | Delivery method | 
**payment_link** | **bool** | Whether to generate a payment link | 
**payment_methods** | **List[str]** | Array of accepted payment methods | 
**status** | **str** | Invoice status | 
**address** | **str** | Address | [optional] 
**phone_number** | **str** | Phone number | [optional] 
**send_date** | **datetime** | Send date | [optional] 
**logo** | **str** | Logo URL | [optional] 
**partial_payment** | **bool** | Allow partial payments | 
**tax_id** | **str** | Tax ID | [optional] 

## Example

```python
from devdraft.models.create_invoice_dto import CreateInvoiceDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInvoiceDto from a JSON string
create_invoice_dto_instance = CreateInvoiceDto.from_json(json)
# print the JSON string representation of the object
print(CreateInvoiceDto.to_json())

# convert the object into a dict
create_invoice_dto_dict = create_invoice_dto_instance.to_dict()
# create an instance of CreateInvoiceDto from a dict
create_invoice_dto_from_dict = CreateInvoiceDto.from_dict(create_invoice_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


