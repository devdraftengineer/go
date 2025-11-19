# UpdateTaxDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | Pointer to **string** | Tax name for identification and display purposes | [optional] 
**Description** | Pointer to **string** | Detailed description of what this tax covers | [optional] 
**Percentage** | Pointer to **float32** | Tax rate as a percentage (0-100) | [optional] 
**Active** | Pointer to **bool** | Whether this tax is currently active and can be applied | [optional] 
**AppIds** | Pointer to **[]string** | Array of app IDs where this tax should be available | [optional] 

## Methods

### NewUpdateTaxDto

`func NewUpdateTaxDto() *UpdateTaxDto`

NewUpdateTaxDto instantiates a new UpdateTaxDto object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUpdateTaxDtoWithDefaults

`func NewUpdateTaxDtoWithDefaults() *UpdateTaxDto`

NewUpdateTaxDtoWithDefaults instantiates a new UpdateTaxDto object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *UpdateTaxDto) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *UpdateTaxDto) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *UpdateTaxDto) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *UpdateTaxDto) HasName() bool`

HasName returns a boolean if a field has been set.

### GetDescription

`func (o *UpdateTaxDto) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *UpdateTaxDto) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *UpdateTaxDto) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *UpdateTaxDto) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetPercentage

`func (o *UpdateTaxDto) GetPercentage() float32`

GetPercentage returns the Percentage field if non-nil, zero value otherwise.

### GetPercentageOk

`func (o *UpdateTaxDto) GetPercentageOk() (*float32, bool)`

GetPercentageOk returns a tuple with the Percentage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPercentage

`func (o *UpdateTaxDto) SetPercentage(v float32)`

SetPercentage sets Percentage field to given value.

### HasPercentage

`func (o *UpdateTaxDto) HasPercentage() bool`

HasPercentage returns a boolean if a field has been set.

### GetActive

`func (o *UpdateTaxDto) GetActive() bool`

GetActive returns the Active field if non-nil, zero value otherwise.

### GetActiveOk

`func (o *UpdateTaxDto) GetActiveOk() (*bool, bool)`

GetActiveOk returns a tuple with the Active field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActive

`func (o *UpdateTaxDto) SetActive(v bool)`

SetActive sets Active field to given value.

### HasActive

`func (o *UpdateTaxDto) HasActive() bool`

HasActive returns a boolean if a field has been set.

### GetAppIds

`func (o *UpdateTaxDto) GetAppIds() []string`

GetAppIds returns the AppIds field if non-nil, zero value otherwise.

### GetAppIdsOk

`func (o *UpdateTaxDto) GetAppIdsOk() (*[]string, bool)`

GetAppIdsOk returns a tuple with the AppIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAppIds

`func (o *UpdateTaxDto) SetAppIds(v []string)`

SetAppIds sets AppIds field to given value.

### HasAppIds

`func (o *UpdateTaxDto) HasAppIds() bool`

HasAppIds returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


