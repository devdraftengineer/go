

# CreateExternalBankTransferDto


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**sourceWalletId** | **String** | The ID of the source bridge wallet |  |
|**sourceCurrency** | **String** | The source currency |  |
|**destinationCurrency** | **String** | The destination currency |  |
|**destinationPaymentRail** | **BridgeFiatPaymentRail** | The destination payment rail (fiat payment method) |  |
|**externalAccountId** | **String** | The external account ID for the bank transfer |  |
|**amount** | **BigDecimal** | The amount to transfer |  [optional] |
|**wireMessage** | **String** | Wire transfer message (1-256 characters, only for wire transfers) |  [optional] |
|**sepaReference** | **String** | SEPA reference message (6-140 characters, only for SEPA transfers) |  [optional] |
|**swiftReference** | **String** | SWIFT reference message (1-190 characters, only for SWIFT transfers) |  [optional] |
|**speiReference** | **String** | SPEI reference message (1-40 characters, only for SPEI transfers) |  [optional] |
|**swiftCharges** | **String** | SWIFT charges bearer (only for SWIFT transfers) |  [optional] |
|**achReference** | **String** | ACH reference message (1-10 characters, only for ACH transfers) |  [optional] |



