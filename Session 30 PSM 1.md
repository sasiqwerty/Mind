---
aliases: 
tags:
  - IC-CyberArk
date created: Friday, October 13th 2023, 3:10:06 pm
date modified: Monday, October 30th 2023, 8:51:40 am
---
[Session 30 PSM 1 - YouTube](https://www.youtube.com/watch?v=YYrePkmOxMc)

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

### RDS CAL License (Windows)

Client Access License (CAL) is a legal permit that authorizes a user to access network server services, such as file and print sharing, within an organization. Unlike standalone software products, a CAL is specifically designed to regulate the number of users connecting to a server for the usage of its services.  

- Device CALs : Device CALs are for every device accessing the server, suitable for shared devices across work shifts.  
- User CALs : User CALs are for every user accessing services on the server, ideal for employees using multiple or unknown devices.  
Until 2016 per user license was free. 2019 severs have a different style of installation for PSM

PSM application users have to be at the domain level when the [[Privileged Session Manager|PSM]] is installed on a Windows 2019 machine and working with a RDS CAL per-user license. (This also extends the sessions beyond one hour.)

#### How to Setup the License for RDS?

1. Install the Remote Desktop Licensing through the server manager
2. Open RD Licensing manager  

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

## Connection Flow of Sessions via PSM

The connection flow describes the series of steps and interactions that occur from the moment a request is initiated from the Password Vault Web Access (PVWA) to the point where a secure session is established with a target server. This process involves several components, including the Vault, the Privileged Session Manager (PSM), and various users and servers.

### Connection Flow Steps

 
1. **Initiate Request & Logon**: IT personnel initiates the process by logging on through the Privileged Web Access (PWWA) using HTTPS. A request is initiated from the PVWA to the Vault.
2. **Connect via RDP**: The Vault sends a message to the PSM server, informing it to expect an RDP (Remote Desktop Protocol) connection. Once authenticated, the IT personnel connects using RDP encapsulated over HTTPS.
3. **Download & Open RDP File**: An RDP file gets downloaded since the PSM functionality is enabled. Clicking on this file moves the process to the next step.
4. **Secure Session Establishment**: The PSMConnect user establishes a secure session, ensuring that the user doesn't need the actual system credentials. The PSM fetches these credentials from the vault.
5. **Temporary Profile Creation**: A temporary profile with the user PSMShadowUser is established on the PSM server.
6. **Connect using Native Protocols**: PSM establishes a connection to the desired system (e.g., databases, Windows servers, UNIX servers, etc.) based on the specified connection component like RDP for Windows servers, SSH for UNIX servers, or SQL for databases.
7. **Work on Target Server**: With the connection in place, a secure session allows work to be performed on the target server.
8. **Session Recording & Storage**: All actions performed during the privileged session are recorded by the PSM. These recordings are stored locally on the PSM server and are essential for auditing and compliance purposes.
9. **Transfer Recordings & Log Forwarding**: After the session is completed or terminated, the recordings are transferred to the Vault server in a designated PSMRecordings safe. Simultaneously, log data, inclusive of session activity, is relayed to SIEM systems, SIM systems, or syslog servers for comprehensive monitoring and analysis.

#### Devices/Systems Involved:

- **PWWA**: A web portal for accessing privileged sessions securely.
- **PSM**: The central component that manages, records, and audits privileged sessions.
- **Vault**: Securely stores credentials used for accessing systems.
- **Target Systems**: Includes databases, Windows servers, UNIX servers, VMWare systems, and network devices like routers and switches.
- **SIEM/SIM/Syslog**: Systems for logging, monitoring, and analyzing security-related events.


![[mermaid-diagram-2023-10-14-002920.svg]]

## PSM Internal Users and Groups

In a Privileged Session Management (PSM) environment, various specialized accounts and session types serve different roles. Here's a quick rundown:

- **PSMConnect**: Initiates PSM sessions on the PSM server.
- **PSMAdminConnect**: Monitors ongoing privileged sessions.
- **PSMShadowUser**: Auto-created for process isolation during a PSM connection.
- **PSMGwUser**: Serves as a gateway for user access to the Vault.
- **PSMAppUser**: Handles internal communication between an application and the vault.
- **PVWAGWUser**: Another gateway account for user access to the Vault.

### Detailed Breakdown

| Account/Session Type | Description | Purpose |
| -------------------- | ----------- | ------- |
| **PSMConnect**       | Initiates sessions on the PSM server. | Starts privileged sessions. |
| **PSMAdminConnect**  | Monitors live privileged sessions. | Session oversight and auditing. |
| **PSMShadowUser**    | Automatically created during a PSM connection. | Process isolation for sessions; prevents data leakage between sessions. |
| **PSMGwUser**        | Gateway account for accessing the Vault. | Impersonates user's access to the Vault. |
| **PSMAppUser**       | Manages internal processing between an app and the vault. | Internal communication and data exchange. |
| **PVWAGWUser**       | Another gateway account for Vault access. | Impersonates user's access to the Vault. |

### Additional Information

- **PSMShadowUser**: These users are created by the SYSTEM user and are non-privileged. Their primary purpose is to isolate processes, ensuring programs run under different identities for different vault users.
- **PSMConnect vs PSMAdminConnect**: While both initiate PSM sessions, PSMAdminConnect has an oversight role, allowing admins to monitor the sessions.
- **PSMGwUser and PVWAGWUser**: These are gateway accounts, but the context or differentiation between them might be specific to an organization's setup.

### Shadow Users

#### Introduction

- A PSM Shadow user is an account created automatically during a PSM (Privileged Session Manager) connection. 
- They serve to sandbox, or isolate, the client session, ensuring that programs initiated by different vault users on the same server run under distinct identities. This prevents information leakage between sessions. 
- These shadow users have no privileges and are created by the SYSTEM user. Their credentials are managed internally by the PSM server, which resets the shadow user's password with each new connection. 
- The PSM server's hardening procedure, detailed in the PIM Suite Installation Guide, restricts the use of these users and limits their permissions.

#### Purpose

Starting from version 6.0, PSM allowed various clients on the server (e.g., Toad, SQL+). To enhance security and scalability, version 7.0 introduced sandboxed client sessions through PSM Shadow users. A unique shadow user account is generated for each Vault user, existing as a local user on the PSM machine. During a PSM connection, the primary connection is made using the PSMConnect user. However, the client software is executed under the shadow user's context, ensuring full session separation. Each user benefits from distinct permissions, files, and registry entries, which protects against interference with other users' sessions.

#### Management

Shadow user accounts and profiles are deleted based on a configurable parameter named `ClearUserProfilesInterval`. This can be accessed in PVWA via:
   1. Administration Tab  
   2. System Configuration - Component Settings - Options  
   3. PIM Suite Configuration - Privileged Session Management - General Settings - Server Settings  
By default, this parameter is set to 30 days. If the associated Vault User is no longer present in the vault, the shadow user account and profile are deleted during this interval.

**Q4: What is the recommended method for cleaning up unused accounts/profiles?**  

For shadow users tied to existing vault users, it's advisable to retain their accounts. If the vault user is deleted, the associated shadow user will be automatically cleaned up during the next `ClearUserProfilesInterval` cycle. If there's a need to manually delete a shadow user account without removing the vault user:
   1. Navigate to Control Panel -> System -> Advanced system settings.
   2. Under the Advanced tab, within the User Profiles section, click on the Settings button.
   3. Select the desired user name and click the Delete button.

**Q5: Why do RDP sessions not require or use a PSM Shadow User account to connect through PSM?**  

The PSMRdpClient is unique in that it uses PSMConnect and not a shadow user. Using a shadow user for this purpose would inhibit certain features, like the ability to copy-paste between the client and target machine. There's also no security necessity for using shadow users with RDP sessions, unlike with other connection clients.

**Q6: How does password rotation on PSM Shadow User accounts work?**  

PSM Shadow User accounts do not have an automatic password rotation mechanism. However, it's worth noting that these accounts are considered low-risk. They are weak users, unable to remotely log into the PSM server. For added security, a new password is generated for each session.


[PSMConnect and PSMAdminConnect Domain Users | CyberArk Docs](https://docs.cyberark.com/PAS/Latest/en/Content/PAS%20INST/Optional-Moving-the-PSMConnec-and-PSMAdminConnect-users-to-your-Domain.htm)

[General settings | CyberArk Docs](https://docs.cyberark.com/PAS/Latest/en/Content/PASIMP/Configuring-the-Privileged-Session-Manager.htm?tocpath=Administrator%7CComponents%7CPrivileged%20Session%20Manager%7CConfiguration%7C_____1)

