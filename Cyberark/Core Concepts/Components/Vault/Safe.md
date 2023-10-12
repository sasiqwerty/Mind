---
aliases: 
tags: 
date created: Tuesday, July 25th 2023, 8:10:55 pm
date modified: Monday, August 28th 2023, 1:00:30 pm
---
In CyberArk, a Safe is a logical container that stores privileged accounts and their passwords. Safes can be used to organize accounts according to your organization's requirements, such as by department, operating system, or application. They can also be used to control access to accounts, by granting different permissions to different users.

*Safes are located inside the [[Vault]].*
- Safes can be created inside the vault directly or by using the [[Password Vault Web Access]] component.
- Each user will only see the accounts that are in Safes to which he or she has been.

For example, you could create a Safe for all of your Windows accounts, and give the IT department permission to view and modify the accounts in the Safe. You could then create a separate Safe for all of your Unix accounts, and give the security team permission to view and modify the accounts in that Safe.

Safes are an important part of CyberArk's Privileged Access Management (PAM) solution. They help to secure privileged accounts by centralizing their storage and control. This makes it easier to manage and rotate passwords, and to track who has access to what accounts.

- Safes can contain any type of privileged account, including Windows accounts, Unix accounts, database accounts, and application accounts.
- Safes can be nested, which means that you can create a Safe within another Safe. This can be useful for organizing accounts into more complex hierarchies.
- Safes can be assigned to users or groups. This allows you to control who has access to the accounts in the Safe.
- Safes can be configured to store different types of data, such as passwords, SSH keys, and certificates.

## Process Related Points

- safes can store around a theoretical maximum of 300k passwords.
- In the interest of performance its advisable to store around 20k to 30k password objects in a single safe, when the value exceeds its ok to create another safe. The total number of password objects can get quite large as history of old passwords is saved as their versions.

## Platforms and Safe - The relation

## Safe Authorizations/Permissions for the Users in [[PrivateArk Client]]

![[add-safe-member-authorizations.png]] #mindmap 


![[Pasted image 20230811202213.png]]  
![[safe-operations.png]] #mindmap 

## Safe Authorizations/Permissions for the Users in [[Password Vault Web Access]]

## [[CyberArk]] Documents

### Safes and Safe Members

This topic describes Safes and Safe members, and how authorizations affect access to a Safe or the actions that can be performed to Safes, Safe members, and accounts.

### Safes Overview

Safes enable you to store and organize authorized user accounts according to your organization's requirements. For example, you can create a Safe for each department such as Finance or HR, and store the accounts for that department in the relevant Safe. Or you can create Safes for accounts based on operating systems such as Windows or Unix.

Organizing accounts in different Safes enables you to limit access to accounts. For example, only the administrator of Windows accounts would have access to the Windows accounts Safe, and only the administrator of the Unix accounts would have access to the Unix accounts Safe.

Users who have the relevant permissions can add Safes in the PVWA and modify their properties, as well as manage Safe members and their permissions.

The entire account management process benefits from all the security and tracking features of the Vault.

### Safe Members Overview

Authorized users with the relevant permissions have access to Safes and accounts. Each user is a member of a Safe and is assigned a specific set of permissions. Permissions give you the flexibility to grant different permissions to different users. For example, some users can only view an account, while others can modify an account's properties or perform tasks on accounts and files in a Safe.