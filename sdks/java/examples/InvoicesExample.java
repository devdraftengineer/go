package org.openapitools.client.examples;

import org.openapitools.client.*;
import org.openapitools.client.api.*;
import org.openapitools.client.model.*;
import java.math.BigDecimal;

/**
 * Invoice Examples
 */
public class InvoicesExample {
    
    public static void simpleCreateInvoice() {
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
        
        InvoicesApi apiInstance = new InvoicesApi(defaultClient);
        
        CreateInvoiceDto invoiceData = new CreateInvoiceDto();
        invoiceData.setCustomerId("cus_12345");
        
        InvoiceProductDto product = new InvoiceProductDto();
        product.setProductId("prod_123");
        product.setQuantity(2);
        product.setPrice(BigDecimal.valueOf(99.99));
        invoiceData.setProducts(java.util.Arrays.asList(product));
        
        try {
            InvoiceResponseDto invoice = apiInstance.invoiceControllerCreate(invoiceData);
            System.out.println("Invoice created: " + invoice.getId());
        } catch (ApiException e) {
            System.err.println("Invoice creation failed: " + e.getMessage());
            e.printStackTrace();
        }
    }
    
    public static void main(String[] args) {
        simpleCreateInvoice();
    }
}
