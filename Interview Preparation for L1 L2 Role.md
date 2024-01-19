---
aliases: 
tags: 
date created: Tuesday, January 9th 2024, 1:43:36 pm
date modified: Thursday, January 18th 2024, 10:20:24 pm
---

## CyberArk Infrastructure Breakdown

### General Infrastructure Overview

| Component            | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| Server Distribution  | 70% on-premises, 30% in the cloud (for testing and validation)               |
| Authentication       | CyberArk with LDAPS (port 636), also unencrypted port 389 available          |
| Failover Standards   | Adheres to fail back and fail over standards to protect data integrity      |
| Accounts & Safes     | Approximately 70,000 accounts, 300 safes, and similar number of platforms   |

### Vault Configuration

| Component | Description                                                                         |
|-----------|-------------------------------------------------------------------------------------|
| Main Vault| Located on-premises                                                                 |
| DR Vault  | In a different location for Disaster Recovery (DR)                                  |
| CPM for DR| Dedicated Central Policy Manager (CPM) connected for DR failover                   |
| DR Drill  | Performed quarterly with full system backup prior to the drill                     |

### Password Vault Web Access (PVWA)

| Component    | Description                                                                      |
|--------------|----------------------------------------------------------------------------------|
| PVWA Count   | 6 PVWAs, with additional 2 on standby for emergencies                            |
| Load Balancer| F1 load balancer, distributed across 2 data centers in a round-robin configuration|
| Cloud PVWAs  | Additional PVWAs in the cloud for resilience testing                             |

### Central Policy Manager (CPM)

| Component | Description                                                |
|-----------|------------------------------------------------------------|
| CPM Count | 3 active CPMs, 2 backup CPMs, and 1 connected to DR Vault  |

### Privileged Session Manager (PSM)

| Component | Description                                                                                     |
|-----------|-------------------------------------------------------------------------------------------------|
| PSM Count | 16 PSMs connected to F1 load balancer, operating in a round-robin fashion for session management|

### Privileged Session Manager for SSH (PSMP)

| Component | Description                                      |
|-----------|--------------------------------------------------|
| PSMP Count| 4 installed PSMPs, with 1 additional for backup  |

This table format simplifies the understanding of the CyberArk implementation, focusing on the key components and their roles in the infrastructure.

## [[Account Discovery and Onboarding]]

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

## PVWA Reports

### Report Types

Based on the CyberArk documentation for version 12.6, here's more information about the five types of reports that can be generated in the Password Vault Web Access (PVWA):

1. **Privileged Accounts Inventory**: This report provides comprehensive information about all privileged accounts in the system. It includes details such as the Safe where the account is stored, the folder, account name, platform ID, device type, username, address, group, dates of last access and modification, and other relevant information. It's useful for understanding the distribution and status of privileged accounts across your organization.

2. **Applications Inventory**: This report offers information about application IDs in the system, covering aspects like the application ID, business owner, location in the Vault’s hierarchy, allowed machines, OS users, and paths from where the application can request a privileged account. It's crucial for managing and auditing applications that interact with privileged accounts.

3. **Privileged Accounts Compliance Status**: This report focuses on the compliance and management status of accounts, providing insights into aspects like target system user name and address, Safe name, platform name, compliance status, non-compliance reasons, expiration due dates, change mode, and more. It helps in ensuring that privileged accounts adhere to internal and external compliance requirements.

4. **Entitlement Report**: This report covers users’ entitlement rights in PAM - Self-Hosted. It includes details about the user or group, full name, group membership, location in the Vault hierarchy, user type, target platform name, system, account, Safe, object name, folder name, and permissions like read, use, change, among others. This report is essential for reviewing and managing user access rights and entitlements.

5. **Activity Log**: The Activity Log report records activities performed in the Vault, including time, user, action, Safe, target account, platform, system, and additional details regarding the activity. This report is pivotal for audit trails and understanding user actions within the Vault.

These reports are instrumental in managing, auditing, and ensuring compliance in environments where privileged access is critical. They provide deep insights into various aspects of privileged account management, from inventory and compliance to user entitlements and activity monitoring.

Generating, configuring, and managing reports in the Password Vault Web Access (PVWA) in CyberArk involves a series of steps as described in the CyberArk documentation for version 12.6. Here is an overview of the process:  

### Report Generation and Configuration

#### Generating Reports

