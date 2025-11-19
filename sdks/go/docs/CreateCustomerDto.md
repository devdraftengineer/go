# CreateCustomerDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**FirstName** | **string** | Customer&#39;s first name. Used for personalization and legal documentation. | 
**LastName** | **string** | Customer&#39;s last name. Used for personalization and legal documentation. | 
**Email** | Pointer to **string** | Customer&#39;s email address. Used for notifications, receipts, and account management. Must be a valid email format. | [optional] 
**PhoneNumber** | **string** | Customer&#39;s phone number. Used for SMS notifications and verification. Include country code for international numbers. | 
**CustomerType** | Pointer to [**CustomerType**](CustomerType.md) | Type of customer account. Determines available features and compliance requirements. | [optional] [default to INDIVIDUAL]
**Status** | Pointer to [**CustomerStatus**](CustomerStatus.md) | Current status of the customer account. Controls access to services and features. | [optional] [default to ACTIVE]

## Methods

### NewCreateCustomerDto

`func NewCreateCustomerDto(firstName string, lastName string, phoneNumber string, ) *CreateCustomerDto`

NewCreateCustomerDto instantiates a new CreateCustomerDto object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateCustomerDtoWithDefaults

`func NewCreateCustomerDtoWithDefaults() *CreateCustomerDto`

NewCreateCustomerDtoWithDefaults instantiates a new CreateCustomerDto object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetFirstName

`func (o *CreateCustomerDto) GetFirstName() string`

GetFirstName returns the FirstName field if non-nil, zero value otherwise.

### GetFirstNameOk

`func (o *CreateCustomerDto) GetFirstNameOk() (*string, bool)`

GetFirstNameOk returns a tuple with the FirstName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFirstName

`func (o *CreateCustomerDto) SetFirstName(v string)`

SetFirstName sets FirstName field to given value.


### GetLastName

`func (o *CreateCustomerDto) GetLastName() string`

GetLastName returns the LastName field if non-nil, zero value otherwise.

### GetLastNameOk

`func (o *CreateCustomerDto) GetLastNameOk() (*string, bool)`

GetLastNameOk returns a tuple with the LastName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastName

`func (o *CreateCustomerDto) SetLastName(v string)`

SetLastName sets LastName field to given value.


### GetEmail

`func (o *CreateCustomerDto) GetEmail() string`

GetEmail returns the Email field if non-nil, zero value otherwise.

### GetEmailOk

`func (o *CreateCustomerDto) GetEmailOk() (*string, bool)`

GetEmailOk returns a tuple with the Email field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmail

`func (o *CreateCustomerDto) SetEmail(v string)`

SetEmail sets Email field to given value.

### HasEmail

`func (o *CreateCustomerDto) HasEmail() bool`

HasEmail returns a boolean if a field has been set.

### GetPhoneNumber

`func (o *CreateCustomerDto) GetPhoneNumber() string`

GetPhoneNumber returns the PhoneNumber field if non-nil, zero value otherwise.

### GetPhoneNumberOk

`func (o *CreateCustomerDto) GetPhoneNumberOk() (*string, bool)`

GetPhoneNumberOk returns a tuple with the PhoneNumber field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPhoneNumber

`func (o *CreateCustomerDto) SetPhoneNumber(v string)`

SetPhoneNumber sets PhoneNumber field to given value.


### GetCustomerType

`func (o *CreateCustomerDto) GetCustomerType() CustomerType`

GetCustomerType returns the CustomerType field if non-nil, zero value otherwise.

### GetCustomerTypeOk

`func (o *CreateCustomerDto) GetCustomerTypeOk() (*CustomerType, bool)`

GetCustomerTypeOk returns a tuple with the CustomerType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomerType

`func (o *CreateCustomerDto) SetCustomerType(v CustomerType)`

SetCustomerType sets CustomerType field to given value.

### HasCustomerType

`func (o *CreateCustomerDto) HasCustomerType() bool`

HasCustomerType returns a boolean if a field has been set.

### GetStatus

`func (o *CreateCustomerDto) GetStatus() CustomerStatus`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *CreateCustomerDto) GetStatusOk() (*CustomerStatus, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *CreateCustomerDto) SetStatus(v CustomerStatus)`

SetStatus sets Status field to given value.

### HasStatus

`func (o *CreateCustomerDto) HasStatus() bool`

HasStatus returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


