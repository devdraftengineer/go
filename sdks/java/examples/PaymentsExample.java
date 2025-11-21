package org.openapitools.client.examples;

import org.openapitools.client.*;
import org.openapitools.client.api.*;
import org.openapitools.client.model.*;
import java.util.UUID;

/**
 * Payment Examples
 * 
 * These examples demonstrate how to process payments, retrieve payment details,
 * and handle refunds.
 */
public class PaymentsExample {
    
    // ============================================================================
    // Simple Example: Create a Payment
    // ============================================================================
    
    public static void simpleCreatePayment() {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        
        String clientKey = System.getenv("CLIENT_KEY");
        if (clientKey == null || clientKey.isEmpty()) {
            clientKey = "your-client-key";
        }
        String clientSecret = System.getenv("CLIENT_SECRET");
        if (clientSecret == null || clientSecret.isEmpty()) {
            clientSecret = "your-client-secret";
        }
        
        defaultClient.setApiKey("x-client-key", clientKey);
        defaultClient.setApiKey("x-client-secret", clientSecret);
        
        TestPaymentsApi apiInstance = new TestPaymentsApi(defaultClient);
        
        PaymentRequestDto paymentRequest = new PaymentRequestDto();
        paymentRequest.setAmount(100.50f);
        paymentRequest.setCurrency("USD");
        paymentRequest.setDescription("Test payment for order #12345");
        paymentRequest.setCustomerId("cus_12345");
        
        String idempotencyKey = "payment_" + UUID.randomUUID().toString();
        
        try {
            PaymentResponseDto response = apiInstance.testPaymentControllerCreatePaymentV0(idempotencyKey, paymentRequest);
            System.out.println("Payment created: " + response.getId());
            System.out.println("Status: " + response.getStatus());
        } catch (ApiException e) {
            System.err.println("Payment creation failed: " + e.getMessage());
            e.printStackTrace();
        }
    }
    
    // ============================================================================
    // Advanced Example: Payment Workflow with Retry Logic
    // ============================================================================
    
    public static void advancedPaymentWorkflow() {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        
        String clientKey = System.getenv("CLIENT_KEY");
        if (clientKey == null || clientKey.isEmpty()) {
            clientKey = "your-client-key";
        }
        String clientSecret = System.getenv("CLIENT_SECRET");
        if (clientSecret == null || clientSecret.isEmpty()) {
            clientSecret = "your-client-secret";
        }
        
        defaultClient.setApiKey("x-client-key", clientKey);
        defaultClient.setApiKey("x-client-secret", clientSecret);
        
        TestPaymentsApi apiInstance = new TestPaymentsApi(defaultClient);
        
        // Step 1: Create payment with idempotency key
        String idempotencyKey = "payment_" + System.currentTimeMillis() + "_" + UUID.randomUUID().toString();
        PaymentRequestDto paymentRequest = new PaymentRequestDto();
        paymentRequest.setAmount(250.00f);
        paymentRequest.setCurrency("USD");
        paymentRequest.setDescription("Premium subscription payment");
        paymentRequest.setCustomerId("cus_premium_001");
        
        PaymentResponseDto payment = null;
        try {
            payment = apiInstance.testPaymentControllerCreatePaymentV0(idempotencyKey, paymentRequest);
            System.out.println("✅ Payment created: " + payment.getId());
        } catch (ApiException e) {
            if (e.getCode() == 409) {
                System.out.println("⚠️  Payment already exists with this idempotency key");
                // In a real scenario, you would extract payment ID from error
            } else {
                e.printStackTrace();
                return;
            }
        }
        
        // Step 2: Retrieve payment details
        if (payment != null && payment.getId() != null) {
            try {
                PaymentResponseDto paymentDetails = apiInstance.testPaymentControllerGetPaymentV0(payment.getId());
                System.out.println("Payment details retrieved: {");
                System.out.println("  'id': " + paymentDetails.getId() + ",");
                System.out.println("  'amount': " + paymentDetails.getAmount() + ",");
                System.out.println("  'status': " + paymentDetails.getStatus() + ",");
                System.out.println("  'timestamp': " + paymentDetails.getTimestamp());
                System.out.println("}");
            } catch (ApiException e) {
                System.err.println("Failed to retrieve payment: " + e.getMessage());
            }
        }
    }
    
