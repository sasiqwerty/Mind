---
aliases: 
tags: 
date created: Wednesday, August 2nd 2023, 3:31:09 pm
date modified: Tuesday, September 19th 2023, 7:40:17 am
---
          

**Q1) what is CyberArk and why do we need it**?

Answ:-CyberArk provides centralized, tamper-proof audit records for all privileged access activities, with personal accountability for any access or usage of shared privileged accounts.

CyberArk creates a whole new layer of security on the inside called privileged account security, which controls, monitor and detect all-around activity with credentials and privileged account. As we know privileged are built into every piece of IT infrastructure and are most common exploited piece in any sophisticated attack, because once inside attacker needs credentials to move around to get the data they are trying to steel. CyberArk gives customers a way to put control over the credential to put lock where they can measure the overall security of privileged account

**Q2****) what is privileged account?**

Answ:- A privileged account is a user account that has more privileges than ordinary users. There are many kinds of privileged accounts like Root and administrator accounts are typically used for installing and removing software and changing configuration. They are super user accounts.

Examples:  Root -Linux

                     Administrator-Windows 

                     SA-Oracle    

                      Enable-Cisco

**Q3) what are different types of privileged accounts?**

Answ:- They are different types of Privileged accounts examples are

1. Local account

2. Domain account

               3. Service account

               4. Shared account

**Local accounts**: A local account controls access to one single, physical computer. Your local account credentials (username, password, and SID/UID) are stored locally on the computer's hard drive, and the computer checks its own files to authenticate your login. ... A local account allows you some level of access to an individual computer.

**Domain account**: A domain user is one whose username and password are stored on a domain controller rather than the computer the user is logging into. When you log in as a domain user, the computer asks the domain controller what privileges are assigned to you.

**Service account**: A service account is a special user account that an application or service uses to interact with the operating system. Services use the service accounts to log on and make changes to the operating system or the configuration. Through permissions, you can control the actions that the service can perform.

**Shared account**: Shared accounts are any resource that uses a single pair of credentials to authenticate multiple users. ... The challenges shared accounts hold for IT: Activity Tracking and visibility: The basic premise of identity and access management (IAM) knows who accessed which resource.

**Q4) what is identity access management?**

Answ:-Identity and access management is the information security discipline that allows users access to appropriate technology resources, at the right time. ... Once a user successfully completes the authentication process, the IAM system must then verify the user's authorization to perform the requested activity.

Identity and access management (IAM) in enterprise IT is about defining and managing the roles and access privileges of individual network users and the circumstances in which users are granted (or denied) those privileges. Those users might be customers (customer identity management) or employees (employee identity management. The core objective of IAM systems is one digital identity per individual. Once that digital identity has been established, it must be maintained, modified and monitored throughout each user’s “access lifecycle.

**Q5) what is EPV?**

Answ:-Enterprise Password Vault – CyberArk’s   Enterprise Password

Vault (EPV) enables organizations to secure, manage, automatically change and log

All activities associated with all types of Privileged Passwords.

        It uses a highly secure central repository to store and protect both SSH keys and passwords for use in on-premises, hybrid and cloud environments. In addition, its auditing and control features mean you can track and identify the misuse of any privileged accounts.

Administer, secure, rotate and control access to privileged account passwords

**Q6) what are vault security layers?**

Answ:-

**Firewall & Code Data Isolation**-The Vault must run on a dedicated server, eliminating security holes in third party Product. This is enforced by the CyberArk firewall, which doesn’t let any communication into the server or out of it other than its own authenticated protocol – the Vault protocol. No other component is able to communicate with the outside world, except for the

Storage Engine. The fact that the Vault’s code is the only code that runs on the dedicated

Server assures a sterile environment and total control over the server by the security System.

**Encrypted Network Communication & Visual Security Audit Trail**- Every password and file stored on the Vault is encrypted, using an encryption infrastructure that is totally hidden from the end user. This means that neither users nor administrators need to concern themselves with any key management issues.

The Vault's Visual Security is the first and only technology that lets Users see activities Carried out in their Safes by other Users. Real-time monitoring of who is logged on to the Safe and the information they have retrieved enables Users to track passwords and files in the Vault. Other Visual Security features inform Users whenever activity occurs in the Vault, and mark passwords and files so that those that have been accessed by other Users are noticeable immediately.

**Strong Authentication & Granular Access Control**-Every access to the Vault must be authenticated. The Privileged Account Security Solution uses a strong two-way authentication protocol. Authentication is based on Passwords, PKI digital certificates, RSA SecurID tokens, RADIUS protocol, USB Tokens, or Windows authentication. Taking the latter approach requires no additional Authentication to be made by the end-user. The Privileged Account Security solution also supports third-party authentication that can be integrated into the organization's existing Authentication server.

The Privileged Account Security solution provides a built-in access control mechanism. Users are totally unaware of passwords or information that is not intended for their use. Users can be permitted to read, write, delete, or administer data according to the access Control rules.

**File Encryption & Dual Control Security**-Every password and file stored on the Vault is encrypted, using an encryption infrastructure that is totally hidden from the end user. This means that neither users nor administrators need to concern themselves with any key management issues

**Q7) what is the latest version of CyberArk and its salient features?**

 Answ:-Present 12.1 latest versions available in market

Privileged Session Manager for SSH connections with modern authentication methods, including SAML, and single multi-factor authentication to multiple targets:

Security teams often wish to enforce modern authentication methods such as SAML and OpenID Connect with strong MFA in their PAS solution. While this can be set up for PVWA access, PSM for SSH did not support all the authentication methods that PVWA does. In this version we are introducing a new way to authenticate to PSM for SSH, which enables using the same authentication methods in both PVWA and PSM for SSH.

CyberArk Telemetry tool:-

Starting from this version, we are introducing a new CyberArk Telemetry tool for CyberArk Privilege on-premises deployments that presents and stores information regarding the usage and adoption of CyberArk PAS components in customer deployments.

Vault:-

Enhanced availability and robustness of syslog integration

Following an infrastructure change in the syslog message queuing mechanism, the Vault can now withstand large scale and high load activity as well as endure slow communication or high latency between the Vault and the syslog servers or when the syslog servers are unavailable.

Additional configuration options in DBParm.ini enable customers to control the message concurrency capacity according to the size of the environment and to manage the queue size.

Password Vault Web Access:-

Platform Management enhancements:

In this version we expanded the Platform Management interface to include access workflow policies indications, showing workflow-related settings and exceptions for each platform. This enables customers, using a single pane of glass, to gain better visibility of a platform and its effective policy.

REST APIs:-

This release provides several improvements in our REST API Web services around the Accounts, Safes and User Management areas for easier automation and usage.

The following new APIs were added:

Get secret versions - Returns the versions of the account's secret.

Link an account - Enables you to associate an existing account as a linked account of a different account. The linked account can be a Reconcile Account, a Logon Account or any other linked account defined on the platform level.

Delete Safe - Deletes an existing empty Safe.

Add member - Adds a user or a group as a member with a specific set of permissions to an existing Safe.

Delete discovered accounts - Enables Vault Admins to clear all Discovered Accounts and their dependencies from the Pending List.

Security improvements:-

Internal components were upgraded to enhance security and make technological improvements to the operating system and third-party components for the PVWA Server.

Central Policy Manager:-

Upgrade improvements:

As part of our installation improvements and simplification of the hardening process, the CPM installation now supports incremental hardening.

Customers can choose whether to run only the latest updates of the hardening script. This enables customers to keep the capabilities they re-enabled after the last hardening that disabled them.

PSM for SSH deployment on Amazon Linux 2:-

Starting from this version, PSM for SSH can be deployed on the next generation of Amazon Linux - Amazon Linux 2.

On-Demand Privileges Manager:-

OPM deployments on Ubuntu

OPM and OPM-PAM can now be deployed on Ubuntu 16.04, 18.04, 18.10, 20.04 and 20.10.

Note: This feature is available from OPM 12.0.

Privileged Threat Analytics:-

PTA scale improvements

This version of Privileged Threat Analytics introduces an additional improvement to the performance of the PTA server.

The server performance was increased to 4000 audits per second by optimizing and refactoring our internal components in the syslog pipeline.

Support MFA for Azure and AWS IAM users:-

Azure and AWS PSM connectors now support logging in to the cloud console with the IAM user enforced with Multi-factor Authentication (MFA). The user must enter the MFA code during the login sequence, therefore this step will be promoted to the user via the RDP session.

Application Access Manager - Credential Providers:-

Credential Provider

Added platform support for Centos 8 and AIX 7.2 TL5 from Credential Provider v11.4

Credential Provider for z/OS

The new version of Credential Provider for z/OS includes bug fixes as well as a new end-user license agreement.

This release includes the following updated components:

Java Provider

C SDK

Java SDK

**Q8)** **what does operator CD & masters CD contain?**

Answ:-

Master CD contains:-

Recovery private key

Recovery public key

Random database key

Server key

Operator CD contains:-        

                        Recovery public key

                        Random database key

                        Server key

**Q9) what are the system requirements for installation of digital vault server?**

 Answ:-Before installing the Vault, make sure that you have the following:

**Q10) what are prerequisites for installing digital vault server?**

 Answ:-

Ø  Vault Installation Package

Ø  The CyberArk Vault installation CD

Ø  MasterCD

Ø  Operator CD

Ø  License file

Ø  Installation documentation

Software prerequisites:

·     Windows 2016 server

·     Windows 2012 server

·     .NET Framework

**Q11) what is standalone vault& cluster vault installation?**

 Answ:-A standalone installation is typically used for a scenario where only one computer or one user will be accessing the program and no other workstations or computers will connect to it in order to access the database. Other scenarios may include a need for a machine used for testing or retrieving data from a backup.

 A cluster installation requires the session information to be saved and shared among the nodes. The session information can be stored either in the SQL Server database or in Redis - an in-memory database. It has 2 Vault Servers which acts as Active Passive mode.

**Q12) what is RCA & how to monitor digital vault with it?**

 Answ:- The Enterprise Remote Control Agent is the software that allows you to take control of a PC. The CyberArk Vault Remote Control feature enables users to carry out several Operations on Vault components from a remote terminal.

Managing the Vault, DR Vault, ENE, and CVM from a Remote Location The following table displays the commands that can be used with the PARClient utility to manage the Vault, DR Vault, ENE, and CVM from a remote physical location

