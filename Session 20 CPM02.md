---
aliases: 
tags: 
date created: Thursday, September 28th 2023, 3:52:23 pm
date modified: Sunday, November 5th 2023, 11:10:14 pm
---
**20:54 28-09-23 Thursday**  
Link - [Session 20 CPM 2 - YouTube](https://www.youtube.com/watch?v=1K07sGrUukg)

## CPM Configuration Settings

### CPM.ini

CPM's primary config file, located in the `passwordmanager` Safe in the vault. Typically fetched from the safe at runtime and temporarily found at:  
`C:\Users\{Username}\AppData\Local\Temp`.

_The CPM settings mentioned in the CPM.ini can be changed in the following way._  
![[Pasted image 20230928175548.png]]  
![[Pasted image 20230928180250.png]]

![[Pasted image 20230928180912.png]]

These are the settings found in the CPM.ini file or in the [[Password Vault Web Access|PVWA]] config CPM settings page.

| Parameter                  | Description                                               | Acceptable values  | Default value      |
|----------------------------|-----------------------------------------------------------|--------------------|--------------------|
| Interval                   | Time (mins) for handling new/removing deleted platforms. | Number             | 1                  |
| NotifyPeriod               | Interval (hours) between email notifications.             | Number             | 12                 |
| NotifyOnlyOnError          | Send only error notifications.                            | Yes/No             | Yes                |
| AdminEmailAddresses        | Address for email notifications.                          | Email address      | [example@email]    |
| SmtpServer                 | SMTP server IP address.                                   | IP address         | [example IP]       |
| SenderAddress              | Address where the email is sent from.                     | Email address      | [example@email]    |
| Subject                    | Subject title of the email.                               | String             | [example subject]  |
| LogCheckPeriod             | Time (hours) before logs are copied to Logs/History.      | Number             | 24                 |
| LogSafeFolderName          | Folder in the Safe for logs.                              | String             | RootLogs           |
| LogSafeName                | Safe name for the logs.                                   | String             | [example SafeName] |
| OldLogRetention            | Days before logs are deleted.                             | Number             | 30                 |
| CPMDebugLevels             | Debug level of the CPM.                                   | 0-6                | [example level]    |
| WriteStartCycleEvent       | CPM writes 'I’m alive' event.                             | Yes/No             | Yes                |
| LogPasswordEvents          | CPM logs password changes/verifications.                  | Yes/No             | Yes                |
| DisableExceptionHandling   | CPM behavior when the system stops.                       | Yes/No             | No                 |
| ADPoolSize                 | Concurrent automatic detection processes size.            | Number             | 5                  |
| AllowManualRequests        | CPM searches for auto-detection processes initiated manually. | Yes/No          | Yes                |
| ManualRequestsInterval     | Time (mins) between searches for manual processes.        | Number             | 1                  |
| PlatformsToManage          | IDs of platforms managed by the CPM.                      | String             | 1-                 |
| PlatformsToManageInputType | Type for PlatformsToManage parameter.                     | List/Regex         | List               |
| ManualRequestsRecoveryStartTime | Retroactive hours for manual processes.              | Number             | 1                  |

### Notes

PlatformsToManage is CPM optimization technique.  
Allowed Safe parameters is another CPM optimization technique.

## Debug Mode

- CASOS is an acronym for: **CyberArk Secure Operating System**.

| Section                        | Setting/Parameter                 | Value/Description                                                       |
|--------------------------------|----------------------------------|-------------------------------------------------------------------------|
| **To set debug mode**           |                                  |                                                                         |
| *For CPM - CPM.ini or PVWA System Configuration* | `CPMDebugLevels`               | `0` - No messages to trace log. <br>`1` - CPM exceptions to trace log. (default) <br>`2` - CPM trace messages to trace log. <br>`3` - CPM CASOS activities to trace log. <br>`4` - CPM CASOS debug activities to trace log. <br>`5` - CPM CASOS errors to trace log. <br>`6` - All CPM CASOS activities and errors to trace log. |
|                                | `OldLogRetention`                | Number of days trace and console logs saved (default is 7). Specify `0` to prevent deletion. |
| *For policy handling*           | `Debug`                         | `Yes` (Under "ExtraInfo" section in policy)                             |
| *For PMTerminal*                | `[Debug Information]`           | DebugLogFullParsingInfo=`yes` <br> DebugLogFullExecutionInfo=`yes` <br> DebugLogDetailBuiltinActions=`yes` <br> ExpectLog=`yes` <br> ConsoleOutput=`yes` |
| *For Windows AD Autodetect*     | `ADLDAPDebug`                   | `Yes` (In Machine Detection section)                                   |
|                                | `ADUsageParameterName`          | `Debug` (In Machine Scan → Usage Types → `<UsageName>` → Usage Parameters) |
|                                | `ADUsageParameterValue`         | `Yes`                                                                  |
| **Log files location**          | *CPM*                           | Various log file paths, e.g., `\<Program Files\CyberArk\PasswordManager\Logs\pm.log`, `pm_error.log`, etc. |
|                                | *All plug-ins*                  | `\<Program Files\CyberArk\PasswordManager\Logs\ThirdParty\*.log`       |
|                                | *For Windows AD Autodetect*     | `\<Program Files\CyberArk\PasswordManager\Logs\ThirdParty LDAP-Debug.log` |

## Log Files

| Component                | Log Location                                                                     |
|--------------------------|----------------------------------------------------------------------------------|
| CPM Main                 | \Program Files\CyberArk\PasswordManager\Logs\pm.log                              |
| CPM Error                | \Program Files\CyberArk\PasswordManager\Logs\pm_error.log                        |
| PM Console               | \Program Files\CyberArk\PasswordManager\Logs\PMConsole.log                       |
| PM Trace                 | \Program Files\CyberArk\PasswordManager\Logs\PMTrace.log                         |
| All plug-ins             | \Program Files\CyberArk\PasswordManager\Logs\ThirdParty\*.log                    |
| Windows AD Autodetect    | \Program Files\CyberArk\PasswordManager\Logs\ThirdParty\LDAP-Debug.log           |

## [[CPM]] Environment

The following table contains a list and description of the folders that are created during installation.

| Folder  | Description |
|---------|-------------|
| bin | Contains all required files for CPM operations on remote machines (e.g., dlls, executables).<br>Contains the UnixProcess.ini and UnixPrompts.ini files  |
| Logs | Contains CPM activity logs. Refer to *CPM Activity Logs* guide. |
| Samples | Sample Files for policies can be found here. |
| tmp | Holds files used for CPM internal processing. |
| Scanner | Contains files for CPM Scanner's Accounts Feed. <br> - Log: Subfolder with Scanner activity logs. <br>CACPMScanner.exe is here and its supporting files ,<br> DNAConsole.log is also found here |
| third party | Holds the files that are related to third-party applications |
| Vault | Contains the Vault parameter and `Vault.ini`. Refer to *Vault Parameter File*. <br> Also houses `CreateCredFile` utility for user credential creation. <br> has the apikey.ini file that is generated by the `ApiKeyManager.exe` |

### [[User Credential Files]]

- [APIKeyManager Utility | CyberArk Docs](https://docs.cyberark.com/PAS/Latest/en/Content/PASIMP/APIKeyManager.htm?tocpath=Administrator%7CUtilities%7CUser%20credential%20files%7C_____1)  
- [CreateCredFile utility | CyberArk Docs](https://docs.cyberark.com/PAS/Latest/en/Content/PASIMP/CreateCredFile-Utility.htm?tocpath=Administrator%7CUtilities%7CUser%20credential%20files%7C_____2)  
- [CreateAuthFile Utility | CyberArk Docs](https://docs.cyberark.com/PAS/Latest/en/Content/PASIMP/CreateAuthFile-Utility.htm?TocPath=Administrator%7CUtilities%7CUser%20credential%20files%7C_____3)  

The PVWA agent account requires a user credential file in order to be able to log onto the Vault and enable users to access files stored inside.

The user credential file, called user.ini, contains the agent account’s Vault username and logon information. The location of this credential file is specified in the ‘GWUserFile’ parameter in the Password Vault Web Access configuration file, PVConfiguration.xml.

The user credential file is created with a utility that is included in the Password Vault Web Access installation package. It is run from a command line prompt, and can specify standard password or token authentication. The authentication used in the credential file must be the same as the authentication method that is specified for the user in the PrivateArk Client.

### APIKeyManager

[APIKeyManager Utility | CyberArk Docs](https://docs.cyberark.com/PAS/Latest/en/Content/PASIMP/APIKeyManager.htm)  
The APIKeyManager utility is a command line tool that generates and maintains an asymmetric key pair which provides a secure way for automated API calls and scripts, as well as CyberArk clients, to connect and authenticate to the Vault.

The private key is stored locally for use by the script or CyberArk client, while the public key is stored in the Vault. Both keys are associated with a username that was previously created in the Vault and used for API authentication.

This utility enables users to:

- Create a key pair and store the public key in the Vault (e.g. during a component registration, or manual key rotation)
- Create a key pair and save the public key locally (e.g. when the key registration will be performed by another person or process)
- Store a previously created public key in the Vault (e.g. when the key was generated by another person or process)
- Revoke an existing key pair

#### Logging

The APIKeyManager utility sends information and error messages to the console, as well as maintaining a log file that contains all types of messages (debug, warning, info, error). This log file is called apikeymanager.log and is stored in the 'Logs' folder with the utility executable.

When the log file reaches 5MB, a backup version of the current log file is saved and a new log file is created. Only one backup file is saved.

### Terminal Plugin Controller

The Terminal Plugin Controller (TPC) platform helps you create new CPM plugins using terminal and scripting languages for terminal-based devices.

TPC functions as both a platform for creating state machine plugins, and as an engine for running these plugins (interpreter)

TPC plugins contain two files that the platform uses to authenticate to target machines: 
- Prompts file
- Process file

|File|Description|
|---|---|
|Prompts|The Prompts file includes a list of conditions. When the plugin runs, TPC matches the conditions defined in this file to the output (prompts) it received from the target machine. For more information, see [Create a Prompts file](https://docs.cyberark.com/PAS/Latest/en/Content/SDK/TPC-promps.htm).|
|Process|The Process file includes all the states and transitions that are relevant to the flow. For more information, see [Create a Process file](https://docs.cyberark.com/PAS/Latest/en/Content/SDK/TPC-process.htm).|
