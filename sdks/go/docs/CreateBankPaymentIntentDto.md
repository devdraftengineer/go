# CreateBankPaymentIntentDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**SourcePaymentRail** | [**BridgePaymentRail**](BridgePaymentRail.md) | The banking payment method to use for the transfer. Determines processing time and fees. | 
**SourceCurrency** | [**FiatCurrency**](FiatCurrency.md) | The fiat currency to convert FROM. Must match the currency of the source payment rail. | [default to USD]
**DestinationCurrency** | [**StableCoinCurrency**](StableCoinCurrency.md) | The stablecoin currency to convert TO. The customer will receive this currency. | 
**DestinationNetwork** | [**BridgePaymentRail**](BridgePaymentRail.md) | The blockchain network where the stablecoin will be delivered. Must support the destination currency. | 
**DestinationAddress** | Pointer to **string** | Destination wallet address. Supports Ethereum (0x...) and Solana address formats. | [optional] 
**Amount** | Pointer to **string** | Payment amount (optional for flexible amount) | [optional] 
**CustomerFirstName** | Pointer to **string** | Customer first name | [optional] 
**CustomerLastName** | Pointer to **string** | Customer last name | [optional] 
**CustomerEmail** | Pointer to **string** | Customer email address | [optional] 
**CustomerAddress** | Pointer to **string** | Customer address | [optional] 
**CustomerCountry** | Pointer to **string** | Customer country | [optional] 
**CustomerCountryISO** | Pointer to **string** | Customer country ISO code | [optional] 
**CustomerProvince** | Pointer to **string** | Customer province/state | [optional] 
**CustomerProvinceISO** | Pointer to **string** | Customer province/state ISO code | [optional] 
**PhoneNumber** | Pointer to **string** | Customer phone number | [optional] 
**WireMessage** | Pointer to **string** | Wire transfer message (for WIRE transfers) | [optional] 
**SepaReference** | Pointer to **string** | SEPA reference (for SEPA transfers) | [optional] 
**AchReference** | Pointer to **string** | ACH reference (for ACH transfers) | [optional] 

## Methods

### NewCreateBankPaymentIntentDto

`func NewCreateBankPaymentIntentDto(sourcePaymentRail BridgePaymentRail, sourceCurrency FiatCurrency, destinationCurrency StableCoinCurrency, destinationNetwork BridgePaymentRail, ) *CreateBankPaymentIntentDto`

NewCreateBankPaymentIntentDto instantiates a new CreateBankPaymentIntentDto object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateBankPaymentIntentDtoWithDefaults

`func NewCreateBankPaymentIntentDtoWithDefaults() *CreateBankPaymentIntentDto`

NewCreateBankPaymentIntentDtoWithDefaults instantiates a new CreateBankPaymentIntentDto object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSourcePaymentRail

`func (o *CreateBankPaymentIntentDto) GetSourcePaymentRail() BridgePaymentRail`

GetSourcePaymentRail returns the SourcePaymentRail field if non-nil, zero value otherwise.

### GetSourcePaymentRailOk

`func (o *CreateBankPaymentIntentDto) GetSourcePaymentRailOk() (*BridgePaymentRail, bool)`

GetSourcePaymentRailOk returns a tuple with the SourcePaymentRail field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSourcePaymentRail

`func (o *CreateBankPaymentIntentDto) SetSourcePaymentRail(v BridgePaymentRail)`

SetSourcePaymentRail sets SourcePaymentRail field to given value.


### GetSourceCurrency

`func (o *CreateBankPaymentIntentDto) GetSourceCurrency() FiatCurrency`

GetSourceCurrency returns the SourceCurrency field if non-nil, zero value otherwise.

### GetSourceCurrencyOk

`func (o *CreateBankPaymentIntentDto) GetSourceCurrencyOk() (*FiatCurrency, bool)`

GetSourceCurrencyOk returns a tuple with the SourceCurrency field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSourceCurrency

