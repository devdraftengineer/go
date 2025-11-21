package org.openapitools.client.examples;

import org.openapitools.client.*;
import org.openapitools.client.api.*;
import org.openapitools.client.model.*;
import java.util.UUID;

/**
 * Health Check Examples
 * 
 * These examples demonstrate how to use the health check endpoints.
 */
public class HealthCheckExample {
    
    // ============================================================================
    // Simple Example: Public Health Check
    // ============================================================================
    
    public static void simplePublicHealthCheck() {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        APIHealthApi apiInstance = new APIHealthApi(defaultClient);
        
        try {
            PublicHealthResponseDto response = apiInstance.healthControllerPublicHealthCheckV0();
            System.out.println("Service status: " + response.getStatus());
            System.out.println("Service is healthy: " + response.getStatus().equals("ok"));
        } catch (ApiException e) {
            System.err.println("Health check failed: " + e.getMessage());
            e.printStackTrace();
        }
    }
    
    // ============================================================================
    // Advanced Example: Authenticated Health Check with Error Handling
    // ============================================================================
    
    public static void advancedAuthenticatedHealthCheck() {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        
        // Configure API key authorization
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
        
        APIHealthApi apiInstance = new APIHealthApi(defaultClient);
        
        try {
            HealthResponseDto response = apiInstance.healthControllerCheckV0();
            
            System.out.println("=== Health Check Results ===");
            System.out.println("Status: " + response.getStatus());
            System.out.println("Version: " + response.getVersion());
            System.out.println("Database: " + response.getDatabase());
            System.out.println("Message: " + response.getMessage());
            System.out.println("Authenticated: " + response.getAuthenticated());
            System.out.println("Timestamp: " + response.getTimestamp());
            
            // Check if service is healthy
            if ("ok".equals(response.getStatus()) && "connected".equals(response.getDatabase())) {
                System.out.println("✅ Service is fully operational");
            } else {
                System.out.println("⚠️  Service may have issues");
            }
        } catch (ApiException e) {
            if (e.getCode() == 401) {
                System.err.println("❌ Authentication failed. Please check your API keys.");
            } else {
                System.err.println("❌ Request failed: " + e.getMessage());
            }
            e.printStackTrace();
        }
    }
    
    // ============================================================================
    // Error Scenario: Handling Authentication Errors
    // ============================================================================
    
    public static void errorScenarioHealthCheck() {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        
        // Intentionally wrong API key
        defaultClient.setApiKey("x-client-key", "invalid-key");
        defaultClient.setApiKey("x-client-secret", "invalid-secret");
        
        APIHealthApi apiInstance = new APIHealthApi(defaultClient);
        
        try {
            apiInstance.healthControllerCheckV0();
        } catch (ApiException e) {
            if (e.getCode() == 401) {
                System.err.println("❌ Unauthorized: Invalid API credentials");
                System.err.println("Please verify your CLIENT_KEY and CLIENT_SECRET environment variables");
            } else if (e.getCode() == 429) {
                System.err.println("❌ Rate limit exceeded. Please wait before retrying.");
            } else {
                System.err.println("❌ Unexpected error: " + e.getMessage());
            }
        }
    }
    
    public static void main(String[] args) {
        simplePublicHealthCheck();
        advancedAuthenticatedHealthCheck();
    }
}
