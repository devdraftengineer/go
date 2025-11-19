

# UpdateWebhookDto


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Name of the webhook for identification purposes |  [optional] |
|**url** | **URI** | URL where webhook events will be sent |  [optional] |
|**isActive** | **Boolean** | Whether the webhook is active and will receive events |  [optional] |
|**signingSecret** | **String** | Secret key used to sign webhook payloads for verification |  [optional] |
|**encrypted** | **Boolean** | Whether webhook payloads should be encrypted |  [optional] |



