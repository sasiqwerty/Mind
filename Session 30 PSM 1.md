---
aliases: 
tags: 
date created: Friday, October 13th 2023, 3:10:06 pm
date modified: Friday, October 13th 2023, 11:22:30 pm
---

## What Are the Functions of PSM?

Privileged Session Manager (PSM) enables organizations to secure, control and monitor privileged access to network devices by using Vaulting technology to manage privileged accounts and create detailed session audits and video recordings of all IT administrator privileged sessions on remote machines.

PSM enables users to log on to remote (target) machines or open applications securely through a proxy machine. The established sessions on the target systems are fully isolated and the privileged account credentials are never exposed to the end-users or their client applications and devices. The PSM architecture enables securing of sensitive privileged sessions while facilitating streamlined and native workflows for the IT administrators.

### Overview

PSM (Privileged Session Manager) offers users two primary methods to connect:

1. **PVWA Portal**: Users can establish a connection via the PVWA portal.
2. **PSM for Windows**: Direct desktop connection is facilitated using standard RDP client tools like MSTSC, various Connection Managers, or an RDP file.

A few key points regarding the connection process:

- **Default RDP Protocol**: Typically, connections to the PSM are initiated using port 3389 with the RDP protocol. However, this port might not always be accessible due to corporate firewall restrictions.
- **HTML5 Gateway**: For users connecting via the PVWA portal, PSM can leverage an HTML5 gateway. This mode employs a secure WebSocket protocol (port 443), eradicating the need for an RDP connection from the user's end. All that's required from the user is a web browser.
- **Microsoft Remote Desktop Gateway (RDGateway)**: PSM is also adaptable to work in tandem with RDGateway. This tunnels the RDP session through the HTTPS protocol (port 443), ensuring a secure connection without firewall modifications. The HTTPS protocol ensures that all data exchanged between the user and the PSM machine remains encrypted and safeguarded, facilitating secure remote and cross-network access.

The above mechanisms promote secure, flexible, and convenient access to PSM, catering to diverse user needs and organizational security standards.

### Connection Flow

**Connect through PVWA portal**: 
1. Users log onto PVWA, select an account and connection protocol.
2. They're redirected to the PSM server.
3. Connection to PSM is made via RDP; SSL can be used for extra security.
4. PSM retrieves account credentials from the Vault and connects to the target system.
5. All session activities are recorded and stored in the Vault for authorized access.

**Connect through PSM for Windows**:
1. Users configure an RDP client application to connect via PSM.
2. After authenticating with Vault credentials, they connect to PSM using RDP; SSL is an option.
3. PSM fetches account credentials from the Vault and connects to the target.
4. Session activities are recorded and saved in the Vault for authorized viewing.

## Server Specifications and Installation Information about PSM

- Windows Server 2016,2019 (Windows 2012 Support is Deprecated and 2022 is yet to be announced)
- .NET Framework 4.8
- Remote Desktop Services (RDS) Session Host
- Remote Desktop Gateway (optional)
- Before installing PSM, make sure that the Users group has the Allow Logon Locally Windows permission in the local security policy. This ensures that the PSMShadowUsers group created during PSM installation will have the required permissions. Alternatively, you can set this local security policy permission for the PSMShadowUsers group directly after PSM installation.  

More on this topic - [[PSM Shadow User]] 

### System Requirements and Installation

| Minimum System Requirements  | Details  |
|---|---|
|Platform:|8 core processor (Intel compatible)|
|Disk space:|80GB free disk space for installation, and additional 80GB space for temporary workspace|
|Minimum memory:|8 GB|
|Communication:|TCP/IP connection Port to the Digital Vault Server|      


| Specification                                 | Small Implementation (1-10 sessions) | Mid-range Implementation (11-50 sessions) | Large Implementation (51-100 sessions) |
|-----------------------------------------------|---------------------------------------|-------------------------------------------|----------------------------------------|
| **Processor**                                 | 8 core (Intel compatible)             | 16 core (Intel compatible)                | 32 core (Intel compatible 2.1-2.6 GHz) |
| **RAM**                                       | 8GB                                   | 16GB                                     | 32GB                                  |
| **Storage**                                   | 2X 80GB SATA/SAS (hot-swappable)      | 2X 80GB SATA/SAS (hot-swappable)         | 2X 250GB SAS (hot-swappable, 15K RPM)  |
| **RAID**                                      | RAID Controller                       | RAID Controller                          | RAID Controller                       |
| **Network**                                   | Network adapter (1Gb)                 | Network adapter (1Gb)                    | Network adapter (1Gb)                 |
| **DVD ROM**                                   | DVD ROM                               | DVD ROM                                  | DVD ROM                               |
| **Maximum Chrome sessions per user**   (RDP)       | 15 concurrent                         | 50 concurrent                            | 100 concurrent                        |
| **Total Chrome sessions per PSM server**   (RDP)   | 15 concurrent                         | 50 concurrent                            | 100 concurrent                        |
| **Maximum Chrome sessions per user**       (RDP)   | 15 concurrent          | 50 concurrent          | 100 concurrent          |
| **Total Chrome sessions per PSM server**   (RDP)   | 15 concurrent          | 50 concurrent          | 100 concurrent          |
- When adding concurrent sessions per user, make sure to increase the default timeout per session accordingly.
- When increasing the number of Chrome sessions, regardless of PSM usage, make sure to follow best practices regarding machine CPU and server capabilities.

