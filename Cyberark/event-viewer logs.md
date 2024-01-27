---
aliases: 
tags: 
date created: Saturday, September 16th 2023, 2:57:12 am
date modified: Saturday, January 27th 2024, 6:59:33 pm
---
#16-09-23 Saturday

## Event Viewer Logs in Windows

**Event Viewer** is a component of Microsoft's Windows OS that lets administrators and users view the event logs on a local or remote machine. These logs contain information messages, warnings, errors, and other system-related events reported by the OS, software applications, and hardware components.

### How to Access Event Viewer:

1. **Via Run Prompt**: Press `Windows + R` to open the Run prompt. Type `eventvwr.msc` and press Enter.
2. **Via Control Panel**: Navigate to Control Panel > Administrative Tools > Event Viewer.
3. **Via Windows Search**: Type "Event Viewer" in the Windows search bar and click on the corresponding result.

### Contents of Event Viewer:

Once inside the Event Viewer, you'll encounter several primary logs:

1. **Application**: This log contains events logged by applications or programs. For example, a database program might report a file error in the application log.
2. **Security**: Contains security-related events such as valid and invalid logon attempts, as well as events related to resource use such as creating, opening, or deleting files or other objects. Administrators can specify what events are recorded in the security log.
3. **Setup**: Logs related to the application setup.
4. **System**: Contains events logged by Windows system components. For example, if a driver fails to load during startup, an event will be recorded in the system log.
5. **Forwarded Events**: This log is used to store events collected from remote computers.
6. **Applications and Services Logs**: These are logs created by applications. For example, if you have SQL Server installed on your computer, you'll see a specific set of logs just for SQL Server.

Each log entry contains:

- **Level**: This indicates the severity of the event, such as "Information", "Warning", "Error", etc.
- **Date and Time**: When the event occurred.
- **Source**: The software or component that logged the event.
- **Event ID**: A number that identifies the specific event type.
- **Task Category**: A classification grouping related events.
- **General Details**: A description of the event.

You can double-click on any event in the list to see its details.

### Uses:

The Event Viewer is a crucial tool for troubleshooting and monitoring Windows systems. If something is going wrong with your system, checking the event logs can give you valuable information about the root cause. For example, if a program isn’t starting as expected, the Event Viewer might reveal that a required DLL file is missing, or that the program crashed due to a specific reason.

![[Pasted image 20230916030114.png]]  
Remember, while Event Viewer provides a lot of data, interpreting that data requires some experience and knowledge about the specific systems and software you are working with.