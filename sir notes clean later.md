---
aliases: 
tags: 
date created: Friday, September 8th 2023, 8:00:51 am
date modified: Friday, September 8th 2023, 8:00:58 am
---
PAM Install & Configuration Lab:
================================
1. About Each component

CyberArk Components Installation Sequence:

Before version 10.7v  
EPV/DV/Vault==>CPM==>pvwa==>PSM==>Other components.

After version 10.7v  
EPV/DV/Vault==>PVWA==>CPM==>PSM==>Other components.


**The order for PVWA first then CPM switched starting in version 10.7,  
because the CPM now uses the API (of the PVWA) for Account Discovery and onboarding.

******Digital Vault/Vault/Enterprise Password Vault(EPV)************

1. What are the prerequisites?

Server and Software Requirements:

https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/11.3/en/Content/PAS%20SysReq/Recommended%20Server%20Specifications.htm

Vault Installation Prerequisites:
*********************************
   -Windows server 2016/2019  
   -.Net Frame work 4.8 or above  
   -Microsoft Visual C++ Redistributable package  
   -Vault software  
   -Master CD  
   -Operator CD  
     *Server.Key  
   -License file  
   -Vault shouldn't be a domain joined server but we will add Vault to the work group.  
   -Vault server we should install in Isolated zone.

Keys in the Operator CD: server.key, recpub.key, rndbase.dat  
Keys in the Master CD : server.key, recpub.key, rndbase.dat, recprv.key



https://cyberark-customers.force.com/s/article/What-is-the-usage-of-the-keys-come-with-Operator-and-Master-CD  
https://cyberark-customers.force.com/s/question/0D55000006G2tSfCAJ/understanding-operator-cd-and-master-cd-operations

*-Vault server is not a domain joined/domain member, we will add to a work group.  
what is workgroup and domain?

A workgroup is a collection of individuals working together on a task.

1. What is hardening Process?  
-NIC Hardening.  
-What is difference between IPV4 X IPV6

- In the DNS tab, deselect “Register this connections addresses in DNS”.
- In the WINS tab, deselect “Enable LMHOSTS lookup”.
- Select Disable NetBIOS over TCP/IP.

-Vault Installation.


https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/Latest/en/Content/PASIMP/Managing-the-CyberArk-License.htm?TocPath=Administrator%7CComponents%7CDigital%20Vault%7COperate%20the%20CyberArk%20Vault%7C_____8
   
Data Encryption:  
Serverkey=>VaultKey=>Safekey=>Object Key=>Sub Objects

==>We shouldn't install any third party applications/software in the vault server.

==>VM-SNAPSHOTS

1. How we will install a Vault component
2. After Installation-changes(safes,default users,groups)
3. Services
4. Configuration & Log files
5. Any default users/internal users


===  
*******Vault***********  
-Default 3 Safes created in Vault Once after installation is done  
 1.Notification Engine  
 2.VaultInternal  
 3.System

-Defualt users

-Services  
 1.PrivateArk Server  
 2.PrivateArk Database  
 3.PrivateArk Remote Control Agent  
 4.CyberArk Logic Container  
 5.Cyber-Ark Event Notification Engine  
 6.Cyber-Ark Windows Hardened Firewall
 
-Service Dependencies

Vault Services->starting-Sequence:

To Start: PrivateArk Database=>CyberArk Logic Container Service=>PrivateArk Server Service=>Rest of the vault services

Vault Services->Stopping Sequence

PrivateArk Server Service=>PrivateArk Database=>Other Services(Except CyberArk Windows Hardened Firewall Service)

-Configuration Files  
-Log files  
-Vault Debugging

How to apply License in Vault?  
2 ways:

1. Once after we have the license file we can move the license file to the vault server  
   under privateark->server->Conf location.  
   (Before we do that we will take the copy of the existing old license.)  
  And we need to restart the PrivateArk server service.

2. Move the license file to the System safe.  
   No need to restart the Vault service.

https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/Latest/en/Content/PASIMP/Viewing-the-Server-Log.htm?TocPath=Administration%7CComponents%7CDigital%20Vault%7COperate%20the%20CyberArk%20Vault%7C_____2

 ENE
=====
-CONFIGURATION Files  
-LOGFILES  
-ENE Default User  
-ENE Safe contents  
-ENE Service name

