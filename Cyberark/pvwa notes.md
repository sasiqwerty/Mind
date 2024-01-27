---
aliases: 
tags: []
date created: Tuesday, September 12th 2023, 2:41:59 pm
date modified: Saturday, January 27th 2024, 7:03:03 pm
---

## Topic Details

#pvwa #classnotes 

1. Session Name : Session 14 [[Password Vault Web Access|PVWA]] 1, session 15 pvwa 2
2. Session Topics : [[Password Vault Web Access|PVWA]] core concepts 
3. Session Date and Time : **11-09-23 Monday**, **12-09-23 Tuesday**
4. **Contents of the video** : The video also contains a mock interview for the vault core files and services.

## PVWA

- PVWA is the web interface and a web server  
- PVWA only works on the windows server and cannot be installed on a Linux server  
- its installed near to the user location  
- its a GUI application

### How Many PVWA?

- with the help of load balancer we distribute the load
- if one is down we direct the traffic to another PVWA

### PVWA Server Requirements

- windows server 2022 is supported

|Small implementation  <br>(<1,000 managed passwords)|Mid-range implementation  <br>(1,000-20,000 managed passwords)|Large implementation  <br>(20,000 – 100,000 managed passwords)|Very large implementation  <br>(more than 100,000 managed passwords)|
|---|---|---|---|
|- Quad core processor (Intel compatible)<br>- 8GB RAM<br>- 2X 80GB SATA/SAS hot-swappable drives<br>- RAID Controller<br>- Network adapter (1Gb)<br>- DVD ROM|- 2X Quad core processor (Intel compatible)<br>- 16GB RAM<br>- 2X 80GB SATA/SAS hot-swappable drives<br>- RAID Controller<br>- Network adapter (1Gb)<br>- DVD ROM|- 2X Eight core processors (Intel compatible)<br>- 32GB RAM<br>- 2X 80GB SAS hot-swappable drives<br>- RAID Controller<br>- Network adapter (1Gb)<br>- DVD ROM|- 4X Eight core processors (Intel compatible)<br>- 64GB RAM<br>- 2X 80GB SAS hot-swappable drives<br>- RAID Controller<br>- Network adapter (1Gb)<br>- DVD ROM|  

### Software Prerequisites

- Windows 2022, Windows 2019, Windows 2016  
- IIS 10.0, 8.5 [[IIS-services]]
- .NET Framework 4.8 - [[dotnet framework]]
- Internet Explorer 11.0  
- SSL certificate is needed
- Microsoft Visual C++ redistributable package - [[visual cpp]]
- PVWA software

#### Miscellaneous Notes

- Chrome (any version released in the last six months on Windows and Linux/UNIX)  
- Firefox (any version released in the last six months on Windows and Linux/UNIX)   
- PVWA can be installed on Amazon Web Services (AWS), Microsoft Azure, and Google Cloud Platforms

### PVWA and ISS

- Every PVWA has one IIS manager installed in its server

### How to Install PVWA?

- Run the prerequisites script  
- Configure the SSL certificate (Import the certificate and Bind the certificate)
- Require SSL option
- PVWA hardening script 

## Services - PVWA

### CyberArk Scheduled Tasks

- Stopping this wont impact the loading of PVWA page
- This is for scheduling the CyberArk reports, automating the report downloading

### IIS Services

These are the services under IIS
1. IIS admin service (IISADMIN)
2. Windows process activation service (WAS)
3. World Wide web publishing service (W3SVC)  

One of the troubleshooting steps for ISS / PVWA issue  
*Note : we need admin privileges to run these commands*

- `iisreset /status` will give us the status of the three services  
- `iisreset` will cause the above mentioned services to restart
- `iisreset /stop` will stop the three services
- `iisreset /start` will start the three services

#### Application Pools

[[application-pools]]
- PasswordVaultWebAccessPool has to be started to ensure that PVWA works, this is created during the installation
- DefaultAppPool has to be started to ensure PVWA actually runs

## PVWA Internal Users

- PVWAAppuser - PVWA app Internal User  
- PVWAGWUser - PVWA Gateway Internal User

- PVWA is connected to the vault and its mentioned in the vault.ini file
- stopping the ISS services will cause the PVWA to not communicate with the vault
- These internal users will not able to communicate with the vault if the services are stopped.
- via the IIS web server the communication takes place.

## How the PVWA URL Will Form?

- during the installation we have provided the installation
- load balancer farm id
- we can login to the particular PVWA using its URL
- we can access the particular PVWA using its URL and its IP address
- when we have multiple PVWA in the infra we can use this step to check what is working and what is not working
- the load balancer contains the URLs of all the PVWA installed in the infra
- the common IP is the called the virtual IP or the load balancer farm id
- having the FQDN we can identify the IP address, we can ping the server with its FQDN also
- each server has its own IP address and we can access the server

