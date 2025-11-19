# CreateStablePaymentIntentDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**SourceCurrency** | [**StableCoinCurrency**](StableCoinCurrency.md) | The stablecoin currency to convert FROM. This is the currency the customer will pay with. | 
**SourceNetwork** | [**BridgePaymentRail**](BridgePaymentRail.md) | The blockchain network where the source currency resides. Determines gas fees and transaction speed. | 
**DestinationCurrency** | Pointer to [**StableCoinCurrency**](StableCoinCurrency.md) | The stablecoin currency to convert TO. If omitted, defaults to the same as source currency (cross-chain transfer). | [optional] 
**DestinationNetwork** | [**BridgePaymentRail**](BridgePaymentRail.md) | The blockchain network where the converted currency will be delivered. Must support the destination currency. | 
**DestinationAddress** | Pointer to **string** | The wallet address where converted funds will be sent. Supports Ethereum (0x...) and Solana address formats. | [optional] 
**Amount** | Pointer to **string** | Payment amount in the source currency. Omit for flexible amount payments where users specify the amount during checkout. | [optional] 
**CustomerFirstName** | Pointer to **string** | Customer&#39;s first name. Used for transaction records and compliance. Required for amounts over $1000. | [optional] 
**CustomerLastName** | Pointer to **string** | Customer&#39;s last name. Used for transaction records and compliance. Required for amounts over $1000. | [optional] 
**CustomerEmail** | Pointer to **string** | Customer&#39;s email address. Used for transaction notifications and receipts. Highly recommended for all transactions. | [optional] 
**CustomerAddress** | Pointer to **string** | Customer&#39;s full address. Required for compliance in certain jurisdictions and high-value transactions. | [optional] 
**CustomerCountry** | Pointer to **string** | Customer&#39;s country of residence. Used for compliance and tax reporting. | [optional] 
**CustomerCountryISO** | Pointer to **string** | Customer&#39;s country ISO 3166-1 alpha-2 code. Used for automated compliance checks. | [optional] 
**CustomerProvince** | Pointer to **string** | Customer&#39;s state or province. Required for US and Canadian customers. | [optional] 
**CustomerProvinceISO** | Pointer to **string** | Customer&#39;s state or province ISO code. Used for automated tax calculations. | [optional] 
**PhoneNumber** | Pointer to **string** | Customer&#39;s phone number with country code. Used for SMS notifications and verification. | [optional] 

## Methods

### NewCreateStablePaymentIntentDto

`func NewCreateStablePaymentIntentDto(sourceCurrency StableCoinCurrency, sourceNetwork BridgePaymentRail, destinationNetwork BridgePaymentRail, ) *CreateStablePaymentIntentDto`

NewCreateStablePaymentIntentDto instantiates a new CreateStablePaymentIntentDto object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateStablePaymentIntentDtoWithDefaults

`func NewCreateStablePaymentIntentDtoWithDefaults() *CreateStablePaymentIntentDto`

NewCreateStablePaymentIntentDtoWithDefaults instantiates a new CreateStablePaymentIntentDto object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSourceCurrency

`func (o *CreateStablePaymentIntentDto) GetSourceCurrency() StableCoinCurrency`

GetSourceCurrency returns the SourceCurrency field if non-nil, zero value otherwise.

### GetSourceCurrencyOk

`func (o *CreateStablePaymentIntentDto) GetSourceCurrencyOk() (*StableCoinCurrency, bool)`

GetSourceCurrencyOk returns a tuple with the SourceCurrency field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSourceCurrency

`func (o *CreateStablePaymentIntentDto) SetSourceCurrency(v StableCoinCurrency)`

SetSourceCurrency sets SourceCurrency field to given value.


### GetSourceNetwork

`func (o *CreateStablePaymentIntentDto) GetSourceNetwork() BridgePaymentRail`

GetSourceNetwork returns the SourceNetwork field if non-nil, zero value otherwise.

### GetSourceNetworkOk

`func (o *CreateStablePaymentIntentDto) GetSourceNetworkOk() (*BridgePaymentRail, bool)`

GetSourceNetworkOk returns a tuple with the SourceNetwork field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSourceNetwork

`func (o *CreateStablePaymentIntentDto) SetSourceNetwork(v BridgePaymentRail)`

SetSourceNetwork sets SourceNetwork field to given value.


### GetDestinationCurrency

`func (o *CreateStablePaymentIntentDto) GetDestinationCurrency() StableCoinCurrency`

GetDestinationCurrency returns the DestinationCurrency field if non-nil, zero value otherwise.

### GetDestinationCurrencyOk

`func (o *CreateStablePaymentIntentDto) GetDestinationCurrencyOk() (*StableCoinCurrency, bool)`