-How to collect logs from vault?

https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/Latest/en/Content/PASIMP/Collecting-Log-Files.htm  
From Vault server go to >Server folder location and type the below command in command prompt with administrator rights
> CAVaultManager.exe CollectLogs

-Break Glass Procedure & utilities(Recovery, Saferecovery)

https://cyberark-customers.force.com/s/article/How-to-recover-password-using-recover-exe-outside-of-Vault  
https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/Latest/en/Content/PASIMP/Recover.htm  
https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/11.3/en/Content/PASIMP/SafeRecover.htm

Master & Operator CD Contents:  
https://cyberark-customers.force.com/s/article/What-is-the-usage-of-the-keys-come-with-Operator-and-Master-CD

=>Event viewer logs  
https://cyberark-customers.force.com/s/article/00002342

Vault Manual Hardening:  
https://cyberark-customers.force.com/s/article/Vault-Hardening-Overview  
https://cyberark-customers.force.com/s/article/00001931


How can you say the Vault is Secure?

-Vault is installed in DMZ(Demilitarized zone)/Isolate state/Zone.  
-Vault will accept only 1858 connections(If any other ports required for communication means we will open the connection for those trusted ports)  
-Vault is Hardened Server(NIC Hardening+Vault database hardening)  
-Vault is not a domain joined server , it is added to Work group.  
-Vault data is encrypted with several Encryption algorithms.  
-Vault is secured with 7 Layers of security.  
-We shouldn't install any third party software(Like antivirus,or other software)  
-Vault data is encrypted with several keys(like Server key->VaultKey->SafeKey->ObjectKey)

-What are all the possible reasons for vault down?
--------------------------------------------------
-Due network issues  
-Due to Physical network issues  
-Hardware failure issues/Disk issues.  
-Due to insufficient resources(RAM,CPU,Hard Disk ,etc,.)  
-Due to load on the vault/Due to huge transactions on the Vault.  
-Due to any windows related issues.  
-Due to Operating system related issues(Dead lock).  
-Due to misconfiguration in the Vault configuration files.  
-Due to Other applications installed in the vault(Like Anti virus).  
-Due to Vault DB Corruptions.



*Trouble shooting approaches that we will follow:
-------------------------------------------------

-We will check the Vault logs(ITALOG, Trace logs)  
-We will try to start the Vault service(PrivateArk Server).  
-Based on the error we will check for the existing articles.  
-We can check the Vault Event viewer logs  
-Check the Memory/CPU utilization with respect to services or applications.

*What could be the reason that vault installation get failure?
--------------------------------------------------------------
-Due to Disk issues/Operating system issues.  
-Due to Memory issues  
-Due to Network issues/firewall  
-During the vault DB Creation.  
-Due to improper keys/license  
-Due to the existing applications behaviour (Antivirus) 


PVWA:
====
-Installation  
  -PVWA Server Prerequisites  
https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/Latest/en/Content/PAS%20SysReq/Recommended%20Server%20Specifications.htm  
-Server Specifications:  
	-Windows 2019, Windows 2016  
-Software Prerequisites  
   -.Net Frame work 4.8 or above
   - ISS Server installation/Web Server roles
   - SSL certificate  
   -MicroSoft Visual C++ Redestributable package
  
-IIS Server

How will you install PVWA?  
-Run PVWAPrequisites script.  
-Configure SSL Certificate.(Import the certificate+Bind the certificate)  
-Require SSL Option.  
-PVWA application installation  
-PVWA Hardening Script we need to run.

************
-iisreset  
https://<PVWAServerFQDN/IPADDRESS/Loadbalancer formid>/PasswordVault/  
-difference between V10 VS V9 interface  
 To change to V9 Interface:  
 Administration->Options->General->Use V10 Logon Page->Yes/No  
-Load Balancing Concept  
-Hardening(PVWA Manual & Automatic)  
 https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/11.4/en/Content/Security/EPV%20IIS%20Hardening%20-%20PVWA%20Only.htm  
-Application Pools  
-Log files location  
   c:\windows\temp\pvwa  
-Configuration file  
https://cyberark-customers.force.com/s/article/Where-do-I-find-the-logs  
-Default Users/Predefined Users/Internal Users  
 -PVWA AppUser  
 -PVWA GWUser  
