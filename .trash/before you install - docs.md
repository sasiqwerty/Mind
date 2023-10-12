---
aliases: 
tags: 
date created: Thursday, August 31st 2023, 10:57:06 am
date modified: Thursday, August 31st 2023, 11:10:55 am
---
[Before You Install | CyberArk Docs](https://docs.cyberark.com/PAS/12.6/en/Content/PAS%20INST/Considerations-before-Installation.htm?tocpath=Installation%7C_____2) #website #docs 

## Stage 1 - Architecture

- Vault
- High Availability Vault
- Disaster Recovery Vault
- Remote Administration
- High Availability Clustering
- PrivateArk Administrative Client
- Backup solution (CyberArk or other)
- Disaster Recovery site
- Password Vault Web Access
- Central Policy Manager
- Developer Tools
    - REST API web services
    - PACLI
- Privileged Session Management
    - Privileged Session Manager
    - Privileged Session Manager SSH Proxy
- Privileged Threat Analytics
    - PTA Server
    - PTA Disaster Recovery
    - PTA Windows Agents
    - PTA Network Sensor
- On-Demand Privileges Management
- Application Access Management
    - Credential Provider
    - Central Credential Provider
    - Application Server Credential Provider

When you prepare this architectural design, consider the following:

1. **Network Topology**:
    
    - **Consideration**: The arrangement and interconnection of your networks and where your vault(s) will be placed.
    - **Details**:
        - How many vaults are needed?
        - Where will these vaults be located - internal network, external network, or DMZ?
        - Management location for these vaults?
        - Access points for these vaults?
2. **High Availability**:
    
    - **Consideration**: Ensuring the system remains available and operational, even when some components fail.
    - **Details**:
        - Total number of passwords stored in the vault.
        - Frequency of password access.
        - Importance of continuous access (24/7).
3. **Multiple CPMs/PSMs (Central Policy Managers/Privileged Session Managers)**:
    
    - **Consideration**: The need for multiple policy and session managers.
    - **Details**:
        - Need for distributed architecture.
        - Need for high availability.
4. **Multiple PVWAs (Password Vault Web Accesses)**:
    
    - **Consideration**: The requirement for multiple web access points to the vault.
    - **Details**:
        - Need for distributed architecture.
        - Need for high availability.
        - Need for different authentication types.
        - Access requirements from various networks.

These considerations are crucial for companies to assess before implementing a password vault system. It helps ensure that the solution is robust, scalable, and can serve the business requirements without causing disruptions or vulnerabilities.

When planning for a PAM system, it's crucial to think about not only the immediate needs but also the potential growth and changes in the company's infrastructure, so future scaling or modifications are as smooth as possible.

## [[Stage 2 - Security Fundamentals]]

## Stage 3 - Authentication and User Management

## Stage 4 - Access to the [[Vault]]

## Stage 5 - Manage the [[Vault]]

## Stage 6 - Manage the Log Vault Activity