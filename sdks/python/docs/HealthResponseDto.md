# HealthResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Overall health status of the service. Returns \&quot;ok\&quot; when healthy, \&quot;error\&quot; when issues detected. | 
**timestamp** | **datetime** | ISO 8601 timestamp when the health check was performed. | 
**version** | **str** | Current version of the API service. Useful for debugging and compatibility checks. | 
**database** | **str** | Database connectivity status. Shows \&quot;connected\&quot; when database is accessible, \&quot;error\&quot; when connection fails. | 
**message** | **str** | Human-readable message describing the current health status and any issues. | 
**authenticated** | **bool** | Indicates whether the request was properly authenticated. Always true for this endpoint since authentication is required. | 

## Example

```python
from devdraft.models.health_response_dto import HealthResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of HealthResponseDto from a JSON string
health_response_dto_instance = HealthResponseDto.from_json(json)
# print the JSON string representation of the object
print(HealthResponseDto.to_json())

# convert the object into a dict
health_response_dto_dict = health_response_dto_instance.to_dict()
# create an instance of HealthResponseDto from a dict
health_response_dto_from_dict = HealthResponseDto.from_dict(health_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


