

# PublicHealthResponseDto


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**status** | [**StatusEnum**](#StatusEnum) | Basic health status of the service. Returns \&quot;ok\&quot; when the service is responding. |  |
|**timestamp** | **OffsetDateTime** | ISO 8601 timestamp when the health check was performed. |  |
|**version** | **String** | Current version of the API service. |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| OK | &quot;ok&quot; |
| ERROR | &quot;error&quot; |



