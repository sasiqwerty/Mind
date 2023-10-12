---
aliases: 
tags: 
date created: Monday, September 4th 2023, 10:30:07 am
date modified: Monday, September 4th 2023, 10:38:00 am
---

## [[Vault]]

![](file:///C:/Users/sarat/AppData/Local/Packages/oice_16_974fa576_32c1d314_1d4f/AC/Temp/msohtmlclip1/01/clip_image002.jpg)              

### Services

#### CyberArk Logic Container

- Manages the execution of master policy settings.

#### Cyber-Ark Event Notification Engine

- Alerts users through email about vault activities.

#### CyberArk Hardened Windows Firewall

- A security measure installed during Vault setup, preventing unauthorized application installations.

#### PrivateArk Database

- Maintains the operation of the MySql Database.

#### PrivateArk Server

- The core service behind the Digital Vault.

#### PrivateArk Remote Control Agent

- Oversees remote client connections and their settings.


installation directory

⮚     **C****:\ProgramFiles (x86)\PrivateArk\Server**

 **III.**          **configuration Files**

**_![](file:///C:/Users/sarat/AppData/Local/Packages/oice_16_974fa576_32c1d314_1d4f/AC/Temp/msohtmlclip1/01/clip_image004.jpg)_**

**1.**    **DBParm.ini**

●      Main configuration file of the Vault

●      Any change requires a restart of the Vault service

●      The Vault’s main configuration files and logs can also be accessed in the System safe from remote stations using the PrivateArk Client.

**dbparm.ini:** Current Vault configuration file, contains parameters for Log Level, Server Key, Syslog, Timeouts, Recovery Key, etc.

**dbparm.sample.ini:** Contains all the possible configuration options

**dbparm.ini.good:** Contains the last known working configuration of the dbparm.ini file. Created automatically when the Vault server starts up.

**2.**    **TSParm.ini**

●      Configure the physical disks path used to store Vault data

**3.**    **PARAgent.ini**

●      Configure Remote Control Agent in the Vault

●      SNMP Configuration

**4.**    **PassParm.ini**

●      Configure password policy for users of the Vault

**IV.**          **logs**

**1.**    **Italog.log**

●      Main log file of the Vault server.

**2.**    **Trace.d0**

●      Trace file of the Vault.

●      It is detailed according to the debug level configured in the dbparm.ini.

   **V.**          **users**

![](file:///C:/Users/sarat/AppData/Local/Packages/oice_16_974fa576_32c1d314_1d4f/AC/Temp/msohtmlclip1/01/clip_image006.jpg)

**1.**    **Administrator**

It is the main admin user in entire vault with all user rights (permissions). we need to provide password while installing

**2.**    **Auditor**

This user who monitor all the activities

**3.**    **Batch**

This user is internal user who perform all the cleaning tasks. -> for batch processing

**4.**    **Master**

He is the king of the vault and cannot be log in normally. We need private key in order to login with master

**5.**    **Notification Engine**

This user is used to send notifications and it is used by ENE service

**6.**    **Backup**

This user is used to perform backup tasks

**7.**    **DR**

This user is used to perform replication of data to DR

**8.**    **Operator**

This is internal user performed for internal operations

**VI.**          **groups**

**1.**    **Auditors**

Auditor user is a member of this group by default

**2.**    **Notification Engines**

Notification Engine user is a member of this group by default

**3.**    **Backup Users**

Backup user is a member of this group by default

**4.**    **DR Users**

DR user is a member of this group by default

**5.**    **Operators**

Operator user is a member of this group by default

**6.**    **Vault Admins**

Members of this group has Vault Administrator Access

**VII.**          **DEFAULT SAFES**

**1.**    **System**

All the Vault configuration and log files are stored in this safe

**2.**    **Notification Engine**

This safe is used by Event Notification Engine Service and all its related configuration is stored

**3.**    **Vault Internal**

This Safe is used to store the accounts that are used to connect to LDAP directories and are used by the LDAP integration components for transparent user management in the Vault and CPM automatic detection.

## 2. CPM

![](file:///C:/Users/sarat/AppData/Local/Packages/oice_16_974fa576_32c1d314_1d4f/AC/Temp/msohtmlclip1/01/clip_image008.jpg)

      **I.**          **services**

⮚     **CyberArk Password Manager**

This is the main service of CPM which is responsible for managing the passwords

⮚     **CyberArk Central Policy Manager Scanner**

This service is responsible for scanning new accounts which are in the enterprise

   **II.**          **destination directory**

⮚     **C:\ProgramFiles (x86)\CyberArk\PasswordManager**

 **III.**          **configuration files**

**1.**    **cpm.ini**

This is the main configuration file for CPM which is stored in PasswordManager Safe

**2.**    **CACPMScanner.exe.config**

The Central Policy Manager Scanner configuration file is called CACPMScanner.exe.config. During installation, it is copied to the Scanner subfolder of the Password Manager Installation folder

**IV.**          **logs**

**1.**    **pm.log**

This file contains all the log messages, including general and informative messages, errors, and warnings.

**2.**    **pm_error.log**

This file contains only warning and error messages.

**3.**    **PMConsole.log**

This file contains informational messages about the CPM, such as ‘Server is starting’ and ‘Server is shutting down’. This log is meant for system administrators who monitor the status of the CPM. Errors that refer to CPM function and user authentication are included in this log.

**4.**    **PMTrace.log**

This file contains errors and trace messages. The types of messages that are included in this log depend on the debug levels.

The process:

●      The CPM logs are stored in the Log subfolder of the Password Manager Installation folder. Every x hours, based on the value of the LogCheckPeriod property, the logs are copied to the Logs/History folder and are renamed to:

▪        <filename> (<date>-<time>).log

●      Every x days, based on the value of the OldLogRetention property, the archived log files are deleted permanently.

**5.**    **Third party log files (Logs\ThirdPartyfolder)**

●      Generated by the CPM’s password generation plug-ins when an error occurs

●      Name of the log file:<type of password>-<Safe>-<folder>-<name of password object>.log E.g., Operating System-UnixSSH-1.1.1.250-Root.log

**6.**    **History log files (Logs\History folder)**

●      After a log file has been uploaded into the Safe, it is renamed and moved into the History subfolder.

●      The file is marked with a time stamp and renamed as follows: <filename> (<date>-<time>).log

**7.**     **CACPMScanner.log *****

   **V.**          **users**

**1.**    **Password Manager**

During installation, a unique CPM user is created to access accounts and manage them. This user is created as a CPM user type and, as such, can only interact with the CPM component and by default is the only user type in the Vault who can run the CPM.

**VI.**          **Default Safes**

**1.**    **PasswordManager** 

This Safe contains the CPM.ini file which includes the main CPM settings, and the ADConfiguration.xml file where auto-detection parameters are configured.

**2.**    **PasswordManager_workspace** 

This Safe is used for internal processing and should not be accessed by users.The default size of this Safe is 5000 MB

**3.**    **PasswordManager_info** 

This Safe is used to store notifications about the CPM’s activities. The PVWAAppUser is automatically added to this Safe so that it can read platform names and details, and display them in the PVWA

**4.**    **PasswordManagerShared** 

This is an internal Safe that is used as a repository of platforms for all CPMs. The default size of this Safe is 500 MB

**5.**    **CPM_ADInternal**

This Safe is used for internal processing during auto-detection activities and should not be accessed by users. This Safe is called <CPM>_ADInternal. As it uses the name of the CPM as part of its name, by default, it is called ‘PasswordManager_ADInternal’.

## 3. PVWA

![](file:///C:/Users/sarat/AppData/Local/Packages/oice_16_974fa576_32c1d314_1d4f/AC/Temp/msohtmlclip1/01/clip_image010.jpg)

      **I.**          **services**

⮚     **CyberArk Scheduled Tasks**

   **II.**          **installation directory**

1. PVWA application files are located at:

**C:\Cyberark\Password Vault Web Access**

1. Web page: IIS Virtual Folder:

**C:\Inetpub\wwwroot\PasswordVault**

 **III.**          **configuration Files**

**1.**    **Web.config**

This file contains the configuration parameters for the PVWA Web application. During installation, it is copied to the PVWA installation folder on the PVWA server. By default, the Password Vault folder is created under Inetpub\wwwroot.

**->C:\Inetpub\wwwroot\PasswordVault**

**2.**    **PVConfiguration.xml**

This configuration file contains parameters for different configurations of the Password Vault Web Access.

->PVConfig safe

**3.**    **SafeTemplate.xml**

This configuration file contains parameters that determine the default Safe properties that will be applied to the Safes that are created in the PVWA.

**4.**    **Policies.xml**

This configuration file consists of all the PVWA Policies

IIS Configuration file:

èapplicationHost.config

=>C:\Windows\System32\inetsrv\Config\

**IV.**          **logs**

1. Default Log File Location:

 **C:\Windows\temp\PVWA**

●      CyberArk.WebApplication.log

●      CyberArk.WebConsole.log

●      CyberArk.WebTasksEngine.log

   **V.**          **users**

**1.**    **PVWAGWUser**

This is the Gateway user through which other users will access the Vault. The credentials file for this user is PVWAGWUser.ini. This user is a member of the PVWAGWAccounts group 

**2.**    **PVWAAppUser**

This user is used by the Password Vault Web Access for internal processing. The credentials file for this user is PVWAAppUser.ini. This user is created as a PVWAApp user type, can only interact with the PVWA component, and by default, is the only user type in the Vault who can run the PVWA. 

**VI.**          **groups**

**1.**    **PVWAMonitor**

This is the monitoring users group. Members of this group can view CPM activities. The Vault user who runs the installation is added automatically to this group. Any other users who should see this information must be added to the group manually

**2.**    **PVWAUsers**

This is the users group for the Password Vault Web Access. Members of this group can change their Password Vault Web Access preferences.

**3.**    **PVWAGWAccounts**

This is a group of gateway accounts that is shared with Safes that will be accessed through the PVWA.  All Safes that are added in the PVWA are automatically shared with this group. This group is automatically shared with the PVWAConfiguration Safe

**4.**    **PVWAAppUsers**

A  group for PVWAAppUser

**VII.**          **Default Safes**

**1.**    **PVWAConfig**

This Safe contains all the configuration settings for the Password Vault Web Access

**2.**    **PVWAUserPrefs**

This Safe contains the user preference settings for the Password Vault Web Access interface.

**3.**    **PVWATicketingSystem**

This Safe is used to store accounts that are used to connect to ticketing systems that are configured to work with the PVWA.

**4.**    **PVWAReports**

This Safe is specifically for reports 

**5.**    **PVWATaskDefinitions**

This Safe contains all the reports that were saved and/or scheduled by users.

**6.**    **PVWAPublicData**

This Safe contains the help documents that can be accessed in the PVWA

## 4. PSM

●      Privileged Session Manager (PSM) enables organizations to secure, control and monitor privileged access to network devices by using Vaulting technology to manage privileged accounts and create detailed session audits and video recordings of all IT administrator privileged sessions on remote machines.

●      PSM enables users to log on to remote (target) machines or open applications securely through a proxy machine.

●      The established sessions on the target systems are fully isolated and the privileged account credentials are never exposed to the end-users or their client applications and devices.

●      The PSM architecture enables securing of sensitive privileged sessions while facilitating streamlined and native workflows for the IT administrators.

![](file:///C:/Users/sarat/AppData/Local/Packages/oice_16_974fa576_32c1d314_1d4f/AC/Temp/msohtmlclip1/01/clip_image012.jpg)

      **I.**          **services**

⮚     CyberArk Privileged Session Manager

   **II.**          **configuration files**

**1.**    **Basic_psm.ini**

The Basic_psm.ini file contains the basic parameters of PSM which are required to start working with PSM. During installation, it is copied to the PSM installation folder.

 **III.**          **logs**

**1.**    **PSMConsole.log**

**2.**    **PSMTrace.log**

This file contains informational messages and errors that refer to PSM function. This log is meant for the system administrator who needs to monitor the status of the PSM.

**3.**    **<SessionID>.Recorder.log**

This file contains errors and trace messages related to the PSM Recorder that can be used for troubleshooting. The types of messages that are included depend on the debug levels that are specified in the Recorder settings of the PSM configuration.

**4.**    **<SessionID>.<connection component>.log**

This file contains errors and trace messages related to the connection component that can be used for troubleshooting. The types of messages that are included depend on the debug levels that are specified in the Connection Client settings of the PSM configuration.

**5.**    **PSMConnectorsDeployment.log**

This file contains errors and trace messages related to the shared universal connector deployment on multiple PSM servers that can be used for troubleshooting.

**IV.**          **users**

**1.**    **PSMGWUser**

This is the Gateway user through which passwords are retrieved from the vault and is provided for PSM Connections.

**2.**    **PSMAppUser**

This user is used by the Privileged Session Manager for internal processing. This user is created as a PSMApp user type, can only interact with the PSM component, and by default, is the only user type in the Vault who can run the PSM. 

**PSMCONNECT**

**PSMADMINCONNECT**

   **V.**          **groups**

**1.**    **PSMAppUsers**

PSMAppUser is a member of this group by default

**2.**    **PSMMaster**

Members of this group has full access to PSM

**3.**    **PSMLiveSessionTerminators**

Members of this group has access to terminate the User’s PSM Live session

## 5. DR

![](file:///C:/Users/sarat/AppData/Local/Packages/oice_16_974fa576_32c1d314_1d4f/AC/Temp/msohtmlclip1/01/clip_image014.jpg)

      **I.**          **services**

⮚     **CyberArk Vault Disaster Recovery**

   **II.**          **installation directory**

⮚     **C:\ProgramFiles (x86)\PrivateArk\PADR**

 **III.**          **configuration Files**

**1.**    **PADR.ini**

⮚     The Disaster Recovery main configuration file, called PADR.ini, is located in the Disaster Recovery installation folder, and follows the same syntax rules as other Vault parameter files.

⮚      A sample parameter file, called PADR.sample.ini, is copied to the Disaster Recovery installation folder during installation. The Disaster Recovery also has a Vault.ini file used to identify the Production Vault Server.

⮚     During a failover process (automatic or manual), the DR service should first synchronize the data and metadata on the DR Vault to avoid any issues.

⮚     This is automatically enabled in the PADR.INI with the default setting EnableDbsync=Yes

**IV.**          **logs**

**1.**    **PADR.log**

All the log regarding Fail-over and Fail-back process & Vault Replication will be stored in this file

   **V.**          **FAILOVER PROCESS: VAULT**

●      When a failover is initiated (either automatically or manually), the DR component will perform the following actions on the DR Vault server:

●      Synchronize the data and metadata on the DR Vault

●      Start the PrivateArk Server service

●      Start the CyberArk Event Notification Engine service

●      Stop the CyberArk Disaster Recovery service

_![](file:///C:/Users/sarat/AppData/Local/Packages/oice_16_974fa576_32c1d314_1d4f/AC/Temp/msohtmlclip1/01/clip_image016.jpg)_

**VI.**          **TEST AUTOMATIC FAILOVER**

●      A failover process is initiated when the DR Vault loses communication with the Production Vault for any reason.

●      To enable automatic failover confirm **EnableFailover=yes** in the PADR.ini (default).

●      The parameter **CheckRetriesCount**= determines how many times the DR server will retry after a failure.

●      The parameter **CheckInterval**= determines how long to wait between checks.

●      To initiate an Automatic failover stop the PrivateArk Server Service on the Primary Server and wait 5 minutes.

●      Monitor the progress of the test by opening the PADR.LOG file and you can confirm that the DR Vault is testing the Primary Vaults availability, corresponding to the parameters set in the PADR.INI file.

**VII.**          **MANUAL FAILOVER**

●      To prevent an automatic failover, and require only a manual failover, set **EnableFailover** to **No** and Activate **ManualFailover** to **Yes**.

●      Restart the DR Service

●      Verify that the DR Vault has been activated and that the DR service was stopped (PADR.log)