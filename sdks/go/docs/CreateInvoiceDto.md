# CreateInvoiceDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** | Name of the invoice | 
**Email** | **string** | Email address | 
**CustomerId** | **string** | Customer ID | 
**Currency** | **string** | Currency for the invoice | 
**Items** | **map[string]interface{}** |  | 
**DueDate** | **time.Time** | Due date of the invoice | 
**Delivery** | **string** | Delivery method | 
**PaymentLink** | **bool** | Whether to generate a payment link | 
**PaymentMethods** | **[]string** | Array of accepted payment methods | 
**Status** | **string** | Invoice status | 
**Address** | Pointer to **string** | Address | [optional] 
**PhoneNumber** | Pointer to **string** | Phone number | [optional] 
**SendDate** | Pointer to **time.Time** | Send date | [optional] 
**Logo** | Pointer to **string** | Logo URL | [optional] 
**PartialPayment** | **bool** | Allow partial payments | 
**TaxId** | Pointer to **string** | Tax ID | [optional] 

## Methods

### NewCreateInvoiceDto

`func NewCreateInvoiceDto(name string, email string, customerId string, currency string, items map[string]interface{}, dueDate time.Time, delivery string, paymentLink bool, paymentMethods []string, status string, partialPayment bool, ) *CreateInvoiceDto`

NewCreateInvoiceDto instantiates a new CreateInvoiceDto object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateInvoiceDtoWithDefaults

`func NewCreateInvoiceDtoWithDefaults() *CreateInvoiceDto`

