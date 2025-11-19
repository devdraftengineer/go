# CreateWebhookDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the webhook for identification purposes | 
**url** | **str** | URL where webhook events will be sent | 
**is_active** | **bool** | Whether the webhook is active and will receive events | [default to True]
**signing_secret** | **str** | Secret key used to sign webhook payloads for verification | [optional] 
**encrypted** | **bool** | Whether webhook payloads should be encrypted | [default to False]

## Example

```python
from devdraft.models.create_webhook_dto import CreateWebhookDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWebhookDto from a JSON string
create_webhook_dto_instance = CreateWebhookDto.from_json(json)
# print the JSON string representation of the object
print(CreateWebhookDto.to_json())

# convert the object into a dict
create_webhook_dto_dict = create_webhook_dto_instance.to_dict()
# create an instance of CreateWebhookDto from a dict
create_webhook_dto_from_dict = CreateWebhookDto.from_dict(create_webhook_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


