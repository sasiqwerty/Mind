---
aliases: account types
tags: 
date created: Thursday, August 3rd 2023, 11:03:28 am
date modified: Thursday, August 3rd 2023, 3:25:34 pm
---

## Domain Accounts

A Windows domain account is a user account that is stored in Active Directory, a directory service that is used to manage users, computers, and other resources in a Windows domain. Domain accounts allow users to access resources and services on any computer in the domain, regardless of where the computer is located.

Domain accounts are more secure than local accounts because they are centrally managed in Active Directory.

## Meta Accounts and Typical Accounts

**Meta accounts in CyberArk** are special accounts that are used to manage other accounts in CyberArk. They have the ability to create, modify, and delete other accounts, as well as view and manage their secrets. Meta accounts are typically used by administrators to manage the CyberArk environment. 

> *Accounts that are owned by the Vault Administrators and that are used by CyberArk PAM to manage other accounts.*  

**Typical accounts** are used to access resources, such as applications, servers, and databases. They have a specific set of permissions that allow them to perform specific tasks. 

> It is an account that is owned by an IT team and as such our Vault Administrators do not need to know the password or have access to it.

|Feature|Typical Account|Meta Account|
|---|---|---|
|Purpose|Used to access resources|Used to manage other accounts|
|Permissions|Specific set of permissions|Ability to create, modify, and delete other accounts, as well as view and manage their secrets|
|Usage|By users to access resources|By administrators to manage the CyberArk environment|

