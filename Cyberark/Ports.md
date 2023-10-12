---
aliases: 
tags: 
date created: Monday, July 31st 2023, 5:25:40 pm
date modified: Wednesday, September 13th 2023, 10:22:39 pm
---

## Introduction

389Port numbers are used to identify specific network services and applications on a device, and their assignments are managed by IANA (Internet Assigned Numbers Authority) through the Service Name and Transport Protocol Port Number Registry.  
![[Pasted image 20230803185943.png]]

## Ports and Their Popularity

### Well-Known Ports

Well-Known Ports (0-1023): Reserved for standard services like HTTP (port 80), HTTPS (port 443), FTP (port 21), etc.  

### Registered Ports

Registered Ports (1024-49151): Assigned to various applications and services by IANA or a designated authority.  

### Dynamic/Private Ports

Dynamic/Private Ports (49152-65535): Available for general use by applications, but not officially assigned by IANA

## CyberArk [[Ports]]

Remote Admin Port - 9022  
LDAP Integration Port - 389  
LDAPS port - 636  
CPM to Linux,Vmware hosts,Cisco devices :22  
CPM to Windows Targets: 135 139 445  
CPM to MYSQL:1521-1526 Range  
CPM to Oracle:1433  
Primary Vault to DR Vault:- 1858  
Components to Vault:-1858  
SSH + SFTP (but can be configured anywhere):-22  
Telnet:-23  
RDP:-3389  
LDAP:-389 and 636  
DNS:-53  
RADIUS:-1812  
SNMP:-161  
SNMP Trap:-162  
Network Trap(NTP):-123  
CPM to Targets: 135 139 445 22 1433 1521 etc