# CreateWebhookDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** | Name of the webhook for identification purposes | 
**Url** | **string** | URL where webhook events will be sent | 
**IsActive** | **bool** | Whether the webhook is active and will receive events | [default to true]
**SigningSecret** | Pointer to **string** | Secret key used to sign webhook payloads for verification | [optional] 
**Encrypted** | **bool** | Whether webhook payloads should be encrypted | [default to false]

## Methods

### NewCreateWebhookDto

`func NewCreateWebhookDto(name string, url string, isActive bool, encrypted bool, ) *CreateWebhookDto`

NewCreateWebhookDto instantiates a new CreateWebhookDto object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateWebhookDtoWithDefaults

`func NewCreateWebhookDtoWithDefaults() *CreateWebhookDto`

NewCreateWebhookDtoWithDefaults instantiates a new CreateWebhookDto object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *CreateWebhookDto) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *CreateWebhookDto) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *CreateWebhookDto) SetName(v string)`

SetName sets Name field to given value.


### GetUrl

`func (o *CreateWebhookDto) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *CreateWebhookDto) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *CreateWebhookDto) SetUrl(v string)`

SetUrl sets Url field to given value.


### GetIsActive

`func (o *CreateWebhookDto) GetIsActive() bool`

GetIsActive returns the IsActive field if non-nil, zero value otherwise.

### GetIsActiveOk

`func (o *CreateWebhookDto) GetIsActiveOk() (*bool, bool)`

GetIsActiveOk returns a tuple with the IsActive field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsActive

`func (o *CreateWebhookDto) SetIsActive(v bool)`

SetIsActive sets IsActive field to given value.


### GetSigningSecret

`func (o *CreateWebhookDto) GetSigningSecret() string`

GetSigningSecret returns the SigningSecret field if non-nil, zero value otherwise.

### GetSigningSecretOk

`func (o *CreateWebhookDto) GetSigningSecretOk() (*string, bool)`

GetSigningSecretOk returns a tuple with the SigningSecret field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSigningSecret

`func (o *CreateWebhookDto) SetSigningSecret(v string)`

SetSigningSecret sets SigningSecret field to given value.

### HasSigningSecret

`func (o *CreateWebhookDto) HasSigningSecret() bool`

HasSigningSecret returns a boolean if a field has been set.

### GetEncrypted

`func (o *CreateWebhookDto) GetEncrypted() bool`

GetEncrypted returns the Encrypted field if non-nil, zero value otherwise.

### GetEncryptedOk

`func (o *CreateWebhookDto) GetEncryptedOk() (*bool, bool)`

GetEncryptedOk returns a tuple with the Encrypted field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEncrypted

`func (o *CreateWebhookDto) SetEncrypted(v bool)`

SetEncrypted sets Encrypted field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


