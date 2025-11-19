# CreateCustomerDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | Customer&#39;s first name. Used for personalization and legal documentation. | 
**last_name** | **str** | Customer&#39;s last name. Used for personalization and legal documentation. | 
**email** | **str** | Customer&#39;s email address. Used for notifications, receipts, and account management. Must be a valid email format. | [optional] 
**phone_number** | **str** | Customer&#39;s phone number. Used for SMS notifications and verification. Include country code for international numbers. | 
**customer_type** | [**CustomerType**](CustomerType.md) | Type of customer account. Determines available features and compliance requirements. | [optional] 
**status** | [**CustomerStatus**](CustomerStatus.md) | Current status of the customer account. Controls access to services and features. | [optional] 

## Example

```python
from devdraft.models.create_customer_dto import CreateCustomerDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCustomerDto from a JSON string
create_customer_dto_instance = CreateCustomerDto.from_json(json)
# print the JSON string representation of the object
print(CreateCustomerDto.to_json())

# convert the object into a dict
create_customer_dto_dict = create_customer_dto_instance.to_dict()
# create an instance of CreateCustomerDto from a dict
create_customer_dto_from_dict = CreateCustomerDto.from_dict(create_customer_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


