---
aliases: 
tags: 
date created: Tuesday, September 26th 2023, 5:31:48 pm
date modified: Saturday, January 27th 2024, 7:02:02 pm
---

## Safes Created after Each Component Install

### After Vault

#### Safes

1. Vault Internal Safe
2. System Safe
3. Notification Engine Safe

#### Users

### After PVWA

PVWAConfig  
 PVWAPrivateUserPrefs  
 PVWAPublicData  
 PVWAReports  
 PVWATaskDefinitions  
 PVWATicketingSystem  
 PVWAUserPrefs

|Safe|Description|
|---|---|
|PVWAConfig|Contains all the configuration settings for the PVWA.|
|PVWAUserPrefs|Contains the user preference settings for the PVWAs interface.|
|In both of the above Safes, relevant information is stored automatically, and users should not modify files in the Safes directly.|   |
|PVWATicketingSystem|Stores accounts that are used to connect to ticketing systems that are configured to work with the PVWA.|
|VaultInternal|Stores accounts that are used to connect to LDAP directories, and are used by the LDAP integration components for transparent user management in the Vault and CPM automatic detection.|
|PVWAPrivateUserPrefs|Stores user preferences.|
|SharedAuth_Internal|Stores credentials for communication between CyberArk components, for example, LCD.|

### After CPM

|User|Description|
|---|---|
|PasswordManagerUser|The local Windows user that runs the CyberArk Password Manager service.|
|PluginManagerUser|The local Windows user used by the CyberArk Password Manager service to execute plugins.|
|ScannerUser|The local Windows user that runs the Scanner service.|



| Safe                         | Description                                                                                                                                                                                           |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PasswordManager Safe         | This Safe contains the CPM.ini file, which includes the main CPM settings, and the ADConfiguration.xml file where auto-detection parameters are configured.                                           |
| CPM name_workspace Safe      | This Safe is used for internal processing and should not be accessed by users. The default size of this Safe is 5000 MB.                                                                              |
|                              | The name of this Safe contains the CPM name. By default, it is called ‘PasswordManager_workspace’.                                                                                                    |
| CPM name_info Safe           | This Safe is used to store notifications about theCPM’s activities. The PVWAAppUser is automatically added to this Safe so that it can read platform names and details, and display them in the PVWA. |
|                              | The name of this Safe contains the CPM name. By default, it is called ‘PasswordManager_info’.                                                                                                         |
| CPM name_ADInternal          | This Safe is used for internal processing during auto-detection activities and should not be accessed by users.                                                                                       |
|                              | The name of this Safe contains the CPM name. By default, it is called ‘PasswordManager_ADInternal’.                                                                                                   |
| PasswordManagerShared Safe - | This is an internal Safe that is used as a repository of platforms for all CPMs. The default size of this Safe is 500 MB.                                                                             |

### After PSM

PSM  
 PSMLiveSessions  
 PSMNotifications  
 PSMRecordings  
 PSMSessions  
 PSMUniversalConnectors  
 PSMUnmanagedSessionAccounts

### After PSMP

AccountsFeedADAccounts  
 AccountsFeedDiscoveryLogs



 SharedAuth_Internal