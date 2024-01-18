---
aliases: 
tags: 
date created: Friday, January 12th 2024, 2:16:47 pm
date modified: Thursday, January 18th 2024, 9:32:09 am
---

## JD Break down

The job description for the "Security Analyst" position at Netlink Software Pvt Ltd includes:

1. **Required Experience and Skills:**
   - Deep technical knowledge in Identity and Access Management (IAM) & Privileged Access Management (PAM) technologies.
   - Expertise in tools such as CyberArk, SailPoint, EPM, and Secrets management.
   - Minimum certification requirement of CyberArk Defender, with Sentry certification preferred.
   - Strong scripting skills in PowerShell, Python, and AutoIT.
   - Good data analytical skills.
   - Experience with cloud solutions (internal, public, and hybrid) across major platforms like AWS, Azure, and GCP.
   - Proficiency in supporting live production environments.

2. **PAM Operational Responsibilities:**
   - Creating Safes, defining Access Control, policies/platforms.
   - User provisioning and entitlements.
   - Managing Applications Credentials and Auto upload.
   - User Access Policy Management.
   - Conducting Privileged Access Reviews, Compliance Reporting, and managing Access Control Processes.

3. **Technical and Professional Abilities:**
   - Ability to understand and follow both high-level and low-level infrastructure architectures.
   - Familiarity with high availability application architectures including load balancing and failover techniques.
   - Significant experience in integration, migration, and resolving communication issues among various applications, databases, and technology platforms.
   - Understanding of login mechanisms to platforms (SSH, RDP).

4. **Working Methodology:**
   - Knowledge and experience with agile methodologies, DevSecOps operation practice, and ITIL service management model.
   - Capability to work as part of a global team, showing initiative, balancing workload, and prioritizing tasks effectively.
   - Proven experience in a Cyber Security environment with an understanding of risk and priorities.

5. **Communication Skills:**
   - Excellent verbal and written communication skills.
   - Ability to interact professionally with multiple stakeholders and technical teams, including Technical Engineers and Developers.

6. **Other Relevant Experience:**
   - Experience and understanding of Software Development Life Cycle (SDLC), ITIL, IT service management processes, and release management.

The role emphasizes a strong background in cybersecurity, specifically in PAM and IAM technologies, with a focus on operational tasks, teamwork, and effective communication in a global team environment.  

## Talking Points

### CyberArk Infrastructure Breakdown

Here's a simplified breakdown of the CyberArk implementation infrastructure, formatted into tables for clarity.

#### General Infrastructure Overview

| Component            | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| Server Distribution  | 70% on-premises, 30% in the cloud (for testing and validation)               |
| Authentication       | CyberArk with LDAPS (port 636), also unencrypted port 389 available          |
| Failover Standards   | Adheres to fail back and fail over standards to protect data integrity      |
| Accounts & Safes     | Approximately 70,000 accounts, 300 safes, and similar number of platforms   |

#### Vault Configuration

| Component | Description                                                                         |
|-----------|-------------------------------------------------------------------------------------|
| Main Vault| Located on-premises                                                                 |
| DR Vault  | In a different location for Disaster Recovery (DR)                                  |
| CPM for DR| Dedicated Central Policy Manager (CPM) connected for DR failover                   |
| DR Drill  | Performed quarterly with full system backup prior to the drill                     |

#### Password Vault Web Access (PVWA)

| Component    | Description                                                                      |
|--------------|----------------------------------------------------------------------------------|
| PVWA Count   | 6 PVWAs, with additional 2 on standby for emergencies                            |
| Load Balancer| F1 load balancer, distributed across 2 data centers in a round-robin configuration|
| Cloud PVWAs  | Additional PVWAs in the cloud for resilience testing                             |

#### Central Policy Manager (CPM)

| Component | Description                                                |
|-----------|------------------------------------------------------------|
| CPM Count | 3 active CPMs, 2 backup CPMs, and 1 connected to DR Vault  |

#### Privileged Session Manager (PSM)

| Component | Description                                                                                     |
|-----------|-------------------------------------------------------------------------------------------------|
| PSM Count | 16 PSMs connected to F1 load balancer, operating in a round-robin fashion for session management|

#### Privileged Session Manager for SSH (PSMP)

| Component | Description                                      |
|-----------|--------------------------------------------------|
| PSMP Count| 4 installed PSMPs, with 1 additional for backup  |

This table format simplifies the understanding of the CyberArk implementation, focusing on the key components and their roles in the infrastructure.

### Daily Activities

We have a personal account which has access to Admin accounts so we login to CyberArk with our account and using PSMs we connect to admin accounts without ever needing to know the password. only very few people are allowed to know the password for security reasons. to the connect to PrivateArk client we use the PSM-PRIVATEARK connection.

#### Health Check

We perform daily health checks and ensure that all the servers are up and running and the connected components are working as intended any deviation is reported.  
I have a written a small script in powershell using Test-NetConnection that automates this process, and pings all the servers and gives the FQDN of the server once the ping test is complete. It will also give back the list of servers that its not able to ping making testing easier and less confusing.  
I am planning to automate this script by adding a service user login to the [[Windows Task Scheduler|Task Scheduler]] and ensuring that this script runs in the background and sends an email automatically to the intended user. This part is still development I only tested this in my VMs.

#### Onboarding of Accounts

- there are 4 ways of doing this, I only get to use 3 of them as REST APIs are beyond me but willing to learn.
- the first is manual and adding everything in the PVWA.
- servers that are part of the CyberArk domain can also be automatically detected and ready to be added
- the the last one is using PVWA bulk upload. we create an excel file and with the platform safe and safe template details and based on that accounts are onboarded.

#### [[Safe Management and Access Provisioning]]

We are tasked to check on permissions and deploy permissions based on requirement with proper safe handling.

#### [[Platform Management]] And Master Policy

#### Reports

#### Backup and Restore

#### DR Drill

## Summary Of Netlink

Netlink Software is a prominent US-based multinational corporation specializing in professional information technology and business process solutions. Since its inception in 1999, Netlink has established itself as a leading provider in these domains. The company boasts a diverse clientele, including major corporations like Starbucks, General Motors, Visteon, Lear, Dish, AT&T, BMW, Lufthansa, Delphi, Land Rover, Ford, Network Solutions, Daimler, Takata, and Rexall.

Key Highlights:

- **Employee Excellence:** Netlink prides itself on its team of dedicated, high-integrity professionals. This includes subject matter experts (SMEs), process experts, individuals with advanced degrees in various fields, and a range of IT professionals (software and network engineers, architects, analysts, programmers, developers, and administrators). These team members are committed to delivering exceptional results and fostering customer-driven relationships, with an emphasis on being approachable and easy to work with.

- **Business Growth:** The company has experienced remarkable growth, with average annual revenue increases exceeding 100% since its founding. This growth is attributed to Netlink's ability to accurately anticipate client needs and provide effective solutions and personnel.

- **Global Presence:** Netlink has an extensive global footprint, with operations in 46 countries. This includes 13 sales offices, 11 operational centers, 6 delivery centers, and 3 data centers, reflecting the company's extensive reach and capability to serve a global clientele.

In summary, Netlink Software stands out for its exceptional team, significant and consistent growth, and a broad international presence, all underpinned by its commitment to delivering immediate and impactful business results to its clients.