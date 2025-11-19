# PaymentRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The amount to charge | 
**currency** | **str** | The currency code | 
**description** | **str** | Description of the payment | 
**customer_id** | **str** | Customer reference ID | [optional] 

## Example

```python
from devdraft.models.payment_request_dto import PaymentRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentRequestDto from a JSON string
payment_request_dto_instance = PaymentRequestDto.from_json(json)
# print the JSON string representation of the object
print(PaymentRequestDto.to_json())

# convert the object into a dict
payment_request_dto_dict = payment_request_dto_instance.to_dict()
# create an instance of PaymentRequestDto from a dict
payment_request_dto_from_dict = PaymentRequestDto.from_dict(payment_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