**Q13) what is CyberArk hardening?**

 Answ:-CyberArk installs the Vault Server on a hardened operating system, based on Microsoft Bastion Host server recommendations which define a highly secured Windows server. The hardening process is performed as part of the Vault installation and results in disablement of many operating system services. The hardened Vault Server is designed to serve only CyberArk protocol requests. As such, it may not function as a regular domain member in a Windows network. In addition, the hardening process also strips the permissions from existing and built-in Windows users (except the user that runs the installation).

**Q14) what is the purpose of administrator account & master account?**

 Answ:-

Master account is used for retrieving the Administrator accounts. Whenever Administrator accounts are blocked / suspended by using master account we can activate the administrator account.

Q15) what are the service of digital vault server?

Answ:-

Ø  CyberArk event notification engine.

Ø  CyberArk logic container.

Ø  CyberArk windows hardened firewall.

Ø  Private ark database.

Ø  Private ark remote control agent.

Ø  Private ark server.

**Q16) what are the log files of vault servers?**

 Anws:-Log files related to vault server are ITA.log, trace logs

**Q17) what are the configuration files of vault server?**

 Answ:- Vault configuration files are

Ø  Dbparm

Ø  Paragent(Remote control agent)-9022

Ø  Passparm(Password management)

Ø  Tsparm(safes directory)

Ø  Vault

**Q18) what does licence.xml file contain?**

 Answ:- **:** .XML contains

Ø  Customer’s unique ID.

Ø  The type of Vault that is installed.

Ø  The version of the license.

Ø  The license key.

Ø  Licensed components.

Ø  The number of EPV Users permitted to work with the CyberArk Vault

Ø  Whether or not to enable high availability clustering.

Ø  Whether or not to enable a connection with an external directory.

Ø  Whether or not to enable Disaster Recovery features.

Ø  Whether or not to enable Remote Monitoring in the Vault.

Ø  Whether or not to enable backup by third party software

Ø  The types of authentication that are permitted by the Vault.

Ø  The types of Clients that the Vault will recognize.

**Q19) what is Dbparm.ini file & what does it contain?**

 Answ:- Dbparm.ini is the main Configuration file of Vault server and it contains the details of Server Keys like Recovery private key,backup key ,Recovery public keys info and also debug levels,Time stramps and syslog and radius server info and if any Non standard firewall addresses.

**Q21) what is safe & what does it contain?**

 Answ:-A safe is a logical container for storing passwords. Safes are typically created based on who will need access to the privileged accounts whose passwords will be stored within the safe. For instance, you might create a safe for a business unit or for a group of administrators

**Q22) what are the default safe that will be created after digital vault installation?**

 Answ:- Default safes are                                                           

1. Systemsafe

2. Vault internal

3. Notification Engine

**Q23) what does system safe contains?**

 Answ:-System safe contains configuration files, license file and log files of vault server.

Ø  dbparm.ini

Ø  italog

Ø  license.xml

Ø  paragant.log

Ø  passparm.ini

Ø  tsparm.ini

**Q24) what does Vault internal safe contain?**

 Answ:-LDAP configuration details.

**Q25) How will you enable debug logs of Digital vault server?**

 Answ:-Debug Logs of Vault server can be enabled in 2 ways One from Server Administrative Console and other way is by mentioning debug levels in Dbparm.ini

  

  

  

**Q26) Is it possible to remove the hardening of digital vault server once it is hardened?**

 Answ:-Not possible we have to re-build the OS If at all need to remove Unistall the Vault and remove the Hardening parameters from the Registry path

**Q27) why the vault server should not be part of Domain?**

 Answ:-The Vault’s DNS sever settings should remain empty to eliminate the risk of attack initiated through compromised DNS servers

**Q28) what is the purpose of CyberArk logic container service?**

 Answ:-The logic container (LC) service is a part of the CyberArk Vault installation and acts as part of the vault in a sense. It is installed on the server machine as a separate service written in .NET which uses NHiberbate* to access the database, this was introduced with the release of version 8.0.

It uses new tables however can also interact with the existing tables which means that quick progress can be made without making changes to the vault or as much as possible. The main purpose of the LC is to create a layer of abstraction, such that will allow us to extend our use of the database without making major changes to the server. As its name implies it hold a lot of the new logic of the EPV flow.

It is also important to note that LC users (e.g. CPM, PVWA) still need to go through the server normal protocol to get access to the LC, so all security mechanisms still apply

 Logic container is also responsible to implement the master policy logic

**Q29) what is private ark Client?**

 Answ:- The PrivateArk Client is a standard Windows application which is used as the administrative client for the PAS Solution. The Client can be deployed on multiple remote computers and can access the Enterprise Password Vault via LAN, WAN, or the Internet through the Web version of the client. From this interface, the users define a vault hierarchy and create safes. Access to the Enterprise Password Vault via the PrivateArk Client requires a user to be validated by the Digital Vault

**Q30) what is tsparm.ini?**

 Answ:-The TSParm.ini file, in the Server\Conf installation folder, contains the list of directories that can store Safes databases

**Q31) what is the order of installing the CyberArk components?**

  Answ:-CyberArk order of installation:

< 10.8:-

Ø  Vault

Ø  CPM

Ø  PVWA

Ø  PSM

> 10.8:-

Ø  Vault

Ø  PVWA

Ø  CPM

Ø  PSM

**Q32) what are default built-in users & groups that are created for CyberArk implementation?**

 Answ:-After cyberark implementation default users and groups are:

Ø  Auditor

Ø  Administrator

Ø  Batch

Ø  Master

Ø  NotificationEngine

Ø  PSMApp_WIN

Ø  PVWAAppUser

Ø  PVWAGwUser

Ø  Auditors  groups

Ø  Notification Engines group

Ø  PSMAppUsers group

Ø  PSMLiveSessionTerminators group

Ø  PSMMaster group

Ø  PVWAGWAccounts group

Ø  PVWAMonitor group

Ø  PVWAUsers group

**Q33) what is CPM?**

 Answ:-The Central Policy Manager:

The Privileged Access Security solution provides a revolutionary breakthrough in password management with the CyberArk Central Policy Manager (CPM), which automatically enforces enterprise policy. This password management component can change passwords automatically on remote machines and store the new passwords in the EPV, with no human intervention, according to the organizational policy. It also enables organizations to verify passwords on remote machines, and reconcile them when necessary.  The CPM generates new random passwords and replaces existing passwords on remote machines. The new passwords are then stored in the EPV where they benefit from all accessibility and security features of the EPV. Due to the Privileged Access Security solution distributed architecture, additional CPMs can be installed on different networks to manage passwords that are all stored in a single Vault. The Vault also supports shared configuration files for additional CPMs in high availability implementations, and password management per Safe in load-balancing implementations. This flexibility enables the Privileged Access Security solution to support complex distributed environments, for example where several data centers are managed by one Vault.

**Q34) what are the system requirements for installing CPM?**

 Answ:-TCP/IP connection to the Digital Vault Server.

**Q35) what are the prerequisites for installing of CPM?**

Answ:- Install  .net Framework 4.5.2

**Q36) what is the default port by which all components of servers will able to connect to the vault server?**

 Answ:-**:** Default port of CyberArk Vault TCP/IP port number is 1858

**Q37) 1858 port can be altered?**

 Answ:-No, If want to alter we need to consult CyberArk OEMs

**Q38) what is DEP & how to disable it in cpm server?**

 Answ:-Data Execution Prevention (DEP) is a security feature that can help prevent damage to your computer from viruses and other security threats. Harmful programs can try to attack Windows by attempting to run (also known as execute) code from system memory locations reserved for Windows and other authorized programs

**Q39) what are the default safes that will be created after cpm installation?**

 Answ:-Default safes of CPM are

Ø  PasswordManager

Ø  PasswordManager_ADInternal

Ø  PasswordManager_Info

Ø  PasswordManager_Pending

Ø  PasswordManager_workspace

Ø  PasswordManagerShared

**Q40) what does password manager contain?**

 Answ:-Password manager safe contains ADConfiguration.xml, cpm.ini files.

**Q41)what is the configuration file of cpm?**

 Answ:-_**cpm**_.ini _**file**_

**Q42) what are the log files related to the cpm?**

 Answ:-

Ø  PM

Ø  PM_error

Ø  PMConsole

Ø  PMTrace

Ø  ThirdParty levels

**Activity Log (logs folder)-** pm.log –contains all the log messages, including general and informative messages, errors, and warnings.

pm_error.log –contains only warning and error messages.

**Third part Logs-** Generated by the Central Password Manager built-in password generation plug-ins when an error occurs. Root log, console log, expect log and debug log.

**History Log files**- After a log file has been uploaded into the Safe, it is renamed and moved into the History subfolder.

**Q43) what are the services related to cpm?**

 Answ:- CPM services are CyberArk Password Manager ,CyberArk Central Policy  manager Scanner.

**Q44) what is the purpose of CyberArkPassword Manager service?**

  Answ:-The Privileged Account Security solution provides a revolutionary breakthrough in password management with the CyberArk Central Policy Manager (CPM), which automatically enforces enterprise policy. The CPM generates new random passwords and replaces existing passwords on remote machines.

**Q45)what is the default user name of cpm?**

 Answ:-Password Manage- which is responsible for Password Managements

**Q46)what are cpm process file & Prompt file and where they are located ?**

 Answ:-process file contains  the work flow of cpm for password Management

 Prompt file contain server end prompts which will manage the passwords  Example:

Enter Password | Enter the Password | Retype Password | Reenter Password etc

 path location  is "(c\program filesx86\cyberark\password manager\bin)"

**Q47) How to enable debug log of cpm ?**

 Answ:-Debug logs can be enabled from platform level and also by mentioning debug Information in Process File:

  

**Q48 ) what does password manager shared safe contain?**

 Answ:-Policies.ini files

The .ini files in the PasswordManagerShared safe contain the Automatic Password Management section for each platform

**Q49) which user is responsible for managing passwords?**

 Answ:- Password Manager

**Q50) what are the system requirements of PVWA?**

 Answ:-The minimum requirements for the PVWA are as follows:

**Q51) what are the prerequisites for installation of PVWA?**

 Answ:-IIS server (internet information services), Windows Server must be a domain member.

**Q52) what is password vault web access?**

 Answ:- The Password Vault Web Access Interface is a complete featured web interface providing a single console for requesting, accessing, and managing privileged account credentials passed throughout the enterprise by both end users and system administrators.

