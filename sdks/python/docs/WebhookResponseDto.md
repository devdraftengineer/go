# WebhookResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the webhook | 
**name** | **str** | Name of the webhook | 
**url** | **str** | URL where webhook events are sent | 
**is_active** | **bool** | Whether the webhook is currently active | 
**encrypted** | **bool** | Whether webhook payloads are encrypted | 
**created_at** | **str** | Timestamp when the webhook was created | 
**updated_at** | **str** | Timestamp when the webhook was last updated | 
**delivery_stats** | **object** | Webhook delivery statistics | 

## Example

```python
from devdraft.models.webhook_response_dto import WebhookResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookResponseDto from a JSON string
webhook_response_dto_instance = WebhookResponseDto.from_json(json)
# print the JSON string representation of the object
print(WebhookResponseDto.to_json())

# convert the object into a dict
webhook_response_dto_dict = webhook_response_dto_instance.to_dict()
# create an instance of WebhookResponseDto from a dict
webhook_response_dto_from_dict = WebhookResponseDto.from_dict(webhook_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


