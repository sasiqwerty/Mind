---
aliases: 
tags: 
date created: Sunday, November 5th 2023, 10:13:06 pm
date modified: Sunday, November 5th 2023, 11:55:03 pm
---
Components in [[CyberArk]]

## Vault

### Services

| Service Name                               | Primary Function                                                                                                          |
|--------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| **PrivateArk Server Service**              | Main service for the vault; dependent services like ENE halt if it's restarted. Handles the start/stop of the vault.       |
| **PrivateArk Database Service**            | Core service for data access. Interruption can halt PrivateArk Server and risk database corruption.                        |
| **PrivateArk Remote Control Agent Service**| Provides remote access and monitoring but is non-essential.                                                                 |
| **CyberArk Logic Container Service**       | Manages master policy execution and application logic for database read/write.                                             |
| **CyberArk Event Notification Engine Service** | Manages email-based notifications for password expiry, user login requests, etc.                                           |
| **CyberArk Windows Hardened Firewall Service** | Converts Windows firewall into CyberArk service during hardening, securing inbound/outbound traffic (only port 1858).    |

### Users

[[Administrator]]  
Auditor  
Batch  
EPMAgent  
Master  
Notification Engine

### Default Safes

System [[Safe]]  
Vault Internal [[Safe]]  
Notification Engine

### Config Files

`C:\Program Files (x86)\PrivateArk\Server\Conf`  
dbparm.ini  
dbparm.ini.good  
DBPARM.sample.ini  
License.xml  
license.xml.good  
PARagent.ini  
ParAgent.pass  
PARAGENT.sample.ini  
passparm.lnl  
passparm.ini.good  
passparm.sample.ini  
tsparm.ini  
tsparm.ini.good  
Vault.ini

### Log Files

`C:\Program Files (x86)\PrlivateArk\server\Logs`  
CACert.log  
CAVaultManager.log  
InstallMySQLService.log  
italog.log  
paragent.log  
SetRemoteControl.Log  
stats.log  
trace log  
VaultConfiguration.log

## [[Password Vault Web Access|PVWA]]

### Services

1. CyberArk Scheduled Tasks
2. IIS admin service (IISADMIN)
3. Windows process activation service (WAS)
4. World Wide web publishing service (W3SVC)

### Users

- PVWAAppuser - PVWA app Internal User
- PVWAGWUser - PVWA Gateway Internal User

### Default Safes

PVWAConfig - contains the config files  
PVWAPrivateUserPrefs  
PVWAPublicData  
PVWAReports  
PVWATaskDefinitions  
PVWATicketingSystem  
PVWAUserPrefs

### Config and Log Files

PVWA related config file : `Web.config`  
PVWA related config file :`Policies.xml`  
PVWA related config file :`PVConfiguration.xml`  
IIS related Config file : `C:\Windows\System32\inetsrv\config\applicationHost.config`

`C:\Windows\Temp\PVWA` - Log Folder Location for [[Password Vault Web Access|PVWA]]

- `CyberArk.WebApplication.log` - Main log file
- `CyberArk.WebConsole.log`
- `CyberArk.WebTasksEngine.log`
- `PVWA.App.log`

## [[CPM]]

### Services

Password Manager Service  
Password Manager Scanner Service

### Users

| CPM Version | Default Users |
|-------------|---------------|
| Before 12.2.4 | PasswordManager |
| After 12.2.4  | PasswordManager, PluginManagerUser, ScannerUser |

| User            | Permissions                                                                                                                    |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| PasswordManager | - Manage CPM settings, objects (policies, platforms, safes), users & groups<br>- Configure CPM replication, logging & auditing <br> - The local Windows user that runs the CyberArk Password Manager service. |
| Pluginmanager   | - The local Windows user used by the CyberArk Password Manager service to execute plugins. <br> - Manage CyberArk plugins (install, update, uninstall)<br>- Configure CyberArk plugins<br>- View plugin logs                   |
| Scanneruser     | - The local Windows user used by the CyberArk Password Manager service to execute plugins.<br> - Read-only access: CPM safes, policies, platforms, users & groups<br>- Report on CPM object status                            |s

### Default Safes

| Safe Name | Description |
|-----------|-------------|
| PasswordManager Safe | Contains `CPM.ini` (main settings) & `ADConfiguration.xml` (auto-detection parameters). |
| `<CPM name>_workspace Safe` | Internal use, not user-accessible. Default: `PasswordManager_workspace`. Size: 5000 MB. |
| `<CPM name>_info Safe` | Stores CPM activity notifications. Readable by PVWAAppUser for display in PVWA. Default: `PasswordManager_info`. |
| `<CPM name>_ADInternal` | Internal use during auto-detection, not user-accessible. Default: `PasswordManager_ADInternal`. |
| PasswordManagerShared Safe | Repository for all CPM platforms. Default size: 500 MB. |  

### Common Safes

Safes that are shared between CPMs in the infrastructure of the company.  
![[Pasted image 20231006005229.png]]

### Config and Log Files

CPM's primary config file `cpm.ini`, located in the `passwordmanager` Safe in the vault. Typically fetched from the safe at runtime and temporarily found at:  
`C:\Users\{Username}\AppData\Local\Temp`. 

| Component                | Log Location                                                                     |
|--------------------------|----------------------------------------------------------------------------------|
| CPM Main                 | \Program Files\CyberArk\PasswordManager\Logs\pm.log                              |
| CPM Error                | \Program Files\CyberArk\PasswordManager\Logs\pm_error.log                        |
| PM Console               | \Program Files\CyberArk\PasswordManager\Logs\PMConsole.log                       |
| PM Trace                 | \Program Files\CyberArk\PasswordManager\Logs\PMTrace.log                         |
| All plug-ins             | \Program Files\CyberArk\PasswordManager\Logs\ThirdParty\*.log                    |
| Windows AD Autodetect    | \Program Files\CyberArk\PasswordManager\Logs\ThirdParty\LDAP-Debug.log           |

## [[Privileged Session Manager|PSM]]

### Services

### Users

PSMAppUser  
PSMGWUser  
PSMConnect  
PSMAdminConnect

### Default Safes

PSMUnmanagedSessionAccounts  
PSMUniversalConnectors  
PSMRecordings  
PSMNotifications  
PSMLiveSessions  
PSM

### Config Files

basic_psm.ini

| Key                          | Value                                           |
|------------------------------|-------------------------------------------------|
| PSMVaultFile                 | "C:\Program Files (x86)\CyberArk\PSM\Vault\Vault.ini" |
| PSMAppCredFile               | "C:\Program Files (x86)\CyberArk\PSM\Vault\psmapp.cred" |
| PSMGWlCredFile               | "C:\Program Files (x86)\CyberArk\PSM\Vault\psmgw.cred" |
| LogsFolder                   | "C:\Program Files (x86)\CyberArk\PSM\Logs" |
| TempFolder                   | "C:\Program Files (x86)\CyberArk\PSM\Temp" |
| RecordingsDirectory          | "C:\Program Files (x86)\CyberArk\PSM\Recordings" |
| PSMServerId                  | "PSMServer" |
| PSMServerAdminId             | "PSMAdmin" |
| ConfigurationSafe            | "PWAConfig" |
| ConfigurationFolder          | Root |
| PVConfigurationFileName      | PVConfiguration.xml |
| PoliciesConfigurationFileName| Policies.xml |

## PSMP

### Services

1. PSM SSH Proxy  
2. PSMP ADBridge

### Users

PSMPAppUser  
PSMPGWUser

### Default Safes