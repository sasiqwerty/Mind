---
aliases: 
tags: 
date created: Saturday, September 30th 2023, 5:01:24 pm
date modified: Saturday, September 30th 2023, 5:01:36 pm
---

## Configure Transparent User Management Using LDAP

This section describes how the PAM - Self-Hosted solution can be configured to communicate with LDAP-compliant directory servers to obtain user identification and security information. This enables automatic user and group provisioning, providing transparent user management.

### Overview

Users are provisioned with their user information (such as full name and email address), and also with their security information such as groups. The latter can provide transparent access control management as users can be given permissions in the Vault based on their LDAP group membership.

In order to maintain a high level of security in the Vault, the security attributes of LDAP user accounts and groups are managed internally.

### LDAP Users and Groups

An LDAP user account is created the first time a user is referenced in one of the following situations:


- The user logs on to the Vault  
- The user is added as a Safe member  
- The user is added as a group member

LDAP groups are created when groups that are defined in one or more external directories are added as Safe owners or as members of a regular group in the Vault.

For more information, see [Manage LDAP users](https://docs.cyberark.com/PAS/Latest/en/Content/PAS%20INST/User-Management-with-LDAP-Introduction.htm).

### Directory Maps

A directory map determines whether a user account or group may be created in the Vault, and according to which criteria. Each map contains a rules list which specifies the users and groups who can access the Vault, and a template which contains the security attributes and authorizations that will be applied when an LDAP user account is created.

During installation, the PAM - Self-Hosted solution creates built-in directory maps for the most common PAM - Self-Hosted solution users. You can use these directory maps immediately, modify them with relevant mapping rules according to your enterprise standards, or create new directory maps.

For more information, see [LDAP integration in V10](https://docs.cyberark.com/PAS/Latest/en/Content/Landing%20Pages/LPLDAPIntegration.htm).

See also: [LDAP Authentication](https://docs.cyberark.com/PAS/Latest/en/Content/PAS%20INST/LDAP-Authentication.htm)

## Authenticate to Privileged Access Manager - Self-Hosted

To work with PAM - Self-Hosted, users must authenticate to the Vault using a predefined authentication method.

This section introduces you to the authentication methods that PAM - Self-Hosted supports and describes how they work.

### General Authentication Considerations

PAM - Self-Hosted supports two layers of authentication, a primary layer and a secondary layer.

The secondary layer is optional and can be set to increase the authentication strength according to your needs.

### Primary Authentication

Primary authentication establishes an initial secure connection between the CyberArk interface and the CyberArk Vault server in order to grant access to users.

The CyberArk Vault supplies the following primary authentication options:

- Amazon Cognito authentication
- CyberArk Password authentication
- LDAP authentication
- NT/Windows authentication
- OpenID Connect (OIDC) authentication
- Oracle SSO (in PVWA)
- PKI authentication (Personal Certificate)
- RADIUS authentication
- SAML authentication

The PVWA can support additional third-party authentication methods. For more information, contact your CyberArk support representative.

### Secondary Authentication

Secondary authentication strengthens the secure connection by adding an additional user identification procedure. This is mainly useful for forcing additional authentication in case of automatic authentication (SSO), such as Windows authentication, PKI authentication or Web SSO.

The following authentication methods can be used as primary authentication methods when applying secondary authentication methods:

- NT/Windows authentication
- PKI authentication (Personal Certificate)
- SAML authentication
- Oracle SSO (in PVWA)
- Amazon Cognito authentication  
The following authentication methods can be used together with the above primary authentication methods as secondary authentication methods:

- LDAP authentication
- RADIUS authentication
- CyberArk authentication

For more information about configuring secondary authentication, see [Configure a secondary authentication method](https://docs.cyberark.com/PAS/Latest/en/Content/PAS%20INST/Defining-Authentication-Methods-in-PVWA.htm#Configur).

## Manage Users and Groups

### Overview

#### Users

When you create users, you can specify permissions and control access for each user such as:

- Assigning a user type, for example, a PWVA or CPM user, and control access to interfaces. For more information, see [User types](https://docs.cyberark.com/PAS/Latest/en/Content/PASIMP/Users-groups-managing-overview.htm?TocPath=Administrator%7CUser%20Management%7CManage%20users%20and%20groups%7C_____0#Types) below.
- Assign a role to a user allowing you to manage their permissions and control tasks that they can perform
- Determine how a user authenticates to an environment
- Assign users to one or more groups

Each user should only be given the permissions that they need to perform their tasks.

Users are generally divided into a hierarchy that mirrors the hierarchy in the office environment. Depending on the permissions granted to users, you can have a User Manager who manages other users who are at the same level or a lower level. The User Manager can create new users and update existing users' properties. This gives User Managers the flexibility to control permissions of users in other departments that are hierarchically beneath them.

For example, the manager of the Engineering department is out of the office for one week. During that week, user permissions for members of that department need to be updated. Using the hierarchy setup, any Department Manager who is above the Engineering department can change the permissions of Engineering department members, and enable the Engineering team to continue working. They don’t have to wait for their own Manager to return to the office to update their permissions.

#### Groups

You can create groups of users that have the same permissions and access to the same Safes.

During PVWA installation, groups that are required for the PVWA are created automatically. For more information, see [The PVWA environment](https://docs.cyberark.com/PAS/Latest/en/Content/PAS%20INST/The-PVWA-Environment.htm)  
Users who are listed in an LDAP-compliant enterprise directory can be added as members of a group and managed transparently by the Vault, depending on their location in the directory. They can also be added as Safe members and given security permissions.

These users benefit from the same permissions as group members created directly in the Vault. For more information, see [Configure transparent user management using LDAP](https://docs.cyberark.com/PAS/Latest/en/Content/PAS%20INST/Configuring-User-Management-via-LDAP.htm).

Depending on how the Vault is configured, users who are members of multiple groups that own the same Safe will either have the permissions of the first group that was added as an owner of a Safe, or a combination of the permissions of all the groups that they belong to,. However, if the user is an independent owner of the same Safe, his own authorizations will override those of the group.

#### How Group Safe Permissions Affect Users that Are in Multiple Groups

If there are users who are members of several groups, and one or more of these groups own the same Safe, the users will either have the permissions of the first group that the user was added to, or a combination of the permissions of all the groups that they belong to. This is determined by the GroupMergeAlgorithm parameter setting in the DBParm.ini file. The parameter can have either of the following settings: