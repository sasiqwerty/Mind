---
aliases: 
tags: 
date created: Friday, August 11th 2023, 12:42:20 pm
date modified: Thursday, August 17th 2023, 2:55:12 pm
---

## [[Groups and Users in PrivateArk]]

#important #memorize 

| User/Group                  | Disambiguation            | Description                                                                                                                                         |
|-----------------------------|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Administrator               | Internal User - CyberArk  |  The CyberArk administrator has full control over the CyberArk vault and can perform all administrative tasks.                                      |
| Auditor                     | Internal User - CyberArk  |  The CyberArk auditor has read only access to the CyberArk vault and can view logs and reports.                                                     |
| Auditors                    | Internal Group - CyberArk |  The CyberArk auditors group is a group of users who have the auditor role.                                                                         |
| Backup                      | Internal User - CyberArk  |  The CyberArk backup user has the ability to back up the CyberArk vault.                                                                            |
| Backup Users                | Internal Group - CyberArk |  The CyberArk backup users group is a group of users who have the backup role.                                                                      |
| Batch                       | Internal User - CyberArk  |  The CyberArk batch user is used to automate tasks in the CyberArk vault.                                                                           |
| CyberArk Auditors           | External Group - CyberArk |  The CyberArk auditors external group is a group of users who have been granted auditor permissions from CyberArk to an external server group.           |
| CyberArk Safe Managers      | External Group - CyberArk |  The CyberArk safe managers external group is a group of users who have been granted safe manager permissions from CyberArk to an external server group. |
| CyberArk Vault Admins       | External Group - CyberArk |  The CyberArk vault admins external group is a group of users who have been granted vault admin permissions from CyberArk to an external server group.   |
| DR                          | Internal User - CyberArk  |  The CyberArk DR user is used to recover the CyberArk vault from a disaster.                                                                        |
| DR Users                    | Internal User - CyberArk  |  The CyberArk DR users group is a group of users who have the DR role.                                                                              |
| EPMAgent                    | Internal User - CyberArk  |  The CyberArk EPMAgent user is used to manage the CyberArk EPM solution.                                                                            |
| Notification Engines        | Internal Group - CyberArk |  The CyberArk notification engines group is a group of users who have the ability to send notifications from the CyberArk vault.                    |
| NotificationEngine          | Internal User - CyberArk  |  The CyberArk notification engine user is used to send notifications from the CyberArk vault.                                                       |
| Operator                    | Internal User - CyberArk  |  The CyberArk operator has the ability to perform basic administrative tasks in the CyberArk vault.                                                 |
| Operators                   | Internal Group - CyberArk |  The CyberArk operators group is a group of users who have the operator role.                                                                       |
| PasswordManager             | Internal User - CyberArk  |  The CyberArk password manager is used to manage passwords in the CyberArk vault.                                                                   |
| PSMApp_COMPONENTS           | Internal User - CyberArk  |  The CyberArk PSMApp_COMPONENTS user is used to manage the CyberArk PSM application.                                                                |
| PSMAppUsers                 | Internal Group - CyberArk |  The CyberArk PSMAppUsers group is a group of users who have the ability to use the CyberArk PSM application.                                       |
| PSMGw_COMPONENTS            | Internal Group - CyberArk |  The CyberArk PSMGw_COMPONENTS group is a group of users who have the ability to manage the CyberArk PSM Gateway.                                   |
| PSMLivesessionTerminators   | Internal Group - CyberArk |  The CyberArk PSMLivesessionTerminators group is a group of users who have the ability to terminate live PSM sessions.                              |
| PSMMaster                   | Internal User - CyberArk  |  The CyberArk PSMMaster user is used to manage the CyberArk PSM solution.                                                                           |
| PSMPTAAppUsers              | Internal Group - CyberArk |  The CyberArk PSMPTAAppUsers group is a group of users who have the ability to use the CyberArk PSMPTA application.                                 |
| PVWAAppuser                 | Internal User - CyberArk  |  The CyberArk PVWAAppuser user is used to manage the CyberArk PVWA application.                                                                     |
| PVWAAppUsers                | Internal Group - CyberArk |  The CyberArk PVWAAppUsers group is a group of users who have the ability to use the CyberArk PVWA application.                                     |
| PVWAGWAccounts              | Internal Group - CyberArk |  The CyberArk PVWAGWAccounts group is a group of users who have the ability to access the CyberArk PVWA Gateway.                                    |
| PVWAGWUser                  | Internal User - CyberArk  |  The CyberArk PVWAGWUser user is used to manage the CyberArk PVWA Gateway.                                                                          |
| PVWAMonitor                 | Internal Group - CyberArk |  The CyberArk PVWAMonitor group is a group of users who have the ability to monitor the CyberArk PVWA application.                                  |
| PVWAUsers                   | Internal Group - CyberArk |  The CyberArk PVWAUsers group is a group of users who have the ability to use the CyberArk PVWA application.                                        |
| Security Admins             | Internal Group - CyberArk |  The CyberArk security admins group is a group of users who have the ability to manage security settings in the CyberArk vault.                     |
| Security Operators          | Internal Group - CyberArk |  The CyberArk security operators group is a group of users who have the ability to perform basic security tasks in the CyberArk vault.              |
| Vault Admins                | Internal Group - CyberArk |  The CyberArk vault admins group is a group of users who have the ability to manage all aspects of the CyberArk vault.                              |