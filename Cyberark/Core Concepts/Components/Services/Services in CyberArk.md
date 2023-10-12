---
aliases: 
tags: 
date created: Tuesday, July 25th 2023, 2:58:05 pm
date modified: Sunday, September 10th 2023, 9:50:40 pm
---

## What Are the [[Windows Service]]s Related to [[PrivateArk Server]]?

- PrivateArk Server Service
- PrivateArk Remote Control Agent Service
- PrivateArk Database Service
- CyberArk Event Notification Engine Service
- CyberArk Hardened Windows Firewall Service
- CyberArk Logic Container Service

	![[Pasted image 20230812130052.png]] #mindmap #important 

## Services Created Needed for Respective Applications

[[CPM]] - CyberArk Password Manager Service and CyberArk Central policy Manager Scanner

*CyberArk Central policy Manager Scanner - Enables the enterprises to detect new machines and scan them in order to provision privileged accounts.*

[[Privileged Session Manager]] - Cyber-Ark Privilege Session Manager Service. 

[[Password Vault Web Access]] - CyberArk Scheduled Task, IIS Admin Service, Windows Process Activation Service and World Wide Web Publishing Service.

![[Pasted image 20230725145236.png]]  
![[iisreset.png]]  
The above command requires admin permissions.

## Process Related Points

### Internet Information Services (IIS)

This web server that runs on Microsoft Windows operating systems. IIS is a crucial component of many web-based applications, and it is necessary to know how to restart IIS when it malfunctions or needs updates. While restarting IIS can be done through the IIS Manager graphical user interface, it can also be performed using the command line interface.

## Disaster Recovery Service