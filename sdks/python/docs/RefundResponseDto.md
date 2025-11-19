# RefundResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Refund ID | 
**payment_id** | **str** | Original payment ID | 
**amount** | **float** | The amount refunded | 
**status** | **str** | Refund status | 
**timestamp** | **str** | Timestamp of the refund | 

## Example

```python
from devdraft.models.refund_response_dto import RefundResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of RefundResponseDto from a JSON string
refund_response_dto_instance = RefundResponseDto.from_json(json)
# print the JSON string representation of the object
print(RefundResponseDto.to_json())

# convert the object into a dict
refund_response_dto_dict = refund_response_dto_instance.to_dict()
# create an instance of RefundResponseDto from a dict
refund_response_dto_from_dict = RefundResponseDto.from_dict(refund_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