-Creating Cred files for default users  
-Multiple Reasons for PVWA Not working.
****************************************
 -Need to check PVWA internal users whether suspended or not if suspended, we need to unsuspend by recreating the credfiles.  
 -PVWA SERVER Network issues  
 -Check the Application Pools status in IIS Server Manager  
 -We have to check in Vault.ini file whether correct vault ip is defined or not.  
 -PVWA SSL Certificate expired  
 -We need to check whether the PVWA Link is down/Load balancer issues  
 -We need to check whether the PVConfiguation.xml, Policies.xml files are corrupted or not  
  we can trouble shoot by replacing the PVConfiguration.xml from the backup.  
 -If PVWA Installation directory is full, due to that also there is a chance that PVWA Wont function.
 

What you will do when PVWA Is down?
1. As a basic step, i will do the IISRESET
2. Will ping the vault ip 
   > ping <Vault ip>
   
   Also we have to check the port connectivity with the Vault server.  
   Open Powershell with administrator mode
   > Test-NetConnection -ComputerName <Ipaddress of the destination server> -Port <Port Number>  
   or > TNC -ComputerName <Ipaddress of the destination server> -Port <Port Number>
   
3. In Vault server, will check the ITALOG/ServerCentral Administration console if any suspected messages were there  
    like PVWA Internal users are suspended or not.  
   If PVWAInternal Users(PVWAAPuser & PVWAGWUser) are suspended, then i will enable the users at privateArk  
   and will run the cred files for the pvwa internal users at pvwa server end.
4. Based on the error messages in the PVWA Logs , we will look for the existing articles/solutions and we will take necessary  
   actions on the issues.  
   If required we will enable the PVWA Debugging for troubleshooting issue.
   
5. Need to check with Load balancer team for the PVWA configuration and we will ask to remove the pvwa ip  
  from Load Balancer pool for particular PVWA Servers if we identify any issues.
6. We can check the connectivity with particular PVWA URL


     
Creating Cred file for PVWA Internal Users:
===========================================

12.1.0 or below ONLY  
https://cyberark-customers.force.com/s/article/PVWA-How-to-create-update-credential-files-for-PVWA-manually  
For 12.1.1 and above  
https://cyberark-customers.force.com/s/article/PVWA-How-can-I-create-or-update-the-credential-files-credfile-for-the-PVWA-manually-VERSION-12-1-1-and-above-ONLY

How to unsuspend the PVWA Internal Users?
1. Check the vault version and accordingly proceed with the article steps.
2. Stop the IIS Services from the respective PVWA Servers
3. Unsuspend the PVWA Internal users via PrivateArk Client by Updating the passwords
4. Create the CREDFILES for the PVWA internal users by following the existing articles  
   as per the vault version.
5. Once after the credential files were created, start the IIS Services.
6. Access the PVWA page now.

****How to set Debugging for PVWA

Login to PVWA=>Administration=>Options=>Logging

https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/Latest/en/Content/PASIMP/Configuring-Debug-Levels.htm

*****************************
		CPM
*****************************

CPM Installation:
=================
CPM Is one of the components of CyberArk and it is called Central Policy Manager.  
CPM performs: Password Change, Verification , Reconciliation.  
All the password management activities would be performed by CPM.

CPM Prerquisites:  
-Verify .NET framework(4.8 or above)  
-CPM IIS-Tls settings.  
https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/Latest/en/Content/PAS%20INST/CPM-install-preinstall-tasks.htm?TocPath=System%20Requirements%20by%20Product%7CIntroduction%20to%20Digital%20Vault%20installation%7CCPM%20pre-installation%20tasks%7C_____0

System Requirements:

==>Windows 2019, Windows 2016  
==>.NET Framework 4.8

https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/Latest/en/Content/PAS%20SysReq/Recommended%20Server%20Specifications.htm?TocPath=Installation%7CSystem%20Requirements%7C_____1

CPM Default users:  
 -Before 12.2.4  
  -PasswordManager  
 -From 12.2.4  
  -PasswordManager  
  -PluginManagerUser  
  -ScannerUser
  
 https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/Latest/en/Content/PAS%20INST/The-Central-Policy-Manager-Environment.htm
  
