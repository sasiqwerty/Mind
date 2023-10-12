---
aliases: PVWA
tags: 
date created: Tuesday, July 25th 2023, 12:48:31 pm
date modified: Thursday, August 3rd 2023, 2:38:37 pm
---

## Introduction

The Password Vault Web Access (PVWA) is a web-based interface that allows users to access and manage privileged accounts in CyberArk Privileged Access Manager (PAM). The PVWA provides a centralized location for users to find and use passwords for applications, servers, and other resources. It also includes features for managing and auditing access to privileged accounts.

The PVWA can be used by both administrators and end users. Administrators can use the PVWA to manage the configuration of PAM, create and manage privileged accounts, and audit access to privileged accounts. End users can use the PVWA to find and use passwords for applications and resources.

The PVWA is a secure way to access and manage privileged accounts. It uses a variety of security features to protect passwords, including:

- **Strong encryption:** Passwords are encrypted in transit and at rest.
- **Multi-factor authentication:** Users must provide multiple pieces of identification to access the PVWA.
- **Role-based access control:** Users are only allowed to access the resources that they are authorized to access.
- **Auditing:** All access to the PVWA is logged, so that administrators can track who has accessed what and when.

The PVWA is a valuable tool for managing privileged accounts. It provides a secure and centralized way for users to access and manage passwords. The PVWA also includes features for managing and auditing access to privileged accounts, which can help to protect organizations from security breaches.

Here are some of the specific uses of the Password Vault Web Access:

- **Accessing privileged accounts:** The PVWA allows users to access privileged accounts without having to know the passwords themselves. This is done by using a single master password to unlock the PVWA, which then provides access to all of the privileged accounts that the user is authorized to access.
- **Managing privileged accounts:** The PVWA allows administrators to manage privileged accounts, such as creating new accounts, changing passwords, and disabling accounts.
- **Auditing privileged account access:** The PVWA can be used to audit privileged account access, which can help to track who has accessed what and when. This can be useful for investigating security breaches or for simply tracking how privileged accounts are being used.

Overall, the Password Vault Web Access is a powerful tool for managing privileged accounts. It provides a secure and centralized way for users to access and manage passwords, and it also includes features for managing and auditing access to privileged accounts.

## Interface

![[Pasted image 20230803142441.png]]

## Functions of [[Password Vault Web Access|PVWA]]

- [[Account Discovery and Onboarding]]
- [[Platform]] Management
- [[Master Policy]] Management 
- Account Access 
- Activating [[Privileged Session Manager]]
- 

## Application Interface

There are two authentication methods to access the site
- LDAP Authentication
- CyberArk Authentication

### Accounts View

![[Pasted image 20230803142531.png]]

### Policies

![[Pasted image 20230803142621.png]]  
![[Pasted image 20230803142707.png]]

### Security Events

![[Pasted image 20230803142813.png]]  
![[Pasted image 20230803142845.png]]

### User Provisioning

![[Pasted image 20230803142936.png]]

#### Configuration Options

![[Pasted image 20230803143010.png]]

##### Options

![[config settings.png]]

##### Safe Templates

![[Pasted image 20230803143538.png]]

##### [[LDAP Integration]]

![[Pasted image 20230803143650.png]]

##### Notification Settings

![[Pasted image 20230803143755.png]]

##### Endpoint Privilege Manager Policy

![[Pasted image 20230803143837.png]]

### Ad-Hoc Connection

An ad hoc connection is a type of wireless network that is created between two or more devices without the use of a wireless access point (AP). Ad hoc networks are often used in temporary or emergency situations, such as when there is no existing wireless infrastructure available.

*To create an ad hoc connection, each device must be configured to use the same wireless network name (SSID) and security settings. Once the devices are configured, they can be connected to each other by selecting the ad hoc network from the list of available networks on each device.*

Ad hoc networks are often used for file sharing, gaming, or other peer-to-peer applications. They can also be used to connect to the internet if one of the devices is connected to a wired network.

### Add Account

### System Health Page

**Vaults** - This tab contains information about the primary vault and disaster recovery vault, informs the user about its current status.
- The IP address is also mentioned.

**Web Portal** - This tab contains information about the number of [[Password Vault Web Access]] portals installed and its active users.

**PSM and PSM for SSH** - This tab contains information about the number of PSMs installed and the active concurrent sessions.

**CPM and Account Discovery** - This tab contains information about the number of CPMs installed and its managed accounts and their number.

**PTA** - This tab contains the information about the number of PTAs installed and their active issues.

## Other Points of Importance

We cannot login into [[PrivateArk Client]] and [[Password Vault Web Access]] at the same time. We have to logout of one to login into the other place.