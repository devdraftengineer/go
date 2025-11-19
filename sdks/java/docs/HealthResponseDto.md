

# HealthResponseDto


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**status** | [**StatusEnum**](#StatusEnum) | Overall health status of the service. Returns \&quot;ok\&quot; when healthy, \&quot;error\&quot; when issues detected. |  |
|**timestamp** | **OffsetDateTime** | ISO 8601 timestamp when the health check was performed. |  |
|**version** | **String** | Current version of the API service. Useful for debugging and compatibility checks. |  |
|**database** | [**DatabaseEnum**](#DatabaseEnum) | Database connectivity status. Shows \&quot;connected\&quot; when database is accessible, \&quot;error\&quot; when connection fails. |  |
|**message** | **String** | Human-readable message describing the current health status and any issues. |  |
|**authenticated** | **Boolean** | Indicates whether the request was properly authenticated. Always true for this endpoint since authentication is required. |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| OK | &quot;ok&quot; |
| ERROR | &quot;error&quot; |



## Enum: DatabaseEnum

| Name | Value |
|---- | -----|
| CONNECTED | &quot;connected&quot; |
| ERROR | &quot;error&quot; |



