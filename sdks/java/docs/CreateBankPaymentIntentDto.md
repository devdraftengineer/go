

# CreateBankPaymentIntentDto


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**sourcePaymentRail** | **BridgePaymentRail** | The banking payment method to use for the transfer. Determines processing time and fees. |  |
|**sourceCurrency** | **FiatCurrency** | The fiat currency to convert FROM. Must match the currency of the source payment rail. |  |
|**destinationCurrency** | **StableCoinCurrency** | The stablecoin currency to convert TO. The customer will receive this currency. |  |
|**destinationNetwork** | **BridgePaymentRail** | The blockchain network where the stablecoin will be delivered. Must support the destination currency. |  |
|**destinationAddress** | **String** | Destination wallet address. Supports Ethereum (0x...) and Solana address formats. |  [optional] |
|**amount** | **String** | Payment amount (optional for flexible amount) |  [optional] |
|**customerFirstName** | **String** | Customer first name |  [optional] |
|**customerLastName** | **String** | Customer last name |  [optional] |
|**customerEmail** | **String** | Customer email address |  [optional] |
|**customerAddress** | **String** | Customer address |  [optional] |
|**customerCountry** | **String** | Customer country |  [optional] |
|**customerCountryISO** | **String** | Customer country ISO code |  [optional] |
|**customerProvince** | **String** | Customer province/state |  [optional] |
|**customerProvinceISO** | **String** | Customer province/state ISO code |  [optional] |
|**phoneNumber** | **String** | Customer phone number |  [optional] |
|**wireMessage** | **String** | Wire transfer message (for WIRE transfers) |  [optional] |
|**sepaReference** | **String** | SEPA reference (for SEPA transfers) |  [optional] |
|**achReference** | **String** | ACH reference (for ACH transfers) |  [optional] |



