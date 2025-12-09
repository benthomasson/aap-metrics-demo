# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains the design and documentation for the **AAP (Ansible Automation Platform) Anonymized Metrics Storage Service** - a bridge service between Segment.io clients and AWS S3 storage for anonymous metrics collection and processing.

## Current State

This is a **documentation-only repository** in the conceptual/design phase. The README.md contains the architectural requirements and data flow specifications, but **no implementation exists yet**. Any code development will be greenfield implementation.

## Architecture Requirements

The service must implement the following data flow:
1. **Collection**: Receive metrics from Segment.io clients
2. **Anonymization**: Process and anonymize incoming data
3. **Storage**: Store anonymized metrics in AWS S3
4. **Processing**: Enable retrieval for analytics and insights

## Key Integration Requirements

- **Segment.io Client Integration**: Must handle incoming metrics from Segment.io clients
- **AWS S3 Integration**: Requires AWS SDK for S3 storage operations
- **Data Anonymization**: Core functionality to anonymize metrics before storage
- **Anonymous Storage**: Ensure no personally identifiable information is stored

## Development Approach

When implementing this service:
- Choose appropriate technology stack for the backend service
- Implement AWS SDK integration for S3 operations
- Add Segment.io client library integration
- Include data anonymization processing logic
- Follow the architectural diagram in README.md for component relationships

## Repository Structure

Currently minimal with only README.md containing the service specification. Implementation will need to establish:
- Backend service code
- AWS configuration
- Segment.io integration
- Testing framework
- Build and deployment configuration