---
aliases: 
tags: 
date created: Saturday, October 28th 2023, 8:02:20 am
date modified: Saturday, October 28th 2023, 8:20:19 am
---

## PSM Introduction

- **Cyber-Ark Privileged Session Manager** is the only service under PSM.  
- Restarting this service will cause the ongoing connections to close and stop working and it will cause an interruption, this kind of action should be informed prior. Its a very serious problem. This should be done during non business hours. 
- Server reboots are performed, this will cause the service to stop. It has to be kept in mind.
- To perform any activity it has to be taken out of VIP/Load balancer before performing a change.

### Active Connections

- The users connected to the target servers can be viewed directly in the target server in the task manager users tab  
- The live connections can also be seen in the monitoring tab in the [[Password Vault Web Access|PVWA]]
- Live sessions safe in the vault contains the details about the live sessions and files are created on the fly.

## PSM Connectors

- PSM connectors enable users to connect to target machines. This is done on a platform-by-platform basis, and affects all the accounts that are associated with the platform.  
- During PSM installation, a series of supported PSM connectors are created. You can use these connectors with the default settings, or you can customize them by changing existing parameters or adding additional parameters manually.  
- In addition, you can develop Custom Universal Connectors or download connectors from the CyberArk Marketplace and then deploy them to your environment, as described in Deploy PSM Connectors.