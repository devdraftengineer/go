"""
Webhook Examples

These examples demonstrate how to create, list, retrieve, and update webhooks.
"""

import os
import devdraft
from devdraft.rest import ApiException
from devdraft.model.create_webhook_dto import CreateWebhookDto
from devdraft.model.update_webhook_dto import UpdateWebhookDto


# ============================================================================
# Simple Example: Create a Webhook
# ============================================================================

def simple_create_webhook():
    configuration = devdraft.Configuration(
        host="https://api.devdraft.ai"
    )
    
    configuration.api_key['x-client-key'] = os.environ.get('CLIENT_KEY', 'your-client-key')
    configuration.api_key['x-client-secret'] = os.environ.get('CLIENT_SECRET', 'your-client-secret')
    
    with devdraft.ApiClient(configuration) as api_client:
        api_instance = devdraft.WebhooksApi(api_client)
        
        webhook_data = CreateWebhookDto(
            url="https://your-app.com/webhooks/payment",
            events=["payment.created", "payment.succeeded"]
        )
        
        try:
            webhook = api_instance.webhook_controller_create(webhook_data)
            print(f"Webhook created: {webhook.id}")
            print(f"Webhook URL: {webhook.url}")
            return webhook
        except ApiException as e:
            print(f"Webhook creation failed: {e}")
            raise


# ============================================================================
# Advanced Example: Webhook Management Workflow
# ============================================================================

def advanced_webhook_workflow():
    configuration = devdraft.Configuration(
        host="https://api.devdraft.ai"
    )
    
    configuration.api_key['x-client-key'] = os.environ.get('CLIENT_KEY', 'your-client-key')
    configuration.api_key['x-client-secret'] = os.environ.get('CLIENT_SECRET', 'your-client-secret')
    
    with devdraft.ApiClient(configuration) as api_client:
        api_instance = devdraft.WebhooksApi(api_client)
        
        # Step 1: Create webhook for payment events
        webhook_data = CreateWebhookDto(
            url="https://your-app.com/webhooks/payments",
            events=[
                "payment.created",
                "payment.succeeded",
                "payment.failed",
                "payment.refunded"
            ]
        )
        
        webhook = None
        try:
            webhook = api_instance.webhook_controller_create(webhook_data)
            print(f"✅ Webhook created: {webhook.id}")
        except ApiException as e:
            if e.status == 400:
                print("❌ Invalid webhook configuration")
                raise
            raise
        
        # Step 2: List all webhooks
        webhooks = api_instance.webhook_controller_find_all()
        print(f"Found {len(webhooks)} webhooks")
        
        # Step 3: Get webhook details
        if webhook and webhook.id:
            webhook_details = api_instance.webhook_controller_find_one(webhook.id)
            print(f"Webhook details: {{
                'id': {webhook_details.id},
                'url': {webhook_details.url},
                'events': {webhook_details.events},
                'active': {webhook_details.active}
            }}")
            
            # Step 4: Update webhook
            update_data = UpdateWebhookDto(
                url="https://your-app.com/webhooks/payments-v2",
                events=[
                    "payment.created",
                    "payment.succeeded",
                    "payment.failed",
                    "payment.refunded",
                    "customer.created"
                ]
            )
            
            updated_webhook = api_instance.webhook_controller_update(webhook.id, update_data)
            print(f"✅ Webhook updated: {updated_webhook.id}")
        
        return webhook


# ============================================================================
# Error Scenario: Handling Webhook Errors
# ============================================================================

def error_scenario_webhooks():
    configuration = devdraft.Configuration(
        host="https://api.devdraft.ai"
    )
    
    configuration.api_key['x-client-key'] = os.environ.get('CLIENT_KEY', 'your-client-key')
    configuration.api_key['x-client-secret'] = os.environ.get('CLIENT_SECRET', 'your-client-secret')
    
    with devdraft.ApiClient(configuration) as api_client:
        api_instance = devdraft.WebhooksApi(api_client)
        
        # Scenario 1: Invalid URL
        try:
            api_instance.webhook_controller_create(CreateWebhookDto(
                url="not-a-valid-url",
                events=["payment.created"]
            ))
        except ApiException as e:
            if e.status == 400:
                print("❌ Bad Request: Invalid webhook URL")
        
        # Scenario 2: Empty events array
        try:
            api_instance.webhook_controller_create(CreateWebhookDto(
                url="https://your-app.com/webhooks",
                events=[]  # Empty events
            ))
        except ApiException as e:
            if e.status == 400:
                print("❌ Bad Request: Webhook must have at least one event")
        
        # Scenario 3: Webhook not found
        try:
            api_instance.webhook_controller_find_one("non-existent-webhook-id")
        except ApiException as e:
            if e.status == 404:
                print("❌ Webhook not found")
        
        # Scenario 4: Invalid event name
        try:
            api_instance.webhook_controller_create(CreateWebhookDto(
                url="https://your-app.com/webhooks",
                events=["invalid.event.name"]
            ))
        except ApiException as e:
            if e.status == 400:
                print("❌ Bad Request: Invalid event name")


if __name__ == "__main__":
    simple_create_webhook()
