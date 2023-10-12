---
aliases: 
tags: 
date created: Sunday, October 1st 2023, 3:30:48 pm
date modified: Thursday, October 5th 2023, 10:47:21 pm
---

## PVWA

- PVWA is the web interface and a web server  
- PVWA only works on the windows server and cannot be installed on a Linux server  
- its installed near to the user location  
- its a GUI application

 `C:\CyberArk\Password Vault Web Access` - PVWA Environment:

   - Houses PVWA's configuration and environment data.
   - Located outside "Program Files" to avoid potential permission issues in Windows.  

### `C:\inetpub\wwwroot\PasswordVault` - PVWA Web Components:

   - Contains PVWA's web-related files.
   - Sits in the default directory for IIS-hosted web applications, ensuring smooth integration with IIS and streamlined web access.

In short, CyberArk's directory structure for PVWA combines functionality with security and seamless IIS integration.

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

[Explaining the Chain of Trust - Learn What is it & How it Works (thesslstore.com)](https://www.thesslstore.com/knowledgebase/ssl-support/explaining-the-chain-of-trust/)

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

1. **IIS Admin Service (IISADMIN)**
    - Manages the IIS metabase, a repository of IIS configuration settings. Essential for IIS administrative tasks.
2. **Windows Process Activation Service (WAS)**
    - Manages application pool configurations in IIS, ensuring correct routing of HTTP requests to worker processes.
3. **World Wide Web Publishing Service (W3SVC)**
    - Handles HTTP traffic for IIS, making sure IIS-hosted websites are available for web requests.

#### Application Pools

[[application-pools]]
- PasswordVaultWebAccessPool has to be started to ensure that PVWA works, this is created during the installation
- DefaultAppPool has to be started to ensure PVWA actually runs

## PVWA Internal Users

- PVWAAppuser - PVWA app Internal User
- PVWAGWUser - PVWA Gateway Internal User

- `PVWAGWUser` manages external logins (e.g., Administrator, LDAP users).
- `PVWAAppUser` handles internal communications with the vault and other components.

- PVWA is connected to the vault and its mentioned in the `vault.ini` file
- stopping the ISS services will cause the PVWA to not communicate with the vault.
- These internal users will not able to communicate with the vault if the services are stopped.
- via the IIS web server the communication takes place.

## Safes Related to PVWA

### pvwaConfig Safe

![[Pasted image 20230915081537.png]]

#### PVconfiguration.xml

 - main config file for PVWA
 - common for all the PVWA in the infra

## Other Notes

### How to Schedule Reports?

 ![[Pasted image 20230912153247.png]]