# Demo Script: AAP Anonymized Metrics Storage Service

*This is a human-readable script for recording a demonstration of the AAP metrics storage service.*

## Introduction (30 seconds)

**"Welcome to the AAP Anonymized Metrics Storage Service demonstration."**

**"This service provides a secure way for Ansible Automation Platform to collect and store anonymized usage metrics. Let's explore how it works."**

*[Show the repository overview in your browser or file explorer]*

## Architecture Overview (45 seconds)

**"First, let's look at the architecture of our metrics storage service."**

*[Open README.md and scroll to the architecture section]*

**"Here's how the data flows through our system:"**

*[Point to the mermaid diagram as you explain each component]*

**"We start with client applications that collect anonymized metrics. These metrics are sent to Segment.io, which acts as our data pipeline. Segment.io then stores the anonymized data in an AWS S3 bucket, where it can be retrieved later for processing and analytics."**

**"The key benefit here is that all personally identifiable information is removed at the client level before transmission, ensuring privacy and compliance."**

## Data Flow Explanation (30 seconds)

*[Scroll down to the Data Flow section]*

**"Let's walk through the four-step process:"**

**"Step 1: Collection - Segment.io clients collect AND anonymize metrics from various sources"**

**"Step 2: Transmission - The anonymized metrics are sent to Segment.io"**

**"Step 3: Storage - Segment.io stores the data in our AWS S3 bucket"**

**"Step 4: Processing - The stored data can be retrieved for analytics and insights"**

## Python Demo Code (60 seconds)

**"Now let's look at a practical example. We've created a Python demonstration that shows how to send anonymized AAP metrics."**

*[Open segment_client_example.py in your editor]*

**"Here's our Python client example. Let me highlight the key parts:"**

*[Scroll to the setup_segment_client function]*

**"First, we set up the Segment client using an API write key from environment variables."**

*[Scroll to the track_user_action function]*

**"This function tracks user actions with anonymized data. Notice how we generate anonymous user IDs and session IDs, but include no personally identifiable information."**

*[Scroll to the main function]*

**"In our main demonstration, we simulate typical AAP operations:"**
- **"Playbook execution with anonymized metrics like execution time and success status"**
- **"Inventory synchronization with host counts and timing"**
- **"Dashboard views with page names and view duration"**

*[Point to the anonymization practices]*

**"Notice that all user IDs are generated anonymously, and we only collect operational metrics - no personal data."**

## Running the Demo (45 seconds)

**"Let's see this in action. I'll run the demonstration now."**

*[Switch to terminal]*

**"First, I need to set up my environment:"**

*[Type and run the commands, explaining each step]*

```bash
# Activate virtual environment
source .venv/bin/activate

# Set the Segment write key (use a demo/test key)
export SEGMENT_WRITE_KEY=your_demo_key_here
```

**"Now let's run our Python demo:"**

```bash
python segment_client_example.py
```

*[Let the script run and show the output]*

**"As you can see, the script successfully:"**
- **"Generated an anonymous user ID"**
- **"Identified the user with safe, non-PII traits"**
- **"Tracked multiple AAP-related events"**
- **"Sent all events to Segment.io"**

## Conclusion (30 seconds)

**"This demonstrates how the AAP Anonymized Metrics Storage Service enables:"**

- **"Privacy-first metrics collection"**
- **"Seamless integration with existing AAP workflows"**
- **"Scalable storage and processing through AWS S3"**
- **"Real-time analytics capabilities through Segment.io"**

**"The anonymized data helps improve AAP while protecting user privacy. Thank you for watching this demonstration."**

---

## Technical Notes for Recording:

1. **Preparation:**
   - Have a test Segment write key ready
   - Ensure virtual environment is set up
   - Open all files in advance
   - Test the Python script beforehand

2. **Screen Setup:**
   - Use a clean desktop
   - Increase font sizes for readability
   - Have README.md and Python file ready in tabs
   - Terminal ready with the project directory

3. **Timing:**
   - Total demo time: ~4 minutes
   - Speak clearly and at a moderate pace
   - Pause between sections for emphasis
   - Allow time for viewers to read code/diagrams

4. **Visual Focus:**
   - Highlight important code sections
   - Use cursor/pointer to guide attention
   - Scroll slowly through code for readability
   - Show terminal output clearly