GetDestinationCurrencyOk returns a tuple with the DestinationCurrency field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDestinationCurrency

`func (o *CreateStablePaymentIntentDto) SetDestinationCurrency(v StableCoinCurrency)`

SetDestinationCurrency sets DestinationCurrency field to given value.

### HasDestinationCurrency

`func (o *CreateStablePaymentIntentDto) HasDestinationCurrency() bool`

HasDestinationCurrency returns a boolean if a field has been set.

### GetDestinationNetwork

`func (o *CreateStablePaymentIntentDto) GetDestinationNetwork() BridgePaymentRail`

GetDestinationNetwork returns the DestinationNetwork field if non-nil, zero value otherwise.

### GetDestinationNetworkOk

`func (o *CreateStablePaymentIntentDto) GetDestinationNetworkOk() (*BridgePaymentRail, bool)`

GetDestinationNetworkOk returns a tuple with the DestinationNetwork field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDestinationNetwork

`func (o *CreateStablePaymentIntentDto) SetDestinationNetwork(v BridgePaymentRail)`

SetDestinationNetwork sets DestinationNetwork field to given value.


### GetDestinationAddress

`func (o *CreateStablePaymentIntentDto) GetDestinationAddress() string`

GetDestinationAddress returns the DestinationAddress field if non-nil, zero value otherwise.

### GetDestinationAddressOk

`func (o *CreateStablePaymentIntentDto) GetDestinationAddressOk() (*string, bool)`

GetDestinationAddressOk returns a tuple with the DestinationAddress field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDestinationAddress

`func (o *CreateStablePaymentIntentDto) SetDestinationAddress(v string)`

SetDestinationAddress sets DestinationAddress field to given value.

### HasDestinationAddress

`func (o *CreateStablePaymentIntentDto) HasDestinationAddress() bool`

HasDestinationAddress returns a boolean if a field has been set.

### GetAmount

`func (o *CreateStablePaymentIntentDto) GetAmount() string`

GetAmount returns the Amount field if non-nil, zero value otherwise.

### GetAmountOk

`func (o *CreateStablePaymentIntentDto) GetAmountOk() (*string, bool)`

GetAmountOk returns a tuple with the Amount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAmount

`func (o *CreateStablePaymentIntentDto) SetAmount(v string)`

SetAmount sets Amount field to given value.

### HasAmount

`func (o *CreateStablePaymentIntentDto) HasAmount() bool`

HasAmount returns a boolean if a field has been set.

### GetCustomerFirstName

`func (o *CreateStablePaymentIntentDto) GetCustomerFirstName() string`

GetCustomerFirstName returns the CustomerFirstName field if non-nil, zero value otherwise.

### GetCustomerFirstNameOk

`func (o *CreateStablePaymentIntentDto) GetCustomerFirstNameOk() (*string, bool)`

GetCustomerFirstNameOk returns a tuple with the CustomerFirstName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomerFirstName

`func (o *CreateStablePaymentIntentDto) SetCustomerFirstName(v string)`

SetCustomerFirstName sets CustomerFirstName field to given value.

### HasCustomerFirstName

`func (o *CreateStablePaymentIntentDto) HasCustomerFirstName() bool`

HasCustomerFirstName returns a boolean if a field has been set.

### GetCustomerLastName

`func (o *CreateStablePaymentIntentDto) GetCustomerLastName() string`

GetCustomerLastName returns the CustomerLastName field if non-nil, zero value otherwise.

### GetCustomerLastNameOk

`func (o *CreateStablePaymentIntentDto) GetCustomerLastNameOk() (*string, bool)`

GetCustomerLastNameOk returns a tuple with the CustomerLastName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomerLastName

`func (o *CreateStablePaymentIntentDto) SetCustomerLastName(v string)`

SetCustomerLastName sets CustomerLastName field to given value.

### HasCustomerLastName

`func (o *CreateStablePaymentIntentDto) HasCustomerLastName() bool`

HasCustomerLastName returns a boolean if a field has been set.

### GetCustomerEmail

`func (o *CreateStablePaymentIntentDto) GetCustomerEmail() string`

GetCustomerEmail returns the CustomerEmail field if non-nil, zero value otherwise.

### GetCustomerEmailOk

`func (o *CreateStablePaymentIntentDto) GetCustomerEmailOk() (*string, bool)`

GetCustomerEmailOk returns a tuple with the CustomerEmail field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomerEmail

`func (o *CreateStablePaymentIntentDto) SetCustomerEmail(v string)`

SetCustomerEmail sets CustomerEmail field to given value.

### HasCustomerEmail

`func (o *CreateStablePaymentIntentDto) HasCustomerEmail() bool`

