---
aliases: 
tags: 
date created: Wednesday, October 4th 2023, 5:05:52 pm
date modified: Wednesday, October 4th 2023, 9:34:56 pm
---
Very similar to [[Session 9 Vault Configuration Files]]

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
