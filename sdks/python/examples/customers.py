"""
Customer Examples

These examples demonstrate how to manage customers: creating, listing,
retrieving, and updating customer records.
"""

import os
import devdraft
from devdraft.rest import ApiException
from devdraft.model.create_customer_dto import CreateCustomerDto
from devdraft.model.update_customer_dto import UpdateCustomerDto


# ============================================================================
# Simple Example: Create a Customer
# ============================================================================

def simple_create_customer():
    configuration = devdraft.Configuration(
        host="https://api.devdraft.ai"
    )
    
    configuration.api_key['x-client-key'] = os.environ.get('CLIENT_KEY', 'your-client-key')
    configuration.api_key['x-client-secret'] = os.environ.get('CLIENT_SECRET', 'your-client-secret')
    
    with devdraft.ApiClient(configuration) as api_client:
        api_instance = devdraft.CustomersApi(api_client)
        
        customer_data = CreateCustomerDto(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            phone_number="+1-555-123-4567",
            customer_type="Startup",
            status="ACTIVE"
        )
        
        try:
            customer = api_instance.customer_controller_create(customer_data)
            print(f"Customer created: {customer.id}")
            return customer
        except ApiException as e:
            print(f"Customer creation failed: {e}")
            raise


# ============================================================================
# Advanced Example: Customer Management Workflow
# ============================================================================

def advanced_customer_workflow():
    configuration = devdraft.Configuration(
        host="https://api.devdraft.ai"
    )
    
    configuration.api_key['x-client-key'] = os.environ.get('CLIENT_KEY', 'your-client-key')
    configuration.api_key['x-client-secret'] = os.environ.get('CLIENT_SECRET', 'your-client-secret')
    
    with devdraft.ApiClient(configuration) as api_client:
        api_instance = devdraft.CustomersApi(api_client)
        
        # Step 1: Create a new customer
        new_customer = CreateCustomerDto(
            first_name="Jane",
            last_name="Smith",
            email="jane.smith@example.com",
            phone_number="+1-555-987-6543",
            customer_type="Small Business",
            status="ACTIVE"
        )
        
        customer = None
        try:
            customer = api_instance.customer_controller_create(new_customer)
            print(f"✅ Customer created: {customer.id}")
        except ApiException as e:
            if e.status == 409:
                print("⚠️  Customer with this email already exists")
                # Try to find existing customer
                customers = api_instance.customer_controller_find_all(
                    skip=0,
                    take=10,
                    status=None,
                    name=None,
                    email="jane.smith@example.com"
                )
                if customers.data and len(customers.data) > 0:
                    customer = customers.data[0]
            else:
                raise
        
        # Step 2: List customers with filters
        active_customers = api_instance.customer_controller_find_all(
            skip=0,
            take=20,
            status="ACTIVE",
            name=None,
            email=None
        )
        
        print(f"Found {active_customers.total} active customers")
        
        # Step 3: Get customer details
        if customer and customer.id:
            customer_details = api_instance.customer_controller_find_one(customer.id)
            print(f"Customer details: {{
                'id': {customer_details.id},
                'name': '{customer_details.first_name} {customer_details.last_name}',
                'email': {customer_details.email},
                'status': {customer_details.status}
            }}")
            
            # Step 4: Update customer
            update_data = UpdateCustomerDto(
                status="ACTIVE",
                phone_number="+1-555-999-8888"
            )
            
            updated_customer = api_instance.customer_controller_update(customer.id, update_data)
            print(f"✅ Customer updated: {updated_customer.id}")
        
        return customer


# ============================================================================
# Error Scenario: Handling Customer Errors
# ============================================================================

def error_scenario_customers():
    configuration = devdraft.Configuration(
        host="https://api.devdraft.ai"
    )
    
    configuration.api_key['x-client-key'] = os.environ.get('CLIENT_KEY', 'your-client-key')
    configuration.api_key['x-client-secret'] = os.environ.get('CLIENT_SECRET', 'your-client-secret')
    
    with devdraft.ApiClient(configuration) as api_client:
        api_instance = devdraft.CustomersApi(api_client)
        
        # Scenario 1: Missing required fields
        try:
            api_instance.customer_controller_create(CreateCustomerDto(
                first_name="",  # Empty required field
                last_name="Doe",
                phone_number="+1-555-123-4567"
            ))
        except ApiException as e:
            if e.status == 400:
                print("❌ Bad Request: Missing required fields")
                print(f"Validation errors: {e.body}")
        
        # Scenario 2: Invalid email format
        try:
            api_instance.customer_controller_create(CreateCustomerDto(
                first_name="John",
                last_name="Doe",
                email="invalid-email",  # Invalid format
                phone_number="+1-555-123-4567"
            ))
        except ApiException as e:
            if e.status == 400:
                print("❌ Bad Request: Invalid email format")
        
        # Scenario 3: Customer not found
        try:
            api_instance.customer_controller_find_one("non-existent-id")
        except ApiException as e:
            if e.status == 404:
                print("❌ Customer not found")
        
        # Scenario 4: Duplicate email
        try:
            api_instance.customer_controller_create(CreateCustomerDto(
                first_name="John",
                last_name="Doe",
                email="existing@example.com",  # Already exists
                phone_number="+1-555-123-4567"
            ))
        except ApiException as e:
            if e.status == 409:
                print("❌ Conflict: Customer with this email already exists")


if __name__ == "__main__":
    simple_create_customer()
