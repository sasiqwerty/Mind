---
aliases: CPM, Central Policy Manager
tags:
date created: Tuesday, July 25th 2023, 1:12:59 pm
date modified: Thursday, September 28th 2023, 3:54:59 pm
---

## Introduction

The Central Policy Manager (CPM) is a component of CyberArk Privileged Access Manager (PAM) that manages and enforces password policies for privileged accounts. It is responsible for:

- Automatically changing passwords on remote machines according to the organizational policy.
- Storing the new passwords in the Enterprise Password Vault (EPV).
- Enforcing password complexity and expiration policies.
- Reporting on password usage and compliance.

The CPM can be installed on a dedicated machine or on a server that is already running other CyberArk components. It is a critical component of the PAM solution and helps to ensure that privileged accounts are secure and compliant.

Here are some of the benefits of using the Central Policy Manager:

- **Automated password management:** The CPM can automatically change passwords on remote machines, which frees up IT administrators to focus on other tasks.
- **Password compliance:** The CPM can enforce password complexity and expiration policies, which helps to protect privileged accounts from unauthorized access.
- **Reporting:** The CPM can generate reports on password usage and compliance, which can help organizations to identify and address security risks.

If you are looking for a way to manage and enforce password policies for privileged accounts, the Central Policy Manager is a valuable tool. It can help to improve the security of your organization's privileged access and reduce the risk of unauthorized access.

Here are some of the default safes in the CPM environment:

- **PasswordManager_info:** This safe is used for internal processing during auto-detection activities and should not be accessed by users.
- **PasswordManager_ADInternal:** This safe contains the Active Directory credentials that are used by the CPM to connect to Active Directory.
- **PasswordManager_LinuxInternal:** This safe contains the Linux credentials that are used by the CPM to connect to Linux systems.

## Functions of CPM

- CPM has cred file and the vault has the password.
- Password Manager is an account that can access the [[Vault]] and make do Reconciliation, password change and recovery activities.
- CPM 
- We can install more than one [[CPM]].