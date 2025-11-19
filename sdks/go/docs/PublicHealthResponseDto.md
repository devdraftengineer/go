# PublicHealthResponseDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Status** | **string** | Basic health status of the service. Returns \&quot;ok\&quot; when the service is responding. | 
**Timestamp** | **time.Time** | ISO 8601 timestamp when the health check was performed. | 
**Version** | **string** | Current version of the API service. | 

## Methods

### NewPublicHealthResponseDto

`func NewPublicHealthResponseDto(status string, timestamp time.Time, version string, ) *PublicHealthResponseDto`

NewPublicHealthResponseDto instantiates a new PublicHealthResponseDto object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPublicHealthResponseDtoWithDefaults

`func NewPublicHealthResponseDtoWithDefaults() *PublicHealthResponseDto`

NewPublicHealthResponseDtoWithDefaults instantiates a new PublicHealthResponseDto object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetStatus

`func (o *PublicHealthResponseDto) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *PublicHealthResponseDto) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *PublicHealthResponseDto) SetStatus(v string)`

SetStatus sets Status field to given value.


### GetTimestamp

`func (o *PublicHealthResponseDto) GetTimestamp() time.Time`

GetTimestamp returns the Timestamp field if non-nil, zero value otherwise.

### GetTimestampOk

`func (o *PublicHealthResponseDto) GetTimestampOk() (*time.Time, bool)`

GetTimestampOk returns a tuple with the Timestamp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTimestamp

`func (o *PublicHealthResponseDto) SetTimestamp(v time.Time)`

SetTimestamp sets Timestamp field to given value.


### GetVersion

`func (o *PublicHealthResponseDto) GetVersion() string`

GetVersion returns the Version field if non-nil, zero value otherwise.

### GetVersionOk

`func (o *PublicHealthResponseDto) GetVersionOk() (*string, bool)`

GetVersionOk returns a tuple with the Version field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVersion

`func (o *PublicHealthResponseDto) SetVersion(v string)`

SetVersion sets Version field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