**Q53) what are the default safes are created after PVWA installation?**

 Answ:-PVWA default safes are

Ø  PVWAConfig

Ø  PVWAPrivateUserPrefs

Ø  PVWAPublicData

Ø  PVWAReports

Ø  PVWATaskDefinations

Ø  PVWATicketingSystem

Ø  PVWAUserPrefs

**Q54) what does PVWA CONFIG safe contain?**

Answ:- Polices.xml and PVConfiguration.xml

**Q55) what is the configuration file of PVWA?**

 Answ:- PVConfiguration.xml

**Q56) what are the log files related to PVWA?**

 Answ:-PVWA log files are

Ø  CyberArk.Web console.log

Ø  CyberArk.WebApllication.log

Ø  CyberArk.WebTaskEngine.log

**Q57) what are the services related to PVWA?**

 Answ:-

PVWA services are:-

Ø  IIS Admin Service(IIS ADMIN)

Ø  Windows Process Activation Service

Ø  World Wide Web Publishing Service.

**Q58) what is HTTP & HTTPS Connections and their port  numbers?**

Answ:- The URL starts with either HTTP or HTTPS: Hypertext Transfer Protocol (HTTP) is the indication of unsecured protocol that uses the port number 80 and Hypertext Transfer Protocol Secure (HTTPS) shows your connection is secure via 443 port

**Q59)** **what does policies.xml file contain?**

Answ:- The Policies.xml contains the “UI & Workflow” settings for all platforms.

The PlatformBaseID, ties the platforms listed in the Policies.xml with the platforms contained in the PasswordManagerSharedsafe

**Q60) what are the default users and groups that are created after installation of PVWA?**

 Answ:-

Ø  PVWAAppUser

Ø  PVWAGwUser

Ø  PVWAGWAccounts group

Ø  PVWAMonitor group

Ø  PVWAUsers group

**Q61) what are the system requirements for installation of PSM?**

  Answ:-

Ø  TCP/IP connection to the CyberArk Password Vault Server

Ø  Windows 2012/2016

Ø   PSM setup

Ø  Windows Server must be a domain member.

Ø  RDS Cal licenses

**Q62) what are the prerequisites for installing PSM?**

 Answ:-Prerequisites of PSM are RD Web access, RD Connection broker and RD Session host,

Only Windows Server 2012 R2, Windows Server must be a domain member, User logged in during installation must be a Domain User with local admin rights.

Ø  RD Web access: Remote desktop web access enables user to connect to resources provided by session collections and virtual desktop collections by using the start menu or web browser.

Ø  RD connection broker: Remote Desktop connection broker connects or reconnects a client device to RemoteApp programs, session-based desktops and virtual desktops.

Ø  RD session host: Remote desktop session host enables a server to host RemoteApp programs or session-based desktops.

**Q63) what is the functionality of PSM?**

 Answ:-Privileged Session Manager® The Privileged Session Manager (PSM) enables organizations to control and monitor privileged accesses to sensitive systems and devices. PSM provides privileged session recording with DVR-like playback and text recording, as well as secure remote access to sensitive systems using privileged single sign-on, and without divulging the used credentials to the end users.

**Q64) why do we need RDS licensing?**

 Answ:-CAL licences.

A client access license (CAL) is needed for each user and device that connects to a Remote Desktop Session (RDS) host. An RDS licensing server is needed to install, issue, and track RDS CALs. When a user or a device connects to an RD Session Host server, the RD Session Host server determines if an RDS CAL is needed.

Connecting to the PSM Server with Microsoft Remote Desktop Services (RDS) Session Host Make sure you have the appropriate RDS CAL licensing. PSM can work with any RDSCAL License scheme (either per user or per device).

**Q65) what is the purpose of RDS connection broker, Web Access, Session Host?**

 Answ:-

**RDS connection broker:**

Remote Desktop Connection Broker (RD Connection Broker) manages incoming remote desktop connections to RD Session Host server farms. RD Connection Broker handles connections to both collections of full desktops and collections of remote apps. RD Connection Broker can balance the load across the collection's servers when making new connections. If a session disconnects, RD Connection Broker will reconnect the user to the correct RD Session Host server and their interrupted session, which still exists in the RD Session Host farm.

**Remote Desktop Web Access:**

Remote Desktop Web Access (RD Web Access) lets users access desktops and applications through a web portal and launches them through the device's native Microsoft Remote Desktop client application. You can use the web portal to publish Windows desktops and applications to Windows and non-Windows client devices, and you can also selectively publish desktops or apps to specific users or groups

**Remote Desktop Session Host** (RDSH) is a role in Remote Desktop Services (RDS). RDSH can host Windows session-based applications and desktops that can be shared with users remotely. To access applications or desktops remotely, users need to be on a network connection

**Q66) what is the default safes where the recordings will be stored?**

 Answ:All the recordings will be stored in PSMRecordings Initially will be stored on PSM Server and then will be uploaded to Vault Server

**Q67) what are the default safes created after installation of PSM Installation?**

 Answ:-**:**Default safes that are created after PSM installation

Ø  PSM

Ø  PSMLiveSession

Ø  PSMUnamanagedAccounts

Ø  PSMRecordings

**Q68) what does PSM Safe contain?**

 Answ:-PSM Safe contains PSMAdmin and PSMServer.

**Q69) what are the default accounts created after PSM installation?**

 Answ:-

Ø  PSMAppUsers

Ø  PSMGwUsers

Ø  PSMLiveSessionTerminators group

Ø  PSMMaster group

**Q70) what are the PSM Connect & PSM Admin Connect?**

 Answ:-During installation, the following users are created locally on the PSM machine:

-PSMConnect–used by end users to launch a session via the PSM.

-PSMAdminConnect–used by auditors to monitorlive sessions

**Q71) what is the PSM Shadow users group?**

 Answ:-.Sessions for Non-RDP client applications (WinSCP, Putty etc.) are launched on the PSM server using the PSM Shadow User accounts

**Q72) what are the log files related to PSM?**

 Answ:-PSM log files are PSMConsole and PSMTrace

**Q73) what are the services related to PSM?**

 Answ:-CyberArk Privileged Session Manager

**Q74) what is the configuration file for PSM?**

 Answ:- basic_psm

**Q75) what is the formula for storage calculation of PSM Recordings?**

 Answ:-

**Q76) what are the certifications available on CyberArk?**

Answ:-

Ø  Level One: Trustee

Ø  Level Two: Defender

Ø  Level Three: Sentry

Ø  Level four: Guardian

**Q77) Are you CyberArk Certified ?**

Answ:-I am Trustee Certified and have planned Defender and Sentry together in next month hope will be Cleared by next month.

**Q78) what is CyberArk HA Cluster?**

 Answ:-The Vault can be installed as a high-availability cluster of servers which provide constant access to the accounts in the Vault. In this implementation, there is always one Server that is on standby in case the other Server in the cluster fails i.e Active Passive mode

**Q79) How will you implement CyberArk HA Cluster?**

 Answ:-

Ø  Make sure all prerequisites are in place.

Ø  Install vault server on node A

Ø  Do the cluster configuration in cluster vault.ini file

Ø  Copy the operator keys to node B

Ø  Stop the CVM on node A and make sure the disks are in offline.

Ø  Install the vault server on node B.

Ø  Do the cluster configuration in cluster vault.ini file

Ø  Vault id and server id should be same on both nodes.

Ø  Start CVM on node A

Ø  Do the failover from active node to passive node and vice versa.

Ø  Now install the components in the following order.

Ø  PVWA,CPM and PSM

**Q80)  what are the system requirements for vaults installation in HA Cluster?**

 Answ:-

Cluster Vault and Cluster DR Vault servers The following table lists the recommended

Software prerequisites:

Windows 2016 English Edition Windows 2012 R2 Standard Edition

Windows 2012 R2 English/German versions

Windows 2008 R2 SP1 (64-bit) Enterprise Edition English/German version (for upgrades of existing deployments only)

.NET Framework 4.5.2

Note: Cluster Nodes must be installed only on physical servers.

**Q81). what are the prerequisites for installing vaults in HA Cluster?**

 Answ:-Prerequisites of HA-Cluster is

Ø  Dedicated SAN and Shared Storage

Ø  Two identical vault servers

Ø  Virtual IP address

Ø  Each node should have only one single static IP

Ø  It is highly recommended that both nodes have the same amount of physical memory

Ø  The clocks on both cluster nodes must be synchronized

Ø  The two Cluster Vault Nodes must be connected directly via a private network or cross-over cable.

Ø  If the storage is based on iSCSi(network storage) then a Windows update (KB2955164) should be installed in order to ensure database stability.

Ø  Ensure that the drive letters for the Quorum and Storage disks are identical in both nodes.

Ø  Ensure that the shared storage resources are only online in one node.

Ø   Make sure that servers are reachable via public ip, private ip and virtual ip.

Ø  Vault Servers (Primary, DR, Satellite)  For each HA Cluster Pair, 2x Vault Servers (Node 1 and Node 2) – Windows 2012 R2 64-bit Standard Edition:

Ø  The Vault servers  is highly recommended to be on physical servers for security and performance purposes. If this is an issue, please contact CyberArk Professional Services.

Ø  The server should be installed as a clean image from ISO, rather than a normal domain image that’s been cleaned to avoid any GPO impact

Ø  .NET Framework 4.5.2 Feature Installed

Ø  2x shared disks via SCSI or Fiber (SAN) attached storage

Ø  Primary disk for data storage based on Vault data size calculations

Ø  Secondary disk for Quorum verification with at least 500MB

Ø  These disks should not be used by any other system

Ø  If SAN is used, these should be on separate LUNs

Ø  Both the Quorum and the Data disks MUST be provisioned as an MBR partition table, NOT a GPT partition table

Ø  Public and Private NICs

Ø  Private NICs should be connected by a crossover cable or be on an isolated /30 VLAN

Ø  Three (3) public IPs, 2 private IPs

Ø  Node 1 public, Node 2 public, Vault VIP

Ø  Node 1 private, Node 2 private

Ø  2 IPs for Out-of-Band management (iLo/DRAC)

Ø  DO NOT install any third party software; this includes Antivirus, Spyware, Backup, Monitoring software.

Ø  The server should not be part of the domain.

