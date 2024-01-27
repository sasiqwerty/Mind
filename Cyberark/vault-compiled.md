---
aliases: 
tags: 
date created: Monday, September 11th 2023, 7:08:52 am
date modified: Tuesday, December 5th 2023, 12:00:53 am
---
[CyberArk Vault Structure | CyberArk Docs](https://docs.cyberark.com/PAS/latest/en/Content/PASIMP/CyberArk-Vault-Structure.htm?tocpath=Administrator%7CComponents%7CDigital%20Vault%7CAdvanced%20Digital%20Vault%20Environment%7CCyberArk%20Vault%20Structure%7C_____0)

## Vault Server Specs

- based on number of [[Privileged Account]] accounts  
- vault server specifications  
- what is cloud server?

[Vault Specifications | CyberArk Docs](https://docs.cyberark.com/PAS/Latest/en/Content/PASREF/Vault%20Specifications.htm)  
![[vault-specs (2).svg]]  
[[vault specifications]]

## Vault Installation Prerequisites

- windows server 2016/2019
- .Net Framework 4.8 or higher
- Vault software
- Master CD
- Operator CD
- Server Key
- License file  
![[Zoom_OJfMRzBmHL.png]]  

### Notes

#### Windows Server

- windows 2012 is not supported anymore for vault installation 

#### Third Party Apps

- avoid installing 3rd party applications, its strictly not allowed  
- not installing 3rd party applications also enhances safety and performance  
- CyberArk team wont support when contacting CyberArk with a problem with 3rd party apps are installed in the vault server

#### Vault Server Location

- vault is not domain joined, if its domain joined the group policies are applicable to the vault also which is not a good idea  
- the vault only accepts data from 1858 port  
- the vault will not talk to other servers  
- the vault will function based on certain security mechanism  
- hence vault is not added under the domain

What are the vault prerequisites? its an important interview question

PAkeygen - used to generate keys like server keys and other stuff

## Group Policy

every server has its own local policies  
manage all the server with one policy - its called group policy

## Vm Snapshots

A VM (Virtual Machine) snapshot is a feature provided by virtualization software that captures the current state of a virtual machine. It is similar to taking a photograph of the VM at a specific point in time. This "photograph" includes:

1. **Memory state**: The contents of the VM's RAM.
2. **VM settings**: Configuration details of the VM, like network settings, CPU allocation, etc.
3. **Disk state**: The current state of the VM's virtual disk.  

[[VM Snapshots|snapshot]] - notes from chatgpt

## [[Data Encryption Flow]]

Data encryption starts with the Server Key, which encrypts the Vault Key. The Vault Key, in turn, protects the Safe Key. This Safe Key encrypts the Object Key, which finally safeguards the Sub Object Key.  
![[Pasted image 20230831112955.png]]

## Vault - Services

![[Zoom_ccqtBFDjOQ 2.png]]  
this is very very important  
there are 3 vault services with the name PrivateArk  
there are 3 services with the CyberArk name ( why is it different? )

what is the log on as? part in the services what is its purpose?  
use the search name method instead of manual search

### PrivateArk Server Service

- The PrivateArk Server is the primary service of the vault. Restarting it will cause the ENE to halt, as the ENE is dependent on the PrivateArk server service. To implement any changes, the vault must be restarted.
- The PrivateArk Server operates as a Windows service. Depending on the Server's key configuration, this service can either start automatically or be initiated manually.
- The [[PrivateArk Server]] console is for troubleshooting, starting and stopping of vault.

### PrivateArk Database Service

- core service, data is accessed as this service is running, if its down the PrivateArk server also wont start
- if the database is suddenly stopped the PrivateArk server will stop too and cause a sudden shock! its not recommended, it might cause database corruption.
- there is some dependency with the PrivateArk database and logic container and when the database is stopped he logic container is also stopping

### PrivateArk Remote Control Agent Service

- remote access, remote monitoring
- it can be considered as optional service, shutting it off will not cause any problem
- non-essential service

### CyberArk Logic Container Service

- very important for the vault
- the master policy is defined, that is executed by the logic container
- if policy issue arises there are related logs that we should look at
- platform level stuff is handled by the CPM
- Master policy level is handled by CyberArk logic container
- The Logic Container is a service in the Vault that is responsible for running application logic for reading/writing to the Vault database. This logic is part of any API request (initiated by an action in the PVWA UI or directly by a script).

### CyberArk Event Notification Engine Service

- the notifications are sent in the form of emails
    - password expiry is sent
    - user requests for login are sent
    - dr user is stopped
    - component services are stopped
- mail based services are managed by the event notification engine in CyberArk
- PTA notifications are not handled directly but have to configured.

### CyberArk Windows Hardened Firewall Service

- never stop the service, ever, in real time environment
- windows server has windows firewall, but during hardening the windows firewall service will convert into CyberArk service now there is no windows firewall service.
- inbound and outbound is restricted.
- only 1858 port is allowed after the firewall is hardened.
- stopping means reducing security.


local account is created to handle the connections and then added to CyberArk and then accessed via RDP  
we create an account in the vault server and that is onboarded, only then it is accessed  
the audit data has to be maintained


![[Zoom_26fE31YoNa 2.png]]

![[Zoom_uMlVsgNtZE.png]]



![[Zoom_4PvmDFsPsW.png]]

![[Zoom_dyCyf2F33d.png]]

## dbparm.ini Configuration Guide

The `dbparm.ini` configuration file plays a crucial role in the initialization of the vault. This guide provides a concise understanding of its significance and relevant parameters.

### Initialization

1. **File Reading**: The vault reads the `dbparm.ini` configuration file upon start-up; any misconfiguration prevents the vault from starting.
2. **Operator CD**: Contains the essential server key for vault operation.
3. **Server Key Integration**: The server key from the Operator CD is loaded into the vault server's memory for successful initialization.
4. **Key Validity & Path Specification**: The server key must be valid, and its path explicitly mentioned in the configuration.

### Task Count Configuration

1. **Definition**: Task Count denotes the vault's capacity to handle simultaneous transactions.
2. **Default Setting**: The pre-set value for task count is 20.
3. **Performance Analysis**: Using the `PASreporter TOOL`, CyberArk reviews and recommends a specific task count value.
4. **Modification Implication**: Altering the task count necessitates adjusting the `maxtaskallocation` parameter based on needs.

## Other Parameters

1. **Entropy File**: Sourced from the operator CD and utilized in the construction of the vault database.
2. **DatabaseConnectionPasswordFile**: An internal password file that grants access to the vault.
3. **ServerCertificateFile**: Initially employs a self-signed certificate, which is eventually replaced with a CA certificate.
4. **AutoClearSafeHistory & AutoClearUserHistory**: Managed by a batch user, this function clears history logs for safes and user sessions.
5. **VaultID**: A unique hexadecimal ID located within the `dbparm.ini` file.
6. **AutosyncExternalObjects**: Enables synchronization with LDAP and other external directories.
7. **VaultDebugLevel**: A flexible setting that adjusts the debug level, permitting increases or decreases as necessary.
8. **DefaultTimeOut**: Establishes the default idle duration after which a user session concludes.
9. **AutomaticallyAddBuiltInGroups**: When safes are generated, certain users are inherently added based on this setting.
10. **LicenseUsageAlert**: Displays remaining license time, with alerts shown in server central administration.
11. **ComponentNotificationThreshold**: Monitors component usage and activates an alert when surpassing a predetermined threshold.
12. **BackupKey**: A link in the `dbparm.ini` that points to the backup location.
13. **StagingAreaDirectory**: Indicates the directory where safes are temporarily staged.

## Procedure to Apply the Vault License

There are two distinct methods to apply the Vault license:

### 1. Application through PrivateArk Client (Before License Expiry)

- Launch the PrivateArk client with administrative privileges (including permissions to rename and upload files).
- Backup the existing license file by saving it to a preferred location.
- Import the new license into the **system safe** within the PrivateArk client.
- Note: This procedure is applicable only if there is remaining time on the current license. If the license has already expired, this method is infeasible.

### 2. Manual File Replacement (After License Expiry)

- Navigate to the server directory within the PrivateArk folder.
- Proceed to the 'conf' sub-directory.
- Backup the existing license file.
- Replace the old license file with the new one in the 'conf' directory.
- After updating, restart the PrivateArk service to apply the new license.
- Caution: This approach is a contingency measure, to be employed only if the license has expired and there was no preemptive action taken.

## Configuration and Logging Files for Vault

### 1. PARagent.ini - Configuration for Remote Control Client

#### Connection and Control Parameters:

- **RemoteStationIPAddress:** Specifies the allowed IP Addresses that can connect to the vault.
- **UserCredentialsPath:** Specifies the location of the password file that grants authentication for connections.

#### Remote Monitoring Configuration Parameters:

- **ExtensionComponentList:** List of components to monitor remotely.
- **AllowedMonitoringServices:** Services permissible for monitoring.
- **SNMPT settings:** Configuration for Simple Network Management Protocol.
- **LogMessagesFilter:** Filters for logging messages.
- **ExcludedMessagesFilterRegexp:** Regular expressions to filter out specific log messages.

#### Reference File:

- **PARagent.sample.ini:** A syntax reference file that contains the necessary parameters for the PARagent.ini file.

### 2. passparm.ini - Password Policy Configuration

- This file delineates the rules for creating passwords for vault users.
- Enables customization of password complexity.
- Located in the same directory as dbparm.ini within the 'conf' folder.

### 3. tsparm.ini - Vault Data Storage Configuration

- Specifies the storage path for safes and their associated data.
- Data is encrypted and can only be accessed using the PrivateArk client.
- For optimal performance, avoid specifying a deep directory structure.
- **Backup Note:** A functional backup of this file is termed as "good file."

### 4. vault.ini - Vault Connectivity Configuration

- Outlines the loopback IP address for vault connectivity.
- Default value is set to `127.0.0.1` with the port `1858`.
- The loopback IP address is `127.0.0.1` for IPv4. (In IPv6, the loopback address is `::1`.) 
- The loopback address allows a networked computer to send data to itself for testing and development purposes. When data is sent to the loopback address, it is rerouted back to the sending system without being transmitted over the external network.

### 5. Log File Management

#### Directory:

- **Path:** Program files(x86) > PrivateArk > Server > Logs

#### Main Vault Log:

- **ITAlog.log:** Comprehensive log file where all vault activities are documented.
  
  **Log Structure:** Date | Time | Message
  
  **Message Tags and Meanings:**
  - **I:** Informational messages.
  - **W:** Warning messages.
  - **S:** System-related messages.
  - **E:** Error messages.
  
  **Accessibility Note:** For recent logs, scroll to the end of the file.

## Vault Trace Logs

### Introduction

- The vault contains internal users, with each component having its own internal user.
- These components interact with the vault securely via port 1858. These interactions are termed as transactions and are logged in trace logs.

### Log File Details

- Each trace log file has a size limit of 200MB.
- Log progression goes from tracelog0 to tracelog4.
- Once a log file fills up, the subsequent log is used.
- Upon reaching tracelog4's limit, it gets archived.
- Logging settings can be toggled using `EnableTrace = Yes` in ini files for debugging purposes.
- when is this trace enabled? #important #doubt #asklater

### Backing Up Logs

- To backup logs, the vault should ideally be stopped. However, this isn't feasible in real-world settings as these files remain in use by the vault, making renaming or modifying them impossible.

## Debugging in Vault

### Enabling Debug Level

- Navigate to the administration tab in the server central administration console.
- Enable the debug level and opt to set it dynamically.
- Codes for debugging can be found and input from CyberArk's documentation.

### Debugging Process

- Debugging aims to recreate and understand issues.
  - **Reproducible Issue**: Issues that can be consistently recreated.
  - **Non-Reproducible Issue**: Issues that occur sporadically.
- Enabling debugging captures in-depth messages in logs to diagnose the issue.
- Note: Excessive debugging can strain the vault due to high log traffic, possibly leading to restarts or failovers. Always deactivate debugging post-troubleshooting.

### Methods to Enable Debugging

1. **Dynamically via Administration Tab**: Temporary until next restart.
2. **dbparm.ini File Modification**: Update with `DebugLevel` for a persistent setting, but necessitates a vault restart.

## CAVaultManager.exe

- Application to collect logs: `CAVaultManager.exe CollectLogs`.
  - This command fetches all vault-related logs, inclusive of system information.
- The primary vault log is `vaultDB.log`, which records all vault transactions and messages.

## my.ini File

### Overview

- `my.ini` configures the vault database.
- Always consult CyberArk support before making modifications.
- The vault's database is MySQL-based and isn't alterable.

### Key Configuration Parameters

- Specifies the metadata location.
- Dictates RAM allocation for the database in kb, particularly for the InnoDB storage engine.
- InnoDB is MySQL's default storage engine from version 8.0, striking a balance between reliability and performance. [More on InnoDB](https://dev.mysql.com/doc/refman/8.0/en/innodb-introduction.html).
- InnoDB buffer pool size generally takes up 80% of available RAM.

### Auxiliary Data

- The `bin` folder (server > database) contains MySQL's auxiliary files.
- Issues within the vault database and InnoDB interactions can be found in `vaultDB.log`.

### MySQL Upgrades

- Prior to CyberArk 11.7, MySQL's version was 5.7. From CyberArk 12 onwards, it's 8.0.
- Upgrade cautiously, transitioning from 5.7 -> 5.8 -> 8 to avoid complications.
- CyberArk recommends specific intermediate versions for smooth upgrades.
- For data recovery (due to corruption), CyberArk offers a clean metadata folder (located in `PrivateArk > safes > metadata`).

## Vault Hardening

### Procedure

- Hardening files are located in `PrivateArk > server > hardening folder`.
- It's advised to harden the vault during installation.
- More details can be found under [[vault hardening overview]].
- For manual hardening: `CAVaultHarden.exe <vaultArchitecture> </allowRDP>`.   

### Integrate with other Directories

- SunOne
- Oracle
- MicrosoftAD
- IBMTds
- eDirectory

we can integrate with other directories using the supporting files found in PrivateArk > Server > LDAP

### Logic Container

- this contains all the details related to master policy, this is how the vault is controlled by the master policy
- the logic container logs are found in the PrivateArk > server > LogicContainer

### Syslog

PrivateArk > server > syslog

### Graphics

PrivateArk > server > Graphics

### Event Notification Engine

Email related config files are found here  
PrivateArk > server > Event Notification Engine

### CACert.exe

- This file is used for installing and configuring the vault related certificates
- if the vault certificate is self signed, we can use this CA signed certificate and this exe can be used to generate a CA signed certificate

### CAVaultManager

[CAVaultManager | CyberArk Docs](https://docs.cyberark.com/PAS/Latest/en/Content/PASIMP/CAVaultManager.htm)  
CAVaultManager has the following syntax:  
- `CAVaultManager <command> [command parameters]`  
- Create a database : `CAVaultManager CreateDB`  
- Secure the vault database : `CAVaultManager SecureDB  /MasterPassword <Password> RndBaseFileName <Filename> /DBEmergencyPasswordFileName <Filename>`  
	- example ; `CAVaultManager SecureDB /MasterPassword mstrpwd123 /RndBaseFileName C:\rndbasefile.dat /DBEmergencyPasswordFileName C:\VaultEmergency.pass`
- securing secret files : `CAVaultManager SecureSecretFiles [/SecretType <Type>] [/Secret <Secret>] [/SecuredFileName <Filename>] [/FileSectionName <SectionName>]`
- CyberArk will helps us run vault database related scripts
- the DBscript file given by CyberArk file can also be run the ca vault manager utility

#### Functions of CAVaultManager

- [Create a database](https://docs.cyberark.com/PAS/Latest/en/Content/PASIMP/CAVaultManager.htm#)  
- [Secure the Vault database](https://docs.cyberark.com/PAS/Latest/en/Content/PASIMP/CAVaultManager.htm#)  
- [Secure secret files](https://docs.cyberark.com/PAS/Latest/en/Content/PASIMP/CAVaultManager.htm#)  
- [Delete partial users](https://docs.cyberark.com/PAS/Latest/en/Content/PASIMP/CAVaultManager.htm#)  
- [Secure the Vault Entropy file](https://docs.cyberark.com/PAS/Latest/en/Content/PASIMP/CAVaultManager.htm#)  
- [Optimize Vault performance](https://docs.cyberark.com/PAS/Latest/en/Content/PASIMP/CAVaultManager.htm#)  
- [Upgrade the Vault database](https://docs.cyberark.com/PAS/Latest/en/Content/PASIMP/CAVaultManager.htm#)  
- [Delete the Vault database](https://docs.cyberark.com/PAS/Latest/en/Content/PASIMP/CAVaultManager.htm#)  
- [Recover the database password](https://docs.cyberark.com/PAS/Latest/en/Content/PASIMP/CAVaultManager.htm#)  
- [Verify LDAP configuration](https://docs.cyberark.com/PAS/Latest/en/Content/PASIMP/CAVaultManager.htm#)  
- [Synchronize the Vault database](https://docs.cyberark.com/PAS/Latest/en/Content/PASIMP/CAVaultManager.htm#)  
- [Recover Backup Files](https://docs.cyberark.com/PAS/Latest/en/Content/PASIMP/CAVaultManager.htm#)  
- [Compile a diagnostics report for the Vault database](https://docs.cyberark.com/PAS/Latest/en/Content/PASIMP/CAVaultManager.htm#)  
- [Replace the current LDAP directory](https://docs.cyberark.com/PAS/Latest/en/Content/PASIMP/CAVaultManager.htm#)

### Dll Files Related to Vault'

### Change Server Keys

server keys can be changed with hsm integration 

### dbmain.exe

- vault database and MySQL, dbmain.exe helps us interact with each other
- in the PrivateArk > server we have this folder
- the vaultDB version has to be shared from the dbmain.exe as a screenshot

## Users, Groups and Safes

Batch User  
Auditors - Default group

system safe  
vault internal safe  
notification engine safe  

#11-09-23

## Server and Recovery Keys

There are two external groups of keys associated with the server. These keys facilitate access to the server and its internal data. It's advised to store these server keys on removable storage like a disk or CD, ensuring they can be securely kept in a physical safe.

- **Keys on the Operator CD**: server.key, recpub.key, rndbase.dat
- **Keys on the Master CD**: server.key, recpub.key, rndbase.dat, recprv.key

### Server Key

The Server Key functions similarly to a key for a physical vault. This key is essential to initiate the vault. Once the vault starts, you can remove the Server Key until the server requires a restart. If the vault is halted, its contents are entirely inaccessible without this key. You can find the path to the Server Key in DBParm.ini.

#### Definitions of Server Keys:

- **Backup.Key**:
  - Encrypts the vault's backup sets.
  - It gets encrypted with the Server Key (Server.key).
  - Generated during installation.

- **VaultUser.Pass**:
  - Contains an encrypted password to connect to the integrated database.
  - Protected and encrypted using the Server Key.
  - Generated during installation.

- **VaultEmergency.Pass**:
  - An encrypted password allowing emergency access to the embedded database.
  - It's safeguarded and encrypted with the Master Key (RecPub.key).
  - Generated during installation.

- **Server.pem, Server.pvk**:
  - Store the vault certificate and its private key, respectively.
  - The private key is encrypted using the Server Key.
  - Both are generated during installation.

- **Rndbase.dat**:
  - The Random Number Generator (RNG) Seed File utilized by the vault.
  - Supplied by Cyber-Ark on the Operator CD.

- **Server.key**:
  - The Server Key encrypts the Safe Keys.
  - Each Vault Server possesses a unique Server Key.
  - Provided by Cyber-Ark on the Operator CD.

### Recovery Key

The Recovery Key plays a crucial role in restoring the vault's data should the vault become non-operational. This key is reserved for rare instances when the vault malfunctions and isn't repairable within the needed timeframe, or if an external key to a safe is forgotten. For the Master User, the Recovery Key is essential to access the vault. Comprising the Public Recovery Key (RecPub.key) and the Private Recovery Key (RecPrv.key), the Recovery Key is asymmetric in nature.

#### Definitions of Recovery Keys:

- **RecPub.key**:
  - Represents the Public Key within the RSA-2048 Asymmetric Master Key pair.
  - Used for encrypting the safe keys, which the Private Master Key (RecPrv.key) can then decrypt.
  - Provided by CyberArk on the Operator CD.

- **RecPrv.key**:
  - The Private Recovery Key, vital for the Master User to access and open the safes during a vault recovery situation.
  - Store this key separately from the server, ideally on a disk or CD within a physical vault.
  - Use this key in conjunction with a recovery utility to retrieve data stored in the Safe.