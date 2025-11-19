# WebhookResponseDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | Unique identifier for the webhook | 
**Name** | **string** | Name of the webhook | 
**Url** | **string** | URL where webhook events are sent | 
**IsActive** | **bool** | Whether the webhook is currently active | 
**Encrypted** | **bool** | Whether webhook payloads are encrypted | 
**CreatedAt** | **string** | Timestamp when the webhook was created | 
**UpdatedAt** | **string** | Timestamp when the webhook was last updated | 
**DeliveryStats** | **map[string]interface{}** | Webhook delivery statistics | 

## Methods

### NewWebhookResponseDto

`func NewWebhookResponseDto(id string, name string, url string, isActive bool, encrypted bool, createdAt string, updatedAt string, deliveryStats map[string]interface{}, ) *WebhookResponseDto`

NewWebhookResponseDto instantiates a new WebhookResponseDto object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewWebhookResponseDtoWithDefaults

`func NewWebhookResponseDtoWithDefaults() *WebhookResponseDto`

NewWebhookResponseDtoWithDefaults instantiates a new WebhookResponseDto object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *WebhookResponseDto) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *WebhookResponseDto) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *WebhookResponseDto) SetId(v string)`

SetId sets Id field to given value.


### GetName

`func (o *WebhookResponseDto) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *WebhookResponseDto) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *WebhookResponseDto) SetName(v string)`

SetName sets Name field to given value.


### GetUrl

`func (o *WebhookResponseDto) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *WebhookResponseDto) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *WebhookResponseDto) SetUrl(v string)`

SetUrl sets Url field to given value.


### GetIsActive

`func (o *WebhookResponseDto) GetIsActive() bool`

GetIsActive returns the IsActive field if non-nil, zero value otherwise.

### GetIsActiveOk

`func (o *WebhookResponseDto) GetIsActiveOk() (*bool, bool)`

GetIsActiveOk returns a tuple with the IsActive field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsActive

`func (o *WebhookResponseDto) SetIsActive(v bool)`

SetIsActive sets IsActive field to given value.


### GetEncrypted

`func (o *WebhookResponseDto) GetEncrypted() bool`

GetEncrypted returns the Encrypted field if non-nil, zero value otherwise.

### GetEncryptedOk

`func (o *WebhookResponseDto) GetEncryptedOk() (*bool, bool)`

GetEncryptedOk returns a tuple with the Encrypted field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEncrypted

`func (o *WebhookResponseDto) SetEncrypted(v bool)`

SetEncrypted sets Encrypted field to given value.


### GetCreatedAt

`func (o *WebhookResponseDto) GetCreatedAt() string`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *WebhookResponseDto) GetCreatedAtOk() (*string, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *WebhookResponseDto) SetCreatedAt(v string)`

SetCreatedAt sets CreatedAt field to given value.


### GetUpdatedAt

`func (o *WebhookResponseDto) GetUpdatedAt() string`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *WebhookResponseDto) GetUpdatedAtOk() (*string, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *WebhookResponseDto) SetUpdatedAt(v string)`

SetUpdatedAt sets UpdatedAt field to given value.


### GetDeliveryStats

`func (o *WebhookResponseDto) GetDeliveryStats() map[string]interface{}`

GetDeliveryStats returns the DeliveryStats field if non-nil, zero value otherwise.

### GetDeliveryStatsOk

`func (o *WebhookResponseDto) GetDeliveryStatsOk() (*map[string]interface{}, bool)`

GetDeliveryStatsOk returns a tuple with the DeliveryStats field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDeliveryStats

`func (o *WebhookResponseDto) SetDeliveryStats(v map[string]interface{})`

SetDeliveryStats sets DeliveryStats field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


