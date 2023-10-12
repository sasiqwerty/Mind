---
aliases: 
tags: 
date created: Sunday, October 1st 2023, 3:32:31 pm
date modified: Thursday, October 5th 2023, 11:28:35 pm
---

## PVWA Environment

1. **Root Directory (C:)**
	- The `C:\CyberArk\Password Vault Web Access` - PVWA Environment:
	- Houses PVWA's configuration and environment data.
	- Located outside "Program Files" to avoid potential permission issues in Windows.  
	- `C:\inetpub\wwwroot\PasswordVault` - PVWA Web Components:
	- Contains PVWA's web-related files.
	- Sits in the default directory for IIS-hosted web applications, ensuring smooth integration with IIS and streamlined web access.  
In short, CyberArk's directory structure for PVWA combines functionality with security and seamless IIS integration.  

### PVWA Environment

- **Password Vault Web Access**
   - **CredFiles**: This directory seems to be focused on credentials with initialization files like:
     - `apigw.ini`
     - `appuser.ini`
     - `gwuser.ini`
   - **Env**: This directory houses several executables, configuration files, and shared libraries. Some notable files and types include:
     - `.exe` files (e.g., `ApiKeyManager.exe`, `CheckConnection.exe`, `ConfigureVault.exe`, etc.)
     - `.dll` files (e.g., `ComponentSpace.SAML2.dll`, `CyberArk.Casos.dll`, etc.)
     - Configuration and template files like `Web.config`, `PVConfiguration.xml`, and `.xsd` files.
   - **Log**: This directory contains log files. It has:
     - Activity, Debug, and Error logs (`Casos.Activity.log`, `Casos.Debug.log`, `Casos.Error.log`, etc.)
     - **old**: An apparent sub-directory for older logs with date and time-stamped filenames.
   - **Services**: This directory contains some shared libraries (`calibeay64102u.dll`, `cassleay64102u.dll`, etc.) and files related to scheduled tasks (`CyberArkScheduledTasks.exe` and its configurations).
   - **Logs**: Another logging directory, but seems specific to web-related logs:
     - `CyberArk.WebConsole.log`
     - `CyberArk.WebTasksService.log`
     - **old**: Another sub-directory for older logs, but contents are not specified in your list.
   - **VaultInfo**: Contains information specific to the vault:
     - `Vault.ini`
   - **WebCharts**: It contains resources related to displaying charts on the web interface.

This structure suggests a typical setup for a web application, with separate directories for configuration files, environment-specific files, logs, and services. The presence of credential-related files indicates that this system likely handles authentication or integration with other systems. The multiple log files and directories show an effort to keep detailed logs of various system activities and errors.

### PVWA Web Components

#### `C:\inetpub`

- Custerr  
- history  
- logs  
- temp
- wwwroot  
`C:\inetpub\logs`  
	- FailedReqLogFiles  
	- LogFiles  
	- wmsvc  
`C:\inetpub\temp`
- appPools
- ASP Compiled Templates
- IIS Temporary Compressed Files  
`C:\inetpub\wwwroot`
- aspnet_client
- PasswordVault
- Webctrl_client
- iisstart.htm
- iisstart.png
- web.config

#### `C:\inetpub\wwwroot\PasswordVault`

The `.aspx` extension represents ASP.NET Web Forms pages. These pages are used in web applications built with Microsoft's ASP.NET framework. They can contain both HTML markup and server-side scripts, allowing dynamic web page generation and interactive web content.

 - `C:\inetpub\wwwroot\PasswordVault\auth`  
 ![[Pasted image 20231003134749.png]]  
	 - Contains the details of the authentication methods  
 - `C:\inetpub\wwwroot\PasswordVault\Bin`  
	 - Contains the Binary files related to PVWA
 - `C:\inetpub\wwwroot\PasswordVault\ClientControls` 
	 - Contains the files related to the [[Password Vault Web Access|PVWA]] web page related to js and other files
- `C:\inetpub\wwwroot\PasswordVault\CSS`
	- CSS related files for [[Password Vault Web Access|PVWA]] web page
 - `C:\inetpub\wwwroot\PasswordVault\ext`
	 - Ext JS 4.1 is a pure JavaScript application framework that works everywhere from IE6 to the latest Chrome. It enables you to create the best cross-platform applications using nothing but a browser, and has a phenomenal API.