Changes in 12.2.4 version:  
https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/Latest/en/Content/Release%20Notes/RN-WhatsNew12-2-4.htm?TocPath=Get%20Started|What%E2%80%99s%20New|Release%20Notes|_____6

=>CPM Installation  
=>CPM Default User  
  -Password Manage User  
=>CPM Common Safes that are created in th vault  
  -Password Manager Pending  
  -Password Manager Shared  
  -Password Manager Temp  
  -Password Manager_Accounts(From 12.2.4)  
=>How to create a credential file for CPM Internal user:

 For 12.0 & Below  
https://cyberark-customers.force.com/s/article/CPM-How-can-I-create-or-update-the-credential-files-credfile-for-the-CPM-manually  
 For 12.1 & Above  
https://cyberark-customers.force.com/s/article/CPM-How-can-I-create-or-update-the-credential-files-credfile-for-the-CPM-manually-12-1-AND-HIGHER

=>How to unsuspend a Default user of components?(PVWA/CPM/PSM)

1.We need to stop the particular component server service  
2.Login to PrivateArk Client and activate the suspended user(via trusted net areas)  
3.Update the credential/password for the user and check the password never expires option alone.  
4.Now go to the respective component server and open the command prompt with administrator and create the cred files  
  based on the version.  
5.Now start the particular service to bring the operations back.

=>Services  
  1-CyberArk Password Manager  
  All password management activities, cpm status,Password Policies  
  2-CyberAr Central Policy Manager Scanner  
  During Account Discovery feature, JIT Activity.  
=>Log files  
  -PM.log  
  -PM_Error.log  
  -PMConsole.log  
  -PMTrace.log  
https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/11.2/en/Content/PASIMP/CPMLogging.htm

=>Configuration files  
 =>CPM.ini(Would be there in Password Manager Safe)  
 or the cpm settings we can do from pvwa=>Administration=>System Configuration=>Central Policy Manager=>CPM Settings.  
=>How to set debugging for CPM  
https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/Latest/en/Content/PASIMP/Configuring-Debug-Levels.htm

=>DEP(Data Execution And Prevention)==>Should be disabled in CPM Server  
DEP is a feature in windows which blocks malicious scripts or executions.  
It interferes with CPM password change process so recommended practice is to disable it or create an exception to it.  
Now in the newer versions exceptions get added automatically eliminating the need to manually create them!

=>plink.exe, pmterminal.exe and telnet.exe are defined as exceptions to Data  
Execution Prevention.

CPM Manual hardening:  
https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/11.4/en/Content/Security/EPV%20In%20Domain%20PVWA%20and%20CPM%20Server.htm

How to disable DEP?  
https://www.windowsworkstation.com/win2016-2019/disabling-dep/  
=>Applying group policy(cmd>gpudate /force)  
==>CPM Hardening(Manul & Automatic)  
https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/Latest/en/Content/PAS%20INST/CPM-hardening-runscript.htm  
https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/11.3/en/Content/Security/EPV%20In%20Domain%20PVWA%20and%20CPM%20Server.htm

==>CPM Load balancing?=>No; Split Brain phenomenon.  
==>In which situations both the Vaults will up and running?
   1. Due to Network issues  
   2. Due to misconfiguration in the DR-Padr.ini file.[Failovermode=Yes]
   3. Due to Communication issues.
   
=>CPM Process files and prompts file  
https://cyberark-customers.force.com/s/question/0D52J00007FsfIRSAZ/what-is-difference-between-process-file-and-prompt-file  
https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/Latest/en/Content/SDK/TPC-process.htm  
https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/Latest/en/Content/SDK/TPC-promps.htm

