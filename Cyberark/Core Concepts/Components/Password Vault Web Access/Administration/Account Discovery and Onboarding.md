---
aliases: onboard, onboarding
tags: 
date created: Tuesday, July 25th 2023, 9:56:27 am
date modified: Thursday, August 3rd 2023, 3:52:03 pm
---
Account onboarding in CyberArk is the process of adding a new account to the CyberArk vault. This process typically includes the following steps:

1. **Gathering information:** The first step is to gather the necessary information about the account, such as the account name, username, password, and the system or application that the account is associated with.
2. **Creating the account:** Once the information has been gathered, the account can be created in the CyberArk vault. This may involve entering the information into the CyberArk administration console.
3. **Assigning permissions:** The account will need to be assigned permissions to the resources that it needs to access. This may involve assigning the account to a role or group, or granting the account specific permissions.
4. **Testing the account:** Once the account has been created and assigned permissions, it should be tested to ensure that it can access the resources [[Create a new user - Windows Server]]that it needs.

Onboarding is considered to be one of the most common activities of a CyberArk [[Administrator]].

## Manual Onboarding Accounts

### Windows Server

- Follow the steps below to create a new user in the Windows Server
	- [[Create a new user - Windows Server]]
	- The account with administrator rights is called a [[Privileged Account]]
- Accounts can be added to other groups, these groups have different rights or privileges based on the settings.
- [[Manage platforms]] Use this feature to select the [[Platform]] of the account you wish to onboard.
	- Selecting a different [[Platform]] wont throw an error, its advisable to select the right [[Platform]].
- Select the [[Safe]] you wish to add the account to from the [[Access Control]] tab in the policies tab.
	- If all the [[Password Vault Web Access]] options are not loaded its advised to restart the IIS service using the *iisreset* command as an admin through the cmd. 
		- related to [[Services in CyberArk]] 
- Enter the [[IP]] address or the [[Fully Qualified Domain Name]], its username and its password(optional).
	- To get the fully qualified domain name
		- **Control Panel > System and Security > System - Full Computer Name**
- When the account is successfully added the accounts page gets updated (manual refresh required)
	- A **yellow lightning icon** is observed next to the account name saying its a newly onboarded account.  
![[Pasted image 20230726103200.png]]

### Linux Server

- To connect to a Linux server we use the [[PuTTY]] tool.
- The [[vi editor]] is used to edit and navigate text files in Linux.

### Oracle Database Server

## Account Discovery

- Accounts > Pending and Discovery > Discovery Management
	- Windows and Unix scanning options available.
	- Select the right domain.
- Domain admin account is needed for account discovery
	- This user can be found in the Active Directory Users and Computers
	- the address of the domain admin account? the address of the domain?
	- Password Manager pending safe, all the discovered accounts are brought there and ready to to be onboarded.
- Onboarding rules
	- Select the domain
	- Select the account category or it can be any
	- Privileged account type can be any or built in admin (SID = 500)
	- Assign the platform and safe
	- keep in mind that you need a reconciliation account to that safe to complete onboarding successfully  
![[Pasted image 20230727073602.png]]  
![[Pasted image 20230727073631.png]]  
![[Pasted image 20230727074754.png]]

## Bulk Account Onboarding Using PUU - Password Utility Tool

## Using Rest API

not going to be taught?

### What Are the Main Differences between Onboarding Linux, Windows and Oracle Database Accounts in CyberArk?

- **The type of account:** Linux accounts are user accounts, Windows accounts can be user accounts or service accounts, and Oracle database accounts are service accounts.
- **The authentication method:** Linux accounts can be authenticated using SSH, Windows accounts can be authenticated using Active Directory, and Oracle database accounts can be authenticated using a variety of methods, such as TNSNames or connection strings.