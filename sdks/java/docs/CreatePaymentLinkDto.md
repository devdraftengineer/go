

# CreatePaymentLinkDto


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**title** | **String** | Display title for the payment link. This appears on the checkout page and in customer communications. |  |
|**url** | **String** | Unique URL slug for the payment link. Can be a full URL or just the path segment. Must be unique within your account. |  |
|**description** | **String** | Detailed description of what the customer is purchasing. Supports markdown formatting. |  [optional] |
|**coverImage** | **String** | Cover image URL |  [optional] |
|**linkType** | [**LinkTypeEnum**](#LinkTypeEnum) | Type of the payment link |  |
|**amount** | **BigDecimal** | Amount for the payment link |  [optional] |
|**paymentForId** | **String** | Payment for ID |  [optional] |
|**customerId** | **String** | Customer ID |  [optional] |
|**paymentLinkProducts** | [**List&lt;PaymentLinkProductDto&gt;**](PaymentLinkProductDto.md) | Array of products in the payment link |  [optional] |
|**isForAllProduct** | **Boolean** | Whether the payment link is for all products |  [optional] |
|**allowQuantityAdjustment** | **Boolean** | Whether to allow quantity adjustment |  |
|**collectTax** | **Boolean** | Whether to collect tax |  |
|**taxId** | **String** | Tax ID |  [optional] |
|**collectAddress** | **Boolean** | Whether to collect address |  |
|**limitPayments** | **Boolean** | Whether to limit payments |  [optional] |
|**maxPayments** | **BigDecimal** | Maximum number of payments |  [optional] |
|**customFields** | **Object** | Custom fields |  [optional] |
|**allowMobilePayment** | **Boolean** | Whether to allow mobile payment |  |
|**currency** | [**CurrencyEnum**](#CurrencyEnum) | Currency |  |
|**expirationDate** | **OffsetDateTime** | Expiration date |  [optional] |



## Enum: LinkTypeEnum

| Name | Value |
|---- | -----|
| INVOICE | &quot;INVOICE&quot; |
| PRODUCT | &quot;PRODUCT&quot; |
| COLLECTION | &quot;COLLECTION&quot; |
| DONATION | &quot;DONATION&quot; |



## Enum: CurrencyEnum

| Name | Value |
|---- | -----|
| USDC | &quot;usdc&quot; |
| EURC | &quot;eurc&quot; |