#### Domain User Installation Step Explained

The PSM, when installed with a domain user, facilitates Remote app features and session collection. Typically, domain users are preferred for application installations due to the benefits of cross-server communication, centralized auditing and logging, and accessing domain resources.

| **Feature/Requirement**         | **Details**                                                                                                      |
|--------------------------------|------------------------------------------------------------------------------------------------------------------|
| **Remote App Features**         | Installing PSM with a domain user allows leveraging Remote App capabilities, letting users access specific applications remotely as if they were running locally.      |
| **Session Collection**          | Supports efficient session collection, enabling the system to capture, store, and manage user session details.                                      |
| **Cross-Server Communication**  | Enables seamless communication across various servers in the domain, vital for interoperability and data sharing.                          |
| **Auditing and Logging**        | Centralizes auditing and logging, ensuring all application activities are tracked and logged in a unified location.                            |
| **Access to Domain Resources**  | Facilitates easy access to other domain resources, including file shares, databases, and domain services, simplifying configurations and permissions. |

#### Hardening

[GPO Parameters for In-Domain Automatic Hardening | CyberArk Docs](https://docs.cyberark.com/PAS/Latest/en/Content/PASREF/PSM-in-domain-GPO.htm)

#### Other Points

1. **Concurrency Limit**: The concurrency of 100 sessions per PSM server should never be surpassed.
2. **Basis of Session Ranges**: The concurrent session ranges derive from RDP and SSH connections performance evaluations.
3. **Resource-Intensive Applications**: Operating applications such as Toad, vSphere Client, etc., on the PSM server can lead to diminished concurrency.
4. **Dedicated Server Assumption**: The mentioned concurrent session ranges presuppose that the PSM operates on a sole server.
5. **Video Recording Influence**: The session ranges are contingent upon performance metrics while capturing user activities in HD resolution (a single screen). Given that video recording's clarity hinges on the desktop resolution of the client device making the connection, higher resolutions or multiple screens can reduce concurrency.
6. **Virtual Machine Installation**: When setting up the PSM server on a VM, it's vital to allocate virtual hardware that mirrors the recommended physical specifications. For a more comprehensive overview, see the section on optimal settings for PSM installation on a virtual platform.
7. **Virtual Machine Impact**: Establishing the PSM server on a virtual machine can cut the peak concurrency by up to 40%. 

### Decommissioning and Upgrade of Servers

1. **Pause**: Wait for 10-15 days post the server shutdown intended for an upgrade.
2. **Checkup**: Inspect other servers for possible issues in this period.
3. **Reroute Traffic**: Divert traffic from the server set for decommissioning.
4. **App Removal**: Delete all software from the designated server.
5. **Cleanse Users**: Remove users associated with the decommissioned server from the storage.
6. **Optimal Positioning**: Keep PSM and PVWA servers near to both users and their associated servers to ensure a quick response time.
7. **Upgrade**: Implement the necessary components on the server.

![[Pasted image 20231013171744.png]]

### Storage Requirement for PSM Recordings

The Privileged Session Manager (PSM) is responsible for securely storing session recordings. These recordings can either be stored on the Digital Vault server or on an external storage device. 

- **Storage Location**: You can opt to store the session recordings on the Digital Vault server or make use of an external storage device. For comprehensive details on how to store recordings on an external device, refer to the [External Storage Device documentation](https://docs.cyberark.com/PAS/Latest/en/Content/PASIMP/ExternalStorage.htm).

- **Estimated Storage Requirement**: It's estimated that each minute of a recording session will require between 50-250 KB of storage space. The exact size is determined by:
  - The type of session recording (console vs. GUI recording).
  - The type and volume of activities performed during the session.
  
  You can get more insights on this from the [Planning capacity documentation](https://docs.cyberark.com/PAS/Latest/en/Content/PAS%20INST/Considerations-Before-Installing-PSM.htm#_Ref465255572).

- **Recommendation**: To pinpoint the recording size more precisely for your session recordings, it's advisable to examine the size of an average session recording within your specific environment.

### **CyberArk Component Compatibility with PSM**

The Privileged Session Manager (PSM) is designed to be compatible with various CyberArk components. Here's a breakdown of its compatibility:

| **CyberArk Component**                   | **Compatibility with PSM**                                                                                                         |
|-----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Digital Vault server                    | ✅ Compatible                                                                                                                      |
| Password Vault Web Access               | ✅ Compatible                                                                                                                      |
| Privileged Session Manager SSH Proxy    | ✅ Compatible                                                                                                                      |
| CPM                                     | ✅ Compatible                                                                                                                      |

Each PSM version aligns with all versions of these components that have not reached their End of Development Date when the PSM version is rolled out.

**Examples**:

- **PSM 11.6**: Released in August 2020. It's compatible with versions 10.5 and above of these components.
  
- **PSM 11.5**: Rolled out in June 2020. This version aligns with versions 10.4 and higher of the said components.

### HTML5 Gateway Hardware Specifications

|Small + Mid-range implementation<br><br>(1-50 concurrent RDP/SSH sessions)|Mid-range + Large implementation<br><br>(51-100 concurrent RDP/SSH sessions)|Very large implementation<br><br>(101-200 concurrent RDP/SSH sessions)|
|---|---|---|
|- 2 core processors (Intel compatible)<br>- 4 GB RAM|- 4 core processors (Intel compatible)<br>- 8 GB RAM|- 8 core processors (Intel compatible)<br>- 16GB RAM|

Files that are transferred during an HTML5 Gateway session are temporarily stored on the HTML5 Gateway machine, so the machine must have enough available storage space. For example, if there will be 20 sessions that transfer files at the same time, and each session will transfer at most 5GB, you need 100GB of available storage.

### Requirements from the End User

|Required Component|Version|
|---|---|
|RDP ActiveX Client|5.2 or later for environments set up to use an ActiveX connection method for PSM connection)|
|CyberArk PSM codec|For viewing high compression session recordings with an external player (for example, Windows Media Player). The PSMCodec.exe is included in the PSM installation package and is required to enable users to view PSM recordings with a regular media player (not PSM Direct Playback).|
|JRE (Java Runtime Environment)|JRE 1.4, or later (for SSH transparent connections)|

### RDS CAL License

Client Access License  
1. Install the Remote Desktop Licensing through the server manager
2. Open RD Licensing manager  
Device CALs : Device CALs are for every device accessing the server, suitable for shared devices across work shifts.  
User CALs : User CALs are for every user accessing services on the server, ideal for employees using multiple or unknown devices.

### Notes

- Due to RDS licensing enforcement in Windows 2019, a per-user license is no longer supported for local users. We recommend using a per-device RDS license. 
- To work with a per-user license on a Windows 2019 machine, <span>PSM</span> users must be moved to the domain level.
- [PSMConnect and PSMAdminConnect Domain Users (cyberark.com)](https://docs.cyberark.com/PAS/Latest/en/Content/PAS%20INST/Optional-Moving-the-PSMConnec-and-PSMAdminConnect-users-to-your-Domain.htm)
- Make sure you have the required number of RDS CALs to enable you to access the RDS server. For more information, refer to [Connect to the PSM server with Microsoft Remote Desktop Services (RDS) Session Host](https://docs.cyberark.com/PAS/Latest/en/Content/PAS%20INST/Considerations-Before-Installing-PSM.htm#_Ref332289750).
- PSM can be installed on Amazon Web Services (AWS), Microsoft Azure, and Google Cloud Platforms

## PSM Supported Connections/Platforms

| Platform                               | Additional Information                                                                                                       |
|----------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| Unix, Linux & Network for SSH-based    | - SSH (including file-transfer capabilities) <br> - Telnet                                                                 |
|                                        | **Note**: Connections to and from Windows 2003 and earlier versions are not supported.                                      |
| Windows RDP (file-transfer capabilities)| **Note**: Target Windows servers must not enable the 'Always prompt for password' policy setting.                           |
| Windows Remotely Anywhere              |                                                                                                                                 |
| AS400 (Series)                         |                                                                                                                                 |
| OS/390 (z/OS)                          |                                                                                                                                 |
| Web-based interfaces & custom apps     |                                                                                                                                 |
| PSM for Databases                      | - Oracle DBA tools: <br>   - Toad <br>   - SQLPlus <br>   - Toad for Oracle (specific versions) <br>   - Toad Admin Module <br> - Microsoft SQL Server DBA tools: <br>   - SQL Server Management Studio (specific versions)                          |
| PSM for Virtualization                 | - VMware administration tools: <br>   - vSphere Client for vSphere/ESX hosts <br>   - vSphere Client for vCenter <br> **Notes**: <br>   - vSphere Client isn't supported on certain configurations <br>   - Alternative solutions for Windows 2016 R2 customers.             |

[General settings | CyberArk Docs](https://docs.cyberark.com/PAS/Latest/en/Content/PASIMP/Configuring-the-Privileged-Session-Manager.htm?tocpath=Administrator%7CComponents%7CPrivileged%20Session%20Manager%7CConfiguration%7C_____1)

