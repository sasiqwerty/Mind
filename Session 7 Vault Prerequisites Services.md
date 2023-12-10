---
aliases: 
tags: 
date created: Wednesday, October 4th 2023, 5:05:45 pm
date modified: Tuesday, December 5th 2023, 5:26:18 am
---
[CyberArk Vault Structure | CyberArk Docs](https://docs.cyberark.com/PAS/latest/en/Content/PASIMP/CyberArk-Vault-Structure.htm?tocpath=Administrator%7CComponents%7CDigital%20Vault%7CAdvanced%20Digital%20Vault%20Environment%7CCyberArk%20Vault%20Structure%7C_____0)  
[[listen-session07]]

![[Session07-Vault-Prerequisites-Services.mp3]]

## Vault Server Specs

- What is cloud server?

[Vault Specifications | CyberArk Docs](https://docs.cyberark.com/PAS/Latest/en/Content/PASREF/Vault%20Specifications.htm)  
![[vault-specs (2).svg]]  
[[vault specifications]]

## Vault Installation Prerequisites

> Windows 2012 is not supported anymore for vault installation

Below are the essential prerequisites for the Vault installation:

| Prerequisite                                        | Description                                                     |
|-----------------------------------------------------|-----------------------------------------------------------------|
| **Operating System**                                | - Windows server 2016/2019                                      |
| **Framework**                                       | - .Net Framework 4.8 or above                                   |
| **Software Packages**                               | - Microsoft Visual C++ Redistributable package                  |
|                                                     | - Vault software                                                |
| **Essential Media & Files**                         | - Master CD                                                     |
|                                                     | - Operator CD                                                   |
|                                                     |   * Server.Key                                                  |
|                                                     | - License file                                                  |
| **Server Configuration Recommendations**            | - Vault should not be a domain-joined server. Instead, add Vault to the workgroup. |
|                                                     | - Install the Vault server in an isolated zone.                 |

### **Specifications By Implementation Size**

| Implementation Size                          | Processor                        | RAM  | Storage                          | Other Components                          |
|----------------------------------------------|----------------------------------|------|----------------------------------|-------------------------------------------|
| **Small (< 1,000 passwords)**                | Quad core (Intel compatible)     | 8GB  | 2X 80GB SATA/SAS hot-swappable  | RAID Controller, 1Gb Network adapter, DVD ROM, Optional: Additional storage for PSM |
| **Mid-range (1,000-20,000 passwords)**       | 2X Quad core (Intel compatible)  | 16GB | 2X 80GB SATA/SAS hot-swappable  | RAID Controller, 1Gb Network adapter, DVD ROM, Optional: Additional storage for PSM |
| **Large (20,000 – 100,000 passwords)**       | 2X Eight core (Intel compatible) | 32GB | 2X 250GB SAS (15K RPM)          | RAID Controller, 1Gb Network adapter, DVD ROM, Optional: Additional storage for PSM |
| **Very Large (> 100,000 passwords)**         | 4X Eight core (Intel compatible) | 64GB | 2X 500GB SAS (15K RPM)          | RAID Controller, 1Gb Network adapter, DVD ROM, Optional: Additional storage for PSM |                                                                                                                                                                                                                                      
Ensure you have all these prerequisites in place before proceeding with the installation of the Vault.  

### Third Party Apps

1. **Installation Restriction**: 
   - Do **not** install 3rd party applications on the system.
   - Such installations are strictly prohibited.
2. **Safety & Performance**: 
   - Abstaining from installing 3rd party applications enhances the overall safety and performance of the system.
3. **Support Limitation**: 
   - If any 3rd party apps are found installed on the vault server, the CyberArk team will not provide support when issues arise.

### Vault Server Location

1. **Domain Joining**:
   - The vault **should not** be domain joined.
   - If domain joined, group policies will be applicable to the vault, which is not recommended.
2. **Port Restrictions**:
   - The [[Vault]] accepts data only through port `1858` (it can be changed, but its a very hard process and its not recommended.)
3. **Security Mechanism**:
   - The [[vault]] operates based on specific security mechanisms to ensure its integrity and safe operations.
4. **Domain Restrictions**:
   - The [[vault]] is explicitly not added under any domain to maintain its isolated and secure environment.  

These guidelines are imperative to ensure the smooth and secure operation of the vault system.


| Parameter                                     | Limitation (Upper Limit) |
|-----------------------------------------------|-------------|
| **Vault Name**                                | 40 chars    |
| **Vault Address**                             | 255 chars   |
| **Ports Vault Listens On**                    | 16          |
| **Concurrent Logged On Users**                | 32,000      |
| **Concurrent Transactions Received by Vault** | 9,000       |
| **Concurrent Transactions Processed by Vault**| 600         |
| **Records Sent Together**                     | 200         |
| **Seconds Between Accessed Files Counters**   | 5 seconds   |
| **Vault Audit Record Size**                   | 500 chars   |
| **Client Request Length**                     | 6,000 chars |
| **Symmetric Key Size**                        | 256 bits    |
| **Asymmetric Key Size**                       | 2048 bits   |                      
> These are the upper limits defined by the code, they may change based on the other factors too

## VM Snapshots

A VM (Virtual Machine) snapshot is a feature provided by virtualization software that captures the current state of a virtual machine. It is similar to taking a photograph of the VM at a specific point in time. This "photograph" includes:

1. **Memory state**: The contents of the VM's RAM.
2. **VM settings**: Configuration details of the VM, like network settings, CPU allocation, etc.
3. **Disk state**: The current state of the VM's virtual disk.

## [[Data Encryption Flow]]

Data encryption starts with the Server Key, which encrypts the Vault Key. The Vault Key, in turn, protects the Safe Key. This Safe Key encrypts the Object Key, which finally safeguards the Sub Object Key.  

**Server Key -> Vault Key -> Safe Key -> Object Key -> Sub Object key**  

### CyberArk Key Generator Utility (PAKeyGen)

The CyberArk Key Generator utility (PAKeyGen) enables you to create a set of two unique encryption keys:
- Server key
- Recovery key  
The server key is a 256-bit symmetric key and the recovery keys are a 2048-bit asymmetric key pair. These keys are located in two separate folders:

**Operator CD** : This folder contains the server key and the public recovery key.  
**Master CD** : This folder contains the server key, the public recovery key, and the private recovery key.

| Folder location | File name    | Description                                                         |
|-----------------|--------------|---------------------------------------------------------------------|
| Operator, Master| recpub.key   | The public recovery key encrypts data for emergency use cases.      |
| Operator, Master| rndbase.dat  | Random base file.                                                   |
| Operator, Master| server.key   | The symmetric server key encrypts and decrypts data.                |
| Master          | recprv.key   | The private recovery key decrypts data in case of emergency.        |

1. `recpub.key` - This is a public recovery key used for encrypting data in emergency scenarios.
2. `rndbase.dat` - A random base file.
3. `server.key` - A symmetric key for both encrypting and decrypting data.
4. `recprv.key` - A private recovery key that decrypts data in emergencies.

## Services

| Service Name                               | Primary Function                                                                                                          |
|--------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| **PrivateArk Server Service**              | Main service for the vault; dependent services like ENE halt if it's restarted. Handles the start/stop of the vault.       |
| **PrivateArk Database Service**            | Core service for data access. Interruption can halt PrivateArk Server and risk database corruption.                        |
| **PrivateArk Remote Control Agent Service**| Provides remote access and monitoring but is non-essential.                                                                 |
| **CyberArk Logic Container Service**       | Manages master policy execution and application logic for database read/write.                                             |
| **CyberArk Event Notification Engine Service** | Manages email-based notifications for password expiry, user login requests, etc.                                           |
| **CyberArk Windows Hardened Firewall Service** | Converts Windows firewall into CyberArk service during hardening, securing inbound/outbound traffic (only port 1858).    |  

### Logon as Service

- Regarding "Log on as" in services: It specifies the account under which the service runs. 
- Depending on service configuration, it could be a local system account, a specific user account, or a service account. 
- It's crucial for permissions and security considerations.  

### Naming Conventions

- Regarding the naming difference between "PrivateArk" and "CyberArk" for services: It's a branding or legacy naming choice by CyberArk. 
- Different components or phases of product development might have influenced this naming convention.

### Service Dependencies

#### Vault Services Starting Sequence

1. **To Start**:
   - `PrivateArk Database`
   - Followed by `CyberArk Logic Container Service`
   - Then `PrivateArk Server Service`
   - Lastly, the rest of the vault services.

#### Vault Services Stopping Sequence

1. **To Stop**:
   - Start with `PrivateArk Server Service`
   - Then `PrivateArk Database`
   - Followed by other services (excluding `CyberArk Windows Hardened Firewall Service`).


