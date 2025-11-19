# CreatePaymentLinkDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Title** | **string** | Display title for the payment link. This appears on the checkout page and in customer communications. | 
**Url** | **string** | Unique URL slug for the payment link. Can be a full URL or just the path segment. Must be unique within your account. | 
**Description** | Pointer to **string** | Detailed description of what the customer is purchasing. Supports markdown formatting. | [optional] 
**CoverImage** | Pointer to **string** | Cover image URL | [optional] 
**LinkType** | **string** | Type of the payment link | 
**Amount** | Pointer to **float32** | Amount for the payment link | [optional] 
**PaymentForId** | Pointer to **string** | Payment for ID | [optional] 
**CustomerId** | Pointer to **string** | Customer ID | [optional] 
**PaymentLinkProducts** | Pointer to [**[]PaymentLinkProductDto**](PaymentLinkProductDto.md) | Array of products in the payment link | [optional] 
**IsForAllProduct** | Pointer to **bool** | Whether the payment link is for all products | [optional] [default to false]
**AllowQuantityAdjustment** | **bool** | Whether to allow quantity adjustment | [default to true]
**CollectTax** | **bool** | Whether to collect tax | [default to false]
**TaxId** | Pointer to **string** | Tax ID | [optional] 
**CollectAddress** | **bool** | Whether to collect address | [default to false]
**LimitPayments** | Pointer to **bool** | Whether to limit payments | [optional] [default to false]
**MaxPayments** | Pointer to **float32** | Maximum number of payments | [optional] 
**CustomFields** | Pointer to **map[string]interface{}** | Custom fields | [optional] 
**AllowMobilePayment** | **bool** | Whether to allow mobile payment | [default to false]
**Currency** | **string** | Currency | [default to "usdc"]
**ExpirationDate** | Pointer to **time.Time** | Expiration date | [optional] 

## Methods

### NewCreatePaymentLinkDto

`func NewCreatePaymentLinkDto(title string, url string, linkType string, allowQuantityAdjustment bool, collectTax bool, collectAddress bool, allowMobilePayment bool, currency string, ) *CreatePaymentLinkDto`

NewCreatePaymentLinkDto instantiates a new CreatePaymentLinkDto object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreatePaymentLinkDtoWithDefaults

`func NewCreatePaymentLinkDtoWithDefaults() *CreatePaymentLinkDto`

NewCreatePaymentLinkDtoWithDefaults instantiates a new CreatePaymentLinkDto object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetTitle

`func (o *CreatePaymentLinkDto) GetTitle() string`

GetTitle returns the Title field if non-nil, zero value otherwise.

### GetTitleOk

`func (o *CreatePaymentLinkDto) GetTitleOk() (*string, bool)`

GetTitleOk returns a tuple with the Title field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTitle

`func (o *CreatePaymentLinkDto) SetTitle(v string)`

SetTitle sets Title field to given value.


### GetUrl

`func (o *CreatePaymentLinkDto) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *CreatePaymentLinkDto) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *CreatePaymentLinkDto) SetUrl(v string)`

SetUrl sets Url field to given value.


### GetDescription