- `C:\inetpub\wwwroot\PasswordVault\extensions`
	- Extension related settings
- `C:\inetpub\wwwroot\PasswordVault\ClientControls`
- `C:\inetpub\wwwroot\PasswordVault\fonts`
- `C:\inetpub\wwwroot\PasswordVault\HelpCenter`
- `C:\inetpub\wwwroot\PasswordVault\Images`
- `C:\inetpub\wwwroot\PasswordVault\JS`
- `C:\inetpub\wwwroot\PasswordVault\RDPWinApplet`
- `C:\inetpub\wwwroot\PasswordVault\Resources`
- `C:\inetpub\wwwroot\PasswordVault\Resources`
- `C:\inetpub\wwwroot\PasswordVault\Services`
- `C:\inetpub\wwwroot\PasswordVault\TransparentConnection`
- `C:\inetpub\wwwroot\PasswordVault\UserControl`
- `C:\inetpub\wwwroot\PasswordVault\v10`
- `C:\inetpub\wwwroot\PasswordVault\WebServices`

| Type           | Name or Example                     | Description/Potential Use                                        |
|:---------------|:-----------------------------------|:---------------------------------------------------------------|
| **Directories**|                                   |                                                               |
|                | auth                               | Possibly for authentication modules or components              |
|                | AWGrid                             | Related to some grid functionality                              |
|                | Bin                                | Contains binary files or executables                           |
|                | ClientControls                     | Client-side controls or components                             |
|                | css                                | Directory for style sheets                                     |
|                | csv                                | Directory for CSV (Comma-Separated Values) files              |
|                | ext                                | Possibly external libraries or extensions                       |
|                | ... (and so on for other dirs)     |                                                               |
| **Web Pages**  |                                   |                                                               |
|                | About.aspx                         | Page providing information about the application               |
|                | addfile.aspx                       | Interface for adding files                                     |
|                | addpassword.aspx                   | Interface for adding passwords                                 |
|                | MyAccounts.aspx                    | Page displaying user accounts                                  |
|                | MyApplications.aspx                | Page displaying user applications                              |
|                | ... (and so on for other .aspx)    |                                                               |
| **Scripts**    | app.js                             | Javascript file for app functionality                          |
| **Styles**     | branding.css                       | Styles related to branding elements                            |
|                | CommonStyles.css                   | General styles used across the application                     |
|                | PVAccountsStyles.css               | Styles related to account displays or operations               |
|                | ... (and so on for other .css)     |                                                               |
| **Config**     | web.config                         | Configuration file for the ASP.NET application                 |
|                | saml.config.template               | Configuration template for SAML authentication                 |
|                | PrecompiledApp.config              | Configuration for a precompiled app                            |
| **Other Files**| MyTicketingValidator.cs            | A C# script/class related to ticketing validation              |
|                | screenpressor.swf                  | A Flash file, possibly related to screen compression           |

| File Type | Description | Example File | Potential Functionality |
|:----------|:------------|:-------------|:------------------------|
| .asmx     | Web services in ASP.NET | AccountsMgt.asmx | Manages account-related operations |
| .ashx     | Generic HTTP handlers in ASP.NET | DownloadCredFile.ashx | Handles downloading of credential files |
| .aspx     | Web forms/pages in ASP.NET | AccountsGridSourceControl.aspx | Displays a grid related to accounts |
| Web.config | Configuration for ASP.NET apps | Web.config | Contains app settings like database connections |
| GridSourceControl & GridDataSource | Data source for grids | LiveSessionsGridSourceControl.aspx | Shows a grid of live sessions |
| Mgt.asmx | "Management" services | PlatformMgt.asmx | Manages platform-related operations |
| OlacTabSourceControl.aspx | Access control tabs | PasswordOlacTabSourceControl.aspx | Related to specific access control |
| PVWA | Password Vault Web Access components | PVWAQueryStringMgt.asmx | Related to PVWA functionalities |
| Report | Reporting functionalities | ReportExport.ashx | Handles reporting aspects |
| Session | User sessions | SessionMgt.asmx | Related to user sessions |
| Setup | Configuration/setup functionalities | SetupMgt.asmx | Deals with app setup |
| SSHKeysTrustsManagement.asmx | SSH key trusts management | SSHKeysTrustsManagement.asmx | Manages SSH key trusts |
| SystemConfigMgt.asmx | Manages system configurations | SystemConfigMgt.asmx | System configuration tasks |
| DiscoveryManagement.asmx | Discovering entities | UnixAccountsDiscoveryManagement.asmx | Discovering accounts or entities |
| Validations & Permissions | Ensure checks & permissions | PasswordValidation.asmx | Validation and permission checks |