NewCreateInvoiceDtoWithDefaults instantiates a new CreateInvoiceDto object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *CreateInvoiceDto) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *CreateInvoiceDto) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *CreateInvoiceDto) SetName(v string)`

SetName sets Name field to given value.


### GetEmail

`func (o *CreateInvoiceDto) GetEmail() string`

GetEmail returns the Email field if non-nil, zero value otherwise.

### GetEmailOk

`func (o *CreateInvoiceDto) GetEmailOk() (*string, bool)`

GetEmailOk returns a tuple with the Email field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmail

`func (o *CreateInvoiceDto) SetEmail(v string)`

SetEmail sets Email field to given value.


### GetCustomerId

`func (o *CreateInvoiceDto) GetCustomerId() string`

GetCustomerId returns the CustomerId field if non-nil, zero value otherwise.

### GetCustomerIdOk

`func (o *CreateInvoiceDto) GetCustomerIdOk() (*string, bool)`

GetCustomerIdOk returns a tuple with the CustomerId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomerId

`func (o *CreateInvoiceDto) SetCustomerId(v string)`

SetCustomerId sets CustomerId field to given value.


### GetCurrency

`func (o *CreateInvoiceDto) GetCurrency() string`

GetCurrency returns the Currency field if non-nil, zero value otherwise.

### GetCurrencyOk

`func (o *CreateInvoiceDto) GetCurrencyOk() (*string, bool)`

GetCurrencyOk returns a tuple with the Currency field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCurrency

`func (o *CreateInvoiceDto) SetCurrency(v string)`

SetCurrency sets Currency field to given value.


### GetItems

`func (o *CreateInvoiceDto) GetItems() map[string]interface{}`

GetItems returns the Items field if non-nil, zero value otherwise.

### GetItemsOk

`func (o *CreateInvoiceDto) GetItemsOk() (*map[string]interface{}, bool)`

GetItemsOk returns a tuple with the Items field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItems

`func (o *CreateInvoiceDto) SetItems(v map[string]interface{})`

SetItems sets Items field to given value.


### GetDueDate

`func (o *CreateInvoiceDto) GetDueDate() time.Time`

GetDueDate returns the DueDate field if non-nil, zero value otherwise.

### GetDueDateOk

`func (o *CreateInvoiceDto) GetDueDateOk() (*time.Time, bool)`

GetDueDateOk returns a tuple with the DueDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDueDate

`func (o *CreateInvoiceDto) SetDueDate(v time.Time)`

SetDueDate sets DueDate field to given value.


### GetDelivery

`func (o *CreateInvoiceDto) GetDelivery() string`

GetDelivery returns the Delivery field if non-nil, zero value otherwise.

### GetDeliveryOk

`func (o *CreateInvoiceDto) GetDeliveryOk() (*string, bool)`

GetDeliveryOk returns a tuple with the Delivery field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDelivery

`func (o *CreateInvoiceDto) SetDelivery(v string)`

SetDelivery sets Delivery field to given value.


### GetPaymentLink

`func (o *CreateInvoiceDto) GetPaymentLink() bool`

GetPaymentLink returns the PaymentLink field if non-nil, zero value otherwise.

### GetPaymentLinkOk

`func (o *CreateInvoiceDto) GetPaymentLinkOk() (*bool, bool)`

GetPaymentLinkOk returns a tuple with the PaymentLink field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPaymentLink

`func (o *CreateInvoiceDto) SetPaymentLink(v bool)`

SetPaymentLink sets PaymentLink field to given value.


### GetPaymentMethods

`func (o *CreateInvoiceDto) GetPaymentMethods() []string`

GetPaymentMethods returns the PaymentMethods field if non-nil, zero value otherwise.

### GetPaymentMethodsOk

`func (o *CreateInvoiceDto) GetPaymentMethodsOk() (*[]string, bool)`

GetPaymentMethodsOk returns a tuple with the PaymentMethods field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPaymentMethods

`func (o *CreateInvoiceDto) SetPaymentMethods(v []string)`

SetPaymentMethods sets PaymentMethods field to given value.


### GetStatus

`func (o *CreateInvoiceDto) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *CreateInvoiceDto) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *CreateInvoiceDto) SetStatus(v string)`

SetStatus sets Status field to given value.


### GetAddress

`func (o *CreateInvoiceDto) GetAddress() string`

GetAddress returns the Address field if non-nil, zero value otherwise.

### GetAddressOk

`func (o *CreateInvoiceDto) GetAddressOk() (*string, bool)`

GetAddressOk returns a tuple with the Address field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAddress

`func (o *CreateInvoiceDto) SetAddress(v string)`

SetAddress sets Address field to given value.

### HasAddress

`func (o *CreateInvoiceDto) HasAddress() bool`

HasAddress returns a boolean if a field has been set.

### GetPhoneNumber

`func (o *CreateInvoiceDto) GetPhoneNumber() string`

GetPhoneNumber returns the PhoneNumber field if non-nil, zero value otherwise.

### GetPhoneNumberOk

`func (o *CreateInvoiceDto) GetPhoneNumberOk() (*string, bool)`

GetPhoneNumberOk returns a tuple with the PhoneNumber field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPhoneNumber

`func (o *CreateInvoiceDto) SetPhoneNumber(v string)`

SetPhoneNumber sets PhoneNumber field to given value.

### HasPhoneNumber

`func (o *CreateInvoiceDto) HasPhoneNumber() bool`

HasPhoneNumber returns a boolean if a field has been set.

### GetSendDate

`func (o *CreateInvoiceDto) GetSendDate() time.Time`

GetSendDate returns the SendDate field if non-nil, zero value otherwise.

### GetSendDateOk

`func (o *CreateInvoiceDto) GetSendDateOk() (*time.Time, bool)`

GetSendDateOk returns a tuple with the SendDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSendDate

`func (o *CreateInvoiceDto) SetSendDate(v time.Time)`

SetSendDate sets SendDate field to given value.

### HasSendDate

`func (o *CreateInvoiceDto) HasSendDate() bool`

HasSendDate returns a boolean if a field has been set.

### GetLogo

`func (o *CreateInvoiceDto) GetLogo() string`

GetLogo returns the Logo field if non-nil, zero value otherwise.

### GetLogoOk

`func (o *CreateInvoiceDto) GetLogoOk() (*string, bool)`

GetLogoOk returns a tuple with the Logo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLogo

`func (o *CreateInvoiceDto) SetLogo(v string)`

SetLogo sets Logo field to given value.

### HasLogo

`func (o *CreateInvoiceDto) HasLogo() bool`

HasLogo returns a boolean if a field has been set.

### GetPartialPayment

`func (o *CreateInvoiceDto) GetPartialPayment() bool`

GetPartialPayment returns the PartialPayment field if non-nil, zero value otherwise.

### GetPartialPaymentOk

`func (o *CreateInvoiceDto) GetPartialPaymentOk() (*bool, bool)`

GetPartialPaymentOk returns a tuple with the PartialPayment field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPartialPayment

`func (o *CreateInvoiceDto) SetPartialPayment(v bool)`

SetPartialPayment sets PartialPayment field to given value.


### GetTaxId

`func (o *CreateInvoiceDto) GetTaxId() string`

GetTaxId returns the TaxId field if non-nil, zero value otherwise.

### GetTaxIdOk

`func (o *CreateInvoiceDto) GetTaxIdOk() (*string, bool)`

GetTaxIdOk returns a tuple with the TaxId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTaxId

`func (o *CreateInvoiceDto) SetTaxId(v string)`

SetTaxId sets TaxId field to given value.

### HasTaxId

`func (o *CreateInvoiceDto) HasTaxId() bool`

HasTaxId returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


