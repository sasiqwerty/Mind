---
aliases: 
tags: 
date created: Wednesday, September 20th 2023, 6:35:57 pm
date modified: Wednesday, September 20th 2023, 6:44:25 pm
---

## Prerequisites

### Starting

1. `Get-ExecutionPolicy`  
	- `Restricted`: No scripts can run, including configuration files and interactive sessions.
	- `AllSigned`: Only scripts that have been signed by a trusted publisher can run.
	- `RemoteSigned`: Scripts that you write on the local computer can run without a digital signature, but downloaded scripts or scripts from the internet must be signed by a trusted publisher.
	- `Unrestricted`: All Windows PowerShell scripts can be run.
	- `Bypass`: Nothing is blocked and there are no warnings or prompts.
	- `Undefined`: No execution policy is set, default is used.
2. `Set-ExecutionPolicy Bypass -Scope Process` (**Purpose**: This cmdlet changes the execution policy setting.)
    - `Bypass`: This sets the execution policy to "Bypass", meaning all scripts and configuration files can be run, and there won't be any warnings or prompts.
    - `-Scope Process`: This specifies that the execution policy change is only for the current PowerShell process/session. It won't affect other PowerShell sessions or the system-wide setting. 

**Notes** : The `Get-ExecutionPolicy` command retrieves the current PowerShell script execution setting. The `Set-ExecutionPolicy Bypass -Scope Process` command temporarily allows all scripts to run in the current session without restrictions or warnings. It's essential to use with caution due to security implications.

### Prerequisites Script

`PS C:\CYBR_Files\Password Vault Web Access-Rls-v12.0\InstallationAutomation> .\PVWA_Prerequisites.ps1`

The above command is the location where the script `PVWA_Prerequisites.ps1` is supposed to be run.  

#### Server Features

These server features are primarily related to the Windows Web Server role and its associated components.
1. **Web-Server**: Basic web server role, allowing the server to host websites.
2. **Web-WebServer**: Core web server capabilities for Windows.
3. **Web-Common-Http**: Basic HTTP protocol functionality for web server.
4. **Web-Static-Content**: Enables serving static web files like HTML, CSS, and images.
5. **Web-Default-Doc**: Allows configuration of default documents for a website.
6. **Web-Dir-Browsing**: Enables directory browsing on a web server.
7. **Web-Http-Errors**: Allows custom HTTP error messages.
8. **Web-Http-Redirect**: Provides URL redirection capability.
9. **Web-App-Dev**: Tools and services for web application development.
10. **Web-ASP**: Support for Active Server Pages, an older dynamic web content technology.
11. **Web-ISAPI-Ext**: Provides Internet Server API extensions, enabling advanced server-side functionality.
12. **Web-ISAPI-Filter**: Allows filters to process requests and responses for the server.
13. **Web-Health**: Tools to monitor and maintain server health.
14. **Web-Http-Logging**: Enables logging of HTTP requests.
15. **Web-Request-Monitor**: Monitors active web requests for real-time data.
16. **Web-Security**: Enhances web server security features.
17. **Web-Basic-Auth**: Provides basic user authentication for web access.
18. **Web-Windows-Auth**: Allows Windows-based authentication for web access.
19. **Web-Filtering**: Tools to filter requests/responses for a web server.
20. **Web-Mgmt-Tools**: Core tools for managing the web server.
21. **Web-Mgmt-Service**: Provides remote management capabilities for the web server.
22. **Web-Mgmt-Console**: GUI tools for managing web server settings.
23. **Web-Scripting-Tools**: Offers scripting capabilities for web server management.
24. **Web-Mgmt-Compat**: Provides compatibility layer for older web server management tools.
25. **Web-Metabase**: Legacy configuration storage mechanism for IIS.
26. **Web-WMI**: Windows Management Instrumentation for the web server, enabling scripting and automation.
27. **Web-ASP**: (Repeated) Support for Active Server Pages.
28. **Web-WebSockets**: Provides support for WebSocket protocol, enabling real-time communication.

The final message after the script finishes running
```powershell
Cleanup - Delete files except logs and backup
Finish Execution

{
    "isSucceeded":  0,
    "errorData":  "Step Verify .Net Version Skipping prerequisites check.\nStep PVWA Install Web Server Roles Skipping prerequisites check.\nStep Disable IPV6 Skipping prerequisites check.\n
Step PVWA Config Self Certificat Skipping prerequisites check.\nStep Setting IIS SSL TLS Configuration Skipping prerequisites check.\n                  Operation Succeeded",
    "logPath":  "C:\\CYBR_Files\\Password Vault Web Access-Rls-v12.0\\InstallationAutomation\\prerequesites_2023-09-20_18-15-01\\Script.log"
}
```