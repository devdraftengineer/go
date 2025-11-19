

# CreateLiquidationAddressDto


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**chain** | [**ChainEnum**](#ChainEnum) | The blockchain chain for the liquidation address |  |
|**currency** | [**CurrencyEnum**](#CurrencyEnum) | The currency for the liquidation address |  |
|**address** | **String** | The liquidation address on the blockchain |  |
|**externalAccountId** | **String** | External bank account to send funds to |  [optional] |
|**prefundedAccountId** | **String** | Developer&#39;s prefunded account id |  [optional] |
|**bridgeWalletId** | **String** | Bridge Wallet to send funds to |  [optional] |
|**destinationPaymentRail** | **BridgePaymentRail** | Payment rail for sending funds |  [optional] |
|**destinationCurrency** | **DestinationCurrency** | Currency for sending funds |  [optional] |
|**destinationWireMessage** | **String** | Message for wire transfers |  [optional] |
|**destinationSepaReference** | **String** | Reference for SEPA transactions |  [optional] |
|**destinationAchReference** | **String** | Reference for ACH transactions |  [optional] |
|**destinationAddress** | **String** | Crypto wallet address for crypto transfers |  [optional] |
|**destinationBlockchainMemo** | **String** | Memo for blockchain transactions |  [optional] |
|**returnAddress** | **String** | Address to return funds on failed transactions (Not supported on Stellar) |  [optional] |
|**customDeveloperFeePercent** | **String** | Custom developer fee percentage (Base 100 percentage: 10.2% &#x3D; \&quot;10.2\&quot;) |  [optional] |



## Enum: ChainEnum

| Name | Value |
|---- | -----|
| ETHEREUM | &quot;ethereum&quot; |
| SOLANA | &quot;solana&quot; |
| POLYGON | &quot;polygon&quot; |
| AVALANCHE_C_CHAIN | &quot;avalanche_c_chain&quot; |
| BASE | &quot;base&quot; |
| ARBITRUM | &quot;arbitrum&quot; |
| OPTIMISM | &quot;optimism&quot; |
| STELLAR | &quot;stellar&quot; |
| TRON | &quot;tron&quot; |



## Enum: CurrencyEnum

| Name | Value |
|---- | -----|
| USDC | &quot;usdc&quot; |
| EURC | &quot;eurc&quot; |
| DAI | &quot;dai&quot; |
| PYUSD | &quot;pyusd&quot; |
| USDT | &quot;usdt&quot; |