`func (o *CreateBankPaymentIntentDto) SetSourceCurrency(v FiatCurrency)`

SetSourceCurrency sets SourceCurrency field to given value.


### GetDestinationCurrency

`func (o *CreateBankPaymentIntentDto) GetDestinationCurrency() StableCoinCurrency`

GetDestinationCurrency returns the DestinationCurrency field if non-nil, zero value otherwise.

### GetDestinationCurrencyOk

`func (o *CreateBankPaymentIntentDto) GetDestinationCurrencyOk() (*StableCoinCurrency, bool)`

GetDestinationCurrencyOk returns a tuple with the DestinationCurrency field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDestinationCurrency

`func (o *CreateBankPaymentIntentDto) SetDestinationCurrency(v StableCoinCurrency)`

SetDestinationCurrency sets DestinationCurrency field to given value.


### GetDestinationNetwork

`func (o *CreateBankPaymentIntentDto) GetDestinationNetwork() BridgePaymentRail`

GetDestinationNetwork returns the DestinationNetwork field if non-nil, zero value otherwise.

### GetDestinationNetworkOk

`func (o *CreateBankPaymentIntentDto) GetDestinationNetworkOk() (*BridgePaymentRail, bool)`

GetDestinationNetworkOk returns a tuple with the DestinationNetwork field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDestinationNetwork

`func (o *CreateBankPaymentIntentDto) SetDestinationNetwork(v BridgePaymentRail)`

SetDestinationNetwork sets DestinationNetwork field to given value.


### GetDestinationAddress

`func (o *CreateBankPaymentIntentDto) GetDestinationAddress() string`

GetDestinationAddress returns the DestinationAddress field if non-nil, zero value otherwise.

### GetDestinationAddressOk

`func (o *CreateBankPaymentIntentDto) GetDestinationAddressOk() (*string, bool)`

GetDestinationAddressOk returns a tuple with the DestinationAddress field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDestinationAddress

`func (o *CreateBankPaymentIntentDto) SetDestinationAddress(v string)`

SetDestinationAddress sets DestinationAddress field to given value.

### HasDestinationAddress

`func (o *CreateBankPaymentIntentDto) HasDestinationAddress() bool`

HasDestinationAddress returns a boolean if a field has been set.

### GetAmount

`func (o *CreateBankPaymentIntentDto) GetAmount() string`

GetAmount returns the Amount field if non-nil, zero value otherwise.

### GetAmountOk

`func (o *CreateBankPaymentIntentDto) GetAmountOk() (*string, bool)`

GetAmountOk returns a tuple with the Amount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAmount

`func (o *CreateBankPaymentIntentDto) SetAmount(v string)`

SetAmount sets Amount field to given value.

### HasAmount

`func (o *CreateBankPaymentIntentDto) HasAmount() bool`

HasAmount returns a boolean if a field has been set.

### GetCustomerFirstName

`func (o *CreateBankPaymentIntentDto) GetCustomerFirstName() string`

GetCustomerFirstName returns the CustomerFirstName field if non-nil, zero value otherwise.

### GetCustomerFirstNameOk

`func (o *CreateBankPaymentIntentDto) GetCustomerFirstNameOk() (*string, bool)`

GetCustomerFirstNameOk returns a tuple with the CustomerFirstName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomerFirstName

`func (o *CreateBankPaymentIntentDto) SetCustomerFirstName(v string)`

SetCustomerFirstName sets CustomerFirstName field to given value.

### HasCustomerFirstName

`func (o *CreateBankPaymentIntentDto) HasCustomerFirstName() bool`

HasCustomerFirstName returns a boolean if a field has been set.

### GetCustomerLastName

`func (o *CreateBankPaymentIntentDto) GetCustomerLastName() string`

GetCustomerLastName returns the CustomerLastName field if non-nil, zero value otherwise.

### GetCustomerLastNameOk

