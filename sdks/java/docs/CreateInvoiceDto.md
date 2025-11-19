

# CreateInvoiceDto


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Name of the invoice |  |
|**email** | **String** | Email address |  |
|**customerId** | **String** | Customer ID |  |
|**currency** | [**CurrencyEnum**](#CurrencyEnum) | Currency for the invoice |  |
|**items** | **Object** |  |  |
|**dueDate** | **OffsetDateTime** | Due date of the invoice |  |
|**delivery** | [**DeliveryEnum**](#DeliveryEnum) | Delivery method |  |
|**paymentLink** | **Boolean** | Whether to generate a payment link |  |
|**paymentMethods** | [**List&lt;PaymentMethodsEnum&gt;**](#List&lt;PaymentMethodsEnum&gt;) | Array of accepted payment methods |  |
|**status** | [**StatusEnum**](#StatusEnum) | Invoice status |  |
|**address** | **String** | Address |  [optional] |
|**phoneNumber** | **String** | Phone number |  [optional] |
|**sendDate** | **OffsetDateTime** | Send date |  [optional] |
|**logo** | **String** | Logo URL |  [optional] |
|**partialPayment** | **Boolean** | Allow partial payments |  |
|**taxId** | **String** | Tax ID |  [optional] |



## Enum: CurrencyEnum

| Name | Value |
|---- | -----|
| USDC | &quot;usdc&quot; |
| EURC | &quot;eurc&quot; |



## Enum: DeliveryEnum

| Name | Value |
|---- | -----|
| EMAIL | &quot;EMAIL&quot; |
| MANUALLY | &quot;MANUALLY&quot; |



## Enum: List&lt;PaymentMethodsEnum&gt;

| Name | Value |
|---- | -----|
| ACH | &quot;ACH&quot; |
| BANK_TRANSFER | &quot;BANK_TRANSFER&quot; |
| CREDIT_CARD | &quot;CREDIT_CARD&quot; |
| CASH | &quot;CASH&quot; |
| MOBILE_MONEY | &quot;MOBILE_MONEY&quot; |
| CRYPTO | &quot;CRYPTO&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| DRAFT | &quot;DRAFT&quot; |
| OPEN | &quot;OPEN&quot; |
| PASTDUE | &quot;PASTDUE&quot; |
| PAID | &quot;PAID&quot; |
| PARTIALLYPAID | &quot;PARTIALLYPAID&quot; |



