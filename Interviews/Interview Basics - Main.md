---
aliases: 
tags: 
date created: Saturday, January 27th 2024, 7:03:18 pm
date modified: Monday, January 29th 2024, 10:24:57 am
---

## 1. Ports for [[CyberArk]]

| Platform                      | Protocol                                      | Port               |
|--------------------------|-----------------------------------------------|--------------------|
| Windows Domain Accounts  | Windows protocols (SMB, RPC, WMI, DCOM, etc.) | 139,445            |
|                          | kerberos                                      | 88                 |
|                          | DNS                                           | 53                 |
|                          | LDAPs                                         | 38,963,632,683,269 |
| UNIX                     | SSH                                           | 22                 |
|                          | Telnet                                        | 23                 |
| OS                       | FTP                                           | 21                 |
|                          | HTTP                                          | 80                 |
|                          | HTTPS                                         | 443                |
| ODBC                     | Can be changed, depending on the database     | Can be changed     |
| Oracle                   | Proprietary protocol                          | 1521               |
| MSSQL                    | Proprietary protocol                          | 1433               |
| MySQL                    | Proprietary protocol                          | 3306               |
| Sybase                   | Proprietary protocol                          | 5000               |


| Port            | Use Case                                                                                                                         |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------|
| 22              | To connect to target machines using SSH. This port can be configured by the SSHPort parameter in the CACPMScanner.exe.config file. |
| 88              | Used for KDC services (only relevant to domain controllers). This port must be accessible both through network-based and host-based firewalls. |
| 135, 137, 138, 139 | To connect to target machines using NetBIOS ports. These ports must be accessible on host-based firewalls.                        |
| 389             | To connect to target machines using the LDAP service (only relevant to domain controllers). This port must be accessible both through network-based and host-based firewalls. |
| 636             | To connect to target machines using the LDAPS service (only relevant to domain controllers). This port must be accessible both through network-based and host-based firewalls. |
| 445             | To connect to target machines using SMB/TCP. This port must be accessible on host-based firewalls.                                |
| 4431            | To discover SSH keys on Windows machines without Cygwin. This port is not configurable.                                           |
| 49154           | This port is used to view and administrate Scheduled Tasks on the remote machine.                                                |
| 49155, 49156    | This port is used to get the list of services from the remote machine.                                                           |

| IP Address Category | Protocol | Port  | Purpose/Description                 |
|---------------------|----------|-------|-------------------------------------|
| DR Vault            | TCP      | 1858  | For connectionless DR Vault         |
| Backup              | ICMPv4   | -     | Uses ICMPv4 protocol                |
| Other Components    | ICMPv4   | -     | Uses ICMPv4 protocol                |
| Clients             | -        | -     | No specific port/protocol mentioned |
| -                   | TCP      | 3389  | For RDP (Remote Desktop Protocol)   |
| -                   | UDP      | 3389  | For RDP (Remote Desktop Protocol)   |
| Remote Control Client IP | TCP  | 9022  | Alternate port for SSH             |

| IP Address Category | Protocol | Port  | Purpose/Description                 |
|---------------------|----------|-------|-------------------------------------|
| HTTPS               | HTTPS    | 443   | For secure web communication        |
| Syslog Server IP    | TCP      | 514   | For Syslog service (TCP)            |
| Syslog Server IP    | UDP      | 514   | For Syslog service (UDP)            |
| LDAP Server IP      | TCP      | 636   | For secure LDAP communication (LDAPS) |
| RADIUS Server IP    | UDP      | 1812  | For RADIUS authentication services  |
| SMTP Server IP      | TCP      | 25    | For SMTP email services             |
| -                   | UDP      | 162   | For SNMP Trap (assuming it's related to SNMP) |


[Standard Ports and Protocols | CyberArk Docs](https://docs.cyberark.com/PAS/13.0/en/Content/PAS%20SysReq/Standard%20Ports%20and%20Protocols.htm?TocPath=Installation%7CSystem%20Requirements%7CStandard%20Ports%20and%20Protocols%7C_____0)  
[Network requirements | CyberArk Docs](https://docs.cyberark.com/DPA/Latest/en/Content/Introduction/dpa_network-requirements.htm)  
![[Pasted image 20240127191023.png]]  

## 2. [[Daily Activities in CyberArk]]

### Health Page

To view the System Health dashboard, you must be in the VaultAdmins group and have at least Audit Users Vault authorization.  
Accounts Unsuspension  
Reports  
Ticket Handling  
Onboarding Accounts  
Checking Vault Logs

1. [[CyberArk Components]]  
	1. https://docs.cyberark.com/PAS/13.0/en/Content/PASIMP/Introducing-the-Privileged-Account-Security-Solution-Intro.htm  
2. [[Account Onboarding - Windows]]  
3. [[Account Onboarding - Linux]]

## 6. Safes Permissions

### Access

| Permission        | Enables Safe Members to... |
|-------------------|----------------------------|
| **Use Accounts**  | Log on to remote machines via PSM or non-PSM (with 'Retrieve accounts') connections, access Accounts List and Details. |
| **Retrieve Accounts** | View, copy, save, and open accounts/files; manage visibility and access based on platform and 'Manage Safe' authorizations. |
| **List Accounts** | View lists of accounts or files within the Safe. |

### Account Management

| Permission                          | Enables Safe Members to... |
|-------------------------------------|----------------------------|
| **Add Accounts**                    | Add accounts in Safe, manage account groups/platforms, and automatically receive 'Update account properties' in PVWA. |
| **Update Account Content**          | Change account values/files, undelete accounts, manage linked account copies, upload files to Vault. |
| **Update Account Properties**       | Update account properties (not values), manage logon/reconcile accounts, associate platforms/groups, save remote connection details. |
| **Initiate CPM Account Management** | Initiate CPM operations (change, verify, reconcile), manage passwords if 'Specify next account content' is authorized. |
| **Specify Next Account Content**    | Specify content for next account value change by CPM, requires 'Initiate CPM account management operations'. |
| **Rename Accounts**                 | Rename existing accounts in the Safe. |
| **Delete Accounts**                 | Delete accounts and linked account copies in the Safe. |
| **Unlock Accounts**                 | Unlock accounts/files locked by other users, relevant for enforced check-in/check-out policies. |

### Workflow
 
| Permission                      | Enables Safe Members to... |
|---------------------------------|----------------------------|
| **Authorize Account Request**   | Confirm account access requests for Safe members. Requires 'List accounts' to view request details. |
| **Access Safe Without Confirmation** | Enter the Safe without needing confirmation, overriding properties requiring access confirmation. |

### Advanced

## [[Reports]]

Reports can be generated in the Reports page in the PVWA by users who belong to the group that is specified in the ManageReportsGroup parameter in the Reports section of the Web Access Options in the System Configuration page. By default, this is the PVWAMonitor group.

## Vendor Access

You must be invited by an existing tenant so that you receive an invitation email with a link to Remote Access.

CyberArk Mobile App  
One-Time Tokens  
Self-Service Invitation