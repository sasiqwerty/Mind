---
aliases: Reconcile
tags: 
date created: Saturday, July 29th 2023, 4:57:20 pm
date modified: Saturday, July 29th 2023, 5:01:56 pm
---

## Overview

Passwords in the Vault must be synchronized with corresponding passwords on remote devices to ensure that they are constantly available. Therefore, the CPM runs a verification process to check that passwords are synchronized. If the verification process discovers passwords that are not synchronized with their corresponding password in the Vault, the CPM can reset both passwords and reconcile them. This ensures that the passwords are resynchronized automatically, without any manual intervention.

The platform contains rules that determine whether automatic reconciliation will take place when a password is detected as unsynchronized, or whether it is launched only through a manual operation by an end user/system admin. A reconciliation account password that will be used to reset the unsynchronized password can be defined either in the platform or at account level. We strongly recommend that you store this account in a separate Safe, where it is only accessible to the CPM for reconciliation purposes.

During password verification, the CPM plug-ins return a list of predefined errors to the CPM. Each platform specifies the specific errors that will launch a reconciliation process for passwords linked to that platform. This enables each enterprise to specify its own prompts for reconciling passwords and gives maximum flexibility to individual needs.

During password reconciliation, the unsynchronized password is replaced in the Vault and on the remote device with a new password that is generated according to the relevant platform. As soon as reconciliation is finished successfully, all standard verifications and changes can be carried out as usual. Users can see details of the last reconciliation process in the Operational Views in the Accounts List.

## Define a Reconciliation account Password

Define a reconciliation password at either of the following levels:

- Platform – All accounts attached to a specific platform will use the reconciliation account password specified in the platform. For more information, refer to Reconcile passwords.  
- Account – A reconciliation account password can be defined at account level and will override the account specified in the platform.  
Define a Reconciliation Account Password

## Reconcile a Password Automatically

Users who belong to the Vault Admins group can configure password verification processes in the platform settings page. The Vault Admins group must be an owner of the CPM Safe with the following authorizations:

- Retrieve accounts (files)  
- Update password (file) value  
Reconcile a Password Automatically  
For more information about these parameters, refer to Reconcile passwords, in Automatic Account Management.

## Reconcile a Password Manually

Although password reconciliation processes can be scheduled to take place automatically at regular intervals, a reconciliation process can also be initiated manually in the PVWA by users who have the following Safe member authorizations:

- Initiate CPM password management operations  
Users who belong to the Vault Admins group can configure password reconciliation processes in the platform settings page. The Vault Admins group must be an owner of the CPM Safe with the following authorizations:

- Retrieve accounts  
- Update password value

#website  
[Reconcile Password | CyberArk Docs](https://docs.cyberark.com/PAS/Latest/en/Content/PASIMP/Reconciling-Passwords.htm#Defineareconciliationaccountpassword)