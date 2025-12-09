
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
    subgraph AMS["&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Segment"]
        Service[Segment.io]
    end
    
    subgraph CA["&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Client Applications"]
        Client[Segment.io Client]
    end
    
    subgraph AWS["&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;AWS"]
        S3[(AWS S3 Bucket)]
    end
    
    subgraph PROC["&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Processing"]
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

1. **Collection**: Segment.io clients collect and anonymize metrics from various sources
2. **Transmission**: Metrics are sent to Segment.io
3. **Storage**: Anonymized metrics are stored in an AWS S3 bucket
4. **Processing**: Stored data can be retrieved and processed for analytics and insights

## Development Setup

### Create Virtual Environment

Create a virtual environment using uv:

```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### Install Dependencies

Install the required Python packages using uv:

```bash
uv pip install -r requirements.txt
```