`func (o *CreatePaymentLinkDto) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *CreatePaymentLinkDto) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *CreatePaymentLinkDto) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *CreatePaymentLinkDto) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetCoverImage

`func (o *CreatePaymentLinkDto) GetCoverImage() string`

GetCoverImage returns the CoverImage field if non-nil, zero value otherwise.

### GetCoverImageOk

`func (o *CreatePaymentLinkDto) GetCoverImageOk() (*string, bool)`

GetCoverImageOk returns a tuple with the CoverImage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCoverImage

`func (o *CreatePaymentLinkDto) SetCoverImage(v string)`

SetCoverImage sets CoverImage field to given value.

### HasCoverImage

`func (o *CreatePaymentLinkDto) HasCoverImage() bool`

HasCoverImage returns a boolean if a field has been set.

### GetLinkType

`func (o *CreatePaymentLinkDto) GetLinkType() string`

GetLinkType returns the LinkType field if non-nil, zero value otherwise.

### GetLinkTypeOk

`func (o *CreatePaymentLinkDto) GetLinkTypeOk() (*string, bool)`

GetLinkTypeOk returns a tuple with the LinkType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLinkType

`func (o *CreatePaymentLinkDto) SetLinkType(v string)`

SetLinkType sets LinkType field to given value.


### GetAmount

`func (o *CreatePaymentLinkDto) GetAmount() float32`

GetAmount returns the Amount field if non-nil, zero value otherwise.

### GetAmountOk

`func (o *CreatePaymentLinkDto) GetAmountOk() (*float32, bool)`

GetAmountOk returns a tuple with the Amount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAmount

`func (o *CreatePaymentLinkDto) SetAmount(v float32)`

SetAmount sets Amount field to given value.

### HasAmount

`func (o *CreatePaymentLinkDto) HasAmount() bool`

HasAmount returns a boolean if a field has been set.

### GetPaymentForId

`func (o *CreatePaymentLinkDto) GetPaymentForId() string`

GetPaymentForId returns the PaymentForId field if non-nil, zero value otherwise.

### GetPaymentForIdOk

`func (o *CreatePaymentLinkDto) GetPaymentForIdOk() (*string, bool)`

GetPaymentForIdOk returns a tuple with the PaymentForId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPaymentForId

`func (o *CreatePaymentLinkDto) SetPaymentForId(v string)`

SetPaymentForId sets PaymentForId field to given value.

### HasPaymentForId

`func (o *CreatePaymentLinkDto) HasPaymentForId() bool`

HasPaymentForId returns a boolean if a field has been set.

### GetCustomerId

`func (o *CreatePaymentLinkDto) GetCustomerId() string`

GetCustomerId returns the CustomerId field if non-nil, zero value otherwise.

### GetCustomerIdOk

`func (o *CreatePaymentLinkDto) GetCustomerIdOk() (*string, bool)`

GetCustomerIdOk returns a tuple with the CustomerId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomerId

`func (o *CreatePaymentLinkDto) SetCustomerId(v string)`

SetCustomerId sets CustomerId field to given value.

### HasCustomerId

`func (o *CreatePaymentLinkDto) HasCustomerId() bool`

HasCustomerId returns a boolean if a field has been set.

### GetPaymentLinkProducts

`func (o *CreatePaymentLinkDto) GetPaymentLinkProducts() []PaymentLinkProductDto`

GetPaymentLinkProducts returns the PaymentLinkProducts field if non-nil, zero value otherwise.

### GetPaymentLinkProductsOk

`func (o *CreatePaymentLinkDto) GetPaymentLinkProductsOk() (*[]PaymentLinkProductDto, bool)`

GetPaymentLinkProductsOk returns a tuple with the PaymentLinkProducts field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPaymentLinkProducts

`func (o *CreatePaymentLinkDto) SetPaymentLinkProducts(v []PaymentLinkProductDto)`

SetPaymentLinkProducts sets PaymentLinkProducts field to given value.

### HasPaymentLinkProducts

`func (o *CreatePaymentLinkDto) HasPaymentLinkProducts() bool`

HasPaymentLinkProducts returns a boolean if a field has been set.

### GetIsForAllProduct

`func (o *CreatePaymentLinkDto) GetIsForAllProduct() bool`

GetIsForAllProduct returns the IsForAllProduct field if non-nil, zero value otherwise.

### GetIsForAllProductOk

`func (o *CreatePaymentLinkDto) GetIsForAllProductOk() (*bool, bool)`

GetIsForAllProductOk returns a tuple with the IsForAllProduct field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsForAllProduct

`func (o *CreatePaymentLinkDto) SetIsForAllProduct(v bool)`

SetIsForAllProduct sets IsForAllProduct field to given value.

### HasIsForAllProduct

`func (o *CreatePaymentLinkDto) HasIsForAllProduct() bool`

HasIsForAllProduct returns a boolean if a field has been set.

### GetAllowQuantityAdjustment

`func (o *CreatePaymentLinkDto) GetAllowQuantityAdjustment() bool`

GetAllowQuantityAdjustment returns the AllowQuantityAdjustment field if non-nil, zero value otherwise.

### GetAllowQuantityAdjustmentOk

`func (o *CreatePaymentLinkDto) GetAllowQuantityAdjustmentOk() (*bool, bool)`

GetAllowQuantityAdjustmentOk returns a tuple with the AllowQuantityAdjustment field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAllowQuantityAdjustment

`func (o *CreatePaymentLinkDto) SetAllowQuantityAdjustment(v bool)`

SetAllowQuantityAdjustment sets AllowQuantityAdjustment field to given value.


### GetCollectTax

`func (o *CreatePaymentLinkDto) GetCollectTax() bool`

GetCollectTax returns the CollectTax field if non-nil, zero value otherwise.

### GetCollectTaxOk

`func (o *CreatePaymentLinkDto) GetCollectTaxOk() (*bool, bool)`

GetCollectTaxOk returns a tuple with the CollectTax field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCollectTax

`func (o *CreatePaymentLinkDto) SetCollectTax(v bool)`

SetCollectTax sets CollectTax field to given value.


### GetTaxId

`func (o *CreatePaymentLinkDto) GetTaxId() string`

GetTaxId returns the TaxId field if non-nil, zero value otherwise.

### GetTaxIdOk

`func (o *CreatePaymentLinkDto) GetTaxIdOk() (*string, bool)`

GetTaxIdOk returns a tuple with the TaxId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTaxId

`func (o *CreatePaymentLinkDto) SetTaxId(v string)`

SetTaxId sets TaxId field to given value.

### HasTaxId

`func (o *CreatePaymentLinkDto) HasTaxId() bool`

HasTaxId returns a boolean if a field has been set.

### GetCollectAddress

`func (o *CreatePaymentLinkDto) GetCollectAddress() bool`

GetCollectAddress returns the CollectAddress field if non-nil, zero value otherwise.

### GetCollectAddressOk

`func (o *CreatePaymentLinkDto) GetCollectAddressOk() (*bool, bool)`

GetCollectAddressOk returns a tuple with the CollectAddress field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCollectAddress

`func (o *CreatePaymentLinkDto) SetCollectAddress(v bool)`

SetCollectAddress sets CollectAddress field to given value.


### GetLimitPayments

`func (o *CreatePaymentLinkDto) GetLimitPayments() bool`

GetLimitPayments returns the LimitPayments field if non-nil, zero value otherwise.

### GetLimitPaymentsOk

`func (o *CreatePaymentLinkDto) GetLimitPaymentsOk() (*bool, bool)`

GetLimitPaymentsOk returns a tuple with the LimitPayments field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLimitPayments

`func (o *CreatePaymentLinkDto) SetLimitPayments(v bool)`

SetLimitPayments sets LimitPayments field to given value.

### HasLimitPayments

`func (o *CreatePaymentLinkDto) HasLimitPayments() bool`

HasLimitPayments returns a boolean if a field has been set.

### GetMaxPayments

`func (o *CreatePaymentLinkDto) GetMaxPayments() float32`

GetMaxPayments returns the MaxPayments field if non-nil, zero value otherwise.

### GetMaxPaymentsOk

`func (o *CreatePaymentLinkDto) GetMaxPaymentsOk() (*float32, bool)`

GetMaxPaymentsOk returns a tuple with the MaxPayments field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxPayments

`func (o *CreatePaymentLinkDto) SetMaxPayments(v float32)`

SetMaxPayments sets MaxPayments field to given value.

### HasMaxPayments

`func (o *CreatePaymentLinkDto) HasMaxPayments() bool`

HasMaxPayments returns a boolean if a field has been set.

### GetCustomFields

`func (o *CreatePaymentLinkDto) GetCustomFields() map[string]interface{}`

GetCustomFields returns the CustomFields field if non-nil, zero value otherwise.

### GetCustomFieldsOk

`func (o *CreatePaymentLinkDto) GetCustomFieldsOk() (*map[string]interface{}, bool)`

GetCustomFieldsOk returns a tuple with the CustomFields field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomFields

`func (o *CreatePaymentLinkDto) SetCustomFields(v map[string]interface{})`

SetCustomFields sets CustomFields field to given value.

### HasCustomFields

`func (o *CreatePaymentLinkDto) HasCustomFields() bool`

HasCustomFields returns a boolean if a field has been set.

### GetAllowMobilePayment

`func (o *CreatePaymentLinkDto) GetAllowMobilePayment() bool`

GetAllowMobilePayment returns the AllowMobilePayment field if non-nil, zero value otherwise.

### GetAllowMobilePaymentOk

`func (o *CreatePaymentLinkDto) GetAllowMobilePaymentOk() (*bool, bool)`

GetAllowMobilePaymentOk returns a tuple with the AllowMobilePayment field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAllowMobilePayment

`func (o *CreatePaymentLinkDto) SetAllowMobilePayment(v bool)`

SetAllowMobilePayment sets AllowMobilePayment field to given value.


### GetCurrency

`func (o *CreatePaymentLinkDto) GetCurrency() string`

GetCurrency returns the Currency field if non-nil, zero value otherwise.

### GetCurrencyOk

`func (o *CreatePaymentLinkDto) GetCurrencyOk() (*string, bool)`

GetCurrencyOk returns a tuple with the Currency field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCurrency

`func (o *CreatePaymentLinkDto) SetCurrency(v string)`

SetCurrency sets Currency field to given value.


### GetExpirationDate

`func (o *CreatePaymentLinkDto) GetExpirationDate() time.Time`

GetExpirationDate returns the ExpirationDate field if non-nil, zero value otherwise.

### GetExpirationDateOk

`func (o *CreatePaymentLinkDto) GetExpirationDateOk() (*time.Time, bool)`

GetExpirationDateOk returns a tuple with the ExpirationDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpirationDate

`func (o *CreatePaymentLinkDto) SetExpirationDate(v time.Time)`

SetExpirationDate sets ExpirationDate field to given value.

### HasExpirationDate

`func (o *CreatePaymentLinkDto) HasExpirationDate() bool`

HasExpirationDate returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


