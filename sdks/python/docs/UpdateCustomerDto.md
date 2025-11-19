# UpdateCustomerDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | Customer&#39;s first name. Used for personalization and legal documentation. | [optional] 
**last_name** | **str** | Customer&#39;s last name. Used for personalization and legal documentation. | [optional] 
**email** | **str** | Customer&#39;s email address. Used for notifications, receipts, and account management. Must be a valid email format. | [optional] 
**phone_number** | **str** | Customer&#39;s phone number. Used for SMS notifications and verification. Include country code for international numbers. | [optional] 
**customer_type** | [**CustomerType**](CustomerType.md) | Type of customer account. Determines available features and compliance requirements. | [optional] 
**status** | [**CustomerStatus**](CustomerStatus.md) | Current status of the customer account. Controls access to services and features. | [optional] 

## Example

```python
from devdraft.models.update_customer_dto import UpdateCustomerDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCustomerDto from a JSON string
update_customer_dto_instance = UpdateCustomerDto.from_json(json)
# print the JSON string representation of the object
print(UpdateCustomerDto.to_json())

# convert the object into a dict
update_customer_dto_dict = update_customer_dto_instance.to_dict()
# create an instance of UpdateCustomerDto from a dict
update_customer_dto_from_dict = UpdateCustomerDto.from_dict(update_customer_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