Ø  Install the latest Microsoft Patches and updates and verify that they do not have MS Windows Update active (setup to “Never Check”)

**Q82) what is ISCSI Storage?**

 Answ:- : ISCSI stands for Internet Small Computer Systems Interface. iSCSI is a transport layer protocol that works on top of the Transport Control Protocol (TCP). It enables block-level SCSI data transport between the iSCSI initiator and the storage target over TCP/IP networks

**Q83) what is the SAN Storage that you are using in your organization?**

 Answ:-Fiber Cable Channel(FC channel)

**Q84) what is the service related to cluster vault?**

 Answ:-ClusterVaultmanager (CVM)

**Q85) what is the configuration file for cluster vault and what does it contain?**

 Answ:-ClusterVault.ini

**Q86) what is the log file of cluster vault?**

 Answ:-

Log files of HA-Cluster are

Ø  ClusterVaultConsole.log

Ø  ClusterVaultTrace.log

**Q87) what is the command for assigning identifiers for storage disk?**

 Answ:-StorageManager.exe -qQ -sS

**Q88) How will the components in  HA cluster communicate to the Vault Server?**

 Answ:-All the components will communicate the HA Vault Server via VIP

**Q89) which keys are responsible for replicating the data from node A to node B?**

 Answ:-ReplicationUser.pass Key

**Q90) How will you reflect client logo in pvwa login page?**

 Answ:-**:** Replace the logo in below path

C:\inetpub\wwwroot\PasswordVault\images

- changes Logon_home_Img with your organisation logo

**Q91) How will you grant report permission to a user or group?**

 Answ:-He should be part of PVWAmonitor group and Auditor role

**Q92) what are the default ports for LDAP?**

 Answ:-LDAP:-389

                LDAP Secure:636

                LDAP Farm: 3269 (Multiple Domains in a Single Farm)

**Q93) How will you do Active directory integration with CyberArk?**

 Answ:- Create an LDAP Bind account with READ ONLY access to the directory.

 - Have the User Name, Password, and DN available.

- Create three LDAP groups for granting access to the vault.

- CyberArk Administrators • CyberArk Auditors • CyberArk Users

**Q94) How will LDAP S integration with CyberArk via 636 port?**

 Answ:-

CyberArk strongly recommend you use LDAP/S :

This ensures that all of the traffic between the Domain Controller or LDAP authenticating Server and the Vault is encrypted

- Install the Root Certificate for the CA that issued the certificate on the directory servers to the Vault Servers.

 - Create a hosts file on the vault servers to manually resolve directory server namesWe strongly recommend you use LDAP/S

**Q95) what is the purpose of BINDUSER Account?**

 Answ:-LDAP Bind User-A user with read access to Active directory passwords With this account Vault is authenticated with Active Directory

Bind operations are used to authenticate clients (and the users or applications behind them) to the directory server, to establish an authorization identity that will be used for subsequent operations processed on that connection, and to specify the LDAP protocol version that the client will use.

Binding is the step where the LDAP server authenticates the client and, if the client is successfully authenticated, allows the client access to the LDAP server based on that client's privileges. Rebinding is simply doing the process over to authenticate the client

**Q96) what are the directories supported by CyberArk?**

 Answ:-CyberArk supports Active Directory, Oracle Internet Directory, Novell edirectory, IBM Tivoli DS etc

**Q97) what are the default groups that will get mapped when AD integration done with CyberArk?**

Answ:-

Ø ADMINS GROUP,

Ø AUDITORS GROUP,

Ø USERS GROUP are the default groups that will get mapped when AD integration done with CyberArk

**Q98) In how many ways safes can be created?**

Answ:-Safe is a logical container it stores privileged accounts stored in the form of files.

Safes can be created in the following ways

Ø  Privateark client

Ø  PVWA

Ø  Pacli script

Ø  ReatApI

**Q99) what is Object Level Access Control (OLAC)?**

 Answ:-The Privileged Access Security solution provides granular access control for passwords and files that are stored in the Vault. Object level access enables you to control who can retrieve and use specific passwords and files in the Safe, regardless of Safe level member authorizations

**Q100) How will you assign cpm to the safes?**

 Answ:- Check mark the Password manager  option(Edit safe and assign cpm)

**Q101) what is safe retention period & how will change it?**

 Answ:-Note that version will not be deleted while still in the safe object history retention period which is defined below

**Q102) How will you change quota for a safe?**

 Answ:-Go to safe Properties and change the quota as per requirement

**Q103) what are the roles that you can assign of safe level?**

 Answ:-

Roles and permissions at safe level are:-

**Access:-**

Ø  Use accounts

Ø  Retrieve accounts

Ø  List accounts

**Account management:-**

Ø  Add accounts (includes update properties)

Ø  Update account content

Ø  Update account properties

Ø  Initiate CPM account management operations

Ø  Specify next account content

Ø  Rename accounts

Ø  Delete accounts

Ø  Unlock accounts

**Safe management:-**

Ø  Manage safe

Ø  Manage safe members

Ø  Backup safe

**Monitor:-**

Ø  View audit log

Ø  View safe members

**Work flow:-**

Ø  Authorize account requests (Level 1, Level 2)

Ø  Access safe without confirmation

**Advanced:-**

Ø  Create folders

Ø  Delete folders

Ø  Move accounts/folders

**Q104) what are the default platforms that CyberArk supports?**

 Answ:-Platform is different types of devices that support in CyberArk

**Q105)why do we need to duplicate platforms?**

 Answ:-Duplicate existing platforms and customize them to support accounts on target accounts according to very specific standards and inorder to apply polices at granular level

**Q106) How will you duplicate platforms?**

 Answ:-

Duplicating existing Platform

Click **ADMINISTRATION** -->Platformmanagent

Select an existing platform that is similar to the new target account platform, then click **Duplicate**.

**Q107) How will you import platforms?**

 Answ:-Administration>platform management>Import platforms

**Q108) How will you activate suspended user?**

 Answ:- We can activate the user in Trusted network area

From PrivateArk Tools->Administrative Tools->Users and Groups->Go to respective User

**Q109) What is purpose of user lock out in minutes in dbparm.ini?**

 Answ:-The purpose of User Lock Out Minute in dbparm.ini is allow suspended user after certain amount of time (minutes) that we assigned in it

**Q110) what are the default ports that needs to be enable from cpm server to the target server?**

 Answ:-Inorder to CPM  manage passwords Uni directional Firewall should be opened from our cpm servers to Target hosts

CPM to Linux,Vmware hosts,Cisco devices :22

CPM to Windows Targets: 135 139 445

CPM to MYSQL:1521-1526 Range

CPM to Oracle:1433

**Q111) In how many ways accounts can be onboarded?**

 Answ:-Accounts can be Onboarded in different ways

Ø  PUU

Ø  Manually

Ø  ResAPI

**Q112) what is Password Upload Utility?**

 Answ:-The Password Upload utility works with the CyberArk Password Vault to create password objects from a passwords list and store them in the Vault. This enables you to upload large numbers of passwords automatically and makes the Vault implementation process quicker and more automatic.

**Q113) How will you onboard Accounts using PUU?**

 Answ:-The PUU contains the executables and configuration files required to run the utility

Ø  Create the csv file.

Ø  Configure the vault address in vault.ini file

Ø  Configure  the credential file the running command createAuthFile.exe user.ini

Ø  Specify the csv file name in conf.ini file 

Ø  run command passwordupload.exe conf.ini

**Q114) what is the configuration file of PUU?**

 Answ:-conf.ini it contains

Os=windows

VaultFile=vault.ini

CredFile=user.ini

PasswordFile=passwords.csv

**Q115) what is the purpose of default templates safes?**

Answ:-These parameters define the default values for the configurable parameters of Safes that will be created through the Password Vault Web Access. They are stored in the SafeTemplate

**Q116)What are the Field or Values that are going to mention in CSV Template?**

  Answ:- Required:

|   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
|Password_name|Safe|Folder|Password|DeviceType|PolicyID|Address|UserName|

**Q117) What is command for Execution Password Upload Utility?**

 Answ:-Password Upload Utility.exe conf.ini

**Q118) what is the log file for PUU?**

 Answ:- Related log file of PUU is Password upload error.

**Q119) How will you run the cred file in order to communicate PUU to vault?**

 Answ:-CreateAuthfile.exe user.ini

**Q120) what is password Reconciliation?**

 Answ:-During password reconciliation, the unsynchronized password is replaced in the Vault and on the remote device with a new password that is generated according to the relevant platform. As soon as reconciliation is finished successfully, all standard verifications and changes can be carried out as usual.

**Q121) what is the difference between password change and reconcile?**

Answ:-Password change: CPM knows the current password

Change the password immediately (by the CPM) – Initiate an immediate password change in which the CPM will change the password to a new random password.

Specify the password for the next CPM change – Specify the password that the CPM will use the next time it changes the password.

Reconcile: CPM doesn’t know the current password

Reconciling a password for an account is synchronizing the password on the target machine with the password in the Vault, making them identical

  
**Q122)what is logon account & its purpose?**

 Answ:-A logon account can be used to initiate sessions to machines that do not permit direct logon. When a logon account is associated with a privileged account, it will be used to log onto the remote machine and then elevate itself to the role of the privileged user.

**Q123)what is Extrapass 1 parameter represents in csv file?**

  Answ:-Extrapass 1 to specify the logon account details

**Q124) what is ExtraPass 3 represents in csv file?**

  Answ:-ExtraPass 3 to specify the reconcile account details.

**Q125) How will you associate logon & reconcile account via Password Upload Utility?**

  Answ:-By specifying the accounts details like(password_name,safe,folder,password) & reconcile account details like (Extrapass3Name,Exrtapass3safe,Etrapass3folder) and run from puu

**Q126) What is dual control password access approval?**

 Answ:-Dual control can be configured in order to allow users to connect to a target device only after they receive approval or confirmation from an authorized safe owner

**Q127) How will you grant permission to approvers for dual control?**

 Answ:-The manual security workflow comprises the following steps:

1. The user creates a request: A user who wishes to access an account in an environment where the Master Policy enforces Dual Control must first create a request. In the request, the user specifies the reason for accessing the account, whether they will access it once or multiple times, and the time period during which they will access it. A notification about the request is sent to users who are authorized to confirm this request.

2. The request is confirmed or rejected by the authorized user: Through the notification, authorized users can access the request and view its details. Based on these details, authorized users either confirm or reject the request. The number of authorized users who are required to confirm requests is defined in the Master Policy.