`func (o *CreateBankPaymentIntentDto) GetCustomerLastNameOk() (*string, bool)`

GetCustomerLastNameOk returns a tuple with the CustomerLastName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomerLastName

`func (o *CreateBankPaymentIntentDto) SetCustomerLastName(v string)`

SetCustomerLastName sets CustomerLastName field to given value.

### HasCustomerLastName

`func (o *CreateBankPaymentIntentDto) HasCustomerLastName() bool`

HasCustomerLastName returns a boolean if a field has been set.

### GetCustomerEmail

`func (o *CreateBankPaymentIntentDto) GetCustomerEmail() string`

GetCustomerEmail returns the CustomerEmail field if non-nil, zero value otherwise.

### GetCustomerEmailOk

`func (o *CreateBankPaymentIntentDto) GetCustomerEmailOk() (*string, bool)`

GetCustomerEmailOk returns a tuple with the CustomerEmail field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomerEmail

`func (o *CreateBankPaymentIntentDto) SetCustomerEmail(v string)`

SetCustomerEmail sets CustomerEmail field to given value.

### HasCustomerEmail

`func (o *CreateBankPaymentIntentDto) HasCustomerEmail() bool`

HasCustomerEmail returns a boolean if a field has been set.

### GetCustomerAddress

`func (o *CreateBankPaymentIntentDto) GetCustomerAddress() string`

GetCustomerAddress returns the CustomerAddress field if non-nil, zero value otherwise.

### GetCustomerAddressOk

`func (o *CreateBankPaymentIntentDto) GetCustomerAddressOk() (*string, bool)`

GetCustomerAddressOk returns a tuple with the CustomerAddress field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomerAddress

`func (o *CreateBankPaymentIntentDto) SetCustomerAddress(v string)`

SetCustomerAddress sets CustomerAddress field to given value.

### HasCustomerAddress

`func (o *CreateBankPaymentIntentDto) HasCustomerAddress() bool`

HasCustomerAddress returns a boolean if a field has been set.

### GetCustomerCountry

`func (o *CreateBankPaymentIntentDto) GetCustomerCountry() string`

GetCustomerCountry returns the CustomerCountry field if non-nil, zero value otherwise.

### GetCustomerCountryOk

`func (o *CreateBankPaymentIntentDto) GetCustomerCountryOk() (*string, bool)`

GetCustomerCountryOk returns a tuple with the CustomerCountry field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomerCountry

`func (o *CreateBankPaymentIntentDto) SetCustomerCountry(v string)`

SetCustomerCountry sets CustomerCountry field to given value.

### HasCustomerCountry

`func (o *CreateBankPaymentIntentDto) HasCustomerCountry() bool`

HasCustomerCountry returns a boolean if a field has been set.

### GetCustomerCountryISO

`func (o *CreateBankPaymentIntentDto) GetCustomerCountryISO() string`

GetCustomerCountryISO returns the CustomerCountryISO field if non-nil, zero value otherwise.

### GetCustomerCountryISOOk

`func (o *CreateBankPaymentIntentDto) GetCustomerCountryISOOk() (*string, bool)`

GetCustomerCountryISOOk returns a tuple with the CustomerCountryISO field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomerCountryISO

`func (o *CreateBankPaymentIntentDto) SetCustomerCountryISO(v string)`

SetCustomerCountryISO sets CustomerCountryISO field to given value.

### HasCustomerCountryISO

`func (o *CreateBankPaymentIntentDto) HasCustomerCountryISO() bool`

HasCustomerCountryISO returns a boolean if a field has been set.

### GetCustomerProvince

`func (o *CreateBankPaymentIntentDto) GetCustomerProvince() string`

GetCustomerProvince returns the CustomerProvince field if non-nil, zero value otherwise.

### GetCustomerProvinceOk

`func (o *CreateBankPaymentIntentDto) GetCustomerProvinceOk() (*string, bool)`

GetCustomerProvinceOk returns a tuple with the CustomerProvince field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomerProvince

