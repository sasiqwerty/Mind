---
aliases: 
tags: 
date created: Friday, October 6th 2023, 8:08:15 pm
date modified: Saturday, October 7th 2023, 8:23:06 am
---

## LDAP Integration with the Privileged Account Security Solution

Directory mapping and integration of the [[Active Directory]] users and groups to the vault using a Bind account.  
- LDAP - Unsecured Connection (Port : 389)  
- LDAPS - Secure Connection over SSL (Port : 636)

### **Purpose Of LDAP Integration**:

1. **Centralized User Management**:
    - The Privileged Account Security solution can be tailored to manage users seamlessly via a unified User database, like LDAP.
2. **Full LDAP Client**:
    - The Enterprise Password Vault operates as a complete LDAP client.
    - It's adept at interfacing with LDAP-adherent or compatible directory servers to retrieve User identification and security details.
3. **Automatic User Provisioning**:
    - The integration facilitates the automatic onboarding of users.
4. **Use of LDAP Groups for Access Control**:
    - Enables the utilization of LDAP groups to grant Access Control to safes.

### **Requirements From the Customer for Integration**:

1. **LDAP Bind Account**:
    - The customer needs to supply an LDAP Bind account.
    - This account should possess READ ONLY privileges to the directory.
2. **Credentials for the LDAP Bind Account**:
    - User Name
    - Password
    - DN (Distinguished Name)
3. **LDAP Groups Representing Roles in the Digital Vault**:
    - CyberArk Administrators: Manages the overall system and its configurations.
    - CyberArk Safe Managers: Oversees the creation, modification, and deletion of safes.
    - CyberArk Auditors: Has the right to review and audit the system.
    - CyberArk Users: Regular users who can access and utilize the vault as per their privileges.  

In summary, integrating LDAP with the Privileged Account Security solution streamlines user management, making it centralized and efficient. It also empowers the solution with the ability to leverage LDAP groups for role-based access, ensuring that users have the right level of access to the right resources.

### LDAP Integration - Prerequisites

### **Security And Encryption**:

- **LDAP/S for Secure Communication**:
    - LDAP/S (LDAP over SSL) is mandatory to ensure a safe communication path between the Digital Vault and the Directory Server.
    - **Purpose**: 
        - To encrypt all traffic between the Domain Controller or the LDAP authenticating Server and the Vault. This step guarantees data integrity and confidentiality during data transmission.

### **Certificate Installation**:

- **Relevant Certificates**:
    - Both Root and Intermediate Certificates from the Certificate Authority (CA) that issued the certificate for the directory servers must be installed on the Vault Servers.

### **Hostname Resolution**:

- **Hosts File Configuration**:
    - A hosts file needs to be created on the vault servers. This aids in hostname resolution, ensuring proper network communication.

#### **Diagram Analysis**:

- **PWA (Password Vault Web Access)**:
    - Communicates over TCP port 443.
- **Production Vault Server**:
    - Links to the PWA over TCP port 1858.
    - Connects with the Directory Server using TCP port 636, which is typical for LDAP over SSL.
- **Directory Server**:
    - This is the server that houses the LDAP database and handles LDAP requests.

In essence, the prerequisites focus on ensuring secure communication, correct certificate management, and proper hostname resolution. These measures ensure that the integration between LDAP and the Digital Vault is both secure and functional.

### **LDAP Synchronization Summary:**

- A daily process synchronizes user attributes with an external directory.
- For removal from the Vault, users must be deleted from the external directory.
- The `DBParm.ini` file contains a parameter for this synchronization.
- The parameter `AutoSyncExternalObjects` is set to "Yes,1,5" which controls the synchronization behavior.

**Details:**

| Description                                 | Information                  |
|---------------------------------------------|------------------------------|
| **Synchronization Status**                  | Yes                          |
| **Number of Hours in One Period Cycle**     | 24                           |
| **Whether to Sync with External Directory** | Yes                          |
| **Duration of Sync**                        | Between 1st and 5th hour     |

## SMTP Integration - Simple Mail Transfer Protocol

- **CyberArk's Event Notification Engine (ENE)** is integrated within the Vault server to automatically dispatch email alerts regarding PAM activities. Through the **Simple Mail Transfer Protocol (SMTP)**, a push protocol, these emails are transmitted from the Vault server to clients.
- Proper SMTP integration, which necessitates details such as the server's name/IP, port, and credentials, ensures the efficient delivery of these notifications to end users.
- The SMTP protocol uses **Port 25** for communication.

| Topic/Concept                                  | Description                                                                      |
|------------------------------------------------|----------------------------------------------------------------------------------|
| **CyberArk Event Notification Engine (ENE)**   | - Sends email notifications about PAM activities.                                |
|                                                | - Installed as part of Vault server.                                             |
|                                                | - Operates as a service named *Cyber-Ark Event Notification Engine*.              |
| **Simple Mail Transfer Protocol (SMTP)**       | - Protocol for transferring electronic mail.                                     |
|                                                | - Utilized for sending mail from sender's client to recipient's server.          |
| **SMTP Integration**                           | - Configures email clients or applications to utilize an SMTP server.            |
|                                                | - Requires details such as the server's name/IP, port, and authentication info.  |

### SMTP Settings Overview

The SMTP settings facilitate email notifications from the Event Notification Engine (ENE). The setup requires specific details for accurate email dispatch:

