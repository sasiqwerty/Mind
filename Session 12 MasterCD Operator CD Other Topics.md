---
aliases: 
tags: 
date created: Wednesday, October 4th 2023, 4:09:52 pm
date modified: Monday, October 16th 2023, 11:52:23 pm
---
#07-09-23 #11-09-23

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

## Master CD Contents and Operator CD Contents

### Master CD

recprv.key  
recpub.key  
rndbase.dat  
server.key

### Operator CD

backup.key  
Server.key  
MasterReplicationUser.pass  
recpub.key  
ReplicationUser.pass  
rndbase.day  
server.pem  
server.pvk  
vaultEmenergency

### Common Files (found on both CDs):

1. recpub.key
2. server.key
3. rndbase.dat

### Files Exclusive to Master CD:

1. recprv.key

### Files Exclusive to Operator CD:

1. backup.key
2. MasterReplicationUser.pass
3. ReplicationUser.pass
4. server.pem
5. server.pvk
6. vaultEmenergency.pass

By examining the list, we can see that the Master CD has an exclusive file `recprv.key` which is the private recovery key. The Operator CD has several exclusive files related to backup, replication, and emergency functions. Both CDs share the public recovery key, the server key, and the rndbase.dat file.

### Server and Recovery Keys

There are two external groups of keys associated with the server. These keys facilitate access to the server and its internal data. It's advised to store these server keys on removable storage like a disk or CD, ensuring they can be securely kept in a physical safe.

- **Keys on the Operator CD**: server.key, recpub.key, rndbase.dat
- **Keys on the Master CD**: server.key, recpub.key, rndbase.dat, recprv.key

#### Server Key

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

#### Recovery Key

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

