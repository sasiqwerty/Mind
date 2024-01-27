---
aliases: 
tags: 
date created: Thursday, August 31st 2023, 7:20:28 am
date modified: Saturday, January 27th 2024, 6:59:00 pm
---
#31-08-23 #classnotes #sentry-course 

[CyberArk Vault Structure | CyberArk Docs](https://docs.cyberark.com/PAS/latest/en/Content/PASIMP/CyberArk-Vault-Structure.htm?tocpath=Administrator%7CComponents%7CDigital%20Vault%7CAdvanced%20Digital%20Vault%20Environment%7CCyberArk%20Vault%20Structure%7C_____0)

## Vault Server Specs

- based on number of [[Privileged Account]] accounts  
- vault server specifications  
- what is cloud server?

[Vault Specifications | CyberArk Docs](https://docs.cyberark.com/PAS/Latest/en/Content/PASREF/Vault%20Specifications.htm)  
![[vault-specs (2).svg]]  
[[vault specifications]]

## Vault Installation Prerequisites

- windows server 2016/2019
- .Net Framework 4.8 or higher
- Vault software
- Master CD
- Operator CD
- Server Key
- License file  
![[Zoom_OJfMRzBmHL.png]]  

### Notes

#### Windows Server

- windows 2012 is not supported anymore for vault installation 

#### Third Party Apps

- avoid installing 3rd party applications, its strictly not allowed  
- not installing 3rd party applications also enhances safety and performance  
- CyberArk team wont support when contacting CyberArk with a problem with 3rd party apps are installed in the vault server

#### Vault Server Location

- vault is not domain joined, if its domain joined the group policies are applicable to the vault also which is not a good idea  
- the vault only accepts data from 1858 port  
- the vault will not talk to other servers  
- the vault will function based on certain security mechanism  
- hence vault is not added under the domain

What are the vault prerequisites? its an important interview question

PAkeygen - used to generate keys like server keys and other stuff

## Group Policy

every server has its own local policies  
manage all the server with one policy - its called group policy

## Vm Snapshots

A VM (Virtual Machine) snapshot is a feature provided by virtualization software that captures the current state of a virtual machine. It is similar to taking a photograph of the VM at a specific point in time. This "photograph" includes:

1. **Memory state**: The contents of the VM's RAM.
2. **VM settings**: Configuration details of the VM, like network settings, CPU allocation, etc.
3. **Disk state**: The current state of the VM's virtual disk.  

[[VM Snapshots|snapshot]] - notes from chatgpt

## [[Data Encryption Flow]]

Data encryption starts with the Server Key, which encrypts the Vault Key. The Vault Key, in turn, protects the Safe Key. This Safe Key encrypts the Object Key, which finally safeguards the Sub Object Key.  
![[Pasted image 20230831112955.png]]

## Vault - Services

![[Zoom_ccqtBFDjOQ 2.png]]  
this is very very important  
there are 3 vault services with the name PrivateArk  
there are 3 services with the CyberArk name ( why is it different? )

what is the log on as? part in the services what is its purpose?  
use the search name method instead of manual search

### PrivateArk Server Service

- The PrivateArk Server is the primary service of the vault. Restarting it will cause the ENE to halt, as the ENE is dependent on the PrivateArk server service. To implement any changes, the vault must be restarted.
- The PrivateArk Server operates as a Windows service. Depending on the Server's key configuration, this service can either start automatically or be initiated manually.
- The [[PrivateArk Server]] console is for troubleshooting, starting and stopping of vault.

### PrivateArk Database Service

- core service, data is accessed as this service is running, if its down the PrivateArk server also wont start
- if the database is suddenly stopped the PrivateArk server will stop too and cause a sudden shock! its not recommended, it might cause database corruption.
- there is some dependency with the PrivateArk database and logic container and when the database is stopped he logic container is also stopping

### PrivateArk Remote Control Agent Service

- remote access, remote monitoring
- it can be considered as optional service, shutting it off will not cause any problem
- non-essential service

### CyberArk Logic Container Service

- very important for the vault
- the master policy is defined, that is executed by the logic container
- if policy issue arises there are related logs that we should look at
- platform level stuff is handled by the CPM
- Master policy level is handled by CyberArk logic container
- The Logic Container is a service in the Vault that is responsible for running application logic for reading/writing to the Vault database. This logic is part of any API request (initiated by an action in the PVWA UI or directly by a script).

### CyberArk Event Notification Engine Service

- the notifications are sent in the form of emails
    - password expiry is sent
    - user requests for login are sent
    - dr user is stopped
    - component services are stopped
- mail based services are managed by the event notification engine in CyberArk
- PTA notifications are not handled directly but have to configured.

### CyberArk Windows Hardened Firewall Service

- never stop the service, ever, in real time environment
- windows server has windows firewall, but during hardening the windows firewall service will convert into CyberArk service now there is no windows firewall service.
- inbound and outbound is restricted.
- only 1858 port is allowed after the firewall is hardened.
- stopping means reducing security.


local account is created to handle the connections and then added to CyberArk and then accessed via RDP  
we create an account in the vault server and that is onboarded, only then it is accessed  
the audit data has to be maintained


![[Zoom_26fE31YoNa 2.png]]

![[Zoom_uMlVsgNtZE.png]]



![[Zoom_4PvmDFsPsW.png]]



![[Zoom_dyCyf2F33d.png]]