HasCustomerEmail returns a boolean if a field has been set.

### GetCustomerAddress

`func (o *CreateStablePaymentIntentDto) GetCustomerAddress() string`

GetCustomerAddress returns the CustomerAddress field if non-nil, zero value otherwise.

### GetCustomerAddressOk

`func (o *CreateStablePaymentIntentDto) GetCustomerAddressOk() (*string, bool)`

GetCustomerAddressOk returns a tuple with the CustomerAddress field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomerAddress

`func (o *CreateStablePaymentIntentDto) SetCustomerAddress(v string)`

SetCustomerAddress sets CustomerAddress field to given value.

### HasCustomerAddress

`func (o *CreateStablePaymentIntentDto) HasCustomerAddress() bool`

HasCustomerAddress returns a boolean if a field has been set.

### GetCustomerCountry

`func (o *CreateStablePaymentIntentDto) GetCustomerCountry() string`

GetCustomerCountry returns the CustomerCountry field if non-nil, zero value otherwise.

### GetCustomerCountryOk

`func (o *CreateStablePaymentIntentDto) GetCustomerCountryOk() (*string, bool)`

GetCustomerCountryOk returns a tuple with the CustomerCountry field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomerCountry

`func (o *CreateStablePaymentIntentDto) SetCustomerCountry(v string)`

SetCustomerCountry sets CustomerCountry field to given value.

### HasCustomerCountry

`func (o *CreateStablePaymentIntentDto) HasCustomerCountry() bool`

HasCustomerCountry returns a boolean if a field has been set.

### GetCustomerCountryISO

`func (o *CreateStablePaymentIntentDto) GetCustomerCountryISO() string`

GetCustomerCountryISO returns the CustomerCountryISO field if non-nil, zero value otherwise.

### GetCustomerCountryISOOk

`func (o *CreateStablePaymentIntentDto) GetCustomerCountryISOOk() (*string, bool)`

GetCustomerCountryISOOk returns a tuple with the CustomerCountryISO field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomerCountryISO

`func (o *CreateStablePaymentIntentDto) SetCustomerCountryISO(v string)`

SetCustomerCountryISO sets CustomerCountryISO field to given value.

### HasCustomerCountryISO

`func (o *CreateStablePaymentIntentDto) HasCustomerCountryISO() bool`

HasCustomerCountryISO returns a boolean if a field has been set.

### GetCustomerProvince

`func (o *CreateStablePaymentIntentDto) GetCustomerProvince() string`

GetCustomerProvince returns the CustomerProvince field if non-nil, zero value otherwise.

### GetCustomerProvinceOk

`func (o *CreateStablePaymentIntentDto) GetCustomerProvinceOk() (*string, bool)`

GetCustomerProvinceOk returns a tuple with the CustomerProvince field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomerProvince

`func (o *CreateStablePaymentIntentDto) SetCustomerProvince(v string)`

SetCustomerProvince sets CustomerProvince field to given value.

### HasCustomerProvince

`func (o *CreateStablePaymentIntentDto) HasCustomerProvince() bool`

HasCustomerProvince returns a boolean if a field has been set.

### GetCustomerProvinceISO

`func (o *CreateStablePaymentIntentDto) GetCustomerProvinceISO() string`

GetCustomerProvinceISO returns the CustomerProvinceISO field if non-nil, zero value otherwise.

### GetCustomerProvinceISOOk

`func (o *CreateStablePaymentIntentDto) GetCustomerProvinceISOOk() (*string, bool)`

GetCustomerProvinceISOOk returns a tuple with the CustomerProvinceISO field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomerProvinceISO

`func (o *CreateStablePaymentIntentDto) SetCustomerProvinceISO(v string)`

SetCustomerProvinceISO sets CustomerProvinceISO field to given value.

### HasCustomerProvinceISO

`func (o *CreateStablePaymentIntentDto) HasCustomerProvinceISO() bool`

HasCustomerProvinceISO returns a boolean if a field has been set.

### GetPhoneNumber

`func (o *CreateStablePaymentIntentDto) GetPhoneNumber() string`

GetPhoneNumber returns the PhoneNumber field if non-nil, zero value otherwise.

### GetPhoneNumberOk

`func (o *CreateStablePaymentIntentDto) GetPhoneNumberOk() (*string, bool)`

GetPhoneNumberOk returns a tuple with the PhoneNumber field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPhoneNumber

`func (o *CreateStablePaymentIntentDto) SetPhoneNumber(v string)`

SetPhoneNumber sets PhoneNumber field to given value.

### HasPhoneNumber

`func (o *CreateStablePaymentIntentDto) HasPhoneNumber() bool`

HasPhoneNumber returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


