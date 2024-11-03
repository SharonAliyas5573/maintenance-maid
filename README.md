# maintenance-maid

Test data available [here]()

## Overview
This system is designed to optimize and automate the scheduling of maintenance tasks by processing daily maintenance logs. It leverages AI for structured data extraction and uses a deterministic scheduling algorithm to prioritize and allocate resources efficiently. The goal is to minimize operational costs and prevent severe maintenance failures in industrial settings.
![mermaid-diagram-2024-11-03-105628](https://github.com/user-attachments/assets/6f1f1193-7724-4926-9222-4ea774d7ef65)


## Problem Statement
Missed or delayed maintenance can lead to exponentially increased costs and operational inefficiencies, especially in large industrial operations. The system addresses these challenges by extracting critical maintenance data from bulk observer reports and scheduling necessary tasks based on severity and resource availability.

## Solution Approach
1. *Data Ingestion and Clustering*: 
   - At the end of each day, bulk maintenance logs and observer reports are processed in batch jobs.
   - Reports are clustered based on similar maintenance requirements, object similarity, and severity of issues.
  
2. *AI-Based Data Processing*: 
   - An LLM (e.g., LLaMA 3.1 70B on Together) is used to convert unstructured maintenance logs into structured reports.
   - The system extracts key information, including:
     - *What is wrong*: A detailed description of the issue.
     - *Severity*: The criticality level of the issue.
     - *Report Time*: When the issue was reported.
     - *Object ID*: The identifier for the affected equipment or system.
  
3. *Combining Reports*:
   - Reports concerning the same object and occurring around the same time are merged into a single high-level maintenance report.
   - These reports outline the issue, required resources, estimated time for repair, and any additional relevant details.
  
4. *Deterministic Scheduling*:
   - A deterministic scheduler takes the formatted maintenance reports and available resources as input.
   - It allocates maintenance tasks based on:
     - *Resource Availability*: Personnel, tools, and equipment needed for the task.
     - *Severity and Priority*: Ensuring critical issues are addressed promptly.
     - *Time Constraints*: Balancing efficiency with the urgency of repairs.

## System Components
1. *Data Processing Pipeline*:
   - *Input*: Bulk maintenance logs and observer reports.
   - *Processing*: Clustering and LLM-based structured data extraction.
   - *Output*: Consolidated and structured maintenance reports.

2. *AI Module*:
   - *Purpose*: Convert unstructured text into structured data.
   - *Model*: LLaMA 3.1 70B for extracting issue details, severity, and other key factors.
   - *Functionality*:
     - Requirement extraction
     - Severity identification
     - Clustering of similar requirements

3. *Deterministic Scheduler*:
   - *Input*: Structured maintenance reports and available resource data.
   - *Functionality*:
     - Schedule tasks based on severity, required resources, and time constraints.
   - *Output*: Optimized maintenance schedule.

## Installation
1. *Clone the Repository*:
   ```bash
   git clone https://github.com/your-repo/maintenance-scheduler.git
   cd maintenance-scheduler
   ```
2. *Install requirements*:
    ```bash
    pip install -r requirements.txt
    ```
3. *Run the app*:
    ```bash
    python3 app/main.py
    ```
