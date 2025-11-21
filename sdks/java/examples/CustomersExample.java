package org.openapitools.client.examples;

import org.openapitools.client.*;
import org.openapitools.client.api.*;
import org.openapitools.client.model.*;
import java.math.BigDecimal;

/**
 * Customer Examples
 */
public class CustomersExample {
    
    public static void simpleCreateCustomer() {
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
        
        CustomersApi apiInstance = new CustomersApi(defaultClient);
        
        CreateCustomerDto customerData = new CreateCustomerDto();
        customerData.setFirstName("John");
        customerData.setLastName("Doe");
        customerData.setEmail("john.doe@example.com");
        customerData.setPhoneNumber("+1-555-123-4567");
        customerData.setCustomerType(CustomerType.STARTUP);
        customerData.setStatus(CustomerStatus.ACTIVE);
        
        try {
            CustomerResponseDto customer = apiInstance.customerControllerCreate(customerData);
            System.out.println("Customer created: " + customer.getId());
        } catch (ApiException e) {
            System.err.println("Customer creation failed: " + e.getMessage());
            e.printStackTrace();
        }
    }
    
    public static void main(String[] args) {
        simpleCreateCustomer();
    }
}
