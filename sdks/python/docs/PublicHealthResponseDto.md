# PublicHealthResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Basic health status of the service. Returns \&quot;ok\&quot; when the service is responding. | 
**timestamp** | **datetime** | ISO 8601 timestamp when the health check was performed. | 
**version** | **str** | Current version of the API service. | 

## Example

```python
from devdraft.models.public_health_response_dto import PublicHealthResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of PublicHealthResponseDto from a JSON string
public_health_response_dto_instance = PublicHealthResponseDto.from_json(json)
# print the JSON string representation of the object
print(PublicHealthResponseDto.to_json())

# convert the object into a dict
public_health_response_dto_dict = public_health_response_dto_instance.to_dict()
# create an instance of PublicHealthResponseDto from a dict
public_health_response_dto_from_dict = PublicHealthResponseDto.from_dict(public_health_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


