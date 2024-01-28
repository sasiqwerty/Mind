---
aliases: 
tags: 
date created: Saturday, January 27th 2024, 7:03:18 pm
date modified: Sunday, January 28th 2024, 7:29:01 pm
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
2. [[Daily Activities in CyberArk]]  
3. [[CyberArk Components]]  
	1. https://docs.cyberark.com/PAS/13.0/en/Content/PASIMP/Introducing-the-Privileged-Account-Security-Solution-Intro.htm  
4. [[Account Onboarding - Windows]]  
5. [[Account Onboarding - Linux]]  
6. [[Reports]]