3. The user connects to the account: Each time an authorized user responds to the request, the user who created it receives a notification. When the total number of required confirmations is received for the request, this user receives final notification. The user can now activate the confirmation and access the

Account according to the request specifications.

**Q128) what is access safe without conformation parameter at safe level?**

Answ:-when the user is granted with access safe without conformation he don’t need to request for anything and perform tasks directly when the dual control password access approval is in active mode

**Q129) what is check-in, check-out exclusive access?**

 Answ:-Enforce check-in/check-out exclusive access – Users can check out an account and lock it so that no other users can retrieve it at the same time. After the user has used the password, they check the password back into the Vault. Together with enforcing one-time password access, this restricts access to a single user, ensuring exclusive usage of the privileged account and guaranteeing accountability. By default, this rule is inactive.

Accounts Check-out and Check-in:

Auditing and control requirements demand full identification and monitoring of users who access privileged accounts during any given period. In addition, to guarantee accountability, each user who accesses a privileged account must be the only one to do so.

The Master Policy enables organizations to permit users to check out a ‘one-time’ password and lock it so that no other users can retrieve it at the same time. After the user has used the password, he checks the password back into the Vault. This ensures exclusive usage of the privileged account, enabling full control and tracking for the password.

If the organizational policy determines that a password can only be used once, the Master Policy can also be configured to change the password’s value before unlocking it and making it available to other users. If a CPM is installed, this can be done automatically

**Q130) How will you release account when exclusive access will configure?**

 Answ:- Under Account details we have Release Option or Edit account go to Advanced section and release. Also CPM will automatically release the account based on minimum validily period configured on the platform level

**Q131) what is onetime Password access?**

 Answ:- Use this rule to ensure that passwords are changed after each access. When a user retrieves an account, a password change process is initiated, and will occur automatically after a predefined timeframe.

**Q132) what is the purpose of Allow EPV transparent Connection Policy?**

 Answ:-Quick to connect.

Allow EPV transparent connections (‘click to connect’) – Users can connect to remote devices without needing to know or specify the required password. This prevents the password from being exposed to the user and maintains productivity as the user does not have to open a login session and then copy and paste the password credentials into it. In addition, advanced settings define whether or not users are permitted to view passwords. This enforces strong authentication for accessing managed devices and restricts user access to passwords according to granular access control.

**Q133) what is the purpose of required users specify reasons for access and how to disable it?**

 Answ:-As part of Audit records we are using this policy and Whenever the user is used to perform task on his account a pop message will come in order to mention the reason & it can be disabled by adding exceptions to particular platform

**Q134) what is audit retention period policy?**

 Answ:-The Master Policy controls the number of days that Safe activities audits are retained. By default, audits of activities are kept for 90 days

**Q135). How will you enable password policies for privileged accounts?**

 Answ:-Master policy>Password Management > select that policy & to Add Exceptions select a platform & specify Noof days require

**Q136) How will you enable session recording and isolation?**

 Answ:-Master policy>Session Management > select that policy & to Add Exceptions select a platform & specify No.of days require

**Q137) How will you monitor the PSM live session?**

 Answ:-

The MONITORING page enables intuitive access to all privileged session recordings. This page is visible to authorized users after the first recording has been uploaded to the Vault.

The Recording Details page enables a more thorough view of a specific session recording. The Account Details page provides access to recordings for individual passwords.

**Q138) How will you grant permission for an auditor in order to monitor live sessions?**

 Answ:-The user must be a member of auditors group & must be added to psmmaster group

**Q139) How will you grant permission for an Auditor to terminate live session?**

Answ:-Logon to privateArk>tools>administrative tools>Users and Groups>PSM Live Session Terminators>update>Add that particular user

**Q140) How & where PSM record will be generated & stored?**

 Answ:-Initially all the record will stored  on PSM Server in<C\programfiles86\cyberark\psm\recordings> after certain time they will automatically uploaded tovault into default safe i.e PSMRecordings

**141) Which user is responsible for monitoring the live sessions?**

 Answ:-PSMAdmin connect is responsible for monitoring the live sessionsfor an Auditor

**142) Is possible to customize the psm recordings?**

 Answ:-Custom recording safes can be defined at the platform level and are created automatically by the PSM when it uploads the first recordings to the Vault.

**143) How will you enable default users or built in user when they are suspended?**

 Answ:-In order to enable default user or built in user we have to run cred file from the specified installation path and update the same password for that user in PrivateArk

**144) How will you logon to the vault via master account?**

 Answ:-We can able to logon to vault via master account in two ways

Ø  From Server Administrator\terminial(RecoveryPrivate Key path shpuld be mentioned in DBParm.ini)

Ø  Emergency Station IP (When this is specified in DBParm.ini)

**Q145) Is it possible to logon into pvwa via master account?**

 Answ:-No (Master cannot be Impersonated)

**Q146) what is Disaster Recovery in CyberArk?**

Answ:-DR means Disaster recovery its same as vault server it uses whenever vault server goes down DR vault server will be automatically up and running. DR is a backup server.

The Disaster Recovery (DR) service that runs on the DR Vaults is responsible for replicating the data and metadata from the Production Vault, as described below. 

Data Replication – The DR Service replicates the external files (Safes files and Safes folders) from the CyberArk Production Vault to the DR Vault. Data replication is performed according to the settings in the Disaster Recovery configuration file (PADR.ini).

 Metadata Replication – The DR Service replicates the metadata files based on exports (full backup) and binary logs (incremental backups). Metadata replication from the Production Vault to the DR Vault occurs after each action in the Vault has been completed.

Replication of the metadata files (MySQL DB) based on exports (full backup) and binary logs (incremental backups)

Ø  Metadata replication from the Production Vault to the Disaster Recovery Vault occurs at the completion of each event

Ø  Since password objects are also stored in the metadata, password objects are always synced between production and DR.

**Q147) How will you perform DR drill in your organization?**

 Answ:-Before doing DR drill we will take the entire backup from vault server and need to check replicating the data or not till the date of DR drill.

Ø  Plan for down time

Ø  Plan for change freeze

Ø  Inform to customers about the activity and to use DR PVWA’s

Ø  Stop the production vault server

Ø  Check the PADR.ini file and make sure that enable failover mode is set to yes.

Ø  After 5 attempts of retries the DR vault server should be automatically up and running.

Ø  Monitor  the PADR.log

**Q148) what are the pre-requisites or prechecks that will you do before while going DR drill?**

Answ:-

Ø  Make sure DR user is in enable mode & set password

Ø   Intimate to the clients\users about the change freeze(down time of sever)

Ø   DR is pointed to vault and other component servers except CPM

**149) which user is responsible for replicating the data?**

 Answ:-DR user and Backup User is responsible replicating the vault data

**150) which service is responsible for replicating the data?**

 Answ:-Data Replication – The DR Service replicates the external files (Safes files and Safes folders) from the CyberArk Production Vault to the DR Vault. Data replication is performed according to the settings in the Disaster Recovery configuration file (PADR.ini).

**151) what is configuration file of DR & what does it contain?**

 Answ:-PADR.ini

**Q152)what is the log file for DR?**

 Answ:-PADR.log

**Q153) what configurations to be Checked in config file in DR when automatic failover is enable?**

 Answ:-We have to make sure that EnableFailOver Mode is set to Yes in PADR

**Q154) what are the services that will be up & running when replication is initiated?**

 Answ:- CyberArk Vault Disaster Recovery service

**Q155) what are the services that will be up & running after failover from primary to DR?**

 Answ:-Except Cyberark Vault Disaster Recovery service & remaining services related to vault will be up & run

**Q156) why do we need to do reverse replication from DR to primary vault?**

 Answ:-Inorder to avoid the data loss we have to perform reverse replication from DR to Primary when DR activity is performed

**Q157) what are reports & its types available in CyberArk?**

Answ:-Reports are of two types

1. Operational reports

a. Privileged account inventory

b. Applications inventory

Audit and compliance reports

a.      Privileged accounts compliance status

b.      Activity log

c.      Entitlement

**Q158)How will you generate reports or in how many ways reports can be generated?**

 Answ:-Reports can be generated in two ways

1. PVWA webpage reports tab

2. Private ark client

**Q159) what are Operational Reports?**

 Answ:-These reports contain information about the information stored in Privilege Cloud, Safes and users, and the operational connections between them.

**Q160) what is Audit\Compliance Reports?**

  Answ:-These reports contain information that enable you to track Safe activities and, specifically, password use in order to meet audit requirements.

**Q161) what is privileged accounts inventory report?**

 Answ:-These reports contain information about the information stored in the Vault, Safes and users, and the operational connections between them like (Target address/username, accessed & modified by/date, change/verification failure & failure reason). Provides information about all the privileged accounts in the system, based on different filters

**Q162) what is application inventory report?**

 Answ:-Applications Inventory. Provides information about all the privileged accounts in the system, based on different filters. PVWA. Safes List. A list of Safes and their properties according to location

**Q163) what is privileged accounts compliance status report?**

 Answ:-Privileged accounts compliance status. An inventory that indicates which accounts are compliant with their platforms, how accounts are managed in order to make them complaint, when password changes are planned, and their management status.

**Q164) what is Entitlement report & what does it contain?**

 Answ:-Entitlement rights in the Privileged Access Security solution regarding user, Safe, active platform, target system, target account, Group membership, other permissions etc.

     This report contain each user's effective access control and authorization level on each account that the user has access to in the Privileged Access Security solution.

**Q165) How will you generate Activity log reports?**

 Answ:-The User and Safe Activities report includes all the activities carried out by users on other users/groups/locations and all the operations carried out by users in the different Safes in the Vault. Each activity is marked as either a User activity or a Safe activity. It can be generated from both pvwa & privateark client.

**Q166) what is license capacity report & what does it contain?**

 Answ:-The License Capacity Reports contains information about the licensed user types and objects in the Vault. It enables users to see the maximum number of license for each user type or object, and the number of used license for each one

**Q166)How will you generate Active or In-active safes & users list?**

 Answ:-Logon with LDAP user/Auditor into privateark>tools>Reports, from here we can generate both active & in-active users & safes list

**Q167)How will schedule reports?**

  Answ:-

   The Schedule reports feature helps the user, that it can generate any reports, if it is specified with schedule setup(likes hours, days, months, years)

