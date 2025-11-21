"""
Invoice Examples

These examples demonstrate how to create, list, and retrieve invoices.
"""

import os
import devdraft
from devdraft.rest import ApiException
from devdraft.model.create_invoice_dto import CreateInvoiceDto
from devdraft.model.invoice_product_dto import InvoiceProductDto


# ============================================================================
# Simple Example: Create an Invoice
# ============================================================================

def simple_create_invoice():
    configuration = devdraft.Configuration(
        host="https://api.devdraft.ai"
    )
    
    configuration.api_key['x-client-key'] = os.environ.get('CLIENT_KEY', 'your-client-key')
    configuration.api_key['x-client-secret'] = os.environ.get('CLIENT_SECRET', 'your-client-secret')
    
    with devdraft.ApiClient(configuration) as api_client:
        api_instance = devdraft.InvoicesApi(api_client)
        
        invoice_data = CreateInvoiceDto(
            customer_id="cus_12345",
            products=[
                InvoiceProductDto(
                    product_id="prod_123",
                    quantity=2,
                    price=99.99
                )
            ],
            due_date="2024-12-31T23:59:59Z"
        )
        
        try:
            invoice = api_instance.invoice_controller_create(invoice_data)
            print(f"Invoice created: {invoice.id}")
            return invoice
        except ApiException as e:
            print(f"Invoice creation failed: {e}")
            raise


# ============================================================================
# Advanced Example: Invoice Management Workflow
# ============================================================================

def advanced_invoice_workflow():
    configuration = devdraft.Configuration(
        host="https://api.devdraft.ai"
    )
    
    configuration.api_key['x-client-key'] = os.environ.get('CLIENT_KEY', 'your-client-key')
    configuration.api_key['x-client-secret'] = os.environ.get('CLIENT_SECRET', 'your-client-secret')
    
    with devdraft.ApiClient(configuration) as api_client:
        api_instance = devdraft.InvoicesApi(api_client)
        
        # Step 1: Create invoice with multiple products
        from datetime import datetime, timedelta
        
        invoice_data = CreateInvoiceDto(
            customer_id="cus_premium_001",
            products=[
                InvoiceProductDto(
                    product_id="prod_premium",
                    quantity=1,
                    price=299.99
                ),
                InvoiceProductDto(
                    product_id="prod_addon",
                    quantity=2,
                    price=49.99
                )
            ],
            due_date=(datetime.now() + timedelta(days=30)).isoformat() + "Z"
        )
        
        invoice = api_instance.invoice_controller_create(invoice_data)
        print(f"✅ Invoice created: {invoice.id}")
        print(f"Total amount: {invoice.total_amount}")
        
        # Step 2: List invoices with pagination
        invoices = api_instance.invoice_controller_find_all(skip=0, take=10)
        print(f"Found {invoices.total} invoices")
        
        # Step 3: Get invoice details
        invoice_details = api_instance.invoice_controller_find_one(invoice.id)
        print(f"Invoice details: {{
            'id': {invoice_details.id},
            'customer_id': {invoice_details.customer_id},
            'status': {invoice_details.status},
            'total_amount': {invoice_details.total_amount}
        }}")
        
        return invoice


# ============================================================================
# Error Scenario: Handling Invoice Errors
# ============================================================================

def error_scenario_invoices():
    configuration = devdraft.Configuration(
        host="https://api.devdraft.ai"
    )
    
    configuration.api_key['x-client-key'] = os.environ.get('CLIENT_KEY', 'your-client-key')
    configuration.api_key['x-client-secret'] = os.environ.get('CLIENT_SECRET', 'your-client-secret')
    
    with devdraft.ApiClient(configuration) as api_client:
        api_instance = devdraft.InvoicesApi(api_client)
        
        # Scenario 1: Invalid customer ID
        try:
            api_instance.invoice_controller_create(CreateInvoiceDto(
                customer_id="invalid-customer-id",
                products=[]
            ))
        except ApiException as e:
            if e.status == 400:
                print("❌ Bad Request: Invalid customer ID")
            elif e.status == 404:
                print("❌ Customer not found")
        
        # Scenario 2: Empty products array
        try:
            api_instance.invoice_controller_create(CreateInvoiceDto(
                customer_id="cus_123",
                products=[]  # Empty products
            ))
        except ApiException as e:
            if e.status == 400:
                print("❌ Bad Request: Invoice must have at least one product")
        
        # Scenario 3: Invoice not found
        try:
            api_instance.invoice_controller_find_one("non-existent-invoice-id")
        except ApiException as e:
            if e.status == 404:
                print("❌ Invoice not found")


if __name__ == "__main__":
    simple_create_invoice()