`func (o *CreateBankPaymentIntentDto) SetCustomerProvince(v string)`

SetCustomerProvince sets CustomerProvince field to given value.

### HasCustomerProvince

`func (o *CreateBankPaymentIntentDto) HasCustomerProvince() bool`

HasCustomerProvince returns a boolean if a field has been set.

### GetCustomerProvinceISO

`func (o *CreateBankPaymentIntentDto) GetCustomerProvinceISO() string`

GetCustomerProvinceISO returns the CustomerProvinceISO field if non-nil, zero value otherwise.

### GetCustomerProvinceISOOk

`func (o *CreateBankPaymentIntentDto) GetCustomerProvinceISOOk() (*string, bool)`

GetCustomerProvinceISOOk returns a tuple with the CustomerProvinceISO field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomerProvinceISO

`func (o *CreateBankPaymentIntentDto) SetCustomerProvinceISO(v string)`

SetCustomerProvinceISO sets CustomerProvinceISO field to given value.

### HasCustomerProvinceISO

`func (o *CreateBankPaymentIntentDto) HasCustomerProvinceISO() bool`

HasCustomerProvinceISO returns a boolean if a field has been set.

### GetPhoneNumber

`func (o *CreateBankPaymentIntentDto) GetPhoneNumber() string`

GetPhoneNumber returns the PhoneNumber field if non-nil, zero value otherwise.

### GetPhoneNumberOk

`func (o *CreateBankPaymentIntentDto) GetPhoneNumberOk() (*string, bool)`

GetPhoneNumberOk returns a tuple with the PhoneNumber field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPhoneNumber

`func (o *CreateBankPaymentIntentDto) SetPhoneNumber(v string)`

SetPhoneNumber sets PhoneNumber field to given value.

### HasPhoneNumber

`func (o *CreateBankPaymentIntentDto) HasPhoneNumber() bool`

HasPhoneNumber returns a boolean if a field has been set.

### GetWireMessage

`func (o *CreateBankPaymentIntentDto) GetWireMessage() string`

GetWireMessage returns the WireMessage field if non-nil, zero value otherwise.

### GetWireMessageOk

`func (o *CreateBankPaymentIntentDto) GetWireMessageOk() (*string, bool)`

GetWireMessageOk returns a tuple with the WireMessage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWireMessage

`func (o *CreateBankPaymentIntentDto) SetWireMessage(v string)`

SetWireMessage sets WireMessage field to given value.

### HasWireMessage

`func (o *CreateBankPaymentIntentDto) HasWireMessage() bool`

HasWireMessage returns a boolean if a field has been set.

### GetSepaReference

`func (o *CreateBankPaymentIntentDto) GetSepaReference() string`

GetSepaReference returns the SepaReference field if non-nil, zero value otherwise.

### GetSepaReferenceOk

`func (o *CreateBankPaymentIntentDto) GetSepaReferenceOk() (*string, bool)`

GetSepaReferenceOk returns a tuple with the SepaReference field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSepaReference

`func (o *CreateBankPaymentIntentDto) SetSepaReference(v string)`

SetSepaReference sets SepaReference field to given value.

### HasSepaReference

`func (o *CreateBankPaymentIntentDto) HasSepaReference() bool`

HasSepaReference returns a boolean if a field has been set.

### GetAchReference

`func (o *CreateBankPaymentIntentDto) GetAchReference() string`

GetAchReference returns the AchReference field if non-nil, zero value otherwise.

### GetAchReferenceOk

`func (o *CreateBankPaymentIntentDto) GetAchReferenceOk() (*string, bool)`

GetAchReferenceOk returns a tuple with the AchReference field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAchReference

`func (o *CreateBankPaymentIntentDto) SetAchReference(v string)`

SetAchReference sets AchReference field to given value.

### HasAchReference

`func (o *CreateBankPaymentIntentDto) HasAchReference() bool`

HasAchReference returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