    // ============================================================================
    // Error Scenario: Handling Payment Errors
    // ============================================================================
    
    public static void errorScenarioPayments() {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        
        String clientKey = System.getenv("CLIENT_KEY");
        if (clientKey == null || clientKey.isEmpty()) {
            clientKey = "your-client-key";
        }
        String clientSecret = System.getenv("CLIENT_SECRET");
        if (clientSecret == null || clientSecret.isEmpty()) {
            clientSecret = "your-client-secret";
        }
        
        defaultClient.setApiKey("x-client-key", clientKey);
        defaultClient.setApiKey("x-client-secret", clientSecret);
        
        TestPaymentsApi apiInstance = new TestPaymentsApi(defaultClient);
        
        // Scenario 1: Missing idempotency key
        try {
            PaymentRequestDto paymentRequest = new PaymentRequestDto();
            paymentRequest.setAmount(100f);
            paymentRequest.setCurrency("USD");
            paymentRequest.setDescription("Test");
            paymentRequest.setCustomerId("cus_123");
            apiInstance.testPaymentControllerCreatePaymentV0("", paymentRequest); // Missing idempotency key
        } catch (ApiException e) {
            if (e.getCode() == 400) {
                System.err.println("❌ Bad Request: Idempotency key is required");
            }
        }
        
        // Scenario 2: Invalid payment data
        try {
            PaymentRequestDto invalidPaymentRequest = new PaymentRequestDto();
            invalidPaymentRequest.setAmount(-100f); // Invalid amount
            invalidPaymentRequest.setCurrency("USD");
            invalidPaymentRequest.setDescription("");
            invalidPaymentRequest.setCustomerId("");
            apiInstance.testPaymentControllerCreatePaymentV0("payment_" + UUID.randomUUID().toString(), invalidPaymentRequest);
        } catch (ApiException e) {
            if (e.getCode() == 400) {
                System.err.println("❌ Bad Request: Invalid payment data");
            }
        }
        
        // Scenario 3: Rate limiting
        for (int i = 0; i < 10; i++) {
            try {
                PaymentRequestDto paymentRequest = new PaymentRequestDto();
                paymentRequest.setAmount(100f);
                paymentRequest.setCurrency("USD");
                paymentRequest.setDescription("Test");
                paymentRequest.setCustomerId("cus_123");
                apiInstance.testPaymentControllerCreatePaymentV0("payment_" + UUID.randomUUID().toString(), paymentRequest);
            } catch (ApiException e) {
                if (e.getCode() == 429) {
                    System.err.println("❌ Rate limit exceeded. Please wait before retrying.");
                    break;
                }
            }
        }
    }
    
    // ============================================================================
    // Refund Example
    // ============================================================================
    
    public static void refundPaymentExample(String paymentId) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        
        String clientKey = System.getenv("CLIENT_KEY");
        if (clientKey == null || clientKey.isEmpty()) {
            clientKey = "your-client-key";
        }
        String clientSecret = System.getenv("CLIENT_SECRET");
        if (clientSecret == null || clientSecret.isEmpty()) {
            clientSecret = "your-client-secret";
        }
        
        defaultClient.setApiKey("x-client-key", clientKey);
        defaultClient.setApiKey("x-client-secret", clientSecret);
        
        TestPaymentsApi apiInstance = new TestPaymentsApi(defaultClient);
        String idempotencyKey = "refund_" + UUID.randomUUID().toString();
        
        try {
            RefundResponseDto refund = apiInstance.testPaymentControllerRefundPaymentV0(paymentId, idempotencyKey);
            System.out.println("✅ Refund processed: " + refund.getId());
            System.out.println("Refund amount: " + refund.getAmount());
            System.out.println("Refund status: " + refund.getStatus());
        } catch (ApiException e) {
            if (e.getCode() == 400) {
                System.err.println("❌ Bad Request: Invalid refund request");
            } else if (e.getCode() == 404) {
                System.err.println("❌ Payment not found");
            } else {
                System.err.println("❌ Refund failed: " + e.getMessage());
            }
            e.printStackTrace();
        }
    }
    
    public static void main(String[] args) {
        simpleCreatePayment();
    }
}
