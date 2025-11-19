# UpdateWebhookDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the webhook for identification purposes | [optional] 
**url** | **str** | URL where webhook events will be sent | [optional] 
**is_active** | **bool** | Whether the webhook is active and will receive events | [optional] [default to True]
**signing_secret** | **str** | Secret key used to sign webhook payloads for verification | [optional] 
**encrypted** | **bool** | Whether webhook payloads should be encrypted | [optional] [default to False]

## Example

```python
from devdraft.models.update_webhook_dto import UpdateWebhookDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWebhookDto from a JSON string
update_webhook_dto_instance = UpdateWebhookDto.from_json(json)
# print the JSON string representation of the object
print(UpdateWebhookDto.to_json())

# convert the object into a dict
update_webhook_dto_dict = update_webhook_dto_instance.to_dict()
# create an instance of UpdateWebhookDto from a dict
update_webhook_dto_from_dict = UpdateWebhookDto.from_dict(update_webhook_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


