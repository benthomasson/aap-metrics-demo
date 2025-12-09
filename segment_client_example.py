#!/usr/bin/env python3
"""
Example Segment.io client for AAP Anonymized Metrics Storage Service

This example demonstrates how to use the Segment.io Python library to send
anonymized metrics that will be stored in AWS S3 through the AAP service.
"""

import segment.analytics as analytics
import os
import uuid
from datetime import datetime


def setup_segment_client():
    """Initialize the Segment analytics client."""
    # Get write key from environment variable
    write_key = os.getenv('SEGMENT_WRITE_KEY')
    if not write_key:
        raise ValueError("SEGMENT_WRITE_KEY environment variable is required")
    
    # Configure the client
    analytics.write_key = write_key
    analytics.debug = True  # Enable debug mode for development
    
    return analytics


def track_user_action(user_id, event_name, properties=None):
    """Track a user action with anonymized data."""
    if properties is None:
        properties = {}
    
    # Add anonymized timestamp and session info
    properties.update({
        'timestamp': datetime.utcnow().isoformat(),
        'session_id': str(uuid.uuid4()),
        'anonymized': True
    })
    
    analytics.track(
        user_id=user_id,
        event=event_name,
        properties=properties
    )
    
    print(f"Tracked event: {event_name} for user: {user_id}")


def identify_anonymous_user(user_id, traits=None):
    """Identify an anonymous user with minimal traits."""
    if traits is None:
        traits = {}
    
    # Only include non-PII traits
    safe_traits = {
        'account_type': traits.get('account_type', 'free'),
        'subscription_tier': traits.get('subscription_tier', 'basic'),
        'created_at': datetime.utcnow().isoformat(),
        'anonymized': True
    }
    
    analytics.identify(
        user_id=user_id,
        traits=safe_traits
    )
    
    print(f"Identified anonymous user: {user_id}")


def main():
    """Example usage of the Segment client for AAP metrics."""
    try:
        # Setup the client
        setup_segment_client()
        
        # Generate an anonymous user ID
        anonymous_user_id = f"anon_{uuid.uuid4().hex[:8]}"
        
        # Identify the anonymous user
        identify_anonymous_user(
            user_id=anonymous_user_id,
            traits={
                'account_type': 'enterprise',
                'subscription_tier': 'premium'
            }
        )
        
        # Track some example events
        track_user_action(
            user_id=anonymous_user_id,
            event_name='Playbook Executed',
            properties={
                'playbook_size': 'medium',
                'execution_time_ms': 2500,
                'success': True,
                'environment': 'production'
            }
        )
        
        track_user_action(
            user_id=anonymous_user_id,
            event_name='Inventory Sync',
            properties={
                'host_count': 150,
                'sync_duration_seconds': 45,
                'sync_method': 'api'
            }
        )
        
        track_user_action(
            user_id=anonymous_user_id,
            event_name='Dashboard View',
            properties={
                'page': 'metrics_overview',
                'view_duration_seconds': 120
            }
        )
        
        # Flush events to ensure they're sent
        analytics.flush()
        print("All events sent successfully!")
        
    except Exception as e:
        print(f"Error: {e}")
        print("\nMake sure to set the SEGMENT_WRITE_KEY environment variable:")
        print("export SEGMENT_WRITE_KEY=your_segment_write_key_here")


if __name__ == "__main__":
    main()