**Q168) Can the reports can be customized?**

 Answ:- Yes reports can be customized according to the customer requirements.

This can be done from Administration->Options->Reports->Settings

**Q169) what is the difference between pvwa reports & privateark client reports?**

Answ:-PrivateArk reports are for Audit purpose where as PVWA reports are Operational reports

Reports in PVWA Reports can be generated in the Reports page in the PVWA by users who belong to the group that is specified in the ManageReportsGroup parameter in the Reports section of the Web Access Options in the System Configuration page. By default, this is the PVWAMonitor group.

**Q170)what is Backup & Restore Utility?**

Answ:-Indirect Backup (Recommended)

-Replicate module is installed on a domain member server, typically the same server as other CyberArk components.

-PAReplicate.exe is used to copy vault data as encrypted files from the Vault server to the domain server.

-Third-party backup software can then be used to backup these files.

-Direct Backup (Not Recommended)

-Replicate module is installed on the Vault Server.

-PAPreBackup.exe is used to prepare the metadata on the Vault server for direct tape backup.

-Warning: Installing a third-party backup agent on the Vault server may introduce vulnerabilities and is not recommended.

**Q171)which user is responsible for taking the Backup of data?**

 Answ:-Backup user is responsible for backing up  the data

**Q172)which user is responsible for restoring the data?**

 Answ:- Operator user is responsible for restoring the data

**Q173) what is the command that needs to be executed for taking full backup?**

 Answ:-PAReplicate.exe vault.ini /logonfromfile user.ini /fullbackup

Note:-This backup is scheduled to run on daily basis with windows task scheduler and we will not run this manually on daily basis

**Q174) what is the command that needs to be executed for restoring the data?**

 Answ:-PARestore.exe vault.ini Operators /RestoreSafe “Safe-Name” /TargetSafe xyz

**Q175) How will perform version upgrade?**

 Answ:-

1. Take file system backup on all component servers where CyberArk components are installed

2. It is better to stop the services while run the script for version upgrade

3. Better plan the activity during off peck time (preferably on weekends) and notify the administrator / end users to use DR PVWA instead of Prod PVWA

4. Ensure all components including Vault, CPM, PVWA and PSM components are up and running in DR

5. Stop the services in production component servers and take file backup

6. Run the script on each component in production

7. Start the services and test if everything is working

8. Then notify the end users to use production PVWA

9. Stop the services on DR and run the same steps to upgrade DR

**Q176) what are the prerequisites for doing version upgrade?**

 Answ:-Take file system backup on all component servers where CyberArk components are installed

Plan the activity during weekends

Inform to customers about this activity ahead

Change freeze applicable during this time no password rotations

**Q177) will there be any down while performing version upgrade?**

Answ:-It depends on how we are planning the Upgrade Activity

If we are not routing the users to DR site then there will be definitely downtime for 5 to 10 minutes while upgrading the Primary Vault server as we have to stop the PrivateArk server service while Upgrading the Vault Server

**Q178) what is logon account?**

 Answ:-

Ø  Used when a user is prevented from logging on but password is known

Ø  Used on a regular basis –i.e. it is common to block root access via SSH

Ø  A ‘super user’, such as root, should not be used as a logon account

Associating Logon Accounts

The CPM associates logon accounts to enable users to log onto remote machines where they can perform identity management tasks. Logon accounts can be configured in either of the following ways:

 At platform level – All accounts attached to a specific platform will use the logon Account specified in the platform.

At account level – A logon account can be initiated manually in the Account Details page. The following parameters in the Privileged Account Management parameters specify the default logon account that will be associated with each new account.

LogonAccountSafe – The name of the Safe or a dynamic rule that specifies it, where the default logon account that will be used for accounts associated with this platform is stored.

Note: PSM cannot access logon accounts if the Master Policy is configured to enforce dual control password access approval.

LogonAccountFolder – The name of the folder or a dynamic rule that specifies it, where the default logon account that will be used for accounts associated with this platform is stored.

LogonAccountName – The name of the default logon account that will be used for accounts associated with this platform.

**Q179) what is psmp & how does it work?**

 Answ:-The PSMP is a Linux-based application similar to the PSM. The only difference is that it acts as a proxy for SSH13 enabled devices. PSMP controls access to privileged sessions and initiates SSH connections to remote devices on behalf of the user without the need to reveal SSH credentials. PSMP records the text based sessions which are stored in the EPV, later to be viewed by an authorized auditor. Unique to the PSMP are single sign in capabilities allowing users to connect to target devices without exposing the privileged connection password

**Q180) How will you implement psmp?**

 Answ:-

STEP1: Copy PSMP setup file to PSMP server via Winscp on OPT folder.

STEP2:Edit the vault.ini file. Change directories to **/opt/PSMP(folder name)/** directory and edit the **vault.ini** file using the VI editor.

            **cd /opt/PSMP/**

**vi vault.ini**

Update the ADDRESS parameter value to the address of your vault server (e.g. **10.0.10.1**). Use the arrow keys to move the cursor to the text you want to amend, type ***R** (case-sensitive) to make the changes and hit **Esc** to stop editing.

Enter the command **:wq!** to save the file and quit vi.

STEP 3: Create a credential file for the built-in Administrator. The built-in Administrator user will authenticate to the Vault and create the Vault environment during installation.

a. Change directories to **cd /opt/PSMP**

b. Enter the following command to assign read, write and execute permissions to the file CreateCredFile. Enter **_“_chmod 755 CreateCredFile”** as show in the graphic below.

c. Run **./CreateCredFile user.cred**, enter **Administrator** as the _Vault Username_ and  _Vault Password_. Accept the default values for the remaining prompts.

STEP4: Edit the psmpparms file to define the installation directory and accept the End User License Agreement. Remain in the current directory, /PSMP.

a.     Move _psmpparms.sample_ to the **/var/tmp** directory and rename it to psmpparms using the command in the following example.

b.     Edit the **psmpparms** file.

**vi /var/tmp/psmpparms**

c.     Edit the following lines as shown.

**InstallationFolder=/opt/PSMP**

**AcceptCyberArkEULA=Yes**

Enter the command **:wq!** to save the file and quit vi.

Step5:

Run the PSMP installation by running **rpm -ivh CARKpsmp-10.5.0-8.x86_64.rpm** from the PSMP installation directory (the version number in the screenshot may not be identical, you can type the first characters of the filename and then press tab to auto-complete).

