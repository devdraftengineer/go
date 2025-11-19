# UpdateCustomerDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**FirstName** | Pointer to **string** | Customer&#39;s first name. Used for personalization and legal documentation. | [optional] 
**LastName** | Pointer to **string** | Customer&#39;s last name. Used for personalization and legal documentation. | [optional] 
**Email** | Pointer to **string** | Customer&#39;s email address. Used for notifications, receipts, and account management. Must be a valid email format. | [optional] 
**PhoneNumber** | Pointer to **string** | Customer&#39;s phone number. Used for SMS notifications and verification. Include country code for international numbers. | [optional] 
**CustomerType** | Pointer to [**CustomerType**](CustomerType.md) | Type of customer account. Determines available features and compliance requirements. | [optional] [default to INDIVIDUAL]
**Status** | Pointer to [**CustomerStatus**](CustomerStatus.md) | Current status of the customer account. Controls access to services and features. | [optional] [default to ACTIVE]

## Methods

### NewUpdateCustomerDto

`func NewUpdateCustomerDto() *UpdateCustomerDto`

NewUpdateCustomerDto instantiates a new UpdateCustomerDto object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUpdateCustomerDtoWithDefaults

`func NewUpdateCustomerDtoWithDefaults() *UpdateCustomerDto`

NewUpdateCustomerDtoWithDefaults instantiates a new UpdateCustomerDto object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetFirstName

`func (o *UpdateCustomerDto) GetFirstName() string`

GetFirstName returns the FirstName field if non-nil, zero value otherwise.

### GetFirstNameOk

`func (o *UpdateCustomerDto) GetFirstNameOk() (*string, bool)`

GetFirstNameOk returns a tuple with the FirstName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFirstName

`func (o *UpdateCustomerDto) SetFirstName(v string)`

SetFirstName sets FirstName field to given value.

### HasFirstName

`func (o *UpdateCustomerDto) HasFirstName() bool`

HasFirstName returns a boolean if a field has been set.

### GetLastName

`func (o *UpdateCustomerDto) GetLastName() string`

GetLastName returns the LastName field if non-nil, zero value otherwise.

### GetLastNameOk

`func (o *UpdateCustomerDto) GetLastNameOk() (*string, bool)`

GetLastNameOk returns a tuple with the LastName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastName

`func (o *UpdateCustomerDto) SetLastName(v string)`

SetLastName sets LastName field to given value.

### HasLastName

`func (o *UpdateCustomerDto) HasLastName() bool`

HasLastName returns a boolean if a field has been set.

### GetEmail

`func (o *UpdateCustomerDto) GetEmail() string`

GetEmail returns the Email field if non-nil, zero value otherwise.

### GetEmailOk

`func (o *UpdateCustomerDto) GetEmailOk() (*string, bool)`

GetEmailOk returns a tuple with the Email field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmail

`func (o *UpdateCustomerDto) SetEmail(v string)`

SetEmail sets Email field to given value.

### HasEmail

`func (o *UpdateCustomerDto) HasEmail() bool`

HasEmail returns a boolean if a field has been set.

### GetPhoneNumber

`func (o *UpdateCustomerDto) GetPhoneNumber() string`

GetPhoneNumber returns the PhoneNumber field if non-nil, zero value otherwise.

### GetPhoneNumberOk

`func (o *UpdateCustomerDto) GetPhoneNumberOk() (*string, bool)`

GetPhoneNumberOk returns a tuple with the PhoneNumber field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPhoneNumber

`func (o *UpdateCustomerDto) SetPhoneNumber(v string)`

SetPhoneNumber sets PhoneNumber field to given value.

### HasPhoneNumber

`func (o *UpdateCustomerDto) HasPhoneNumber() bool`

HasPhoneNumber returns a boolean if a field has been set.

### GetCustomerType

`func (o *UpdateCustomerDto) GetCustomerType() CustomerType`

GetCustomerType returns the CustomerType field if non-nil, zero value otherwise.

### GetCustomerTypeOk

`func (o *UpdateCustomerDto) GetCustomerTypeOk() (*CustomerType, bool)`

GetCustomerTypeOk returns a tuple with the CustomerType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomerType

`func (o *UpdateCustomerDto) SetCustomerType(v CustomerType)`

SetCustomerType sets CustomerType field to given value.

### HasCustomerType

`func (o *UpdateCustomerDto) HasCustomerType() bool`

HasCustomerType returns a boolean if a field has been set.

### GetStatus

`func (o *UpdateCustomerDto) GetStatus() CustomerStatus`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *UpdateCustomerDto) GetStatusOk() (*CustomerStatus, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *UpdateCustomerDto) SetStatus(v CustomerStatus)`

SetStatus sets Status field to given value.

### HasStatus

`func (o *UpdateCustomerDto) HasStatus() bool`

HasStatus returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