**we can access the PVWA using the following values**
1. PVWA FQDN
2. IP address
3. Load balancer farm id  
4. server name  
***Note** : we will not share the individual PVWA URLs to the end user*  
[[ns-lookup]] - `nslookup` `nslookup` is a network administration command-line tool available in many computer operating systems for querying the Domain Name System (DNS) to obtain domain name or IP address mapping or for any other specific DNS record.

when nslookup is used with the load balancer id we get all the ip addresses that the load balancer is handling.

### Problem Identification

- ping all the pvwa IP addresses and see if they are all up and running, another way of doing this is trying to access the individual PVWA urls one after the other and then noting down the one that is not working.
- if one of them is down note that down
- we have to check the logs and see what the issue is
- we use the individual URLs to check if they are working
- if its not loading at the load balancer we have to check that
- the vault can also be down, if the vault is down the PVWA will not work
- if the vault is running but the PVWA is not running we have to test each PVWA individually

## Upgrade Activity for PVWA

**How to perform upgrade for multiple PVWAs**  

*Keep in mind*
- We have to check the CyberArk Security bulletins when they get updated
- based on the security update we have to check if we have to update the components to avoid the vulnerability

*This method is common to all components*

1. We have to install PVWAs near to the users location  
2. we have to talk to change review board, or take the approval from the client if there is no change review board.
3. the upgrading server has to removed out of the Virtual IP or the farm
4. The waves should be planned.

| Component | Old Version | New Version | Region | Change No | Wave No | Execution Date | Status of the Upgrade   |
|-----------|---------|-------------|--------|-----------|---------|----------------|-------------------------|
| PVWA1     | 12.2.4  | 12.2.12     | HKG    |           | Wave 1  | 20-Sep         | Complete / Report Error |
| PVWA2     | 12.2.4  | 12.2.12     | HKG    |           | Wave 2  | 21-Sep         | Complete / Report Error |
| PVWA3     | 12.2.4  | 12.2.12     | LDN    |           | Wave 2  | 21-Sep         | Complete / Report Error |
| PVWA4     | 12.2.4  | 12.2.12     | LDN    |           | Wave 3  | 22-Sep         | Complete / Report Error |
| PVWA5     | 12.2.4  | 12.2.12     | US     |           | Wave 3  | 22-Sep         | Complete / Report Error |
| PVWA6     | 12.2.4  | 12.2.12     | US     |           | Wave 1  | 20-Sep         | Complete / Report Error |

## V9 and V10 Interface for PVWA

- v9 is the older interface, its for the OG users  
- v10 is the newer interface

***Steps to activate v9 interface***
1. Go to Administration in PVWA
2. Go to options
3. Go to general
4. Use v10logonPage : set it to No

This will revert back to the old v9 interface

## Load Balancer Concept

- The end users connect to the load balancer (vip or the load balancer farm id)  
- the the load balancer determines the PVWA they should connect to in a round robin fashion to ensure that the load is distributed evenly.

### Note

- The PVWA and PSM load balancer has a difference, its not easy to distinguish which PVWA is being for a connection but that is possible for the PSM load balancing
- in the case of PSM we have to define which PSM is being used at the platform level but that is not the case for the PVWA.

## PVWA Internal User Suspension and Unsuspension

**if PVWA internal users are suspended how to unsuspend the users?**

- In the starting, while installing the PVWA the safes, PVWA internal users are created and added to the vault.
- The vault IP and port number is stored in the vault.ini file.
- In the vault we have the credentials for the internal users, and in the respective PVWA server we have the cred file for the PVWAAppUser, PVWAGWUser cred files.
- All transactions or commutations will contain cred file during the transaction, if its correct, the transaction is genuine if its not the transaction will not be completed.
- The PVWAGWUser is for external Logins ( Users like Administrator, LDAP users etc.)
- The PVWAAppUser is for internal use ( communication with vault and other components when needed)
- After 5 Incorrect attempts the user gets suspended, this message shows up in the server central administration console, this will also show up in the logs of the respective component.
- In the PVWA page it will show the connectivity status as disconnected. ( if there is only one PVWA in the infra as the PVWA is down we cannot see this setting in the PVWA)

### Steps to Create the CRED File

We have to first check which user is suspended, and then to note the server and its detail login and start the process 

We have to go the component that is not working and its server and stop its services  
	- the IIS services are stopped ( if its a different component, stop its respective services )
- Go to the vault and update the password
- Go to the component server and update the cred file with the password that was updated in the vault, ensure that there is no mistake.
- Its advised to update the password for both the users (PVWAGWUser and PVWAGWUser) and create the cred file.

## Entropy Files

for security entropy files are created, before 12.0 this didn't exist, it was introduced in the version 12  
1. appuser.ini.entropy  
2. gatewayuser.ini.entropy

## Safes Related to PVWA

### pvwaConfig Safe

![[Pasted image 20230915081537.png]]

#### PVconfiguration.xml

 - main config file for PVWA
 - common for all the pvwas in the infra

## Other Notes

### How to Schedule Reports?

 ![[Pasted image 20230912153247.png]]

SMTP integration is called ENE integration