**cd /opt/PSMP/**

**[root PSMP]#** **rpm -ivh CARKpsmp-10.5.0-8.x86_64.rpm**

Run **service psmpsrv status** to ensure that the server is running as the installation has completed

**Q181)what is the command\string that is used in order to connect to linux host via psmp?**

 Answ:-User@Account~domain%Hostname@PSM Server

**Q182) will there be key stroke audit record is possible via psmp?**

 Answ:-SSH text recorder The PSM can record all the keystrokes that are typed during privileged sessions on SSH connections.

Yes Key stroke Audit record is possible

SSH Keystrokes Audit To disable or customize SSH Keystrokes Audit for PSM-SSH, and/or PSMP-SSH and/or PSM-Telnet connection components using this platform:

a. Right-click Audit Settings, then from the pop-up menu, select Add SSH Keystrokes Audit.

b. By default, SSH keystrokes auditing is enabled for the supported connection component.

c. To disable auditing for this component, in the Properties list, set the value of Enable to No. Note: This configuration affects SSH Keystrokes Audits in both PSM and PSM for SSH.

d. To audit SSH keystrokes, PSM uses the shell prompt of the target system to understand text that was entered by the enduser. As different systems and devices have different prompts, you can configure the regular expression that represents the shell prompt so that PSM is able to recognize the text entered by the user. In addition, you can configure whether the session will continue without an audit, or will be terminated if the shell prompt is not recognized. To configure the regular expression, use the parameter ShellPromptForAudit. To configure whether the session will continue without an Privileged Access Security Privileged Access Security Implementation Guide 910audit, or will be terminated if the shell prompt is not recognized, use the parameter TerminateOnShellPromptFailure.

e. See Connection Component Configuration, page 951 for details on the f. Configure advanced properties to determine how the PSM will manage audit records.

**Q183)what are the log file & configuration file for psmp?**

 Answ:-

The following parameters define the location of the log file and the amount of information that is stored in this file. The PSMPOpenSSHLogFolder parameter specifies the PSM for SSH log folder.

The default folder is /var/opt/CARKpsmp/logs/components.

The PSMPOpenSSHTraceLevels parameter specifies the level of debug messages that will be included in the log file. You can set several values, separated by commas.

**Q184) what is the service related to psmp?**

 Answ:- PSM SSH Proxy Service

               PSM ADBridge Service

**Q185) what is the default port for RCA?**

 Answ:- 9022

**Q186) How will you monitor the digital vault server in your organization?**

 Answ:- Vault Can be monitored via Remote Control agent and SNMP Traps defined in the Paragent file

**Q187) what is the command that is used for remote control client in order to check the status of DR vault?**

 Answ:-PARClient [/Port ] [/CreatePassFile ] [/UsePassFile ] [/StateFileName ] [/Q] [/C "command"] /?

Example :- parclient.exe 1.1.1.250/Asdf1234 /c "status vault"

**Q187) what is the configuration file & service of RCA?**

 Answ:-Config File:PARagent.ini

              Service : PrivateArk Remote Control Agent

**Q188) what is psm secure connect?**

 Answ:-We can connect to the Target hosts without onboarding that account into CyberArk via this Secure Connect

Ad hoc connections for specific users and groups By default, all users and groups can use Ad Hoc connections. However, you can customize it so that only specific users and groups can use it. After you specify at least one user or group, only those users can use Ad Hoc Connections and no others.

**Q189) How will launch session via secure connect?**

 ANsw:-

**Q190) will there be live monitoring & recording will be possible if sessions are launched via secure connect?**

 Answ:-

Yes,there will be live monitoring & recording will be possible if sessions are launched via secure connect

**Q191) what is Export vault data?**

 Answ:-The ExportVaultData utility exports data from the Vault to TXT or CSV files, from

where they can be imported into third party applications or databases. Each report issaved in a different file.

**Q192) what kind of audit data that can be pulled out from the vault server using EVD?**

 Answ:-

The ExportVaultData utility runs from a command line.

You can export the information to as many reports as you require. Reports that are

not specified in the utility are not generated and exported.

The ExportVaultData utility uses the following syntax:

ExportVaultData \VaultFile=<VaultFileName>

\CredFile=<CredentialFileName> \Logfile=<LogfileName>

\Target=<MSSQL>

\DBServerName=<DBServerName>

\Separator=<SeparatorCharacter>

[\<ContinueOnErrors>]

\<OutputName>

[{\<OutputName>=<DB>} ...]

\ChunkSize=<number>

/?

Parameter Specifies

**Q193) what is the command that is used for running Export data vault utility?**

 Answ:-The following example shows how to use this utility to generate a log list:

ExportVaultData \VaultFile="D:\ExportVaultData\Vault.ini"

\CredFile="D:\ExportVaultData\auditor.cred" \Target=MSSQL

\DBServerName=localhost \LogList \ContinueOnErrors

**Q194) How will you onboard SSH keys?**

 Answ:- A public and Private Key pair will be generated inorder to Onboard the SSH Keys

**Q195) which keys are stored in vault when your managing linux server via SSH keys?**

 Answ:- Private Key will be stored on Vault Server and Public key will be on Linux Target host

**Q196) How cpm will rotate SSK keys?**

 Answ:-

Cpm will rotate this Key pair and will replace private and public key randomly on server and on Vault

**Q197) what is accounts discovery?**

 Answ:-Accounts Discovery is used to Pull out the accounts existing in a Domain

**Q198) How will you run  windows\linux discovery?**

 Answ:-Create a discovery process for Windows accounts

1. Log onto the PVWA with a user who is a member of the Vault Admins group.

2. In the ACCOUNTS page, under Accounts Management, click Accounts

Discovery; the Pending Accounts page

1. In the Pending Accounts page, click Discovery Management; the Discovery

Management page appears.

1. In the Discovery Management page, click New Windows Discovery; the New

Windows Accounts Discovery window appears.

1. Under Which account to use for scanning?, do the following:

a. Specify the Active Directory domain from which the list of machines to scan will

be retrieved.

Note:

Make sure that the PVWA machine has access to the Active Directory in order to

show the tree-view of the OUs.

Make sure that the CPM scanner that will perform the scan has access to the Active

Directory.

Specify the domain name in fully-qualified domain name (FQDN) format and with

up to 170 characters.

b. To configure the discovery to connect to remote machines using an LDAPS

secure connection, select Connect to the Active Directory using a secure

connection.

c. By default, this option is selected.

d. Select the user who will perform the scan. Either select an account from the

Vault or manually specify a user and password:

Select from Vault – Select a Vault account to run the scan. This is

recommended for recurrent scans.

i. Click Click to select an account from the Vault; a list of Vault

accounts appears. These are all domain accounts in the specified

domain.

Privileged Access Security

Accounts Feed 205ii. Select the account to use for the discovery process, then click Select

Account; details of the selected account are displayed.

Note:

Make sure the user in this account has the relevant permissions.

Specify Account – Specify a domain account that will run the scan.

i. Click Specify Account; prompts for the required details appear.

ii. Specify the following information:

User – The Active Directory user that will access the domain to retrieve

the list of machines and will access each machine to perform the scan.

Note:

Specify the user name in username or domain\username format.

This user requires read permissions in the OU and all sub-OUs to

scan.

Password – The domain user’s password.

1. Under What to scan?, specify the OU that will be scanned for accounts and their

dependencies. You can either select it from the tree view or type its distinguished

name.

To select the OU from a tree – Click Browse; the PVWA connects to the

Active Directory using the user credentials specified in the 'Which user to use

for scanning?' section and displays the accessible Active Directory tree.

If Connect to the Active Directory using a secure connection is

selected, the PVWA connects to the Active Directory using a secure

Privileged Access Security

Privileged Access Security Implementation Guide 206connection.

Select the OU to scan, then click OK; the selected OU appears in the

Accounts Discovery window. This OU will be scanned recursively.

Note:

You can only select one OU. If no OUs are selected, by default, the

selected domain will be scanned.

To type the OU’s distinguished name – In OU to scan, type the

distinguished name of the OU.

1. Under Which CPM scanner to use? select the CPM scanner that will scan for

accounts and their dependencies. The CPM scanner will scan only machines that

it can physically access.

If multiple CPM scanners are installed, select the relevant scanner from the

drop-down list.

If only one CPM scanner is installed, only the name of that scanner will be

displayed and it will be automatically selected.

1. Under What recurring pattern to set for this Discovery? select one of the

following:

Recurring – Enables you to define an automatic recurring discoveries.

Specify the following details:

Recur On – Select the day(s) when the discovery will run.

Starting – Set the time after which the discovery will run.

Privileged Access Security

Accounts Feed 207One time – Defines a one time discovery process that will run after you finish

setting it up.

1. Click Done; the following message appears:

2. Click OK; the discovery is added to the list of discoveries in the Discovery

Management page.

■ One time discoveries are performed as soon as the scanner finishes current

discoveries.

■ Recurrent discoveries are added to the list of pending discoveries and will be

performed on the defined day at the specified time.

**Q199) which service is responsible for accounts discovery?**

 Answ:-CyberArk Central Policy Manager Scanner Service

**Q200) what is the log file related accounts discovery?**

 Answ:-CACPMScanner

**Q201) Have you worked on Connectors?**

Answ:-

Yes I worked on Connectors like for managing the oracle databases we need Toad Connector.

We have installed Toad.exe on all PSM Servers and After that from PVWA Administration Tab under Options ->Connection Components we have to specify the PSM-Toad Connector Parameters like the Toad.exe path under client Dispatcher and also need to enable Authentication Level:1 and few other parameters were defined as per the document that we received from Developer Team

**Q202) What are your day-to-day activities in your project?**

Answ:-

1)Access related issues, for example end user is not able to access target windows server from PIM

2)End user is not able to login to PIM (PVWA), we need to find out the root cause and resolve the issue and ensure the user is successfully login into PIM

3)Senior management or concerned application teams may ask for the video recordings, we need to pull out the video recordings and send them

4)Weekly reports to be send to management I need to generate various reports in PIM console and send to management every week

5)New target systems (privileged accounts) need to on-board as and when require I need to add (on-board) target servers (privileged account) as and when new target servers or privileged accounts created on target servers

6)Policies may be required to change as per the client requirements time to time Policies that are defined during the implementation might be required to modify in due course due to change of requirements at platform level. I need to modify policies such as password rules, check-out / check-in etc.,

7)PIM System default users such as PasswordManager, PSM etc., may be expired, and PIM do not function if those users are expired, we need to connect to Vault through vault client and activate them

8)Monitor the logs daily and make sure the logs are pushing to SIEM tool

9)Monitor the PIM services in Windows services are all ways up and running

10)Application team do ask to hold the password change for specific privileged account on specific target server. Applications on target servers might be using the local windows server accounts (privileged account), if the password for privileged account is changed by CPM, applications running on the target server will get impacted. Hence application teams will ask PIM administrator to hold the password change for the privileged account on target server

11)Password Policy may be changed on different platforms as per the platform requirements time to time, we need to change the password rules in PIM password policy to align the password change interval

12)We need to on-board service accounts as and when required

**Q203) Have you onboarded any Application?**

Answ:- Yes I have Onboarded Tenable Application which is used to Scan the machines

From PVWA->Applications->Add Application

Specify Application ID:TenableAPP

Owner Details and the Authenticator details

After that we need to add the allowed machines which we got from the Application Team

Later we have granted the access to the safe by adding this TenableApp and Credential Provider User with default permissions

The Tenable team will perform the scan by retrieving the credentials from Vault

**Q204) What Kind of Tickets that you have worked on?**

Answ:- 1. Creation of Safes

2.Onboarding of Accounts

               3. CPM Automation Failures

               4.Decommission of servers removing from CyberArk

               5.Users Access related Issues

               6.Activation of Suspended Users

               7. Policy Changes on Particular Platforms

               8. CyberArk related patches like replacing the dll files on PVWA servers etc

               9. Platform duplication and parameters configurations

**Q205) What is the most Challenging issue that you have ever faced?**

Answ:- The Challenging issue that I have faced is that one of our PSM server is down and the users were not able to connect to their Targets when LB is routing to that particular PSM server.

Initially as workaround we asked LB Team to remove this PSM Server from Load balanced and upon troubleshooting I have figured out the issue by looking into both PSM Logs and ITA logs and found that PSMApp User got suspended I have activated that and run the cred file from that psm server and fixed the issue

**Q206) What are the Platform Parameters?**

Answ:-If we edit any platform we can see the below parameters

**Q207) What are the Scripts that you have Worked on?**

Answ:- I have worked on Pacli and RestAPI scripts for creation of safes and Platforms etc

**Q208) What is CyberArk Conjur?**

Answ:-Conjur Enterprise is a secrets management solution tailored specifically to the unique infrastructure requirements of cloud native, container and DevOps environments. The solution helps developers and security organizations secure, rotate, audit and manage secrets and other credentials used by dynamic applications, automation scripts and other non-human identities.

**Q209) What is CyberArk Alero?**

Answ:-CyberArk Remote Access (formerly Alero™) combines Zero Trust access, biometric multi-factor authentication and just-in-time provisioning into one SaaS-based offering. Remote Access is designed to provide fast, easy and secure privileged access to 3rd party vendors who need access to critical internal systems via CyberArk, without the need to use passwords. By not requiring VPNs or agents Remote Access removes operational overhead for administrators, makes it easier and quicker to deploy and improves organizational security.

**Q210). What are the default ports?**

Answ:-

PORTS:-

Primary Vault to DR Vault:- 1858

Components to Vault:-1858

SSH + SFTP (but can be configured anywhere):-22

Telnet:-23

RDP:-3389

LDAP:-389 and 636

DNS:-53

RADIUS:-1812

SNMP:-161

SNMP Trap:-162

Network Trap(NTP):-123

CPM to Targets: 135 139 445 22 1433 1521 etc

**Q211).What is  PTA?**

Answ:- CyberArk’s Privileged Threat Analytics detects malicious privileged account behavior.

-By comparing current privileged activity in real-time to historical activity, CyberArk can detect and identify anomalies as they happen, allowing the incident response team to respond, disrupting the attack before serious damage is done.

-By continuously monitoring privileged accounts for reset and change password activities, the PTA can detect when a user changes a password of a managed privileged account without using the CPM, and can automatically respond to contain the risk by reconciling the password of this account.

**Q212).What is On-Demand Privileges Manager (OPM)?**

Answ:- On-Demand Privileges Manager permits privileged users to use administrative commands from their native Unix or Linux session while eliminating the need for root access or admin rights. This secure and enterprise ready pseudo solution provides unified and correlated logging of all super user activity linking it to a personal username while providing the freedom required to perform job function. Granular access control is provided while monitoring all administrative commands continuously of super users activity based on their role and task.

**Q213).What is Application Identity Manager (AIM) ?**

Answ:- The Application Identity Manager is an application based on Windows and Linux which facilitates access to privileged passwords and eliminates the need to hard code plaintext passwords in applications, scripts, or configuration files. As with all other credentials stored in the Enterprise Password Vault, AIM passwords are stored, logged, and managed strongly. AIM is separated into two components: a Provider, which securely retrieves and caches passwords and provides immediate access to the requesting application; and the SDK, which provides a set of APIs for Java, .NET, COM14, CLI15, and C/C++. In the evaluated version, the AIM Provider for Windows and SDK have been excluded.

**Q214).****What is SplitPassword?**

Answ:-Password policy to ensure that single user doesn't have access to complete password on account.

**Q215).** **What is PrivateArk Vault Command Line Interface?**

Answ:-The PrivateArk Vault Command Line Interface (PACLI) enables the users to access the PAS Solution from any location using fully automated scripts, in a command line environment. Usersaccessing the PAS solution via the PACLI have access to limited interface for management, control, and audit features.

**Q216). How can you change the password for privileged accounts, let say I want to change the password for 100 accounts?**

Answ:- We can change the password for multiple accounts at a time manually.  Select the required accounts in accounts page (where you can view the list of accounts) and run the change password (in Manage button, you can click on “change” option). Please see the screen below, you can choose the option change the password by CPM immediately, so that CPM will change the password for all the selected accounts

**Q217).What is break glass id and why it is required?**

Answ:-Break Glass Id will be created on servers and in case of Emergency we will use this Break Glass account and passwords to access the target servers when our Environment is down

## Break-glass Process Design and Procedures

Given the critical nature of the CyberArk ecosystem, you need to implement a well-defined break-glass process. Although a break-glass account for the CyberArk solution itself is always required, other critical assets (such as network devices) may also need break-glass accounts in the event that the outage prevents other CyberArk-oriented break-glass procedures from being followed. That latter type of account is not covered in this section. However, at the very least organizations should develop a plan to both secure and retrieve the CyberArk Master private encryption key, as well as the associated Master password.

Typically this is accomplished by storing the Master private key (usually delivered and stored on a physical CD) in a physical safe or similar solution. We also recommend setting the Master password using two trusted individuals, where one person types in half of the password, with the other typing in the remaining half. Those two halves of the password would then be stored in a physical safe as well.

When designing the break-glass process for retrieval, always be mindful to ensure that more than one person has access to each physical safe, if possible. If an emergency occurs and the break-glass procedure must be followed, the last thing you want is for one half of the password to remain irretrievable because the person is away on vacation or otherwise unavailable.

**Q218). What is password randomization?**

Answ:- Password randomization means, changing the passwords for privileged account at regular interval. We can schedule the password change in Policy as shown below. We can set the value for “Required password change for X days”, default value is 90 days.

**Q219).How does the file sharing can be done through PIM?**

Answ:- Sometimes the files, could be log files, configuration files or any other files may need to be copied from a target server (could be an Unix server or windows server) to other target server.

PIM allows to use WinSCP as the interface or client to copy the file from one target server to PSM server, and copy the file from PSM server to another target server. WinSCP should be installed on PSM server and configured.

**Q220). How do you implement CyberArk?**

Answ:-First Step is to install the components:

Enterprise Vault is the critical component in CyberArk, this component should be installed on a separate server.  Hence first steps are to install Enterprise Vault on dedicated Windows server.

Hardening   option – Do not select Hardening option when you install Vault for the first time. Once the installation of all components successfully we harden the Vault

CPM (Central Policy Manger) and PVWA components should be installed on another server. First CPM should be installed and then PVWA should be installed. .Net Frame work should be installed and IIS server also should be installed. RDP service should be installed.

It is recommended to install PSM on another server.

Second step is configuration :

1.AD integration to import end users and groups in to PIM

2.Create Safes

Create required safes as per the design confirmed in PVWA

3.Platform Duplication

It is better to duplicate the default platform available in the system For example if there is a platform “Windows Server Local Accounts”, duplicate it with “IBM Windows Server Local accounts” so that policies can be applied at more granular level.

4.Policy Management:-

Set the policies for check-in check-out exclusive access, one-time password, duel control etc., if required for any platform Set the password rules, session management rules etc., for the required platform.

5.Account on-boarding:-

Accounts can be on-boarded manually one by one Accounts can be on-boarded in bulk using password upload utility

**Q221).End user is not able to access target server, how do you handle?**

Answ:-

a)           there may be password mismatch between target server and vault for the selected privileged account. We have to synch the password in between vault and target server for the privileged id

b)           Target server might be down or not reachable and not accepting requests. We need to talk to application or server team to ask them to resolve the issue at target server level and ensure the requests are accepted from PIM to login.

c)           Selected privileged account may not exists on target server When the privileged account is on-boarded to PIM using password upload utility, data in the csv file might be wrong, and wrong privileged account is added to PIM (on-boarded to PIM) Work with target server team and ask them to create privileged account on target server. Or delete the privileged account in PIM console and add correct privileged account which is existing on target server

d)           Required interface is not installed or registered under connection components in PIM configuration. For example toad is not installed and the user is trying to access database target server, connection will not be established and user cannot access target server

We need to install the interface and register under connection components if there is no entry in PIM configuration. (Check under Administration -> Options)

**Q222).What is rest API?**

Answ:- The PAS Web Services is a REST full API that enables users to create, list, modify and delete entities in Privileged Account Security solution from within programs and scripts.

The main purpose of the PAS Web Services is to automate tasks that are usually performed manually using the UI, and to incorporate them into system and account provisioning scripts.

The PAS Web Services are installed as part of the PVWA installation, and can be used immediately without any additional configuration. Make sure your CyberArk license enables you to use the CyberArk PAS SDK

**Q223). How will you do the incremental and full backup in your current organization?**

Answ:-  Incremental backup on daily basis and ful backup on weekly basis using the cyberark task scheduler.

**Q224).  What is DR?**

Answ:- DR means Disaster recovery its same as vault server it uses whenever vault server goes down DR vault server will be automatically up and running. DR is a backup server.

The Disaster Recovery (DR) service that runs on the DR Vaults is responsible for replicating the data and metadata from the Production Vault, as described below. 

Data Replication – The DR Service replicates the external files (Safes files and Safes folders) from the CyberArk Production Vault to the DR Vault. Data replication is performed according to the settings in the Disaster Recovery configuration file (PADR.ini).

 Metadata Replication – The DR Service replicates the metadata files based on exports (full backup) and binary logs (incremental backups). Metadata replication from the Production Vault to the DR Vault occurs after each action in the Vault has been completed.

Replication of the metadata files (MySQL DB) based on exports (full backup) and binary logs (incremental backups)

Ø  Metadata replication from the Production Vault to the Disaster Recovery Vault occurs at the completion of each event

Ø  Since password objects are also stored in the metadata, password objects are always synced between production and DR.

**Q225). How will you take vault backup by using replicate software?**

Answ:-1. Enable the Backup user and set an initial password.

1. Install the Replicate module and specify a location for Replicated Data.

2. Edit the Vault.ini to point to the Vault server.

3. Create a Credential File for the Backup user.

4. Create a batch file to execute the Replicate Process.

**Q226). What are default user that needs to be enabling for doing backup and restore?**

Answ:-Backup and operator.

**Q227). What are the CPM Automation Failures that you have worked with?**

## Answ:-[CPM - CACPM344E - Error: Invalid prompt or did not receive any prompt. State: "StartSessionSSH". code: 7001 - plug-in cannot work with old cached key / The server's host key does not match the one PuTTY has cached in the registry (force.com)](https://cyberark-customers.force.com/s/article/CPM-CACPM344E-Error-Invalid-prompt-or-did-not-receive-any-prompt-State-StartSessionSSH-code-7001-plug-in-cannot-work-with-old-cached-key-The-server-s-host-key-does-not-match-the-one-PuTTY-has-cached-in-the-registry)

[Firewall-1 - Code: 2114, Error: Error in verifypass (force.com)](https://cyberark-customers.force.com/s/article/00002210)

[Failed to verify user after reconcile user switch for Oracle Linux. code: 8008 (force.com)](https://cyberark-customers.force.com/s/article/Failed-to-verify-user-after-reconcile-user-switch-for-Oracle-Linux-code-8008)

[CPM - WinRC=53. The network path was not found, WinRC=67 The network name cannot be found (force.com)](https://cyberark-customers.force.com/s/article/00002929)

**Q228).****Tell me about your past projects and profile.**

Answ:- So far i am carrying an experience of 4 yrs in administrating and implementing customized IT solutions i.e cyber-ark privileged identity management and i have done 3 projects one on cyber-ark PAS and the other two projects on Administration and Networking side. coming to the cyber-ark's project i have been involved in both implementation and support level. we have installed Enterprise password vault on a dedicated physical server ,Cpm’s , Pvwa’s and PSM’s on  virtual servers . After installing these components we were moved into configuration i.e first AD is integrated to Cyberark  to import users and groups in to PIM. We have Created required safes as per the design confirmed in PVWA and As per our client requirement we have duplicated the windows platforms with the name _windows server local accounts. I have on-boarded multiple accounts to PIM i,e  windows servers, Linux servers and some databases . We have configured Session recording & live monitoring on Privileged Session Manager, One-Time Password (OTP), Dual Control Approval Workflow and exclusive access for check-in check-out etc. Then i was assigned to support role and i need to monitor the cyberark services on regular basis whether they are running or not. Handling login issues related to PVWA and target systems for example if the end user is not able to access the target server i need to check the log files why the user is not able to access the particular account and i need to resolve this issue, There might be many reasons like Target server might be down or not reachable, There may be password mismatch between target server and vault for the selected privileged account, Selected privileged account may not exists on target server. I need to Create and Manage Safes, platforms and Owners, Policy specification etc these are the daily day to day support activities i am going to do in this current project.