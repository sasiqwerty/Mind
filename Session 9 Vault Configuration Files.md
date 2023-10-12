---
aliases: 
tags: 
date created: Wednesday, October 4th 2023, 5:05:50 pm
date modified: Saturday, October 7th 2023, 8:09:54 am
---
Very similar to [[Session 10 Log Files Debugging Levels]]

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

## Log File Management

### Directory:

- **Path:** Program files(x86) > PrivateArk > Server > Logs

### Main Vault Log:

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