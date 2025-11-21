"""
Health Check Examples

These examples demonstrate how to use the health check endpoints.
"""

import os
import devdraft
from devdraft.rest import ApiException


# ============================================================================
# Simple Example: Public Health Check
# ============================================================================

def simple_public_health_check():
    configuration = devdraft.Configuration(
        host="https://api.devdraft.ai"
    )
    
    with devdraft.ApiClient(configuration) as api_client:
        api_instance = devdraft.APIHealthApi(api_client)
        
        try:
            response = api_instance.health_controller_public_health_check_v0()
            print(f"Service status: {response.status}")
            print(f"Service is healthy: {response.status == 'ok'}")
        except ApiException as e:
            print(f"Health check failed: {e}")


# ============================================================================
# Advanced Example: Authenticated Health Check with Error Handling
# ============================================================================

def advanced_authenticated_health_check():
    configuration = devdraft.Configuration(
        host="https://api.devdraft.ai"
    )
    
    # Configure API key authorization
    configuration.api_key['x-client-key'] = os.environ.get('CLIENT_KEY', 'your-client-key')
    configuration.api_key['x-client-secret'] = os.environ.get('CLIENT_SECRET', 'your-client-secret')
    
    with devdraft.ApiClient(configuration) as api_client:
        api_instance = devdraft.APIHealthApi(api_client)
        
        try:
            response = api_instance.health_controller_check_v0()
            
            print("=== Health Check Results ===")
            print(f"Status: {response.status}")
            print(f"Version: {response.version}")
            print(f"Database: {response.database}")
            print(f"Message: {response.message}")
            print(f"Authenticated: {response.authenticated}")
            print(f"Timestamp: {response.timestamp}")
            
            # Check if service is healthy
            if response.status == 'ok' and response.database == 'connected':
                print("✅ Service is fully operational")
            else:
                print("⚠️  Service may have issues")
                
        except ApiException as e:
            if e.status == 401:
                print("❌ Authentication failed. Please check your API keys.")
            else:
                print(f"❌ Request failed: {e.reason}")
            raise


# ============================================================================
# Error Scenario: Handling Authentication Errors
# ============================================================================

def error_scenario_health_check():
    configuration = devdraft.Configuration(
        host="https://api.devdraft.ai"
    )
    
    # Intentionally wrong API key
    configuration.api_key['x-client-key'] = 'invalid-key'
    configuration.api_key['x-client-secret'] = 'invalid-secret'
    
    with devdraft.ApiClient(configuration) as api_client:
        api_instance = devdraft.APIHealthApi(api_client)
        
        try:
            api_instance.health_controller_check_v0()
        except ApiException as e:
            if e.status == 401:
                print("❌ Unauthorized: Invalid API credentials")
                print("Please verify your CLIENT_KEY and CLIENT_SECRET environment variables")
            elif e.status == 429:
                print("❌ Rate limit exceeded. Please wait before retrying.")
            else:
                print(f"❌ Unexpected error: {e.reason}")


if __name__ == "__main__":
    simple_public_health_check()
    advanced_authenticated_health_check()
