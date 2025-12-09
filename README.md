
# AAP Metrics Demo

A demo of how to use the AAP Anonymized Metrics Storage Service

## Overview

The AAP (Ansible Automation Platform) Anonymized Metrics Storage Service acts as a bridge between Segment.io clients and AWS S3 storage. This service allows Segment.io clients to collect and store metrics anonymously for later processing and analysis.

## Architecture

The following diagram shows how the components connect and data flows through the system:

```mermaid
---
title: AAP Anonymized Metrics Storage Service
---
flowchart TB
    subgraph "Client Applications"
        Client[Segment.io Client]
    end
    
    subgraph "AAP Metrics Service"
        Service[Segment.io]
    end
    
    subgraph "AWS"
        S3[(AWS S3 Bucket)]
    end
    
    subgraph "Processing"
        Analytics[Data Processing & Analytics]
    end
    
    Client -->|Send Metrics| Service
    Service -->|Store Anonymized Data| S3
    S3 -->|Retrieve for Analysis| Analytics
    
    style Service fill:#e1f5fe
    style S3 fill:#fff3e0
    style Analytics fill:#f3e5f5
```

## Data Flow

1. **Collection**: Segment.io clients collect metrics from various sources
2. **Transmission**: Metrics are sent to the AAP Anonymized Metrics Storage Service
3. **Anonymization**: The service processes and anonymizes the incoming data
4. **Storage**: Anonymized metrics are stored in an AWS S3 bucket
5. **Processing**: Stored data can be retrieved and processed for analytics and insights


