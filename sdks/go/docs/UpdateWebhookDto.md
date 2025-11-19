# UpdateWebhookDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | Pointer to **string** | Name of the webhook for identification purposes | [optional] 
**Url** | Pointer to **string** | URL where webhook events will be sent | [optional] 
**IsActive** | Pointer to **bool** | Whether the webhook is active and will receive events | [optional] [default to true]
**SigningSecret** | Pointer to **string** | Secret key used to sign webhook payloads for verification | [optional] 
**Encrypted** | Pointer to **bool** | Whether webhook payloads should be encrypted | [optional] [default to false]

## Methods

### NewUpdateWebhookDto

`func NewUpdateWebhookDto() *UpdateWebhookDto`

NewUpdateWebhookDto instantiates a new UpdateWebhookDto object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUpdateWebhookDtoWithDefaults

`func NewUpdateWebhookDtoWithDefaults() *UpdateWebhookDto`

NewUpdateWebhookDtoWithDefaults instantiates a new UpdateWebhookDto object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *UpdateWebhookDto) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *UpdateWebhookDto) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *UpdateWebhookDto) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *UpdateWebhookDto) HasName() bool`

HasName returns a boolean if a field has been set.

### GetUrl

`func (o *UpdateWebhookDto) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *UpdateWebhookDto) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *UpdateWebhookDto) SetUrl(v string)`

SetUrl sets Url field to given value.

### HasUrl

`func (o *UpdateWebhookDto) HasUrl() bool`

HasUrl returns a boolean if a field has been set.

### GetIsActive

`func (o *UpdateWebhookDto) GetIsActive() bool`

GetIsActive returns the IsActive field if non-nil, zero value otherwise.

### GetIsActiveOk

`func (o *UpdateWebhookDto) GetIsActiveOk() (*bool, bool)`

GetIsActiveOk returns a tuple with the IsActive field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsActive

`func (o *UpdateWebhookDto) SetIsActive(v bool)`

SetIsActive sets IsActive field to given value.

### HasIsActive

`func (o *UpdateWebhookDto) HasIsActive() bool`

HasIsActive returns a boolean if a field has been set.

### GetSigningSecret

`func (o *UpdateWebhookDto) GetSigningSecret() string`

GetSigningSecret returns the SigningSecret field if non-nil, zero value otherwise.

### GetSigningSecretOk

`func (o *UpdateWebhookDto) GetSigningSecretOk() (*string, bool)`

GetSigningSecretOk returns a tuple with the SigningSecret field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSigningSecret

`func (o *UpdateWebhookDto) SetSigningSecret(v string)`

SetSigningSecret sets SigningSecret field to given value.

### HasSigningSecret

`func (o *UpdateWebhookDto) HasSigningSecret() bool`

HasSigningSecret returns a boolean if a field has been set.

### GetEncrypted

`func (o *UpdateWebhookDto) GetEncrypted() bool`

GetEncrypted returns the Encrypted field if non-nil, zero value otherwise.

### GetEncryptedOk

`func (o *UpdateWebhookDto) GetEncryptedOk() (*bool, bool)`

GetEncryptedOk returns a tuple with the Encrypted field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEncrypted

`func (o *UpdateWebhookDto) SetEncrypted(v bool)`

SetEncrypted sets Encrypted field to given value.

### HasEncrypted

`func (o *UpdateWebhookDto) HasEncrypted() bool`

HasEncrypted returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


