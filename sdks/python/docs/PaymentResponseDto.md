# PaymentResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Payment ID | 
**amount** | **float** | The amount charged | 
**currency** | **str** | The currency code | 
**status** | **str** | Payment status | 
**timestamp** | **str** | Timestamp of the payment | 

## Example

```python
from devdraft.models.payment_response_dto import PaymentResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentResponseDto from a JSON string
payment_response_dto_instance = PaymentResponseDto.from_json(json)
# print the JSON string representation of the object
print(PaymentResponseDto.to_json())

# convert the object into a dict
payment_response_dto_dict = payment_response_dto_instance.to_dict()
# create an instance of PaymentResponseDto from a dict
payment_response_dto_from_dict = PaymentResponseDto.from_dict(payment_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


