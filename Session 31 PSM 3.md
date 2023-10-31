---
aliases: 
tags: 
date created: Monday, October 30th 2023, 9:24:59 am
date modified: Monday, October 30th 2023, 11:28:18 am
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

Enabling debug mode will apply the change to all the PSMs in the VIP/Load balancer, its advisable to complete the debug task as quickly as possible and disable debug as the messages generated would increase the load on the servers and in some cases also the vault.

## PSM Folder Structure

#todo  
`PSMInitSession.exe` : The main application the initializes the sessions via [[CyberArk]].