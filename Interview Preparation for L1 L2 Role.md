---
aliases: 
tags: 
date created: Tuesday, January 9th 2024, 1:43:36 pm
date modified: Thursday, January 18th 2024, 10:10:46 am
---

## Infrastructure Breakdown

- Vault and a DR Vault.  
	- DR Vault has a dedicated CPM server that can immediately take over in case of failure. Everything is preconfigured, as the settings cannot be set after the disaster.
- We have 3 CPMs serving the end user, 2 are configured and ready for deployment with minimum business impact.
- 16 PSMs in a load balancer but they are in two different data centers for robustness and redundancy.
- there are 300 safes and roughly the same number of platforms.

## [[Account Discovery and Onboarding|onboarding]]

### Overview

[Add Accounts | CyberArk Docs](https://docs.cyberark.com/PAS/latest/en/Content/PASIMP/Adding-Accounts.htm?tocpath=End%20user%7CPrivileged%20accounts%7CClassic%20Interface%7CAccount%20Management%7C_____1)  
What are the types of devices, accounts and other objects that can be onboarded into [[CyberArk]]? #important 

#### What is Provisioning?

The term is used (sometimes loosely) in a variety of ways in IT, but generally means to make something available for use. Provisioning is an early step in the deployment process and is not to be confused with configuration. Once resources like servers, network components, applications or devices are provisioned, they are then configured according to organizational or user specifications, deployed, managed and maintained over their lifecycle.

#### Introduction

- To Onboard accounts one must be a member of Vault Admins or PVWAAccountsFeedAdmins
	- One must be also a member of the safe and should have the permissions to add account for that safe.
	- All the selected accounts should belong to the same [[Platform]]
	- Any dependencies will be automatically onboarded
	- When onboarding multiple accounts that share the same SSH key, the private SSH key will only be associated with one account. After onboarding, associate all these accounts with the same group so that they can all use the same SSH key.  

#### Methods of Onboarding

There are in total 4 ways of onboarding accounts into [[CyberArk]]

| Provisioning method | Description                                                                                                                                                |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PVWA                | Accounts can be provisioned individually in the vault in the Add accounts page of the PVWA.                                                                |
| Accounts Feed       | The CPM can be configured to scan an organizational network and retrieve a list of accounts and their dependencies                                          |
| Auto Detection      | You can detect and provision accounts automatically providing a full life-cycle automatic management system for privileged accounts and their dependencies |
| Web Service         | You can provision accounts using the AddAccount web service. For more information, refer to REST APIs.                                                     |

### Onboarding Windows and Unix Accounts

1. Accounts that are not yet onboarded that have been discovered would be displayed in the pending accounts page. If multiple accounts are selected the selected number would displayed on the preview page. (This method is using the accounts feed)
	1. Accounts can be individually provisioned using the PVWA
2. if only one is selected the rest are displayed on the preview page.
3. Once the appropriate selection has been made, click on onboard accounts at the bottom of the preview page.
4. Specify the safe name of which the account is going to onboarded in.
	1. If you have to create a new safe, the new safe will be created with the safe template parameters.
5. Assign the platform from the drop down list, with this method only one platform be selected.
	1. Only active platforms are displayed in the list.
	2. We have an option to select automatic password reconciliation and default password option in the settings drop down.
	3. This sets passwords stored in accounts in the Vault, but does not reset actual passwords on target systems. 
6. Click on onboard, the process begins and a window indicates the progress.
7. If the onboarding process is successful

#### SSH Keys

[Accounts Feed | CyberArk Docs](https://docs.cyberark.com/PAS/latest/en/Content/PASIMP/Accounts-Feed.htm#_Ref451331144)

### Keep in Mind

- Only Safes where the user is a member with the Add accounts permission are displayed in this list. 
- When onboarding accounts using PVWA, this process only supports one platform per batch.
- Internal Safes are not displayed in this list.

### Troubleshooting

1. Ensure that the platform is active.
2. Ensure that the safe the account is being onboarded to has the right permissions for the user.
3. When onboarding multiple accounts, ensure that the platform is common to all.
4. Ensure that the account is onboarding to an active platform.

## Authentication Methods in Infra

### [[CyberArk]]

[CyberArk password authentication | CyberArk Docs](https://docs.cyberark.com/PAS/11.1/en/Content/PAS%20INST/CyberArk-Password-Authentication.htm)

### LDAP

[LDAP Authentication | CyberArk Docs](https://docs.cyberark.com/PAS/11.1/en/Content/PAS%20INST/LDAP-Authentication.htm)

### RADIUS

[RADIUS authentication | CyberArk Docs](https://docs.cyberark.com/PAS/11.1/en/Content/PAS%20INST/RADIUS-Authentication.htm)

### SAML

[SAML authentication | CyberArk Docs](https://docs.cyberark.com/PAS/11.1/en/Content/PAS%20INST/SAML-Authentication.htm)

## [[Reports]] And Audits

### PVWA

[Reports in PVWA | CyberArk Docs](https://docs.cyberark.com/PAS/12.6/en/Content/PASIMP/ReportsInPVWA.htm?tocpath=End%20user%7CReports%20and%20Audits%7C_____1)  

Reports can be generated in the Reports page in the PVWA by users who belong to the group that is specified in the ManageReportsGroup Parameter in the reports section of the web access option in the system configuration page by default its the PVWAMonitor group.

The following reports are generated in the PVWA :

#### Privileged Accounts Inventory

- Provides information about all the privileged accounts in the system, based on different filters. Users who have the following authorizations can generate this report:
- List accounts and View Safe members in the Safes that will be included in the report.
- Users who do not have the View Safe members authorization will only be able to view complete information about their own activities.  

| Column              | Description                                                                                 |
|---------------------|---------------------------------------------------------------------------------------------|
| Safe                | The name of the Safe where the privileged account is stored.                                |
| Folder              | The name of the folder where the privileged account is stored.                              |
|                     | This column is not displayed by default.                                                    |
| Name                | The name of the privileged account.                                                         |
|                     | This column is not displayed by default.                                                    |
| PlatformId          | The ID of the platform that is associated with the privileged account.                      |
| DeviceType          | The type of device that the privileged account is allocated to.                             |
| Username            | The name of the user that is authorized to use the privileged account on the remote device. |
| Address             | The address of the remote device where the privileged account is used.                      |
| Group               | The group that the privileged account belongs to, if any.                                   |
| LastAccessedDate    | The date when the privileged account was last accessed.                                     |
| LastAccessedBy      | The name of the last human user who accessed the privileged account.                        |
| LastModifiedDate    | The date when the privileged account was last modified by any user, human or component.     |
| LastModifiedBy      | The name of the last human user who modified the privileged account.                        |
| VerificationDate    | The last date when the privileged account was verified.                                     |
| CheckoutDate        | The last date when the privileged account was checked out.                                  |
| CheckedOutBy        | The name of the last user who checked out the privileged account.                           |
| Age                 | The number of days since the password was created.                                          |
| ChangeFailure       | Whether or not the password in the privileged account could be changed.                     |
|                     | ‘Yes’ indicates that the password change failed                                             |
| VerificationFailure | Whether or not the password in the privileged account could be verified.                    |
|                     | ‘Yes’ indicates that the password change failed                                             |
| MasterPassFolder    | The folder where the master account associated with the current usage is stored.            |
|                     | This column is not displayed by default.                                                    |
| MasterPassName      | The name of the master account associated with the current usage.                           |
|                     | This column is not displayed by default.                                                    |
| DisabledBy          | Whether the privileged account was disabled by a human user or by the CPM.                  |
|                     | This column is not displayed by default.                                                    |
| DisabledReason      | The reason why the privileged account was disabled.                                         |

#### Applications Inventory

Provides information about the application IDs in the system, based on different filters. Users who have the following authorizations in the Vault can generate this report: **Audit Users**  
Users can generate this report for users in the same level or lower in the Vault hierarchy.

| Column                  | Description                                                                                                                                                                                      |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Default columns:        |                                                                                                                                                                                                  |
| Application ID          | The unique ID of an application defined in the Vault.                                                                                                                                            |
| Business owner          | The full name of the application’s business owner.                                                                                                                                               |
| Location                | The location of the application in the Vault’s hierarchy.                                                                                                                                        |
| Allowed machines        | A list of machines that are defined in the Vault for the listed application and from where the application can request a privileged account.                                                     |
| OS User/s               | A list of OS users that are defined in the Vault for the listed application and can request a privileged account.                                                                                |
| Path/s                  | A list of paths that are defined in the Vault for the listed application and from where the application can request a privileged account.                                                        |
| Optional columns:       |                                                                                                                                                                                                  |
| Application description | A description of the application requesting the privileged account.                                                                                                                              |
| Business owner email    | The email address of the application’s business owner.                                                                                                                                           |
| Business owner phone    | The phone number of the application’s business owner.                                                                                                                                            |
| Disabled                | Whether or not the application’s Vault definition is disabled.                                                                                                                                   |
|                         | If the application is disabled in the Vault, ‘Yes’ is displayed. If not, ‘No’ is displayed.                                                                                                      |
| Hash                    | A list of unique hash values that has been created by the Secrets Manager Credential Providers utility to enable the application to authenticate to the Vault and retrieve a privileged account. |
| Access permitted        | The date from when and until when the application is permitted to access the privileged account.                                                                                                 |
| Expiration date         | The date when the application’s Vault definition expires.                                                                                                                                        |

#### Privileged Accounts Compliance Status

Accounts compliance and management status. Users who have the following authorizations can generate this report:

The following permissions are required in the Safes that will be included in the report:  
List passwords/files  
View Audit or Confirm Safe request – in Safes that are configured for dual control  
Membership in the following group: PVWAMonitor  
To enable users to run this report for the entire system, add them as members to the following group: Auditors

#### Entitlement Report

#### Activity Log

### [[PrivateArk Client]]

[Reports in PrivateArk | CyberArk Docs](https://docs.cyberark.com/PAS/12.6/en/Content/PASIMP/ReportsInPrivateArkClient.htm?TocPath=End%20user%7CReports%20and%20Audits%7C_____2)

## Master Policy

The Master Policy offers a centralized overview of the security and compliance policy of privileged accounts in your organization while allowing you to configure compliance driven rules that are defined as the baseline for your enterprise. It is configured out-of-the-box and can be used immediately after implementation, providing an intuitive, simplified user experience and enhanced bottom-line insight for administrators, IT personnel, managers and auditors.

The Privileged Access Manager - Self-Hosted solution separates higher-level and compliance driven policy rules such as privileged access workflows, account management and session monitoring requirements from technical settings that determine how the policy will be carried out on each platform.

The Master Policy groups together sets of rules and offers better visibility and control over policy configurations and enforcement. Each policy rule has basic settings and, sometimes, advanced settings that are displayed when you select the rule, as well as context-sensitive help that explains each rule and its interdependency on other rules.

Although the Privileged Access Manager - Self-Hosted solution’s Master Policy can be applied to most privileged accounts in your organization, you can create rule exceptions to manage specific workflows. For example, you can define a dual control workflow for highly sensitive accounts on a specific platform that require permission from authorized users before they can be used, while access to other accounts in the organization does not require such confirmation.

The Master Policy defines basic system behavior for the entire lifecycle of privilege account management and access.

| Concept | Description |
| ---- | ---- |
| Basic Policy Rules | Basic policy rules allow you to define specific aspects of privileged account management. These rules include several groups of policy rules for the access workflow, management of passwords, session monitoring and auditing. |
| Advanced Policy [[Rules]] | Some policy rules have related advanced settings. For example, in the basic policy rules you can determine whether users will be allowed to transparently connect to target systems using ‘Click to Connect’. In the related advanced settings, you can determine whether users will also be able to view passwords. |
| Exceptions | The Master Policy model introduces the ability to define Exceptions. These are policy rules that differ from the overall Master Policy for a specific scope of accounts, for example accounts associated with a specific platform. Each exception contains the basic policy rule as well as its related advanced settings. For example, the Master Policy may define that Dual Control is disabled in the organization. However, the Windows PCI production servers require Dual Control to be enabled because of their higher sensitivity. You can make this allowance by creating an exception to the Dual Control rule that enables Dual Control enforcement on the scope of Windows PCI production servers platform. |                                      
In the Platform Management settings, the IT administrator can configure technical settings defined by your organization’s environment and security policies to control how the system manages accounts on various platforms. Most of these settings have default values that do not need to be changed, but certain specific features need to be set according to your organizational requirements.

### Privileged Access Workflows

| Workflow | Description |
| ---- | ---- |
| Require Dual Control Access Approval | Users require approval from authorized users before they can access passwords. |
|  | Advanced Settings : Multiple User Approval, Direct Manager Approval, Number of Authorized users to confirm requests. |
| Enforce Check-in/Check-out | Users can check out an account and lock it so that no other user can retrieve at the same time. After the user has used the password, they can check the password back into the vault. |
| Enforce One Time password Access | Accounts can be retrieved for one time use only, and the password stored inside must be changed after each use before the account is released and can be used again. By default this rule is inactive. |
| Allow EPV Transparent Connections ('Click to Connect') | users can connect to remote devices without needing to know or specify the required password. |
| Require Users to specify reason for access | Users can only retrieve accounts after they specify a reason for access. |

### Password Management

| Password Settings | Description |
| ---- | ---- |
| Require Password Change every X days | The Master Policy determines how frequently passwords must be changed. By default, passwords are changed every 90 days. You can see when password changes are planned in the Compliance Report. |
| Require Password Verification every X days | Passwords will be verified after the timeframe specified in the previous rule. They can be changed manually or replaced by a unique and highly secure password that is randomly generated by the Password Vault. By default, passwords are verified every 7 days. |

### Session Management

### Audit

## [[Safe Management and Access Provisioning]]

## [[Platform Management]]

## Classic Interface

[Classic Interface | CyberArk Docs](https://docs.cyberark.com/PAS/latest/en/Content/Landing%20Pages/LPVersion9Interface.htm?tocpath=End%20user%7CPrivileged%20accounts%7CClassic%20Interface%7C_____0)