## Executable Files in the PVWA Environment

| File Name                 | Location                                                 |
|---------------------------|----------------------------------------------------------|
| `ApiKeyManager.exe`       | Password Vault Web Access/Env                           |
| `CheckConnection.exe`     | Password Vault Web Access/Env                           |
| `ConfigureInstance.exe`   | Password Vault Web Access/Env                           |
| `ConfigurePOCMode.exe`    | Password Vault Web Access/Env                           |
| `ConfigureVault.exe`      | Password Vault Web Access/Env                           |
| `CreateCredFile.exe`      | Password Vault Web Access/Env                           |
| `RegisterInstance.exe`    | Password Vault Web Access/Env                           |
| `CyberArkScheduledTasks.exe` | Password Vault Web Access/Services                     |

1. **ApiKeyManager.exe:** Manage API keys for PVWA.
2. **CheckConnection.exe:** Check connection to PVWA instance.
3. **ConfigureInstance.exe:** Configure PVWA instance.
4. **ConfigurePOCMode.exe:** Configure PVWA instance in POC mode.
5. **ConfigureVault.exe:** Configure Password Vault.
6. **CreateCredFile.exe:** Create credential file for PVWA.
7. **RegisterInstance.exe:** Register PVWA instance with Password Vault.
8. **CyberArkScheduledTasks.exe:** Manage CyberArk scheduled tasks for PVWA.
	- Report related "logon as a service" tasks and services are handled from here.
	- Stopping this wont impact the loading of PVWA page
	- This is for scheduling the CyberArk reports, automating the report downloading  
![[Pasted image 20231005232442.png]]

## Log Files in the PVWA Environment

| File Name                                  | Location                                        |
|--------------------------------------------|-------------------------------------------------|
| `Casos.Activity.log`                       | Password Vault Web Access/Log                  |
| `Casos.Debug.log`                          | Password Vault Web Access/Log                  |
| `Casos.Error.log`                          | Password Vault Web Access/Log                  |
| `CheckConnection.log`                      | Password Vault Web Access/Log                  |
| `ConfigureInstance.log`                    | Password Vault Web Access/Log                  |
| `ConfigureVault.log`                       | Password Vault Web Access/Log                  |
| `RegisterInstance.log`                     | Password Vault Web Access/Log                  |
| `CyberArk.WebConsole.log`                  | Password Vault Web Access/Logs                |
| `CyberArk.WebTasksService.log`             | Password Vault Web Access/Logs                |

### `C:\Windows\Temp\PVWA` - Log Folder Location for [[Password Vault Web Access|PVWA]]

- `CyberArk.WebApplication.log` - Main log file
- `CyberArk.WebConsole.log`
- `CyberArk.WebTasksEngine.log`
- `PVWA.App.log`  
These log files are built on top of a standard logging library. Their clear log structure enable you to troubleshoot failures without having to enable debug mode, which provides the ability to track business flows in the log file.

These log files are created by the PVWA and stored on the Web server in the location specified in the LogFolder parameter in the web.config file. If this location is not specified, the log files will be stored in the Temp folder on the Web server. By default, this folder is %windir%\temp.  

### Log File Structure

`<Date> <Severity> [<ThreadID>] <username> <sessionID> <CorrelationID> <Message> <Exception Details> [<Source>]`

| **Field**      | **Description**                                                                     |
|:-------------------|:------------------------------------------------------------------------------------|
| Date               | The date and time when the log entry was created.                                   |
| Severity           | Log level: Debug, Info, Warning, Error, Critical (ordered from low to high severity).|
| ThreadID           | ID of the thread running the process creating the log entry.                        |
| Username           | Name of the logged-on user (if relevant).                                           |
| SessionID          | Segment of the logged-on user session ID (if relevant).                             |
| CorrelationID      | Unique ID for each request handled by the app. Helps correlate log entries.         |
| Message            | Actual log message.                                                                 |
| Exception Details  | Exception message and stack trace (if relevant).                                    |
| Source             | Class from which the log entry originated.                                          |


