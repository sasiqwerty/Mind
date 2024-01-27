---
aliases: 
tags: 
date created: Friday, September 29th 2023, 12:21:31 am
date modified: Friday, September 29th 2023, 12:21:46 am
---
credentials=account names & passwords

CyberArk: CyberArk is one of the Cyber Security Products.  
 Which is used to protect the provileged Accounts credentials and its access.

CyberArk Components:
====================
1. Enterprise Password Vault(EPV)/Digital Vault(DV)/Vault

   -To store the privileged Accounts credentials.  
   -we will store the privileged accounts credentials in the safes.

2. Password Vault Web Access(PVWA)  
   -PVWA is one of the components of CyberArk  
   -PVWA is a Web Interface  
   -To view the contents of the vault(Accounts & Its passwords)  
   -PVWA Acts as a administration console.

3. Central Policy Manager(CPM)  
   -CPM Will perform the Password management activities.  
   -Password Change, Verification,Reconciliation

-Port Number: 1858  
-CyberArk Compoenents communication


-----------
1. Users(Mater,Administrator,Vault admins,users)  
   i)Unsuspending a user account
2. Account onboarding
3. Activate PSM
4. Reason for Access  
5.How to Create an Exception
-------
*Safe: Basic Access control unit and also we use Safe to secure & store the password objects  
  -28 Characters  
  -3L but 20,000-30,000 objects  
-Safe owner  
-Safe permissions  
  -Use: The connect option will be enabled/we can connect to the accounts using connect button.  
  -Retrieve Accounts:To retrieve the password(copy,show buttons would be enabled)  
  -List Accounts:(To list the accounts) for the user, for which he is having access
 
-CPM Password management Activities.  
 -Change  
 -Verify  
 -Reconcile

-Object Level Access Control(OLAC)  
-PrivateArk Client  
-Server Central Administration Console  
-Vault Service(PrivateArk Server Service)  
-ipconfig  
-Deleting and Creating the Vault icon  
-Dbparm.ini  
-ITLOG.log  
-Remote Control Client.

-Users Creation  
-Group/Directory creation  
-LDAP Directory Mapping  
-LDAP Integration

-User Login in PrivateArk.
  1. PrivateArk Authentication(Master,Administrator)
  2. Ldap Authentication(All external users)  
-User Activation(Unsuspend) in PrivateArk Client  
-Login with the master user  
https://cyberark-customers.force.com/s/article/How-to-log-in-as-the-Master-user  
-Safes difference when you login with master and Administrator  
-What is Master user is suspended or lost the Master CD?


-Platform Duplication  
-Exceptions  
-Platform parameters: AutoChangeOnAdd, AutoVerifyOnAdd  
-AllowedSafes  
-CPM Performance optimization  
-Password policy(Generate Password)


-Linux Account creation,directory creation  
-Linux Account Onboarding  
-Safe,Platform Naming convention.  
-Linux Account Connect

-Auditing Activities:

-Auditors group,PVWA Monitor  
-Linux Recordings(Key Stroke format)  
-Recordings & Monitoring  
-Live session monitoring  
-How the recordings are stored(PSMRecordings safe)  
-To terminate the sessions, the user should be part of PSMLiveSessionTerminators group.


=====  
-Oracle Account onboarding  
 *Port number(1521)  
 *Database name

-Linked Accounts:
 1. Reconcile Account
 2. Logon Account  
   -We can define/link the linked accounts in two ways  
     i) At account level  
    ii) At platform level

Reconciliation permissions:
---------------------------
Reset Password  
Read Account Restrictions  
Read General Information  
Read Group membership  
Read logon information  
Read permissions

===  
Securing Unix Accounts with SSH Keys:

Dependent Accounts/Service Accounts/Usages

https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/10.10/en/Content/PASIMP/Managing-Service-Accounts.htm  
https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/Latest/en/Content/PASIMP/Managing-Service-Accounts.htm

====
Master Policy:
--------------
1.Privilege Access Workflows
  -Dual Control Access Approval
  Dual Control Access:
====================
1. We need to enable the DUAL Control Policy rule from Master policy for the particular platform.
2. The user should have access to the account.
3. At safe level for the Approvers we will enable the Work flow option and choose Levels of approval.
4. Now the user will request for access..
5. Manager will validate the request..
6. Now the user can access the account.

  -Enforce Check-in/Check-out exclusive access  
  -Enforce One-time password access  
  -EPV Transparent connections  
  -Reason for access

2.Password Management  
3.Session Management  
4.Audit


===  
-Enforce Check-in/Check-out Exclusive Access  
-Enforce One-time password access  
 -(Verify the Definition in the PVWA)

-CyberArk Account Onboarding Methods:  
 -Manual Account Onboarding  
 -Account Discovery  
 -Bulk Accounts Onboarding(Using PUU/PACLI)  
 -Using RestAPI.
 


-HTML5 GATEWAY  
-AD-HOC Connections/PSM SECURE CONNECT  
-PSM FOR SSH/PSMP/PSM Proxy  
 Syntax: Vaulusername@TargetLinxUsername@TargetLinuxServerIp/FQDN@PSMPServerIP/FQDN  
-Auditing Activities: (Session Recordings, Live Monitoring,Suspend, Terminate)  
-Monitoring Recordings

***PTA***
- Unmanaged privileged access
- Suspected credential theft and automatic password rotation
- Suspicious password change and automatic reconciliation
- Suspicious activities in a session and automatic suspension

**Reports***  
Types Of Reports:

https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/Latest/en/Content/PASIMP/ReportsInPVWA.htm  
https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/Latest/en/Content/PASIMP/ReportsInPrivateArkClient.htm?tocpath=End%20user%7CReports%20and%20Audits%7C_____2

1. PrivateArk Reports  
=====================  
  -Safe List  
  -Owners List  
  -Safe Activities  
  -Active/Non-Active Safes  
  -Entitlement Report  
  -Licence Capacity Report  
  -Users List  
  -User Activities  
  -Active/Non-Active Users
  
2. PVWA Reports  
  I) Operation Reports  
     i. Privileged Accounts Inventory Report  
    ii. Application Inventory 

  II)Audit/Compliance Reports  
     i. Privilege Accounts Compliance Status  
    ii. Entitlement Report  
   iii. Activity log Report.
   


Backup & Restore
=================

Restore:

https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/11.2/en/Content/PASIMP/Restore-Utilities.htm#_Ref364686739  
https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/Latest/en/Content/PASIMP/Restoring-Safes-or-the-Vault.htm

Full Restore:  
https://cyberark-customers.force.com/s/article/Video-How-to-Perform-a-Full-Vault-Restore-Using-PARestore

Disaster Recovery:
=================
-Just In Time Access(JIT)

-Password Upload Utility:
=========================
1. Prepare the .csv file by updating all the account details(Account names, Safe names, Template safe, Policy ID, password, etc,.)
2. Update the Vault ip in Vault.ini file.
3. Create credfile for Administrator user that is user.ini file.
4. Update the Conf.ini file with Vault.ini file name, password.csv file name,DefaultTemplateSafe name
5. Run the Password upload utility command>PasswordUpload.exe conf.ini
6. Will check whether all the accounts were onboarded or not and cross check if any errors
