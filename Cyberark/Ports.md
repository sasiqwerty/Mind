---
aliases: 
tags: 
date created: Monday, July 31st 2023, 5:25:40 pm
date modified: Wednesday, January 24th 2024, 10:05:55 pm
---

## Introduction

Port numbers are used to identify specific network services and applications on a device, and their assignments are managed by IANA (Internet Assigned Numbers Authority) through the Service Name and Transport Protocol Port Number Registry.  
![[Pasted image 20230803185943.png]]

## Ports and Their Popularity

### Well-Known Ports

Well-Known Ports (0-1023): Reserved for standard services like HTTP (port 80), HTTPS (port 443), FTP (port 21), etc.  

### Registered Ports

Registered Ports (1024-49151): Assigned to various applications and services by IANA or a designated authority.  

### Dynamic/Private Ports

Dynamic/Private Ports (49152-65535): Available for general use by applications, but not officially assigned by IANA

## Network Port Definitions for CyberArk Components

| Component / Target                 | Ports and Protocols Used                     | Description/Usage                           |
|------------------------------------|----------------------------------------------|---------------------------------------------|
| Vault                              | TCP/1858                                     | Default port for Vault                      |
| Disaster Recovery Vault (DR Vault) | TCP/1858                                     | Communication with DR Vault                 |
| Central Policy Manager (CPM)       | TCP/1858, TCP/443, TCP/22, TCP/135, TCP/139, TCP/445, TCP/1521-1526, TCP/1433 | Communication with various targets including Linux, VMware hosts, Cisco devices, Windows, MYSQL, Oracle |
| Password Vault Web Access (PVWA)   | TCP/1858                                     | Default port for PVWA                       |
| Privileged Session Manager (PSM)   | TCP/1858, TCP/443, TCP/22, TCP/23, TCP/3389  | Communication for SSH, SFTP, Telnet, RDP    |
| PSM for SSH                        | TCP/1858, TCP/443, TCP/22                    | Communication for SSH, SFTP                 |
| Credential Provider                | TCP/1858                                     | Default port for Credential Provider        |
| OPM                                | TCP/1858                                     | Default port for OPM                        |
| PTA                                | TCP/1858, UDP/1858, TCP/80, TCP/443          | Default port for PTA                        |
| User (Administrator)               | TCP/1858, TCP/3389, TCP/80, TCP/443, TCP/3389| Admin communication                         |
| SMTP Server                        | TCP/25                                       | Email communication                         |
| PSM HTML5 Gateway                  | TCP/3389                                     | Gateway for PSM                             |
| Remote Admin                       | TCP/9022                                     | Remote Administration                       |
| LDAP Integration                   | TCP/389, TCP/636                             | LDAP and LDAPS integration                  |
| CPM to Linux, VMware, Cisco        | TCP/22                                       | SSH communication                           |
| CPM to Windows Targets             | TCP/135, TCP/139, TCP/445                    | Windows RPC and SMB communication           |
| CPM to MYSQL                       | TCP/1521-1526                                | MYSQL communication range                   |
| CPM to Oracle                      | TCP/1433                                     | Oracle communication                        |
| Primary Vault to DR Vault          | TCP/1858                                     | Communication between Vaults                |
| Components to Vault                | TCP/1858                                     | General Vault communication                 |
| Telnet                             | TCP/23                                       | Telnet communication                        |
| RDP                                | TCP/3389                                     | Remote Desktop Protocol                     |
| DNS                                | TCP/53, UDP/53                               | Domain Name System                          |
| RADIUS                             | UDP/1812                                     | RADIUS authentication                       |
| SNMP                               | UDP/161                                      | Simple Network Management Protocol          |
| SNMP Trap                          | UDP/162                                      | SNMP Trap                                   |
| Network Time Protocol (NTP)        | UDP/123                                      | Time synchronization                        |

This table combines information from the CyberArk documentation and the additional ports you listed. It provides a comprehensive overview of the network ports used in the CyberArk environment, including communication between various components and integration with other systems and protocols.