![[Pasted image 20231003153059.png]]  

`C:\Windows\Temp\CPM` - Log Folder location for CPM

## Config and Cred Files in the PVWA Environment

| File Name                         | Location                                        |
|-----------------------------------|-------------------------------------------------|
| `apigw.ini`                       | Password Vault Web Access/CredFiles             |
| `appuser.ini`                     | Password Vault Web Access/CredFiles             |
| `gwuser.ini`                      | Password Vault Web Access/CredFiles             |
| `EPMConfiguration.xml`            | Password Vault Web Access/Env                   |
| `Policies.xml`                    | Password Vault Web Access/Env                   |
| `PVConfiguration.xml`    | Password Vault Web Access/Env                   |
| `SafeTemplate.xml`                | Password Vault Web Access/Env                   |
| `Web.config`                      | Password Vault Web Access/Env                   |
| `Vault.ini`                       | Password Vault Web Access/VaultInfo             |

### Important Config Files

PVWA related config file : `Web.config`  
PVWA related config file :`Policies.xml`  
PVWA related config file :`PVConfiguration.xml`  
IIS related Config file : `C:\Windows\System32\inetsrv\config\applicationHost.config`

## Inetsrv

`inetsrv` is a directory commonly found on Windows servers, specifically related to Internet Information Services (IIS). IIS is a web server software package created by Microsoft for hosting web content, websites, web applications, and services.  

IIS related Config file : `C:\Windows\System32\inetsrv\config\applicationHost.config`

| **Content in `inetsrv`**  | **Description**                                             |
|:-------------------------|:------------------------------------------------------------|
| Core IIS Files           | Essential .dll and .exe files for IIS operations.           |
| Configuration Files      | Files like `MetaBase.xml` for IIS configurations.           |
| Management Tools         | Utilities such as `appcmd.exe` for IIS management.          |
| Extensions and Modules   | Modules providing functionalities like authentication.      |
| Language Directories     | Resources for localization, e.g., `en` or `en-US`.          |

| File Name      | Potential Purpose/Functionality                       |
|:---------------|:-------------------------------------------------------|
| appcmd.exe     | IIS command-line tool for management tasks             |
| iisrstas.exe   | Might be related to IIS restart or status              |
| iissetup.exe   | IIS setup-related executable                           |
| iisual.exe     | Unclear, possibly a utility related to IIS             |
| inetinfo.exe   | Core IIS executable for the service                    |
| InetMgr.exe    | IIS Manager GUI tool                                   |
| w3wp.exe       | Worker process for IIS, handles web requests           |
| WMSvc.exe      | Web Management Service, allows remote management       |

## [[Password Vault Web Access|PVWA]] Access Pools

In Internet Information Services (IIS), an Application Pool (often abbreviated as App Pool) is a mechanism used to separate sets of IIS worker processes that share the same configuration and application boundaries. This separation provides a way to isolate different web applications, so that issues in one app pool won't affect the websites or applications running in another.

- PasswordVaultWebAccessPool has to be started to ensure that PVWA works, this is created during the installation
- DefaultAppPool has to be started to ensure PVWA actually runs

## APIKeyManager

The APIKeyManager is a command-line tool that manages asymmetric key pairs for secure API connections and authentication with the Vault. The private key is retained locally for scripts or CyberArk clients, while the public key is kept in the Vault, linked to a pre-established Vault username. Users can:

- Generate and save a key pair, storing the public key in the Vault.
- Generate a key pair and save the public key locally.
- Store an externally created public key in the Vault.
- Revoke a key pair. 

**In the context of [[Password Vault Web Access|PVWA]] its used to create the `apigw.ini` Cred file.**

## [[Password Vault Web Access|PVWA]] Debugging

