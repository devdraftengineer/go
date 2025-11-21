package org.openapitools.client.examples;

import org.openapitools.client.*;
import org.openapitools.client.api.*;
import org.openapitools.client.model.*;
import java.util.Arrays;

/**
 * Webhook Examples
 */
public class WebhooksExample {
    
    public static void simpleCreateWebhook() {
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
        
        WebhooksApi apiInstance = new WebhooksApi(defaultClient);
        
        CreateWebhookDto webhookData = new CreateWebhookDto();
        webhookData.setUrl("https://your-app.com/webhooks/payment");
        webhookData.setEvents(Arrays.asList("payment.created", "payment.succeeded"));
        
        try {
            WebhookResponseDto webhook = apiInstance.webhookControllerCreate(webhookData);
            System.out.println("Webhook created: " + webhook.getId());
            System.out.println("Webhook URL: " + webhook.getUrl());
        } catch (ApiException e) {
            System.err.println("Webhook creation failed: " + e.getMessage());
            e.printStackTrace();
        }
    }
    
    public static void main(String[] args) {
        simpleCreateWebhook();
    }
}
