

# CreateCustomerDto


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**firstName** | **String** | Customer&#39;s first name. Used for personalization and legal documentation. |  |
|**lastName** | **String** | Customer&#39;s last name. Used for personalization and legal documentation. |  |
|**email** | **String** | Customer&#39;s email address. Used for notifications, receipts, and account management. Must be a valid email format. |  [optional] |
|**phoneNumber** | **String** | Customer&#39;s phone number. Used for SMS notifications and verification. Include country code for international numbers. |  |
|**customerType** | **CustomerType** | Type of customer account. Determines available features and compliance requirements. |  [optional] |
|**status** | **CustomerStatus** | Current status of the customer account. Controls access to services and features. |  [optional] |



