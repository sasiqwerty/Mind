---
aliases: 
tags: 
date created: Thursday, October 5th 2023, 7:28:35 pm
date modified: Thursday, October 5th 2023, 7:34:27 pm
---

## Vault Installation Prerequisites

**Note**: Windows 2012 is not supported anymore for vault installation.

**Essential Prerequisites for Vault Installation**:

- **Operating System**: Windows server 2016/2019.
- **Framework**: .Net Framework 4.8 or above.
- **Software Packages**:
  - Microsoft Visual C++ Redistributable package.
  - Vault software.
- **Essential Media & Files**:
  - Master CD.
  - Operator CD containing Server.Key.
  - License file.
- **Server Configuration Recommendations**:
  - The Vault should not be a domain-joined server. It is advised to add the Vault to a workgroup.
  - Install the Vault server in an isolated zone.

## Specifications By Implementation Size

- **For Small Implementations (less than 1,000 passwords)**:
  - **Processor**: Quad core (Intel compatible).
  - **RAM**: 8GB.
  - **Storage**: 2X 80GB SATA/SAS hot-swappable.
  - **Other Components**: RAID Controller, 1Gb Network adapter, DVD ROM. Optionally, additional storage for PSM can be added.

- **For Mid-range Implementations (1,000-20,000 passwords)**:
  - **Processor**: 2X Quad core (Intel compatible).
  - **RAM**: 16GB.
  - **Storage**: 2X 80GB SATA/SAS hot-swappable.
  - **Other Components**: RAID Controller, 1Gb Network adapter, DVD ROM. Optionally, additional storage for PSM can be added.

- **For Large Implementations (20,000 – 100,000 passwords)**:
  - **Processor**: 2X Eight core (Intel compatible).
  - **RAM**: 32GB.
  - **Storage**: 2X 250GB SAS (15K RPM).
  - **Other Components**: RAID Controller, 1Gb Network adapter, DVD ROM. Optionally, additional storage for PSM can be added.

- **For Very Large Implementations (more than 100,000 passwords)**:
  - **Processor**: 4X Eight core (Intel compatible).
  - **RAM**: 64GB.
  - **Storage**: 2X 500GB SAS (15K RPM).
  - **Other Components**: RAID Controller, 1Gb Network adapter, DVD ROM. Optionally, additional storage for PSM can be added.

Please ensure all these prerequisites are in place before proceeding with the Vault installation.

## Third Party Apps

- **Installation Restriction**:
  - Do not install 3rd party applications on the system. Such installations are strictly prohibited.
- **Safety & Performance**:
  - Avoiding 3rd party applications enhances the overall safety and performance of the system.
- **Support Limitation**:
  - If any 3rd party apps are found on the vault server, the CyberArk team will not provide support for arising issues.

## Vault Server Location Guidelines

- **Domain Joining**:
  - The vault should not be domain joined. If it is, group policies will be applicable, which is not recommended.
- **Port Restrictions**:
  - The Vault accepts data only via port 1858. Changing this is discouraged due to the complexities involved.
- **Security Mechanism**:
  - The Vault operates based on specific security mechanisms to ensure its integrity and safety.
- **Domain Restrictions**:
  - The Vault should not be added under any domain to maintain its isolated and secure environment.

Following these guidelines ensures the smooth and secure operation of the Vault system.

## Data Encryption Flow

- Data encryption starts with the **Server Key**.
- The **Server Key** encrypts the **Vault Key**.
- The **Vault Key** then protects the **Safe Key**.
- This **Safe Key** encrypts the **Object Key**.
- The **Object Key** finally safeguards the **Sub Object Key**.

## CyberArk Key Generator Utility (PAKeyGen)

- The **CyberArk Key Generator utility (PAKeyGen)** enables the creation of two unique encryption keys: the **Server key** and the **Recovery key**.
- The **Server key** is a 256-bit symmetric key.
- The **Recovery keys** consist of a 2048-bit asymmetric key pair.
  

## Key File Locations and Descriptions

- Both the **Operator CD** and **Master CD** folders contain:
  - **recpub.key**: A public recovery key used for encrypting data in emergency scenarios.
  - **rndbase.dat**: A random base file.
  - **server.key**: A symmetric key for both encrypting and decrypting data.
  
- The **Master CD** folder also contains:
  - **recprv.key**: A private recovery key that decrypts data in emergencies.

### Services

**PrivateArk Server Service**:
- This is the main service for the vault.
- Any dependent services, such as the Event Notification Engine, will stop if this service is restarted.
- It handles the start and stop procedures of the vault.

**PrivateArk Database Service**:
- This is the core service for data access.
- If interrupted, it can halt the PrivateArk Server and may risk database corruption.

**PrivateArk Remote Control Agent Service**:
- This service provides remote access and monitoring.
- However, it is non-essential.

**CyberArk Logic Container Service**:
- This manages the master policy execution.
- It's responsible for the application logic for database read and write operations.

**CyberArk Event Notification Engine Service**:
- It manages email-based notifications.
- This includes notifications for password expiry, user login requests, and so on.

**CyberArk Windows Hardened Firewall Service**:
- This service converts the Windows firewall into a CyberArk service during the hardening process.
- It secures inbound and outbound traffic, allowing only port 1858.

### Logon as Service

- The "Log on as" feature in services specifies which account the service runs under.
- The service could run under different configurations: it might be a local system account, a specific user account, or a service account.
- This specification is vital for permissions and security considerations.

### Naming Conventions

- The distinction in naming between "PrivateArk" and "CyberArk" for services is due to branding or legacy naming decisions made by CyberArk.
- The naming convention might have been influenced by different components or phases during product development.

### Service Dependencies

#### Vault Services Starting Sequence:

1. Begin with the **PrivateArk Database Service**.
2. Next, activate the **CyberArk Logic Container Service**.
3. Then, start the **PrivateArk Server Service**.
4. Finally, initiate the remaining vault services.

#### Vault Services Stopping Sequence:

1. Begin by stopping the **PrivateArk Server Service**.
2. Next, halt the **PrivateArk Database Service**.
3. Subsequently, cease the other services. However, do not stop the **CyberArk Windows Hardened Firewall Service** at this point.