> [Where can I find the logs for each CyberArk component? (site.com)](https://cyberark.my.site.com/s/article/Where-do-I-find-the-logs)  
> Please turn on debugging for the PVWA by doing the following
  
- Please go to **Administration** -> **Options** -> **Logging**, and set Debug and Information level to High.  

### **Password Vault Web Access Debugging Steps:**

#### Configuration File(s)

- `wwwroot\PasswordVault\web.config`
- `PWAConfig Safe` → `Root\PV\Configuration.xml`
- `PWAConfig Safe` → `Root\Policies.xml`

#### Setting Debug Mode

version 4.6 or lower, use the `PWAConfig Safe` → `Root\PV\Configuration.xml`.  
For Version 5.0 or later:

1. Open PVWA and go to the System Configuration page.
2. Navigate to the Web Access section and select Options, followed by Logging. Configure as:
   - `DebugLevel` = High (Options: None/High/Low)
   - `InformationLevel` = High (Options: None/High/Low)
   - Enable `Profiling` for deeper performance insights.
   - It has to be kept in mind that enabling debug here in [[Password Vault Web Access|PVWA]] mean that **all the components** will have their debug level increased.

#### Log Files Location

- Default location: `%windir%\temp\`  
- Based on the `LogFolder` parameter in `web.config` inside the IIS PasswordVault folder, you'll find:
   - `PVWA.App.log`
   - `PVWA.Reports.log`
   - `PVWA.Console.log`

For a more comprehensive understanding, refer to the PVWA Logging documentation.


- Run an iisreset to ensure the change takes effect and then reproduce the issue.  
  ![[Pasted image 20231004135340.png]]  

### **CyberArk xRay Overview**

> [How to use Cyberark XRay (site.com)](https://cyberark.my.site.com/s/article/How-to-use-Cyberark-XRay)

CyberArk xRay is a diagnostic and troubleshooting tool tailored for CyberArk products. It streamlines the process of gathering logs and configuration files, simplifying a traditionally complex procedure. 

Here's a breakdown of its key features and attributes:

| Feature/Attribute | Description |
|-------------------|-------------|
| **Purpose** | Facilitates in-house troubleshooting for issues related to CyberArk products. |
| **Data Collection** | Gathers product logs and configuration files from various CyberArk products in a single step. |
| **Secure Transfer** | Ensures that the collected data is encrypted during the transfer process. |
| **Collaboration** | Allows sharing of data with partners or directly with CyberArk, linking it to specific support cases. |
| **Configuration Flexibility** | Supports different access approaches for each CyberArk product and offers both manual and automatic data collection. |
| **Execution** | Can be run either remotely or directly on CyberArk servers. |
| **Data Encryption** | Encrypts all data files during the collection phase, irrespective of the data's source. |
| **Recording Option** | Enables users to record specific scenarios to provide a comprehensive view of issues to CyberArk. |
| **Compliance** | Ensures data storage and encryption adheres to GDPR standards. |

In essence, CyberArk xRay empowers organizations to be more self-reliant in troubleshooting while ensuring data security and compliance.

## [[Password Vault Web Access|PVWA]] - Malfunctions and Troubleshooting

### Malfunctions

- Internal User Suspension
- [[Password Vault Web Access|PVWA]] network issues
- Application Pool related errors in IIS Manager
- Improper Mapping to vault (vualt.ini)
- [[Password Vault Web Access|PVWA]] SSL Certificate Expiration 
- Load Balancer Issues
- Config file corruptions
- Low Storage Errors
- Improper Cred file permissions/owners of [[Password Vault Web Access|PVWA]]
- [[Group Policy]] Changes

### Troubleshooting

1. **IIS Reset**
    - Use the command `iisreset /status` to check the status of IIS.
    - Alternatively, simply use `iisreset` to reset the IIS.
2. **Ping PVWA Servers**
    - Ping all the PVWA servers to ensure they are up and running.
    - ping the Vault from the fault [[Password Vault Web Access|PVWA]] server.
3. **Check PVWA URL Connectivity**
    - Test if you can access the particular PVWA URL.
4. **Port Connectivity**
    - Check port connectivity between all the PVWA servers and the vault server.
5. **Use Test-NetConnection**
    - This PowerShell cmdlet can be used to check network connections.
    ```powershell
    Test-NetConnection -ComputerName <PVWA_Server_Name> -Port <Port_Number>
    ```
6. **Review Logs**
    - Check the **ITALOG** or the **Server Central Administration Console** for any related errors.
7. **Online Research**
    - Search and read articles online related to the observed errors to see if they offer applicable solutions.
8. **Enable Debugging**
    - If the issue remains unresolved after the above steps, consider enabling debugging to get more detailed information.


