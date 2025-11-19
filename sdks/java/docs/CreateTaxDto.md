

# CreateTaxDto


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Tax name. Used to identify and reference this tax rate. |  |
|**description** | **String** | Optional description explaining what this tax covers. |  [optional] |
|**percentage** | **BigDecimal** | Tax percentage rate. Must be between 0 and 100. |  |
|**active** | **Boolean** | Whether this tax is currently active and can be applied. |  [optional] |
|**appIds** | **List&lt;UUID&gt;** | Array of app IDs where this tax should be available. If not provided, tax will be available for the current app. |  [optional] |



