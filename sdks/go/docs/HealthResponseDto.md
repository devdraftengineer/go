# HealthResponseDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Status** | **string** | Overall health status of the service. Returns \&quot;ok\&quot; when healthy, \&quot;error\&quot; when issues detected. | 
**Timestamp** | **time.Time** | ISO 8601 timestamp when the health check was performed. | 
**Version** | **string** | Current version of the API service. Useful for debugging and compatibility checks. | 
**Database** | **string** | Database connectivity status. Shows \&quot;connected\&quot; when database is accessible, \&quot;error\&quot; when connection fails. | 
**Message** | **string** | Human-readable message describing the current health status and any issues. | 
**Authenticated** | **bool** | Indicates whether the request was properly authenticated. Always true for this endpoint since authentication is required. | 

## Methods

### NewHealthResponseDto

`func NewHealthResponseDto(status string, timestamp time.Time, version string, database string, message string, authenticated bool, ) *HealthResponseDto`

NewHealthResponseDto instantiates a new HealthResponseDto object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewHealthResponseDtoWithDefaults

`func NewHealthResponseDtoWithDefaults() *HealthResponseDto`

NewHealthResponseDtoWithDefaults instantiates a new HealthResponseDto object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetStatus

`func (o *HealthResponseDto) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *HealthResponseDto) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *HealthResponseDto) SetStatus(v string)`

SetStatus sets Status field to given value.


### GetTimestamp

`func (o *HealthResponseDto) GetTimestamp() time.Time`

GetTimestamp returns the Timestamp field if non-nil, zero value otherwise.

### GetTimestampOk

`func (o *HealthResponseDto) GetTimestampOk() (*time.Time, bool)`

GetTimestampOk returns a tuple with the Timestamp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTimestamp

`func (o *HealthResponseDto) SetTimestamp(v time.Time)`

SetTimestamp sets Timestamp field to given value.


### GetVersion

`func (o *HealthResponseDto) GetVersion() string`

GetVersion returns the Version field if non-nil, zero value otherwise.

### GetVersionOk

`func (o *HealthResponseDto) GetVersionOk() (*string, bool)`

GetVersionOk returns a tuple with the Version field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVersion

`func (o *HealthResponseDto) SetVersion(v string)`

SetVersion sets Version field to given value.


### GetDatabase

`func (o *HealthResponseDto) GetDatabase() string`

GetDatabase returns the Database field if non-nil, zero value otherwise.

### GetDatabaseOk

`func (o *HealthResponseDto) GetDatabaseOk() (*string, bool)`

GetDatabaseOk returns a tuple with the Database field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDatabase

`func (o *HealthResponseDto) SetDatabase(v string)`

SetDatabase sets Database field to given value.


### GetMessage

`func (o *HealthResponseDto) GetMessage() string`

GetMessage returns the Message field if non-nil, zero value otherwise.

### GetMessageOk

`func (o *HealthResponseDto) GetMessageOk() (*string, bool)`

GetMessageOk returns a tuple with the Message field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMessage

`func (o *HealthResponseDto) SetMessage(v string)`

SetMessage sets Message field to given value.


### GetAuthenticated

`func (o *HealthResponseDto) GetAuthenticated() bool`

GetAuthenticated returns the Authenticated field if non-nil, zero value otherwise.

### GetAuthenticatedOk

`func (o *HealthResponseDto) GetAuthenticatedOk() (*bool, bool)`

GetAuthenticatedOk returns a tuple with the Authenticated field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAuthenticated

`func (o *HealthResponseDto) SetAuthenticated(v bool)`

SetAuthenticated sets Authenticated field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


