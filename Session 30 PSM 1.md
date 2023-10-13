---
aliases: 
tags: 
date created: Friday, October 13th 2023, 3:10:06 pm
date modified: Friday, October 13th 2023, 3:57:54 pm
---

## What Are the Functions of PSM?

Privileged Session Manager (PSM) enables organizations to secure, control and monitor privileged access to network devices by using Vaulting technology to manage privileged accounts and create detailed session audits and video recordings of all IT administrator privileged sessions on remote machines.

PSM enables users to log on to remote (target) machines or open applications securely through a proxy machine. The established sessions on the target systems are fully isolated and the privileged account credentials are never exposed to the end-users or their client applications and devices. The PSM architecture enables securing of sensitive privileged sessions while facilitating streamlined and native workflows for the IT administrators.

### Overview

Users can connect through the PVWA portal, or alternatively through PSM for Windows, that is, directly from their desktops using any standard RDP client application, such as MSTSC, different Connection Managers or an RDP file.

By default, the user connects to the PSM machine through port 3389, using the RDP protocol. This is required to facilitate remote access, although this port is not usually opened in the corporate firewall, and in some cases it is not permitted.

You can configure PSM to provide secure remote access to a target machine through an HTML5 gateway when connecting with the PVWA portal. The HTML5 gateway tunnels the session between the end user and the PSM machine using a secure WebSocket protocol (port 443). This eliminates the requirements to open an RDP connection from the end-user's machine. Instead, the end user only requires a web browser to establish a connection to a remote machine through PSM.

Alternatively, PSM can be configured to work with the Microsoft Remote Desktop Gateway (RDGateway) which tunnels the RDP session between the user and the PSM machine using the HTTPS protocol (port 443). This provides a secure connection without needing to open the firewall. All information that is transferred between the user and the PSM machine is encrypted and protected by the HTTPS protocol, which enables secure cross-network and remote access.

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

## Server Specifications for PSM

- Windows Server 2016,2019 (Windows 2012 Support is Deprecated and 2022 is yet to be announced)
- .NET Framework 4.8
- Remote Desktop Services (RDS) Session Host
- Remote Desktop Gateway (optional)
- Before installing PSM, make sure that the Users group has the Allow Logon Locally Windows permission in the local security policy. This ensures that the PSMShadowUsers group created during PSM installation will have the required permissions. Alternatively, you can set this local security policy permission for the PSMShadowUsers group directly after PSM installation.  

More on this topic - [[PSM Shadow User]] 

### Minimum System Requirements

| Minimum System Requirements  | Details  |
|---|---|
|Platform:|8 core processor (Intel compatible)|
|Disk space:|80GB free disk space for installation, and additional 80GB space for temporary workspace|
|Minimum memory:|8 GB|
|Communication:|TCP/IP connection to the Digital Vault Server|      

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