1. **Accessing Report Generation**: Users who belong to the group specified in the `ManageReportsGroup` parameter (by default, the PVWAMonitor group) can generate reports in PVWA.
2. **Selecting Report Type**: Click on `REPORTS` to access the My Reports page, then select `Generate Report`.
3. **Configuring Report Filters**: Choose the report to generate and specify filters. These filters include general report filters and any additional criteria for the exact report needed.
4. **Scheduling Reports**: You have the option to schedule reports for automatic and manual generation. Reports can be set to run weekly or monthly, with specific start times and frequencies.
5. **Adding Subscribers**: Specify users who will have access to the generated report. You can also opt to send automatic notifications to these users when the report is ready.
6. **Finishing Setup**: Complete the setup to generate the report, which will then be displayed in the Generated Reports tab on the My Reports page.

#### Managing Reports

1. **Accessing Generated Reports**: In the My Reports page, you can view and manage reports in the `Generated Reports` and `Report Definitions` tabs.
2. **Performing Actions on Reports**: Options include saving reports in Excel or CSV formats, protecting reports from automatic deletion, deleting reports, hiding reports, and sending notifications with report links to other subscribers.
3. **Protecting and Deleting Reports**: Protect reports to prevent automatic deletion, or manually delete reports that are no longer needed.
4. **Editing and Deleting Report Definitions**: Edit the scheduling and subscribers of a report or delete report definitions that are no longer required.
5. **Handling Reports in Multiple PVWA Deployments**: In environments with multiple PVWAs in different time zones, it's important to manage the CyberArk Scheduled Tasks services appropriately to ensure consistent report generation.

#### Important Considerations

- **User Authorization**: Reports contain only the information that the generating user is authorized to access.
- **Report Parameters Configuration**: Report parameters can be configured in the Web Access Options of the System Configuration page.
- **Report Status**: The status of each report (Pending, Running, Failed, Done) is displayed and can be monitored for successful generation and access.
- **Access to Reports**: Users can view their own generated reports or reports they are subscribed to, depending on the access authorizations set in the Reports Safe.

For detailed instructions and additional information, it is recommended to refer directly to the CyberArk documentation.

## [[PrivateArk Client]] Reports

According to the CyberArk documentation for version 12.6, the following reports can be generated in the PrivateArk Administrative Client:

1. **Safes List**: This report provides a list of Safes and their properties, organized according to their location. It's useful for getting a quick overview of all the Safes in your system and their respective attributes.

2. **Owners List**: This report lists the owners of specified Safes and their permissions. It is crucial for managing access rights and understanding who has control over different Safes.

3. **Active/Non-active Safes**: This report identifies active or non-active Safes based on activities over a specified period. The status of a Safe is determined by the administrative or data-related tasks carried out in it. This report includes a list of these Safes along with some of their properties and is useful for monitoring Safe usage.

4. **License Capacity Report**: This report details the licensed user types and objects in the Vault, the maximum number of licenses for each type or object, and the number of used licenses. It's essential for license management and ensuring compliance with licensing agreements.

5. **Users List**: This report includes information about users’ activities in the Vault, including those who have been disabled. However, it does not include data-related activities. User Managers and the Auditor User can generate these reports, which are valuable for auditing and monitoring user activities within the Vault.

6. **Active/Non-active Users**: This report lists active or non-active users, including disabled users, in the specified Vault over a given period. Active users are defined as those who have logged on to the Vault. This report is useful for tracking user engagement and identifying potentially inactive accounts.

7. **Entitlement Report**: This report provides details on users’ entitlement rights in the Enterprise Password Vault (EPV). It includes each user’s effective access control and authorization level on each account they have access to in the EPV. This report is vital for access rights management and ensuring that users only have the access they require.

To generate these reports, users need to select the report type from the 'Tools' menu, specify the information to include, set the period the report will cover, and choose the output format. Reports in Excel are displayed immediately, while text reports are saved to a specified location. 

These reports are integral to managing, auditing, and ensuring the security and efficiency of the CyberArk environment.