What if the CPM is failed to change the password?  
What are the trouble shooting steps that we will do?  
-Check the Connectivity with the target server(Ping we do)  
-From Cpm Server to the Target server we do check the port connectivity(135,139,445)  
  Example: [>Test-NetConnnection/tnc -ComputerName <IP/Name of the computer> -Port <Port Number>
- Will try with Reconciliation acco	unt.  
-We will check the CPM log files and we will take the necessary actions.  
-We will check the articles for any solutions.  
-Use net use command to check the target account is connecting or not.  
https://cyberark-customers.force.com/s/question/0D52J00007TVOSLSA5/cpm-unable-to-perform-access-net-use-to-target-win-system-nat-ip-address-error-winrc5  
-We do enable the debug for CPM To understand the issue.

-CPM Default ports between cpm and target server: 135,139,445; for SSH it is 22

  
*****Integrations:******
=============
1.LDAPS Integration:

LDAP: PORT NUMBER: 389  
LDAPS: PORT NUMBER: 636

  -Need to move SSL Certificate to Vault server  
  -Install the SSL Certificate(LDAPS Certificate) in the Vault Server.
 
  A command /Another way of installing the LDAPS certificate in the Vault Server

    >certutil -addstore Root "CertficateName"

  -Define the Hosts entries with Domain details in the Vault server  
   <Domain server ip>	<FQDN>  
  -Bind Account Onboarding in PVWA  
  -Directory Mapping at PVWA  
  -Change the port number to LDAPS port number: 636 (Note:LDAP Port number is 389)  
  -Make SSL Connection to Yes in PVWA.  
  -Change the Server ip as FQDN.  
  -Restart the Vault Server/PrivateArk Server Service.
  
How do I test outgoing LDAP external directory connectivity to the vault?  
 https://cyberark-customers.force.com/s/article/00004795
 
 

1. SMTP Integration:follow the guide
2. SIEM Integration/SYSLOG:follow the guide [Security information and event management]  
https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/11.4/en/Content/EVD/Action-Codes.htm  
https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/Latest/en/Content/PTA/Configuring-Vault-Forward-syslog-Messages.htm?Highlight=syslog

4.NTP Integration:

-How to open a Ports in Vault Server  
  i.At Firewall Level we will enable the port.  
 ii.DBPARM.ini Level we will create a rule for inbound/outbound with server details.

 https://cyberark-customers.force.com/s/article/00002003

5.SNMP Integration:  
https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/Latest/en/Content/PASIMP/Configuring-Remote-Monitoring.htm  
https://cyberark-customers.force.com/s/article/How-to-Configure-Basic-SNMP-Integration-for-Vault-Monitoring

******************************************************************

-Authentication Methods:  
 *Radius Authentication  
 *PKI(Public key Infrastructure) Authentication  
  -Get the user CA certificate  
  -Install the Certificate  
  -Enable the PKI authentication method in PVWA  
  -Configure the PKI Authentication in applicationHost.config file(C:\Windows\System32\Inetsrv\Config\).  
   <location path="Default Web Site/PasswordVault/api/auth/pki/logon” />
   
  *Two Factor Authentication(2FA)/Multi-Factor authentication


###################PSM###################

what will happen when we click connect button from pvwa?  
https://cyberark-customers.force.com/s/question/0D55000006B7DjvCAF/what-is-the-workflow-after-pressing-connect-button-in-pvwa-console-  
https://blog.51sec.org/2019/07/cyberark-notes.html#point2

***********************Once after the Connect button is pressed what will happen?**********
1. Once after we click connect button after loggin in to PVWA

   From PVWA, the request will go to the Vault Server.  
   Vault sends a message to PSM server to expect an RDP connection  
   Now the RDP file will get download since we enabled the PSM.
   
2. Click on RDP File.
3. Now One of the PSM User's called 'PSMConnect' user will establish the session  
   through PSM.
4. Now PSM Will fetch the credentials from Vault server.
5. Once the credentials are fetched, Now PSMConnect user creates a temporary profile  
   with the username PSMShadowUser on the PSM server.  
   then PSM Will establish the connection to the target server based on the connection component  
   either it may be a RDP/SSH/SQL..
6. Now the session would be established to the target server and we can connect.
7. During the session is ongoing, the PSM Recordings will store locally in the PSM Server and  
   once after the session is closed, then the Session recordings will be stored on the vault server  
   in PSMRecordings safe.
*************************

PSM Installation:  
 -PSM Server specifications  
 https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/Latest/en/Content/PAS%20SysReq/Recommended%20Server%20Specifications.htm?TocPath=Installation%7CSystem%20Requirements%7C_____1  
 -PSM Prerequisites**
 
 -Windows 2016/2019 Server is required  
 -.Net frame work 4.8 or above  
 -RDS Rules should be installed.  
 -NLA should be Disabled  
 -Update RDS Security Layer  
 -PSM Software  
 -RDS Certificate

**Network Level Authentication (NLA) is a feature of Remote Desktop Services (RDP Server) or Remote Desktop Connection (RDP Client)  
that requires the connecting user to authenticate themselves before a session is established with the server.

 ***Why we install the PSM with Domain admin user?  
 -To enable Remote App features and for session collection.
 
 -PSM Server Installation.  
 -PSM Group policy creation link:  
 https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/Latest/en/Content/PASREF/PSM-in-domain-GPO.htm
 
 How to install RDS CAL(Client Access License) License?  
 https://in.video.search.yahoo.com/search/video;_ylt=AwrKC3BwqhpjHs0HQ1C7HAx.;_ylu=Y29sbwNzZzMEcG9zAzEEdnRpZAMEc2VjA3Nj?p=RDS+CAL&type=E211IN885G0&ei=UTF-8&fr=mcafee&turl=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOVP.CXKV8xUgfcQZHx3udMj2twHgFo%26pid%3DApi%26w%3D296%26h%3D156%26c%3D7%26p%3D0&rurl=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3Db5s5Hq8bckQ&tit=How+To+Install+and+Setup+RDS+CAL+Licence+On+a+Windows+Server&pos=1&vid=cffd61dc1046f3a2a56c9bf9c008980b&sigr=a0AHgLXsuU8T&sigt=KlOe5da1vrCA&sigi=arXeFqlx2McP
 
 
 What will differ PSM Installation in windows 2019 server?  
***Note:  
Due to RDS licensing enforcement in Windows 2019, a per-user license is no longer supported for local users.  
We recommend using a per-device RDS license.  
To work with a per-user license on a Windows 2019 machine, PSM users must be moved to the domain level.  
See PSMConnect and PSMAdminConnect Domain Users for details.

 =>https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/Latest/en/Content/PAS%20INST/Optional-Moving-the-PSMConnec-and-PSMAdminConnect-users-to-your-Domain.htm  
 https://cyberark-customers.force.com/s/article/What-are-licensing-requirements-for-Microsoft-Remote-Desktop-Services-RDS-when-deploying-CyberArk-s-Privileged-Session-Manager-PSM
 
 https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds-client-access-license  
 https://cyberark-customers.force.com/s/article/Windows-2019-RDS-Server-for-PSM
 
 
 -PSM ID Configuration at platform level  
 -PSM Loadbalancer Concept & Configuration  
 -How to identify which psm is established the connection.
 
 -RDP Over SSL
*********RDP Over SSL*****************
============
1. Definition:  
The connections from the PSM Server to the Target servers will be secured & encrypted  
with SSL connections.  
Users can configure secure RDP connections to the PSM machine using an SSL connection.

2. To achieve this we need to install RDS certificate in each PSM SERVER.

 <Check certificate installation steps in installation guide: "Update RDS Certificate">

1. In PSM Server at group policy we will enable the SSL settings.  
   <Check "Use RDP Over SSL" section in guide>
2. Need to configure the authentication levels in each active connection components at PVWA End.  
   -authentication level:i  
    value:1

   <Check page number 106 in guide>
- Secure RDP Connections with SSL concept in docs.cyberark.com  
  https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/11.2/en/Content/PASIMP  
  /Securing-RDP-Connections-with-SSL.htm
   
********************************************************
 -PSM Service  
  -CyberArk Privileged Session Manager(& Its importance)  
 -PSM Safes  
  -Size declaration  
  -Safe retention  
  -**PSMRecordings safe  
 -PSM Log files  
  =>PSMConsole.log  
  =>PSMTrace.log  
 -PSM Configuration files  
 **-basic_psm.ini (And understand the contents in the file for interview point of view)
  
 -PSM Default Users  
  *PSMAppUser  
  *PSMGWUser  
 Credfile cration for PSM Internal user:  
https://cyberark-customers.force.com/s/article/PSM-update-credential-files  
https://cyberark-customers.force.com/s/article/PSM-How-can-I-create-or-update-the-credential-files-credfile-for-the-PSM-manually-12-1-AND-HIGHER
  
 *PSMConnect:Starts PSM sessions on the PSM machine/To establish the sessions to the target server.  
 *PSMAdminConnect:Monitors live privileged sessions.(For Live Monitoring)  
https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/Latest/en/Content/PAS%20INST/Optional-Moving-the-PSMConnec-and-PSMAdminConnect-users-to-your-Domain.htm

 -**PSM Shadow User  
https://cyberark-customers.force.com/s/article/00003736  
A PSM Shadow user is automatically created during a PSM Connection.  
The PSM Shadow users sandbox the client session.  
The point of the Shadow users is process isolation,  
so the programs launched on the same server by different vault users run under different identities,  
and cannot leak information between the sessions. 


When users initiate a connection (session) to a target machine via PSM,  
a PSM Shadow user is automatically created on the PSM machine and that's  
the user that is used to log on to the target machine and perform actions.


Different WINDOWS ERROR CODES:  
https://social.technet.microsoft.com/wiki/contents/articles/37870.remote-desktop-client-troubleshooting-disconnect-codes-and-reasons.aspx

The purpose of the Shadow user is to isolate the session.  
https://docs.cyberark.com/Product-Doc/OnlineHelp/PrivCloud-SS/Latest/en/Content/Privilege%20Cloud/privCloud-cleanup-shadow-user.htm#:~:text=When%20users%20initiate%20a%20connection,is%20to%20isolate%20the%20session.



The credentials of the shadow users are managed and changed internally by the PSM server. The PSM will change (reset) the shadow user password every time a new connection is made.


PSM-PRIVATEARK CLIENT Connection:

1.Onboard the Administrator account using CyberArk Vault Platform as a Application account.  
2. Export the PrivateArk client settings and save the configuration file as  
   GlobalSettings.ini  
3. Add the PSMShadowUsers group and give R+X Permissions.  
4. Run the Configuration settings.  
   PAConfig.exe /inifile c:\Users\Admin02\Desktop\GlobalSettings.ini  
5. Enable the PSM-PrivateArk client connection code line in the PSMAppLocker script and execute the Powershell script to apply.  
6. Check the PSM Private-Ark Client connection.  
7. Will troubleshoot if any issues identified.

-PSM Applocker script

-How to enable the debug for PSM  
 https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/Latest/en/Content/PASIMP/Configuring-Debug-Levels.htm

*******PSM For SSH*************
PSM For SSH/PSMP/PSM Proxy
-----------------------------------
-It is used only for Linux purpose.
- To give the comfort/to facilitate the Linux Administrators PSMP is being used.  
-Linux administrators use native protocols like putty to connect to the linux boxes/linux machines.  
-We use a special connection string to connect to the Linux target servers.
 
Connection String Syntax:  
 Vaultusername@TargetLinuxUser@Target LinuxServerip/Address@PSMPServerip/FQDN Of PSMP

** PSM X PSMP

PSMP Server specifications:

https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/Latest/en/Content/PAS%20SysReq/System%20Requirements%20-%20PSMP.htm  
https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/Latest/en/Content/PAS%20SysReq/Recommended%20Server%20Specifications.htm?TocPath=Installation%7CSystem%20Requirements%7C_____1

PSMP Hardening:  
https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/Latest/en/Content/PAS%20INST/Following-Installation-of-PSMP.htm?Highlight=SELINUX#Automati


What is Proxymng User:  
ProxyMng User is a Maintenance User

By default "proxymng" is considered a maintenance user.  
So it can connect to ssh in, with no prompts for psmp parameters (target server) etc.  
So after logging in with it, you can switch to root to do maintenance.  
You can also add more maintenance users with a parameter to sshd_config (either user or group depending on what you set integrated mode to)  
So it's sort of a logon account.

https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/Latest/en/Content/PASIMP/Administrating-the-PSMP.htm?Highlight=Maintenance%20user%20psmp

PSMP Installation document:

https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/Latest/en/Content/PAS%20INST/Installing-the-PSMP.htm
How to Operate services in PSMP:
--------------------------------
service psmpsrv status

service psmpsrv start

service psmpsrv stop

service psmpsrv restart

PSMP Services:  
-PSM SSH Proxy  
-PSMP ADBridge  
https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/Latest/en/Content/PAS%20INST/Following-Installation-of-PSMP.htm?Highlight=SELINUX#Automati  
https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/Latest/en/Content/PASIMP/Administrating-the-PSMP.htm?Highlight=Maintenance%20user%20psmp  
PSMPConfiguration files:  
https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/Latest/en/Content/PAS%20INST/The-PSMP-Environment.htm

PSMP Log files:  
**  
https://cyberark-customers.force.com/s/article/Where-do-I-find-the-logs

PSMP Safes & Users in Vault:  
Default users: 3 users  
  -PSMP_ADB_<Hostname>  
  -PSMPApp_<Hostname>  
  -PSMPGW_<Hostname>

PSMP Recordings:  
https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/Latest/en/Content/PASIMP/Configuring-Recording-and-Audits-in-PSMP.htm

PSMP Internal User Cred file creation:  
For 12.0 and below  
https://cyberark-customers.force.com/s/article/PSMP-How-can-I-create-or-update-the-credential-files-credfile-for-the-PSMP-manually

For 12.1 and above  
https://cyberark-customers.force.com/s/article/PSMP-How-can-I-create-or-update-the-credential-files-credfile-for-the-PSMP-manually-12-1-and-above-ONLY

PSMP Debugging:  
https://cyberark-customers.force.com/s/article/How-to-set-debug-log-levels-on-PSMP-integrated-mode  
https://cyberark-customers.force.com/s/article/00003368

rpm -ivh  
-i : install a package  
-v : verbose for a nicer display  
-h: print hash marks as the package archive is unpacked.  
https://www.tecmint.com/20-practical-examples-of-rpm-commands-in-linux/

=================================================================================  
-Authorized Interfaces  
-Automatic Password Management  
 -interval  
 -Immediate Interval  
 -HeadStart Interval  
https://cyberark-customers.force.com/s/article/00004112

-----------
-Onboarding & Managing BindAccount,PSMConnect,PSMAdminConnect
-Administrator Account Management
-PSM-PrivateArk client connection
===

-Backup & Restore Activities  
-AllowNonStandardFWAddresses(allow ports)  
https://cyberark-customers.force.com/s/article/00002003  
-Login with Master User  
  You need:  
    -Master CD(RecPrv.key)  
    -Master User password  
    -Vault server login access.  
 How to Login with the Master User?  
 1.We have to make sure that the MasterCD is available and copied to the Vault server.  
 2.Update the RecPrv.key path in the DBParm.ini with the help of "RecoveryPrvKey" Parameter.  
 3.Restart the vault service(PrivateArk Server service)  
 4.Login with master user using privateArk authentication.
 
->How to reset the master user password?

==========  
-***DR Activity  
-PSMP-AD Bridging  
https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/Latest/en/Content/PASIMP/Integrating-with-AD-Bridge.htm

**psmp Connection String:

	Vaultusername@linuxtargetuser@linuxtargetserver ip/address@PSMPServerip

**PSMP-ADBridging Connection String:

	linuxtargetuser@linuxtargetserver ip/address@PSMPServerip

Real time issues/component wise.  
https://blog.51sec.org/2019/07/cyberark-notes.html  
https://blog.51sec.org/2019/11/cyberark-pta-solution-issues-and.html  
https://blog.51sec.org/search?q=cyberark

HSM Introduction:  
https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/Latest/en/Content/PAS%20INST/configuring-HSM-Key-Management.htm  
-Upgrade activity

1. Checking the compatibility version between the components and we will finalize the version.
2. We will list out all the components which need to be upgraded.
3. Prepare the Upgrade document
4. We will do health check of the CyberArk components by verifying the logs, event viewer messages and will get clarified.
5. We will raise the changes for upgrade activity.
6. We will take the backup/snapshot of the server
7. We have to blockout the monitoring(services/event messages)
8. We will communicate with end users with outage details.
9. Change Execution..
10. Checks..Service checks, version checks, logs(upgrade)

-AAM Concept  
***-How to check product version of the each component.  
https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/12.1/en/Content/PASIMP/View-product-version.htm

-HTML5 GW  
**Change requests

For Revocation errors:  
https://cyberark-customers.force.com/s/article/A-revocation-check-could-not-be-performed-for-the-certificate  
https://cyberark-customers.force.com/s/article/PSM-Troubleshooting-The-connection-cannot-proceed-because-authentication-is-not-enabled-and-the-remote-computer-requires-that-authentication-be-enabled-to-connect#:~:text=%22A%20revocation%20check%20could%20not%20be%20performed%20for,could%20cause%20this%20particular%20error%20are%20as%20follows%3A
