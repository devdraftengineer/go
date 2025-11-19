# CreateTaxDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** | Tax name. Used to identify and reference this tax rate. | 
**Description** | Pointer to **string** | Optional description explaining what this tax covers. | [optional] 
**Percentage** | **float32** | Tax percentage rate. Must be between 0 and 100. | 
**Active** | Pointer to **bool** | Whether this tax is currently active and can be applied. | [optional] [default to true]
**AppIds** | Pointer to **[]string** | Array of app IDs where this tax should be available. If not provided, tax will be available for the current app. | [optional] 

## Methods

### NewCreateTaxDto

`func NewCreateTaxDto(name string, percentage float32, ) *CreateTaxDto`

NewCreateTaxDto instantiates a new CreateTaxDto object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateTaxDtoWithDefaults

`func NewCreateTaxDtoWithDefaults() *CreateTaxDto`

NewCreateTaxDtoWithDefaults instantiates a new CreateTaxDto object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *CreateTaxDto) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *CreateTaxDto) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *CreateTaxDto) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *CreateTaxDto) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *CreateTaxDto) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *CreateTaxDto) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *CreateTaxDto) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetPercentage

`func (o *CreateTaxDto) GetPercentage() float32`

GetPercentage returns the Percentage field if non-nil, zero value otherwise.

### GetPercentageOk

`func (o *CreateTaxDto) GetPercentageOk() (*float32, bool)`

GetPercentageOk returns a tuple with the Percentage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPercentage

`func (o *CreateTaxDto) SetPercentage(v float32)`

SetPercentage sets Percentage field to given value.


### GetActive

`func (o *CreateTaxDto) GetActive() bool`

GetActive returns the Active field if non-nil, zero value otherwise.

### GetActiveOk

`func (o *CreateTaxDto) GetActiveOk() (*bool, bool)`

GetActiveOk returns a tuple with the Active field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActive

`func (o *CreateTaxDto) SetActive(v bool)`

SetActive sets Active field to given value.

### HasActive

`func (o *CreateTaxDto) HasActive() bool`

HasActive returns a boolean if a field has been set.

### GetAppIds

`func (o *CreateTaxDto) GetAppIds() []string`

GetAppIds returns the AppIds field if non-nil, zero value otherwise.

### GetAppIdsOk

`func (o *CreateTaxDto) GetAppIdsOk() (*[]string, bool)`

GetAppIdsOk returns a tuple with the AppIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAppIds

`func (o *CreateTaxDto) SetAppIds(v []string)`

SetAppIds sets AppIds field to given value.

### HasAppIds

`func (o *CreateTaxDto) HasAppIds() bool`

HasAppIds returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