[Reports in PrivateArk | CyberArk Docs](https://docs.cyberark.com/PAS/12.6/en/Content/PASIMP/ReportsInPrivateArkClient.htm?TocPath=End%20user%7CReports%20and%20Audits%7C_____2)

## Master Policy

- The Master Policy offers a centralized overview of the security and compliance policy of privileged accounts in your organization while allowing you to configure compliance driven rules that are defined as the baseline for your enterprise. It is configured out-of-the-box and can be used immediately after implementation, providing an intuitive, simplified user experience and enhanced bottom-line insight for administrators, IT personnel, managers and auditors.
- The Privileged Access Manager - Self-Hosted solution separates higher-level and compliance driven policy rules such as privileged access workflows, account management and session monitoring requirements from technical settings that determine how the policy will be carried out on each platform.
- The Master Policy groups together sets of rules and offers better visibility and control over policy configurations and enforcement. Each policy rule has basic settings and, sometimes, advanced settings that are displayed when you select the rule, as well as context-sensitive help that explains each rule and its interdependency on other rules.
- Although the Privileged Access Manager - Self-Hosted solution’s Master Policy can be applied to most privileged accounts in your organization, you can create rule exceptions to manage specific workflows. For example, you can define a dual control workflow for highly sensitive accounts on a specific platform that require permission from authorized users before they can be used, while access to other accounts in the organization does not require such confirmation.
- The Master Policy defines basic system behavior for the entire lifecycle of privilege account management and access.

| Concept | Description |
| ---- | ---- |
| Basic Policy Rules | Basic policy rules allow you to define specific aspects of privileged account management. These rules include several groups of policy rules for the access workflow, management of passwords, session monitoring and auditing. |
| Advanced Policy [[Rules]] | Some policy rules have related advanced settings. For example, in the basic policy rules you can determine whether users will be allowed to transparently connect to target systems using ‘Click to Connect’. In the related advanced settings, you can determine whether users will also be able to view passwords. |
| Exceptions | The Master Policy model introduces the ability to define Exceptions. These are policy rules that differ from the overall Master Policy for a specific scope of accounts, for example accounts associated with a specific platform. Each exception contains the basic policy rule as well as its related advanced settings. For example, the Master Policy may define that Dual Control is disabled in the organization. However, the Windows PCI production servers require Dual Control to be enabled because of their higher sensitivity. You can make this allowance by creating an exception to the Dual Control rule that enables Dual Control enforcement on the scope of Windows PCI production servers platform. |                                                                                                                      
In the Platform Management settings, the IT administrator can configure technical settings defined by your organization’s environment and security policies to control how the system manages accounts on various platforms. Most of these settings have default values that do not need to be changed, but certain specific features need to be set according to your organizational requirements.

The CyberArk Master Policy, as outlined in the CyberArk documentation for version 12.6, allows organizations to define baseline rules for managing accounts in their environment. Here is an overview of the key Master Policy rules:

### 1. Privileged Access Workflows

These rules define how access to privileged accounts is managed:
   - **Require dual control password access approval**: Users need approval from authorized users before accessing passwords. This rule enhances oversight over who accesses passwords and for what purpose.
   - **Enforce check-in/check-out exclusive access**: Allows users to check out an account, locking it so that no other users can retrieve it simultaneously. This ensures exclusive usage of the privileged account.
   - **Enforce one-time password access**: Accounts can be retrieved for one-time use only, with the password changed after each use.
   - **Allow EPV transparent connections ('Click to connect')**: Users can connect to remote devices without knowing the specific password, enhancing security and convenience.
   - **Require users to specify reason for access**: Users must provide a reason for retrieving accounts, which can be either a free text reason or one of the predefined reasons.

### 2. Password Management

These rules govern how passwords are managed:
   - **Require password change every X days**: Specifies the frequency for mandatory password changes.
   - **Require password verification every X days**: Ensures that passwords are verified and possibly changed at regular intervals.

### 3. Session Management

Rules related to the recording and monitoring of privileged sessions:
   - **Require privileged session monitoring and isolation**: This rule, when active, mandates the monitoring and isolation of all IT administrator privileged sessions on remote machines.
   - **Record and save session activity**: All activities in each privileged session are recorded in text and/or video format for future auditing.

#### 4. Audit

This section includes rules for retaining Safe activity audits:
   - **Activities audit retention period**: Controls the number of days that audits of activities in Safes are retained.

These Master Policy rules are critical for ensuring the secure and compliant management of privileged accounts. They allow organizations to enforce consistent security practices across their entire privileged account landscape. By leveraging these rules, organizations can significantly enhance their security posture, particularly in terms of access control, password management, session monitoring, and audit trails.

## [[Safe Management and Access Provisioning]]

 

## [[Platform Management]]

## Classic Interface

[Classic Interface | CyberArk Docs](https://docs.cyberark.com/PAS/latest/en/Content/Landing%20Pages/LPVersion9Interface.htm?tocpath=End%20user%7CPrivileged%20accounts%7CClassic%20Interface%7C_____0)

## Authentication Methods

### [[CyberArk]]

[CyberArk password authentication | CyberArk Docs](https://docs.cyberark.com/PAS/11.1/en/Content/PAS%20INST/CyberArk-Password-Authentication.htm)

### LDAP

[LDAP Authentication | CyberArk Docs](https://docs.cyberark.com/PAS/11.1/en/Content/PAS%20INST/LDAP-Authentication.htm)

### RADIUS

[RADIUS authentication | CyberArk Docs](https://docs.cyberark.com/PAS/11.1/en/Content/PAS%20INST/RADIUS-Authentication.htm)

### SAML

[SAML authentication | CyberArk Docs](https://docs.cyberark.com/PAS/11.1/en/Content/PAS%20INST/SAML-Authentication.htm)
