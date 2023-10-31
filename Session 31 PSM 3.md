---
aliases: 
tags: 
date created: Monday, October 30th 2023, 9:24:59 am
date modified: Tuesday, October 31st 2023, 12:04:47 pm
---

## Introduction

- The PSM is installed on a Windows system as an automatic system service called CyberArk Privileged Session Manager.  
- It can be stopped and started through the standard Windows service management tools.  
- **PSM activity logs are stored in the Log subfolder of the PSM installation folder**. These log files can be uploaded to the Vault for long term storage. 
- The PSM install log is located at `C:\Temp\PSM\PSMInstall.log`. This log file monitors the installation process and ensures that PSM was installed successfully. 
- You can check the `PSMConsole` and `PSMTrace` logs to find out why the PSM Service is stopping. 
- The maximum size of the log file is specified in the PSM configuration.

## PSM Logging Overview

- **Location**: Log files are stored in the `Log` subfolder of the PSM installation.
- **Upload**: Logs can be transferred to the Vault for extended storage.
- **Max Size**: Determined by the PSM configuration.

### Log Handling

| Aspect                 | Details                                                                                             |
|------------------------|-----------------------------------------------------------------------------------------------------|
| Event Viewer Errors    | Some PSM-specific errors appear only in the event viewer.                                           |
| Log Rotation           | When logs attain the size defined in `LogRotationSize`, they move to the `\old` subfolder. A new log is then initiated. |

### Recording in Event Viewer

- **Standard Monitoring**: PSM errors are recorded in the machine's Event Log and specific log files.
- **Identification**: Messages in the Event Log carry the prefix **CyberArk PSM** to denote PSM-related activities.

| Log                                       | Description                                                                                                                                                                           |
|-------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `PSMConsole.log`                          | Contains informational messages and errors related to PSM function. Intended for system administrators monitoring PSM status.                                                           |
| `<SessionID>.Recorder.log`                | Contains errors and trace messages for the PSM Recorder. Useful for troubleshooting. Messages depend on the Recorder's debug settings in the PSM configuration.                          |
| `<SessionID>.connection component>.log`   | Contains errors and trace messages related to the connection component. Useful for troubleshooting. Messages depend on the Connection Client's debug settings in the PSM configuration. |
| `PSMConnectorsDeployment.log`             | Contains errors and trace messages about the shared universal connector deployment on multiple PSM servers. Useful for troubleshooting.                                                |
| `PSM Server log files`                    | These logs are in the `PSM\Logs` directory and are subsequently moved to the `PSM\Logs\old` subdirectory.                                                                              |
| `PSM Recorder and Connection client`      | These logs are in the `PSM\Logs\Components` directory and later shifted to the `PSM\Logs\Components\old` subdirectory.                                                                |

## Enable Debugging

- We have to set the debug level from the [[Password Vault Web Access|PVWA]], this setting applies to all the [[Privileged Session Manager|PSM]]s in the load balancer. 
	- Server Settings > TraceLevels = 1,2,3,4,5,6,7  
	- Recorder Settings > TraceLevels= 1,2  
	- Connection Client Settings > TraceLevels = 1,2
- Enabling debug mode will apply the change to all the PSMs in the VIP/Load balancer, its advisable to complete the debug task as quickly as possible and disable debug as the messages generated would increase the load on the servers and in some cases also the vault.  

### Levels

TraceLevels indicate:  
0 - None.  
1 - Exceptions only. Each error in the system will be sent to the trace file, whether  
it is recoverable or not.  
2 - Controller trace. Includes the initialization of the PSMServer, recovery  
procedure and configuration.  
3 - Listener trace. Each session identified by the listener is reported, whether it is  
handled or not.  
4 - Session trace. Includes all the work done for a session (authentication and  
impersonation, password retrieval, activation of components, etc.).  
5 - Uploader trace.  
6 - CASOS errors trace (Vault errors trace).  
7 - CASOS debug and activity trace.

## PSM Folder Structure

#todo  
`PSMInitSession.exe` : The main application the initializes the sessions via [[CyberArk]].