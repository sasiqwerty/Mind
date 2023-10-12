---
aliases: 
tags: 
date created: Monday, July 31st 2023, 10:52:54 am
date modified: Wednesday, September 27th 2023, 9:59:35 am
---

## What is CyberArk?

The PAM suite or Privileged access management suite, manages privileged accounts. Accounts of elevated privileges are always susceptible to attacks hence they need secure access. The software suite ensures that all the processes run on a [[Zero Trust]] concept. 

## [[Core Components of CyberArk]]

These are the core components of the CyberArk Privileged Account Management Suite
- [[Password Vault Web Access]] Interface
- [[Vault]]
- [[CPM]]
- [[Cyberark/Core Concepts/Components/Privileged Threat Analytics/Privileged Threat Analytics]]
- [[Privileged Session Manager]]
- [[Privileged Session Manager for SSH]]

### [[Password Vault Web Access]] Interface

#### Introduction

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

### [[Vault]]

### [[CPM]]

#### Introduction

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

### [[Cyberark/Core Concepts/Components/Privileged Threat Analytics/Privileged Threat Analytics]]

### [[Privileged Session Manager]]

### [[Privileged Session Manager for SSH]]