---
aliases: 
tags: 
date created: Tuesday, September 19th 2023, 7:12:24 am
date modified: Saturday, January 27th 2024, 6:59:26 pm
---
IIS - TLS Settings  
cpm server specifications

Also used in Just In Time in step 3 and 5  
plugin manager user - supports different platforms

## PluginManagerUser

The PluginManagerUser role in CPM CyberArk is a local Windows Service user that is created during the CPM hardening process. It is used to run CPM plugins, which are used to connect PAS to target machines in order to manage passwords.

PluginManagerUser is a privileged account, so it is important to keep it secure. The password for PluginManagerUser is stored in the CPM_Accounts Safe in the Vault.

### Here Are Some Examples of Tasks that PluginManagerUser is Used For:

- Installing and configuring CPM plugins
- Running CPM plugins to manage passwords on target machines
- Generating reports from CPM plugins

### PluginManagerUser is also Used to Run the following CPM Services:

- CPM Plugin Service
- CPM Agent Service
- CPM Connector Service

## ScannerUser

The ScannerUser role in CPM CyberArk is a local Windows Service user that is created during the CPM installation process. It is used to run the CPM Scanner service, which is responsible for discovering and scanning target machines for privileged accounts.

The ScannerUser account is a privileged account, so it is important to keep it secure. The password for ScannerUser is stored in the CPM_Accounts Safe in the Vault.

Here are some examples of tasks that ScannerUser is used for:

- Discovering and scanning target machines for privileged accounts  
- Collecting information about privileged accounts, such as passwords, permissions, and usage history  
- Generating reports on privileged accounts  
ScannerUser is also used to run the following CPM services: CPM Scanner Service

## Latest Version

The latest version of CyberArk Privileged Access Manager (PAM) is **13.2.3**, released in August 2023.  
Release notes have the updates.

Enhancement Request - 

## CyberArk Password Manager Service

## Default Safes for CPM

These three safes are shared between all the CPMs in the infra  
- Shared  
- Temp  
- Pending

PasswordManager - the safe gets created

CPM.ini - main configuration File for CPM  
![[Pasted image 20230919075204.png]]

![[Pasted image 20230919075544.png]] - pending accounts are stored in password Manager pending safe  

![[Pasted image 20230919080851.png]]