| **Setting**            | **Description**                                                              | **Example from Image**                       |
|------------------------|------------------------------------------------------------------------------|----------------------------------------------|
| **SMTP address**       | IP address of the SMTP server; multiple IPs can be added for high availability. | `10.0.0.2`                                   |
| **Sender Email**       | Email address displayed as the notification sender.                         | `CyberArkNotifications@cyberark.com`         |
| **Sender Display Name**| Name displayed as the sender's name.                                         | `CyberArk Notifications`                     |
| **SMTP Port**          | Port used by the ENE to send notifications.                                  | `25`                                         |
| **Recipients Domain**  | Domain where the recipient's email account resides.                         | `https://comp1a.cyber-ark.demo.local`        |
| **PVWA URL**           | URL of the machine where the PVWA is installed.                              | Not explicitly shown in the provided image. |

These settings ensure that ENE sends notifications properly via the SMTP protocol to the intended recipients.

## SNMP - Simple Network Management Protocol

SNMP (Simple Network Management Protocol) is a protocol used to manage and monitor network devices like servers and more. Integration of SNMP allows administrators to remotely monitor network performance, detect faults, or assess the health of devices in their network.

### **Purpose Of SNMP in Remote Monitoring:**

Remote monitoring uses SNMP to relay Vault traps to a distant terminal, enabling the extraction of information both from the Operating System and the Vault Server.

- **Operating System Information:**
  - **CPU Usage:** Monitors the processing power usage.
  - **Memory Usage:** Keeps track of RAM utilization.
  - **Disk Usage:** Observes the storage consumption.
  - **Event Log Notifications:** Alerts based on specific system events.
  - **Service Status:** Updates about the status of various services running.

- **Component-specific Information:**
  - **Password Vault Status:** Provides the operational status of the Password Vault.
  - **DR Vault Status:** Indicates the Disaster Recovery Vault's operational condition.
  - **Password Vault and DR Vault Logs:** Records of activities and events related to the Password Vault and DR Vault.

This integration ensures that administrators receive real-time updates on both system metrics and specific components, helping in proactive management and issue resolution.

### **SNMP Integration with CyberArk:** Simple Network Management Protocol

CyberArk recommends using the Digital Vault to send SNMP status information directly to your monitoring solution.

**Prerequisites for Integration:**

| Requirement | Description | Example |
|:---|:---|:---|
| **IP Addresses** | Servers that can receive SNMP traps. | |
| **Community String** | A password for device stats access. | |
| **MIB Files** | Files for the SNMP administrator. Included with the Digital Vault. | |
| **Team Resource** | An expert in SNMP monitoring. | |

### **Remote Control Agent for SNMP Configuration:**

Configure the Remote-Control Agent during initial vault server setup for SNMP. If missed, it can be configured post-installation. For detailed steps, visit [CyberArk's Documentation](https://docs.cyberark.com).

**Visual Guide**:  
In the PrivateArk Server Setup:
1. **Skip** or **Configure** the Remote Control Agent.
2. Input:
   - IP Addresses: e.g., `192.168.128.1,192.168.128.22`
   - Password and confirmation.

### **`paragent.ini` Configuration for SNMP:**

Ensure SNMP traps are sent to the specified remote computer.

| Configuration | Description | Example |
|:---|:---|:---|
| **SNMPHostIP** | IP of the remote computer. | `10.0.1.1` |
| **SNMPTrapPort** | Port for SNMP traps. | `162` |
| **SNMPCommunity** | Origin of SNMP traps. | `"public"` |

Post changes, save the `paragent.ini` file with correct infrastructure and network values.

### **Post-Configuration Steps:**

1. **Restart**: Navigate to services panel and restart the `PrivateArk Remote Control Agent` service.
	1. **Verify**: Check with the SNMP console administrator to ensure SNMP messages are received and readable.

### **SIEM Integration with CyberArk:**

SIEM (Security Information and Event Management) Integration correlates Privileged Account Usage with its Activity.

**Key Aspects:**

- IP addresses for servers accepting **SYSLOG messages**.
- The Vault can utilize **TLS, TCP, or UDP** protocols for message transmission.
- To use **TLS**, a signed certificate for the syslog server is essential.

### **SIEM Setup:**

1. **Purpose**: Integrating with SIEM enables the forwarding of audit log data to the SIEM console for aggregation, alerts, and reporting.
2. **Translator Files**: These files convert CyberArk's log format to that of the SIEM's.
   - Rename one of the provided sample translator files.
   - Five files are included for popular SIEM systems.
   - For **Splunk** users, download the CyberArk add-on from the Splunk website.  
![[Pasted image 20231006222514.png]]

### **Syslog Configuration in `dbparm.ini`:**

| Feature | Details |
|:---|:---|
| **Multiple IPs & Filters** | Allows various IP addresses and Message Code filters. |
| **Example Configuration** | Demonstrates how to send different syslog messages encrypted to one syslog server. |
| **Root CA Certificate** | Located at the root of the Vault installation directory. |

![[Pasted image 20231006222533.png]]

![[Pasted image 20231006222546.png]]  
For a comprehensive guide, refer to [CyberArk's Documentation](https://docs.cyberark.com) under "Security Information and Event Management Applications".

### **Post-Integration Steps:**

1. **Restart Service**: Use the Windows Services tool to restart the `PrivateArk Server Service`. Ensure service dependencies also restart.
2. **Verification**:
   - Communicate with the SIEM console's administrator to confirm the receipt and readability of SYSLOG messages.
   - Review logs for error checking and validation.