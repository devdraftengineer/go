"""
Payment Examples

These examples demonstrate how to process payments, retrieve payment details,
and handle refunds.
"""

import os
import uuid
import devdraft
from devdraft.rest import ApiException
from devdraft.model.payment_request_dto import PaymentRequestDto


# ============================================================================
# Simple Example: Create a Payment
# ============================================================================

def simple_create_payment():
    configuration = devdraft.Configuration(
        host="https://api.devdraft.ai"
    )
    
    configuration.api_key['x-client-key'] = os.environ.get('CLIENT_KEY', 'your-client-key')
    configuration.api_key['x-client-secret'] = os.environ.get('CLIENT_SECRET', 'your-client-secret')
    
    with devdraft.ApiClient(configuration) as api_client:
        api_instance = devdraft.TestPaymentsApi(api_client)
        
        payment_request = PaymentRequestDto(
            amount=100.50,
            currency="USD",
            description="Test payment for order #12345",
            customer_id="cus_12345"
        )
        
        idempotency_key = f"payment_{uuid.uuid4()}"
        
        try:
            response = api_instance.test_payment_controller_create_payment_v0(
                payment_request,
                idempotency_key=idempotency_key
            )
            print(f"Payment created: {response.id}")
            print(f"Status: {response.status}")
            return response
        except ApiException as e:
            print(f"Payment creation failed: {e}")
            raise


# ============================================================================
# Advanced Example: Payment Workflow with Retry Logic
# ============================================================================

def advanced_payment_workflow():
    configuration = devdraft.Configuration(
        host="https://api.devdraft.ai"
    )
    
    configuration.api_key['x-client-key'] = os.environ.get('CLIENT_KEY', 'your-client-key')
    configuration.api_key['x-client-secret'] = os.environ.get('CLIENT_SECRET', 'your-client-secret')
    
    with devdraft.ApiClient(configuration) as api_client:
        api_instance = devdraft.TestPaymentsApi(api_client)
        
        # Step 1: Create payment with idempotency key
        idempotency_key = f"payment_{int(uuid.uuid4().int)}"
        payment_request = PaymentRequestDto(
            amount=250.00,
            currency="USD",
            description="Premium subscription payment",
            customer_id="cus_premium_001"
        )
        
        payment = None
        try:
            payment = api_instance.test_payment_controller_create_payment_v0(
                payment_request,
                idempotency_key=idempotency_key
            )
            print(f"✅ Payment created: {payment.id}")
        except ApiException as e:
            if e.status == 409:
                print("⚠️  Payment already exists with this idempotency key")
                # In a real scenario, you would extract payment ID from error
                # and retrieve it
            else:
                raise
        
        # Step 2: Retrieve payment details
        if payment and payment.id:
            payment_details = api_instance.test_payment_controller_get_payment_v0(payment.id)
            print(f"Payment details retrieved: {{
                'id': {payment_details.id},
                'amount': {payment_details.amount},
                'status': {payment_details.status},
                'timestamp': {payment_details.timestamp}
            }}")
        
        return payment


# ============================================================================
# Error Scenario: Handling Payment Errors
# ============================================================================

def error_scenario_payments():
    configuration = devdraft.Configuration(
        host="https://api.devdraft.ai"
    )
    
    configuration.api_key['x-client-key'] = os.environ.get('CLIENT_KEY', 'your-client-key')
    configuration.api_key['x-client-secret'] = os.environ.get('CLIENT_SECRET', 'your-client-secret')
    
    with devdraft.ApiClient(configuration) as api_client:
        api_instance = devdraft.TestPaymentsApi(api_client)
        
        # Scenario 1: Missing idempotency key
        try:
            api_instance.test_payment_controller_create_payment_v0(
                PaymentRequestDto(
                    amount=100,
                    currency="USD",
                    description="Test",
                    customer_id="cus_123"
                ),
                idempotency_key=""  # Missing idempotency key
            )
        except ApiException as e:
            if e.status == 400:
                print("❌ Bad Request: Idempotency key is required")
        
        # Scenario 2: Invalid payment data
        try:
            api_instance.test_payment_controller_create_payment_v0(
                PaymentRequestDto(
                    amount=-100,  # Invalid amount
                    currency="USD",
                    description="",
                    customer_id=""
                ),
                idempotency_key=f"payment_{uuid.uuid4()}"
            )
        except ApiException as e:
            if e.status == 400:
                print("❌ Bad Request: Invalid payment data")
                print(f"Validation errors: {e.body}")
        
        # Scenario 3: Rate limiting
        try:
            # Make multiple rapid requests (simplified example)
            for i in range(10):
                api_instance.test_payment_controller_create_payment_v0(
                    PaymentRequestDto(
                        amount=100,
                        currency="USD",
                        description="Test",
                        customer_id="cus_123"
                    ),
                    idempotency_key=f"payment_{uuid.uuid4()}"
                )
        except ApiException as e:
            if e.status == 429:
                print("❌ Rate limit exceeded. Please wait before retrying.")
                retry_after = e.headers.get('retry-after')
                if retry_after:
                    print(f"Wait {retry_after} seconds before retrying")


# ============================================================================
# Refund Example
# ============================================================================

def refund_payment_example(payment_id: str):
    configuration = devdraft.Configuration(
        host="https://api.devdraft.ai"
    )
    
    configuration.api_key['x-client-key'] = os.environ.get('CLIENT_KEY', 'your-client-key')
    configuration.api_key['x-client-secret'] = os.environ.get('CLIENT_SECRET', 'your-client-secret')
    
    with devdraft.ApiClient(configuration) as api_client:
        api_instance = devdraft.TestPaymentsApi(api_client)
        idempotency_key = f"refund_{uuid.uuid4()}"
        
        try:
            refund = api_instance.test_payment_controller_refund_payment_v0(
                payment_id,
                idempotency_key=idempotency_key
            )
            print(f"✅ Refund processed: {refund.id}")
            print(f"Refund amount: {refund.amount}")
            print(f"Refund status: {refund.status}")
            return refund
        except ApiException as e:
            if e.status == 400:
                print("❌ Bad Request: Invalid refund request")
            elif e.status == 404:
                print("❌ Payment not found")
            else:
                print(f"❌ Refund failed: {e.reason}")
            raise


if __name__ == "__main__":
    simple_create_payment()
