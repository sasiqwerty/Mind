---
aliases: 
tags: 
date created: Saturday, October 21st 2023, 8:30:27 pm
date modified: Sunday, October 22nd 2023, 1:12:11 am
---
- Your customer has 5 main data centers with one PVWA in each Centre under different URL's. How can you make this setup fault tolerant?  
	- This setup is already fault tolerant  
	- install more PVWA in each datacenter  
	- continuously monitor the PVWA status and send users the link to another PVWA if issues are encountered.  
	- load balanced all PVWA under the same URL.
- Which Pre-requisite step must be completed before installing Vault ?
	- (A) Join the server to domain  
	- (B) Install a clean operating system  
	- (C) Install Antivirus Software  
	- (D) Copy the master CD to a folder in the vault server  
- You have been asked to design the number of PVWAs a customer must deploy. The customer has three data centers with a distributed vault in each, requires high availability and to use all Vault at all times, how many PVWAs does the customer need.
	- 6
	- 2
	- 3
	- 4
- You are configuring Vault to send syslog data to you organization's SIM solution. What is a valid value for SyslogServer protocol parameter in dbparm.ini  
	- TLS
	- SSH
	- SNMP
	- SMTP
- A customer installed multiple PVWAs in the production environment behind Balancer VIP. They subsequently observed that all the incoming traffic from the load balancer only one PVWA. Even though all the PVWAs are up and running. What could be the likely situation.
	- The load balancing algorithm is the least connections algorithm
	- the certificate of the load balancer is not a wild cart cert
	- the load balancing pool only has one PVWA server
	- SSL passthrough is not configured on the load balancer
- What is a requirement for setting fault tolerance for PSM?
	- Use a load balancer
	- use a backup solution
	- CPM must be in all data center
	- install the vault HA cluster
- Which Browser is supported by PSM web connectors developed using the CyberArk
	- Internet Explorer
	- Opera
	- Internet Edge 
	- Google Chrome
- A customer asked you to help scope the company's PSM development what should be included in the scoping Conversation.
	- Recording File path
	- Recording Codec
	- Recording retention period
	- Recording File type
- Which Parameter must be provided when registering a primary vault in Azure, but not in Amazon Web Service.
	- /RecPub
	- /AdminPass
	- /MasterPass
	- /RDPGateway
- When creating Distributed Vault environment Architecture, What is the Maximum number of Vault servers that can be deployed.
	- 5 - Number of primary and satellite vaults can be specified during installation
	- 3 - all primary
	- 6 - 1 primary and 5 satellite
	- 10 - 2 Primary and 8 satellite  
- You have been asked to install three additional PSMs after the initial PSM install. The first PSM was installed with a secondary Administrator Account which account should you use when installing new PSM?
	- Use the default vault administrator account
	- use the secondary administrator account
	- you may use any user in the vault admin group
	- create a new administrator in the installation  
- Q14 You are installing PSM for SSH with AD-bridge in CyberArkSSHD mode for your customer, My Cyber Classes. What do you need to install to meet your customer Need (Choose2)
	- libssh
	- CARKPSMP - Infra
	- CARKpsmp
	- CARKpsmp-ADBridge  
- You are responsible for installing a CPM, Which Vault authorization will your CyberArk user need to install the CPM? Choose best one
	- Add Safes, Add/Update Users, Reset Users Password, Activate User Manage server file categories
	- Add Safes, Add/Update Users, Manage Directory Mapping
	- manage directory, backup all safes, restore all safes
	- audit users, activate users, add network areas, Manage directory Mapping
- Before the hardening process, your customer identified a PSM universal connector executable that will be required to run on the PSM. Which file should you update to allow this run?
	- PSMConfigureApplocker.xml
	- PSMHardening.xml
	- PSMAppConfig.xml
	- PSMConfigureHardening.xml  
- After installing the first PSM server and before installing additional PSM servers. You must ensure the user performing the installation is not direct owner of which safe?  
	- PSMUnmanagedSessionAccounts Safe  
	- PSMRecordingsSessionAccounts Safe 
	- PSMUnmanagedApplicationAccount Safe  
	- PSMSessionBakcupAccount safe  
- You are setting up HTML5 Gateway for PSMSessions. Which servers need to be trusted by the Linux Host to secure communications through the gateway?
	- PSM & PVWA
	- PSM & CPM
	- PVWA & Vault
	- Vault & PSM  
- You need to recover and account mcc-loc for target server host4.mcc com stored in safe1, what do you need to recover and decrypt the object? (Choose3)
	- Recovery Private Key
	- Recovery.exe
	- Vault Data
	- Recovery Public Key
	- Server Key
	- Master Password  
- You are installing multiple PYWAs behind the load balancer, which statement is correct?  
	- Port 1858 must be opened between the load balancer and PVWAs.  
	- The Load balancer must be configured in DNS(Round Robin).  
	- The load balancer must support "sticky sessions".  
	- The LoadbalancerClientAddressHeader parameter in the PVWA.ini file must be set.
- When running a privileged account Inventory report through the report page in PVWA on a specific safe, which permissions are required on that safe to show complete account inventory information
	- List account, view safe members
	- manage safe owners
	- list account access safe without confirmation
	- manage safe, view audit  
- A company requires challenge/response multi-factor authentication for PSMP sessions which server must you integrate with CyberArk Vault?  
	- LDAP
	- PKI
	- SAML
	- RADIUS  
- What is default username for the PSM for SSH maintenance user?  
	- Proxymng  
	- Psmp_maintenance  
	- Psmpmaintenanceuser  
	- Proxymng_usr
- Which CyberArk group does a user need to be part of to view recordings or monitor live sessions?
	- (A) Vault Admin
	- (B) Users
	- (C) Auditors
	- (D) Operator  
- How Much disk Space do you need on the servers for a PAReplicate?
	- (A) 500GB  
	- (B) ITB  
	- (C) Same as disk size on Satellite Vault  
	- (D) Same as disk size on Primary Vault  
- PAM solution provide an out-of-the box target platform to manage SSH keys, called Unix Via SSH keys How are these keys called Managed?  
	- (A)CyberArk stores Private keys in Vault and update Public key on Target System  
	- (B) CyberArk stores Public keys in Vault and update Private key on Target System  
	- (C) CyberArk does not store Public or Private Key & instead use a reconcile account to create keys to demand  
	- (D) CyberArk stores both Private & Public Key and can update target systems with Either Key  
- In your organization, "click to connect" button is not active by default, how can this feature be activated  
	- (A) Policies > Master Policy > Allow EPV transparent connection > Inactive  
	- (B) Policies Master Policy Session Management -Require Privileced session monitoring and isolation Add Exception  
	- (C) Policies Master Policy Allow EPVtransparent connection Active  
	- (D) Policies Policy Password Management  
- Status of Services when OF server is running on replication mode
	- (A) CyberArk Windows Hardened firewall - Running
	- (B) PrivateArk Database - Running
	- (C) PrivateArk Server - Stopped
	- (D) CyberArk Vault Disaster Recovery- Running
	- (E) CyberArk Event Notification Engine -- Stopped  
- Which option in PrivateArk Client is used to update users Vault Group Membership?
	- (A) Update > General Tab
	- (B) Update > Authorization Tab
	- (C) Update > Member of Tab
	- (D) Update > Group Tab  
- Which pre-requisite is mandatory or not to run PSM Health Check?
	- (A) PSM Service Installed on Windows 2008R2,2012R2 and 2016— Mandatory
	- (B) PSM Service Installed on Windows 2012R2, 2016 & 2019- Mandatory
	- (C) A Valid SSL cert installed on Web Server— Not Mandatory
	- (D) IIS Web Server— Not Mandatory
- There us a requirement for a password change 01:00 and 03:00 on Saturdays and Sundays, however, this doesnt work consistently. Which Platform settings you need to check?
	- (A) The interval setting for the platform is incorrect and must be less than 120
	- (B) The immediateinterval setting for the platform is incorrect and must be greater than or equal to 1
	- (C) The DaystoRun setting for the platform is incorrect and must be set to Sat, Sun
	- (D) The HeadStartlnterval setting for the platform is incorrect and must be set to 0  
- Question 34 – After installing the Vault, you need to allow Firewall access for Windows Time Service to sync with NTP server 10.1.1.1 and 10.2.2.2 what should you do?
	- (A) Edit dbparm.ini file and add AllowNonStandardFWAddresses=[10.1.1.1,10.2.2.2],Yes:outbound/udp
	- (B) Edit dbparm.ini file and add NTPServer=[10.1.1.1,10.2.2.2],Yes:outbound/udp
	- (C) Edit dbparm.ini file and add AllowNonStandardFWAddresses=[10.1.1.1,10.2.2.2],Yes:outbound/udp, 123:outbound/inbound udp
	- (D) Edit Windows Firewall to add a rule to allow port 123  
- Which Permission are needed for Active Directory users required by the Windows Discovery Process?
	- (A) Domain Admin
	- (B) Local Admin
	- (C) Read/Write
	- (D) Read  
- Match each component to its respective log file location:
	- (A) PTA System - /opt/tomcat/logs  
	- (B) PSM for SSH (PSMP) - /var/opt/CARKpsmp/logs  
	- (C) Disaster Recovery – C:\Program Files(x86)\PrivateArk\Server\PADR
- When Dual Control is enabled a user must first submit a request in the Password Vault Web Access (PVWA) and receive approval before being able to launch a secure connection via PSM for Windows (previously known as RDP Proxy).  
	- (A) True  
	- (B) False, a user can submit the request after the connection has already been initiated via the PSM for Windows  
- Which certificate type do you need to configure the vault for LDAP over SSL?  
	- (A) CA Certificate that signed the certificate used by the External Directory
	- (B) CA signed Certificate for the Vault server
	- (C) CA signed Certificate for the PVWA server
	- (D) self-signed Certificate for the Vault  
- Match the connection component with their corresponding OS/Functions. All correct answers below  
	- (A)PSM-SSH - Unix  
	- (B) PSM-RDP-Windows  
	- (C) PSM-WinSCP - Unix File Transfer  
	- (D) PSM-SQLPlus-Database  
	- (E) PSM-OS390-Mainframe  
- Which Master Policy Setting must be active in order to have an account checked-out by one user for a pre-determined amount of time?
	- (A) Require dual control password access Approval  
	- (B) Enforce check-in/check-out exclusive access  
	- (C) Enforce one-time password access  
	- (D) Enforce check-in/check-out exclusive access & enforce one-time password access  
- A user with administrative privileges to the vault can only grant other users privileges that the himself has
	- True
	- False  
- You receive this error message :error in changepass to user domain\user on domain server mcc.com(WinRc=50 Access is denied" which root cause should you investigate.
	- (A) The account doesn't have sufficient permission to change its own password
	- (B) Domain Controller is unreachable
	- (C) CPM Service is disabled and need to restarted
	- (D) The password has been changed recently and minimum password age is preventing the
	- change.  
- You have been asked to limit a platform called “Windows_server” to safes called “WindowsDC1” & “WindowsDC2”. The platform must not be assigned to any other safe. What is the correct way to accomplish this?
	- (A) Edit the Windows_Server Platform expand automatic password management then select General and Modify “AllowedSafes” to be “WindowsDC1 &WindowsDC2”
	- (B) Edit the Windows_Server Platform expand automatic password management then select Options and Modify “AllowedSafes” to be “Win*”
	- (C) Edit the safe “WindowsDC1” &WindowsDC2 through safe management. Add “Windows_Server” to allowed platform
	- (D) Login to PrivateArk Client with Admin user, select file, Server File Categories. Locate the Category “WindowsServersAllowedSafe” and Specify “WindowsDC1” & "WindowsDC2”  
- You are creating a Dual Control workflow for a team’s safe. Which safe permissions must you grant to the Approver’s group?
	- (A) List Accounts, Authorize account request
	- (B) Retrieve accounts, Access safe without confirmation
	- (C) Retrieve accounts, Authorize account request
	- (D) Lists accounts, Unlock accounts
- In large enterprise environments with complicated network zoning, what is the main reason to install more than one CPM?
	- (A) to utilize a load balancer to distribute workloads between multiple servers
	- (B) to manage passwords on the DR vault
	- (C) To increase performance of the CPMs
	- (D) To avoid implementing complex firewall rules  
- What should you recommend to a customer planning to deploy multiple vaults into the cloud?  
	- (A) Deploy vaults in a high availability manner in one region with a DR vault in a separate region  
	- (B) Deploy distributed Vaults in multiple regions and multiple availability zone within each region  
	- (C) Deploy the vaults using a physical HSM for the keys  
	- (D) Deploy the first DR vault using the cloud templates and subsequent DR vaults manually  
- What is mandatory for a PVWA installation?
	- (A) A DNS entry for the PVWA url must be created
	- (B) A company signed TLS certificate must be imported into the server
	- (C) A vault administrative user must be used to register the PVWA
	- (D) Data Execution Prevention must be disabled  
- A customer installed multiple PVWAs in the production environment behind a load balancer VIP. They subsequently observed that all incoming traffic from the load balancer VIP goes to only one PVWA, even though all the PVWAs are up and running.
	- (A) A load balancing algorithm is the least connections algorithms
	- (B) The certificate of the load balancer is not wild card cert
	- (C) The load balancing pool only has one PVWA server
	- (D) SSL Passthrough is not configured on load balancer  
- Which Parameters can be used to harden the credential files (CredFiles) While using createcred utility  
	- (A) Operating System Username  
	- (B) Host IP Address  
	- (C) Client Hostname  
	- (D) Operating System Type (Linux/Windows/HP-UX)  
	- (E) Vault IP Address  
	- (F) Time frame  
- In the Private Ark Client, how do you add an LDAP group to a CyberArk Group?  
	- (A) Select update on the CyberArk group, and then click Add > LDAP group  
	- (B) Select update on the LDAP Group, and then click Add > LDAP group  
	- (C) Select member of on the CyberArk group, and then click Add > LDAP group  
	- (D) Select member of on the LDAP group, and then click Add > LDAP group
- If a customer has one data centre and requires high availability, how many PVWAs should be deployed.
	- (A) Two
	- (B) one PVWA cluster
	- (C) one
	- (D) Two PVWA clusters  
- Your organization has a requirement to allow users to "check out passwords" and connect to targets with the same account through the PSM. What needs to be configured in the master policy to ensure this will happen?
	- **(A) Enforce check-in/check-out exclusive access=active; Require privileged session monitoring and isolation=active**
	- (B) Enforce check-in/check-out exclusive access=inactive; Require privileged session monitoring and isolation=inactive
	- (C) Enforce check-in/check-out exclusive access=inactive; Record and save session activity=active
	- (D) Enforce check-in/check-out exclusive access=active; Record and save session activity=inactive  
- Which service must be set to Automatic (Delayed Start) after the vault is installed?
	- **(A) Windows Time Service**
	- (B) PrivateArk database
	- (C) Windows Update Service
	- (D) PrivateArk Server  
- For a Digital Vault Cluster in a high availability configuration, how does the cluster determine if a node is down?
	- **(A) The heartbeat is no longer detected on the private network.**
	- (B) The shared storage array is offline.
	- (C) An alert is generated in the Windows Event log.
	- (D) The Digital Vault Cluster does not detect a node failure.  
- Which files does the Vault Installation Wizard prompt you for during the Vault install?
	- **(A) Operator CD & License file**
	- (B) Master CD & License file
	- (C) Operator CD & Vault Certificate
	- (D) Master CD & DBparm.ini  
- Arrange the steps to restore a vault using PARestore for a backup in correct sequence:
	- (A) Backup Files Deletion = No
	- (B) PARestore vault.ini operator/Full Vault restore
	- (C) CAVault Manager Recovers Backup file
	- (D) CAVault Manager restore DB
	- (E) Backup File Deletion = Yes, 24,1,5.7d
- As Vault Admin, you have been asked to configure LDAP authentication for your organization’s CyberArk Users. Which permission do you need to complete this task?
	- (A) Audit Users and Add Network Areas
	- (B) Audit Users and Manage Directory Mapping
	- (C) Add Users and Add/Update Users
	- (D) Audit Users and Activate Users
- Which PTA sensors are required to detect suspected credential theft?
	- (A) Logs, Vault Logs
	- (B) Logs, Network Sensors, Vault Logs
	- (C) Logs, PSM Logs, CPM Logs
	- (D) Logs, Network Sensors, EPM
- You are installing HTML5 gateway on Linux host using the RPM Provided. After installing the Tomcat webapp, what is the next step in the installation process?
	- (A) Deploy the HTML5 Service (guacd)
	- (B) Secure the connection between guacd and webapp
	- (C) Secure the webapp and JWT validation endpoint
- To enable automatic response "Add to pending" within PTA when unmanaged credentials are found. What are the minimum permissions are required for PTA user for passwordmanager_pending safe?
	- (A) List Account, View Safe Members, Add account (include update properties), Update account content, Update Account Properties
	- (B) List Account, Add account (include update properties), Delete Account, Manage Safe
	- (C) Add account (include update properties), Update account content, Update Account Properties, view Audit  
- A customer Environment has three data centres consisting of 5000 servers in Germany, 10000 servers Canada Server in india, You want to manage Target server and avoid complex firewall rules, how many CPM's you should deploy?  
	- (A) 1  
	- (B) 3 total, I per data centre  
	- (C) 9  
	- (D) 6 total , 2 per data centre
- Which statement is correct about CPM behaviour in a distributed Vault environment?
	- (A) CPMs Can only access the primary vault. When it's unavailable. CPM cannot access any vault is promoted as the new primary vault
	- (B) CPMs can access only the Satellite Vaults
	- (C) CPMs can only access the primary vault when it is unavailable. CPM cannot access any Vault until the original primary vault is operational again
	- (D) CPM can access all vaults- Primary and the satellite  
- Match each permission to where it can be found?
	- (A) Add Accounts - Safe
	- (B) Initiate CPM account management operations - Safe
	- (C) Add/Update Users - Vault
	- (D) Add Safes - Vault  
- What is a prerequisite step before CyberArk can be configured to support RADIUS authentication?
	- (A) Log on to the PrivateArk Client, display the user properties of the user to configure, run the Authentication method drop down list, and select RADIUS authentication
	- (B) In the RADIUS server, define the cyberArk vault as a RADIUS client/agent
	- (C) In the vault installation folder, run CAVaultManager as administrator with the SecureSetFiles Command
	- (D) Navigate to /Server/Conf and open DBParm.ini and set the RadiusServerInfo parameter  
- Which components can connect to a satellite Vault in distributed Vault architecture?
	- (A) CPM, EPM, PTA
	- (B) PVWA, PSM
	- (C) CPM, PVWA, PSM
	- (D) CPM, PSM  
Q68 : Match the built in Vault user with the correct definition  
#later 

62cdebe6180af89ba336df341a67eb17-23.jpg  
Question 68-Match the builtin Vault user with the coge�t de(iMetion  
(A) This user appears on the highest al set hierarchy and has all the possible

permissions.As such, it can create and ether users on any level on the User's  
hiererchy >  
(B) This user appears at the user hierarchy,enabling it to view all the users in

to keep track of activity in ang User requirements > iz

(C) This user is an set that cannot be lagged onto and carries out internal  
tasks,such as aut ly Clgaring expired user and safe history > J

(D) This use available Safe mamber authorizations except authorize password  
requests. Thimyser hSs complete system cantrol,manages a full recovery when necessary and

cannot Prom any sata |

Er  
CYHER  
rm PLaSses

Q69 A new HTMLS Gateway has been deployed in your organization

Ss . cvneR  
CLASSES  
ay TMILS Gateway has been deployed in your organization.

you configure the PSM to use the HTMLS Gateway?

the safe. The user can prod s of Safe activities and user activities which enablas it  
:  
alt

Question

{B} Administration >Options>Privileged Session Management>Add Configured PSM  
Gateway Servers

{C) Administration >Options>Privilegad Session Management>Add PSM Gateway  
{D} Administration >Options>Privilagad Session Management=Connestion Details

Question 70-4 Vault Administrator team member can log in to CyberArk,but for some reason,is not  
given Vault Admin rights. Where can you check to verify that the Yault Admins directory mapping  
points to the correct AD group?

Q70 70-A Vault Administrator team member can log in to CyberArk. but for some reason, is not  
given Vault Admin rights where can you check to verify that the vault admins directory mapping  
pints to the correct AD group?

{B) PVWA>User Provisioning>LDAP Integrations Map Name  
{Cc} PYWA>Administration=LDAP Integration> Mappings  
{0} PYWA->=Administration=LDAP Integration > AD groups

Q71 in the PrivateArk Client, How do you add an LDAP group to a CyberArk Group?


62cdebe6180af89ba336df341a67eb17-24.jpg  
Question 71-In the privateArk Client,how do you add an LDAP group to a CyberArk group?

(B) Select Update on the LDAP Group, and then click Add> LDAP Group  
(C) Select Member of the CyberArk Group, and then Click Add >LDAP Group  
(D} Select Member of the LDAP group and then Click Add>LDAP Group

af

Q72 What are the basic network requirements to deply a CPM server?

Question 72-What are the basic network requirements to deploy a CPM server? C ,  
(B) Port 1858 only ( L�)  
(C) All ports to the vault a

(D) Port UDP/1858 to vault and all required ports to targets and Pane fhe PSM

Q73 � You have been asked to identify up or down status of Vault Services

Question 73-You have been asked to identify up or down status of ae  
Which CyberArk utility can you use to accomplish this task?

(A) Vault Replicator for  
(B) PAS Reporter \\  
(D) Syslog 4

Q74 Which is Mandatory for a PVWA installation? A DNS entry for the PVWA URL must be created

~ |  
Question 74-Which is mandatory for a P' on?A Owns Entry for the PYWA url must be  
created  
(A) A company signed TLS cgrtr must be imported into the server

(C) Data Execution Pye� must be disabled


62cdebe6180af89ba336df341a67eb17-25.jpg  
Q76 You are helping a customer prepare a Windows Server for PSM installation what is required for  
a successful installation?

Question 76-You are helping a customer prepare a Windows Server for PSM Installation.  
What is required for a successful installation?  
(A) Windows 2012 KB4558843 rv

CYBER

es =f

(C} Windows 2016 KB4558843  
(D) Remote Desktop Services (RDS) Session Broker

Q78 In addition to bit rate and estimated total duration of recordings per day. What is needed to  
determine the amount of storage required for PSM recordings.

Question 78-In addition to bit rate and estimated total duration of recordings per day,w, & to

determine the amount of storage required for PSM recordings?

{B) Number of PSMs = CG

(C) Number of users Se) �

{D) Number of targets

-~

1. CyberArk user XYZ is trying to connect to the Target Linux server 192.168.1.164 using a domain  
account MCC/linuxuser01 on domain mycyberclassess.com PSM for SSH server 192.168.65.145.  
What is the correct syntax?

Question 79-CyberArk user XYZ is trying to connect to the Target� x Wer 192.168.1.164 using a  
domain account MCC/linuxuser01 on domain mycyberclagseg.c g PSM for SSH server  
192.168.65.145. What is the correct syntax?  
(A) ssh xyz@linuxuser0i@myc lass@e.com@192.168.1.164@192. 168.65.145  
(B) sshxyz@linuxuser01@mi rclasSes.com@192.168.1.164@192.168.65.145

(D) ssh xyz@linuxus erclasses.com@192.168.1.164(@192.168.65.145

1. Which component must be installed on the vault if distributed vaults is used with PSM?

(B) Disaster Rec,  
(C) Remote C  
(D) Distribut

nv  
Cymer  
CLASSES

Question 80-Which component mus mS on the vault if distributed vaults is used with PSM?  
Fe  
i)



62cdebe6180af89ba336df341a67eb17-26.jpg  
82) Which tools are used during a CPM renaming process

Question 82-Which tools are used during a CPM renaming process (Choose 2)  
Mr

ee art

(C) CPM/nDomain_Hardening.ps1 CLASSES  
(D) PMTerminal.exe  
(E) Date Execution Prevention

1. If a customer has one data center and requires high availability, how many PVWAs should be  
deplyed?

Question 83-If a customer has one data center and requires high availability,how many PVWAs should

be deployed?  
(A) Two  
{B) One PVWA Cluster 7  
(C}_ One fn,

1. In addition to disabling Windows services or feature not needed for PVWA operations, which  
tasks does PVWA_Hardeing.ps1 perform when run?

Question 84-In Addition to disabling Windows services or features not needed for PYWA  
operations,which tasks does PYWA_Hardening.ps1 perform when run?  
(A) performs IIS hardening;imports the CyberArk INF configuration

(C) Performs IIS hardening;renames the local Administrator Account  
(D) Configures Windows Firewall;removes all installation files - CQ)

1. Refer to the exhibit- A customer is building a development environment in the Amazon Public  
Cloud through Amazon Web Services


62cdebe6180af89ba336df341a67eb17-27.jpg  
What is an ideal specification for the vault if it will only hold less than 1000 accounts?

~~  
Question 85- Refer to the exhibit- A customer is building a development enviganmeNwathe Amazon  
Public Cloud through Amazon Web Services S .

EC2 instance | vCPU Memory (GB) QC

T2.micro | 1 1 | General Purpose

T3.medium i 4 General Purpose  
CS large 2 4 fal \ Computer Optimized

What is an ideal specification for the vault if it will og� hold less than 1000 accounts?

(A) t2.micro ge,

(B) T3.medium NO HY  
CYBER

a SEs

(D) C5.large

Vault servers and standalone DR Vault servers 2

Small Medium Large Very large  
{<1,000 managed (1,000-20,000 managed (20,000 - 100,000 managed {more than 100,000 managed  
passwords) passwords) passwords) passwords)
> mSilarge + mS.xlarge + mBxlarge * mSxlarge

- 250GB storage * S00GB storage

1. A customer is deploying PVWAs in Amazon Web Services Punlic Cloud. Which load Balancing  
option does CyberArk recomment?

Question 86 -A customer is deploying PYWAs in Amazon Web Services Public Cloud. Which load  
Balancing option does CyberArk recommend?

(A} network load balancer  
(C) HTTPS load balancer cusses  
(D} Public standard load balancer

1. Due to network activity, My Cyber Classes PrivateArk Server become active on the DR Vault  
while the private vault was also running normally. All the components continues to point to the  
Primary Vault. Which steps should you perform to restore DR replication to normal?


62cdebe6180af89ba336df341a67eb17-28.jpg  
Question 87 -Due to network activity,My Cyber Classes PrivateArk Server become active on tye DR  
Vault while the private vault was also running nermally.All the components continued to oO  
Primary Vault.Which steps should you perform ta restore DR replication to normal?

(Aj Replicate data from DR Vault to primary Vault >Shutdown Private. GY nOR  
Vault=Start Replication on DR Vault

(C) Shutdown PrivateArk Server on Primary Vault>Replicat R Vault ta  
primary Vault +S hutdown PrivateArk Server on DR Vault=Sta ie,

(D} Shutdown PrivateArk Server on DR Vault>Replic GS DR Vault ta primary  
Vault >Shutdown PrivateArk Server on DR Voult-Start Rag on DR Vault

1. Which authentication method does PSM for SSH support?  
i OQ�  
Question 88 -Which authentication methods P �or SSH support?  
(A) CyberArk password,LD. IUS'SAML

(B) LDAP,Windows Authen' SH Keys  
Password CLASSES  
ft

(C) RADIUS, Oracle  
89) To ensure all session are being recorded, a CyberArk Administrator goes to the master policy  
and makes configuratuon changes.

Question 89 -To ens ig are being recorded, a CyberArk Administrator goes to the

master policy and makes gigtic&changes.  
What configuration is cori  
{A} Reg re privileged session monitoring and isolatiansinactive: Record save  
Kn Bctivity=active  
Require privileged session monitoring and isclation=inactive; Record save  
sion activity=inactive

& (D} Require privileged session monitoring and isolatian=active; Recard save  
session activity=inactive

1. Refer to the exhibit To Enable PKI Authentication for PYWA(Version 10 and above), which web  
server config file must be updated and appended with displayed settings?

Question 90- Refer to the exhibit  
To Enable PKI Authentication for PYWA(Version 10 and above),which web server contig file must be  
updated and appended with displayed settings?

location path="Default WebSite/PasswordVault/api/auth/pki/logan �>  
�system. WebServer>  
<Security>


62cdebe6180af89ba336df341a67eb17-29.jpg  
<access sslFlags="Ssl,$sl NegotiateCert,SslRequireCert/>

</Security>
</system. WebServer>
<flocation>

(B) CAinetpub\adminscripts\web.canfig  
{C} PasswordVault\CustomAuthenticationDLs\CyberArk.Authentication.CustomPKIPN.dll

(Dj CAinetoub\wwewroot\PasswardVault\Eny

1. To use PSM Connections while in the PVWA, what are the minimum safe permissions a user a

group will need?

Question $1-Ta use PSM Connectio aA. .. PYWA what are the minimum safe permissions 4  
user or group will need?

CYBER  
(B} List Accoygis,| ounts,Retrieve Accounts SLASHES  
(C} Use Acctint  
(D) Lis coun Use Accaunts,Retrieve Accourts,Access Sate without Confirmatian

1. Which is a valid combination of primary and secondary layers of a authentication to a  
company�s two factor authentication policy?

Question 93-Which is a valid combination of primary and secondary prey tericoion toa

company's twa factor authentication policy?

{A} RSA SecurelD Authentication (in PVW, My Diwissin  
(B} CyberArk Authentication and RADIUS t ada

iC} Oracle SSO(In PVWA) and SAML Au icagi

ry

1. A customer wants to inplement as multi-cloud strategy for a vault deployment.

Question 94 -A customer wants to implem� EA Mtoud strategy for a vault deployment.  
Which architecture should you recommen?  
{A} Primary Vault in AVS tin Azure.Both Primary and DAR Vault integrate with  
AWS Key management ne  
(B} Primary Vaubgei  
Azure Key Vault

.DOR Vault in AWS.Both Primary and DR Vault integrate with

aultin Azure,DR Vault in AWS.Neither will integrate with Cloud native key  
systems. The Server key will reside on the operating system.

1. You have been asked to configure SNMP remote monitoring for your organization�s vault  
servers. In the PARAgent.ini which parameter specifies the destination of the Vault SNMP traps?


62cdebe6180af89ba336df341a67eb17-30.jpg  
Question $5-You have been asked to configure SNMP remate monitoring far your organization's vault  
servers. In the PARAgent.ini which parameter specifies the destination of the Vault SNMP traps?

{A} SNMPHostIP rs

(B) SNMPTrapPort cases

(Cc) SNMPCommunity

{D) SNMPVersion

220120-073626.log .a| fitace 40 2 [>] PARAGENT sample.n &  
[Main]  
"RemcteadminFort=9022  
"RemotettationIPAddress=1.1.1.1,1.1.1.2  
| "UserCredentialsPato="Wi\Pragram Files\PrivateArk\ervez\PARAgent .p  
onentliste"H:\Pregram Files\PzivateArk Server \PARVaile)  
mtLog

My Community"  
"SNMPTrapsTrresocidCPu=200, 90,4, 30, YES  
. �SAMPTrapsTeresnciddiskUsage=200, 65, 3,30, YES  
*SNMPTrapsTrresnoidPhysicaiMemory=200,90, 3,30, YES

1. Which component must be installed before the first CPM instllation?

Question 96-Which component must be installed beforeape fj CPN pstallation?  
(A) PTA A  
{B} PSM �  
�N  
(D) EPM  
_ �

1. In a default CyberArk installation, which group must a user be a member of a view the  
�reports� page in PVWA?

Question 98- Inad It cy �Ark installation, which group must @ user be a member of a view the

�reports� page |

�ar

D} Operators

Reports in PVWA

Reports can be generated in the Reports page in the PVWA by users who belong to the group thal is specifies in the

ManageReporsGrowp param eter in the Reparts section of the Web Access Opriens In the System Configurarion page. By default, this 1s

he FWA group.

1. You are creating a new RestAPI user that utilizes CyberArk Authentication. What is the correct  
process to provision this user?


62cdebe6180af89ba336df341a67eb17-31.jpg  
Question 99 -You are creating a new RestAPl user that utilizes CyberArk Authentication .  
What is the correct process to provision this user?

{B) PrivateArk Client>Tools>Administrative Tools >Directery Mapping=Add  
iC) PVWA>User Provisioning>LDAP integration >Add mapping  
{D) PYWA>LUser Provisioning >Users and Groups>New >User

1. You want to generate a license capacity report. Which tool accomplishes this?

Question 100-You want to generate a license capacity report.

Which teol accomplishes this?  
(A} Password Vault Web Access

(C} DiagnosisDB Report  
(D} �RestAPl

1. For a digital Vault cluster in a high availability configuration, how do you determine if a node  
is down?

Question 101-For a digital Vault cluster in a high availability configuration, how do:  
determine if a node is dawn? {

(B} The shared storage array is offline Cc,  
iC) An alertis generated in the Windows Event Log ,  
iD) The Digital Vault cluster does not detect a node fail

What does the Export Vault Data(EVD) utility do?

1. You need to move a platform from using PMTermisnal to using Terminal Plugin  
Controller(TPC).


62cdebe6180af89ba336df341a67eb17-32.jpg  
Question 102-You need to move a platform from using PI iro using Terminal Plugin

Controller{T PC),  
What must you do? X

ereEn  
CLASSES

(B} Using Priya A the PasswordManager_Shared safe and then select open  
Locate the ini fileNglatMyg to the platform you wish ta change.and double click  
At the bott fihg e insert a line �UseTPC=True� Remove any lines that reference

Regta for this change to take effect  
rh pen the process file of the platform you wish to configure to use TPC  
Qs he following parameter under the states section �use TPC =yes�  
Itis not possible to change a platform from using PMTerminal to using TPC.  
You must locate a new version of the platform that supports TPC and import the new platform  
wover writing the existing platform.

1. Users are unavle to launch Web Type Connection components from the PSM Server. Your  
manager asked you to open the case with CyberArk Support. Which logs will helo the CyberArk  
Support Team debug the issue?

�  
Question 103-Users are unable to launch Web Type Connection components M  
Server. Your manager asked you to cpen the case with CyberArk Support. will help  
the CyberArk Support Team debug the issue? (Choose 3)

{B} = PSMDebug.log  
(C} PSMTrace.log

(E] PMCaonsale.log Cc >

|  
�

Liver otk i cence

SZ ape dcconet Patent  
4 5]W error



62cdebe6180af89ba336df341a67eb17-33.jpg  
104) Which of the following properties are mandatory when adding accounts from a file?

Question 104-Which of the following properti ep hdatory when adding accounts from a  
fila? (Choose 3} X

(D) Username  
(E) Address G  
(F) Hosta

1. Which Automatic Remediation is configurable for a PTA detection of a �Suspected Credential  
Theft�?

~ 7  
Question 105- with ona Remediation is configurable for a PTA detection of a  
�Suspecte degtial Theft�?

id to Pending

1. A customer has two data centres and requires a single PVWA URL. Which deployment  
provided the best performance and the most redundancy?  
Question 107- A customer has two data centres and requires a single PYWA URL. Which deployment  
provides the best performance and the most redundancy?  
{A} Deploy two PVWAs behind a global traffic Manager

{B} Deploy one PVWA only  
ici Deploy two PVWAs in an active/standby made CLASES

: . a  
Reconcile Credentials clean

Disable Accounts CLASSES


62cdebe6180af89ba336df341a67eb17-34.jpg  
108) Arrange the steps to install the password Vault Web Access(PVWA) in correct sequence

Question 108-Arrange the steps to install the password Vault Web Access(PVWAJ in correct sequence

Correct Ordered Response -

7 on, 4

1. Which SMTP address can be set on the notification settings page to re-invoke the ENE.setup  
wizard after the initial vault installation?

Question 108-Which SMTP address can he set on the cane oder to re-invoke the

ENE.setup wizard after the initial vault installation? NO  
(A255. 255.255.255 � )

(B)8.8.8.8  
(C}192,168,1.1

Enable the ENE

After insta ling the Wault Une ENE must be enabled =� that ycu wt be able to receive email rouficauions about the vault actin: es.

Mare!

After the �SE has been vonFa_rad, thal rerunthe 2h E se: 4p  
vaigarrul, in Mig yh setae Sellnngs

1. Which file does the Vault installation Wizard Prompt you for during the vault install?

.  
Question 110-WWig Fy oes the Vault installation Wizard Prompt you for during the yault install?

a � 0 and License file wine  
ator CD and Vault Certificate CLASSES

aster CD and DBparam.ini



62cdebe6180af89ba336df341a67eb17-35.jpg  
111) Your customer, My Cyber Classes, wants to store the safes data in Drive D instead of Drive C.

Question 111-Your customer ,My Cyber Classes, wants to store the safes data in Drive D instead of  
Drive C.

(B) OBParm. ini ne  
(Cc) Vaultini SLASSES  
(0) User ini

TSParm. ini

The TaParm.ini �ile, ir the ServervConf install ation falder. conta the 1st of directories that can store Safes datahases.

1. In a rule using �Privileged Session Analysis and Responses� in PTA, which session options are  
available to configure as responses to activities?

Question 112-In a rule using �Privileged Session Analysis and Responses� in PTA, which session  
options are available to configure as responses to activities?

(B} Suspend,Terminate,Lack Account rs

(C} Pause, Terminate, None cm,  
(D} Suspend,Terminate

Session response

Serermine [i Session response. =tver None. Suspend, cr Terminate. tr the suopin ous $255107 arty Ty,

The cefanll rey pane is Mone



62cdebe6180af89ba336df341a67eb17-36.jpg  
113) Which configuration file & Vault utility are used to migrate the server key to an HSM?

Question 113 - Which configuration file & Vault utility are used to migrate the server key to an HSM?

(A) DBParm.ini & CAVaulitManagaer.exe  
(B) Vaultkeys.ini & CAVauitManagaer.exe  
(C) DBParm.ini & Changeserverkeys.exe  
(D) Vauitkeys.ini & Changeserverkeys.exe

4 In DBP armani, cow

1. What is the configuration file used by CPM scanner when scanning Unix/Linux Machine?

Question 714 � What is the configuration file used by CPM scanner when seanning Unix/Linux  
Machine?  
(A) UnixPrompts.ini  
{B} Flink.exe  
(C) DBParm.ini evn  
{0} P�Config.xml

Unix/Linux-specific configuration <

Whan scanning UniuLinux devices, the CPM scanner uses various parameters tn theUnixPrompesini configuration file. This te

sancer neral aon tld aunt. OF Fi = nC bers� ord Manage

tit CACPMScannerexe. avd can be cm ged gccorging ip tte les Dre iechine

1. A customer is moving from On-Premise to public cloud deployment, what is the best and  
most cost-effective way to secure the server keys?


62cdebe6180af89ba336df341a67eb17-37.jpg  
and most cost-effective way to secure the server kag?

Question 116- A customer is moving from uO deployment, what is the best

{A) Install the Vault in the cloud the game you would in an On-premise environment.  
Place the server key in a password folder on the operating system.

(B) Install the Vault in the cloud thes fy that you would in an On-premise environment.

Purchase a Ha � to secure the server key

{B) Install the Vau achine Images and secure the server key with a Hardware

security madel.

1. In PVWA, you are attempting to play a recording mode a session by user mycyberclasses, but  
there is no option to �FastForward� within the video. It plays and only allows you to skip between  
commands instead. You are also unable to download the video. What could be the issue?

Rare attempting to play a recording mode a session by user  
re is no option ta �Fast Forward� within the video, It plays and only allows you  
ands instead. You are also unable to download the video. What could ba the

{B] The browser you are suing is out of date and needs to update to be supported

{C) You don�t have view audit permission on safe where the account is stored

{D) You need to update the recorder settings in the platform to enable secure capture every  
10000ms or less.

Questian 117-|

issue?

1. A newly created platform allows users to access a Linux endpoint. When users click to  
connect, nothing happens which piece of platform is missing?

Question 118- A newly created platform allows users to access a Linux endpoint. When users click to  
connect, nothing happens which piece of platform is missing?

{B) UnixPrompts.ini  
(C) UnixProcess.ini  
{D) PSM-RDP Connection component

1. A new domain controller has been added to your domain. You need to ensure the CyberArk  
Infrastructure can use the new domain controller for authentication, which location you must

update?


62cdebe6180af89ba336df341a67eb17-38.jpg  
Question 119� A new domain controller has been added to your domain. You need to ensure the

CyberArk Infrastructure can use the new domain controller far authentication, which location you  
must update?

{B) On Vault Server Windows\System3?\ete\Hosts and in PYWA Windaws\System3?tetc  
{C) In Private Ark client under tools > Administrative tool > Directory Mapping  
(D} On the Vault Server in the Certificate store and on PVWA Server in Certficatagig��s

sts

1. Arrange the steps to complete CPM Hardening for Out of Domain deployment in the correct  
sequence:-

correct sequence: -

Correct Sequence arranged below >

~*  
Question 120 - Arrange the steps to complete CPM Hardening for Out of Domain �era in the

cyere  
CLASSES

~ Harden the CPM server

1. In the installatian media, in the InstallatonAutomazion folder (..  
senpt.

Se

This Script C�ates 4 bog file that lists all the steps (hat were Gar cied dutisuccesstul or failed). For each step the log ncludes the walle before the  
change and after the change.

- The scripe lng is created the same folder as the script and is ee

- The steps performed hy the senpt are explained b�low. in Y/enual wig eureei lat 27h

This script also credles a log file that analyzes the changes made when the Hardening Im F file is imparted.

- The log file i

- after the script has finished running, gach customer should review this log to verify that ne errors occurred.

- The steps perform ed wher th� Hardening INF file Is imported are explained below, in Manual inp uit Lut 374

1. What is the last step to ensure that a stand-alone Vault is synchronized with Organization�s  
NTP server?

Question Oe last step ta ensure that a stand-alone Vault is synchronized with  
izatiin's' Server?

ar rithe Vault Application using PrivateArk Client  
i tart the Organizations NTP Server

(D} Restart the Vault event Notification Engine Service



62cdebe6180af89ba336df341a67eb17-39.jpg  
122) A customer wants to store PSM recordings for 100 days. They estomate they will have 10  
Windows Sessions per day for 100 minutes each. How much storage is required for vault and  
PAReplicate for the PSM Storage?

Question 122- A customer wants to store PSM recordings for 100 days. They estimate they will have  
10 Windows Sessions per day for 100 minutes each. How much storage is required for the vault and  
PAReplicate for the PSM Storage?

(B} 250 GB ene,  
(C} 500 GB  
{D) 5GB

The PSM session's recording file sizes are:
- Windows (and other GUI tools such as Oracle Toad and wSphere Client) - ~250KB/min

� �SH (and other command line tools such as SQLPlus) - ~100KB/min

eS == (100� 10"100"250) = 2,50.00,000kb

= 25GB

Dignal Storage

cy

2,50,00,000 clasaes

Kilobyte Gigabyte

multiply the digital storage value by 12.6

1. You are logging intro CyberArk as Master User to recover an orphaned safe, which items are  
required to login as master?


62cdebe6180af89ba336df341a67eb17-40.jpg  
Question 123 - You are logging inte CyberArk as Ma  
items are required to login as master?

p Ksegh recover an orphaned safe, which

(B) Operator CD, Master Password, > Recess to PYWA Server, PVWA Access  
(C} Operator CD, Master Passwa some Access to Vault Server, Recover.exe |  
(D} Master CO, Master Passwp Access to PVWA, Recover.exe i

1. A user requested to view a password secured by dual control & is unsure who to contact to  
expediate the approval process. Vault Admin has been asked to look at account and identify who  
can approve the request? What is the correct way to identify users & groups who can approve?

ne  
Question 124 - A user reque wa password secured by dual control & is unsure who to  
contact to expedite the a ocass. Vault Admin has been asked to look at account and identify

who can approve the req

1. Which parameter must be identical for both the identity provider(idp) and PVWA?

Questignet25 - Which parameter must be identical for both the identity providerlidp} and PYWA?

(B} Idp �username� and �singleSignonServieURL� in PYWA saml.canfig file  
(C} Idp �audience�and �ServiceProviderNam� in PYWA samlLcaonfig file  
(D} Idp �secure hash alogorithm� and �certificate� in PVWA saml.config file

� Enter the IdP identifier that enables the PVWA ta idenufy the IdP. Also known as the [EEE of  
the ldP,



62cdebe6180af89ba336df341a67eb17-41.jpg  
126) Match each PTA Alert category with the PTA sensors that collect the data for it:-

Question 126 � Match each PTA Alert category with the PTA sensors that callect the data for it-

(A) Unmanaged Privileged Account � a  
{B} Anomalous access to multiple machine � [i

{C) Suspicious activities detected ina privileged session - [a

{D) Suspected Credential Theft � nn CLASSES

Detected when � user connects to a machine or a cloud service without fist a  
retrieving the required credentials from the �ault. *  
| |

Detected wren:

- a@connecton to a machine ora cloud service is Made with 2 prbvileged  
ACEOUNE BAL 1s HOt Stored in the VaulL

or

an accourt that Is net storedin the vault was added to a Windows local

privileged roup. .  
2  
NO  
CLASSES  
eC  
Detected when PTA ISernlines a privileged Session with actnaties [commands  
fF and Vault anomalies) defined a5 suspicious.

-_ Ww 4

Detected when an account logged onta a high number of machines during a 30  
relatively short time.

1. When are external vault users and groups synchronized by default?

2. When are external vault users and as a by default?

B. They are synchronized once every 24 hours between 7 PM and 12  
C. They are synchronized every 2 hours.

D. They are not synchronized according to a specific schedule


62cdebe6180af89ba336df341a67eb17-42.jpg  
130) Which file must be edited on the vault to configure it to send date to PTA?

1. Which file must be edited on the Vault to configure it ta send date to PTA?

B.PARAge nt. ini  
C.my.ini  
O.padr.ini

1. You created a new safe and need to ensure the user group cannot see the password, but can  
connect through PSM, which safe permissions must you grant to the group?

2. You Created a new safe and need to ensure the user group cannot see the password,  
But can connect through PSM, which safe permissions must you grant to the group?

C, Access safe without confirmation  
D, Retrieve files  
E. confirm requests

1. You receive this error �Error in change password to user domain\ user on domain server  
(\domain(winRc=5) Access is denied� which could be the cause?

2. You receive this error

�Error in change password to user domain \user on domain server(\domain{winRc=5)  
Access is denied" Which cauld be the cause?

#8. The domain controller is unreachable

c.. The password has been changed recently and minimum password age is preventing the  
change

D.The CPM service is disabled and will need to be restarted tite  
CLASSE


62cdebe6180af89ba336df341a67eb17-43.jpg  
135) You want to built a connector that connects to a website through the web applications for  
PSM framework. Which default connector do you duplicate and modify?

1. You want to built a connector that connects to a website through the web  
applications for PSM framework.  
Which default connector do you duplicate and modify?

A.PSM-Chrome sample crate

B.PSM- Webform CLARSES  
C. psm-webapp

1. Where can you assign a Reconcile account?

2. Where can you assign a Reconcile account?{ Choose 2}

c. in the Master policy of the PYWA
> . At the Safe level  
E. in the CPM settings


62cdebe6180af89ba336df341a67eb17-44.jpg  
137) The privileged Access Management solution provides an out-of-the-box target platform to  
manage SSH keys, called UNIX Via SSH keys. How are these keys managed?

1. The Privileged Access Management solution provides an out-of-the-box target  
platform to manage SSH keys ,called UNIX Via SSH Keys.  
How are these keys managed?

.CyberArk stores Public keys in the Vault and updates Private keys on target systems

7m

oy

. CyberArk does not store Public or Private keys and instead uses a reconcile account to create  
keys on demand

i

. CyberArk stores both Private and Public keys and can update target systems with  
either key

ny  
CYeER  
ELASSES

1. If PTA is integrated with a supported SIEM solution, which detection becomes available?

2. If PTA is integrated with a supported SIEM solution, which detection becomes  
available?

B. privileged access to the Vault dunng irregular days  
Gc. riskySPN

C. exposed credentials

1. Where can PTA be configured to send alerts?

15.Where can PTA be configured to send alerts? {Choose 2)

C. Google Analytics v  
D.EVD CTBER  
E. PAReplicate


62cdebe6180af89ba336df341a67eb17-45.jpg  
142) Which method can you use to add a user directly to the vault Admin Group?

16.Which method can you use to add a user directly to the vault Admin  
Group?{Choose 3}

C. PACL|  
D. PYWA

F. Sailpeoint

1. In a default CyberArk Installation, which group must a user be a member of to view the  
reports page in a pywa?

2. In a default CyberArk Installation ,Which group must a user be a member of to view  
the reports page in a pywa?

B. REPORTS USER  
Cc. PVWA REPORTS

BD. PERATORS

1. Which Automatic Remediation is configurable for a PTA detection of a �Suspected Credential  
Theft�?

20,.Which Autamatic Remediation is configurable for a PTA detection of a "Suspected  
Credential Theft?

&. Add to Pending

Hi  
c. Reconcile Credentials crsen

CLAgSES  
C. Disable Account :


62cdebe6180af89ba336df341a67eb17-46.jpg  
147) Match each permission to where it can be found

21.Match each permission to where it can be found  
Add Accounts  
2. Initiate CPM account management operations  
2. Add/Update Users

1. Add Safes

2. What do you need on the vault to support LDAP over SSL?

3. What do you need on the Vault to suppert LDAP over SSL?

RECPRV. key  
a private key for the external directory  
D. self signed Certificate(s) for the Vault

a

1. You have been asked to create an account group and assign three accounts which belong to a  
cluster, When you try to create a new group, you receive an unauthorized you are able to edit  
other aspects of the account properties. Which safe permission do you need to manager account  
groups?


62cdebe6180af89ba336df341a67eb17-47.jpg  
24. You have been asked te create an account group and assign three accounts which  
belong to a cluster .When you try to create a new group

�you receive an unauthorized you are able to edit other aspects of the account  
properties. which safe permission do you need to manage account groups?

A. create folders

B. specity next account content

(2. rename accounts cVaER  
a ci

1. Users are unable to launch Web Type Connection Components from the PSM server, Your  
manager asked you to open the case with CyberArk Support which logs will be most useful for the  
CyberArk Support Team to debug the issue?

2. Users are unable to launch Web Type Connection components from the PSM server,  
Your manager asked you to open the case with CyberArk Support Which logs will be most  
useful for the CyberArk Support Team to debug the issue? (Choose 3)

B. PSM Debug.log

a

PSMTrace log

FB. PMconsole, log

1. According to CyberArk which issues most commonly cause installed components to display as  
disconnected in the System Health Dashboard?

2. According te CyberArk which issues most commonly cause installed components  
to display as disconnected in the System Health Dashboard? (Choose 2)


62cdebe6180af89ba336df341a67eb17-48.jpg  
B. vault license expiry

}. browser compatibility issues

Ki. installed location file corruption

1. Your organization has a requirement to allow only one user to �check out passwords� and  
connect through the PSM securely. What needs to be configured in the Master policy to ensure  
this will happen?

2. Your organization has a requirement to allow only one user to "check out passwords"  
and connect through the PSM securely.  
What needs to be configured in the Master policy to ensure this will happen?

B, Enforce check-in/check-out exclusive access = inactive ; Require privileged session  
monitoring and isolation = inactive

C..Enforce check-in/check-out exclusive access = inactive; Record and save session activity  
= active

D. Enforce check-in/check-out exclusive access = active ;-Record and save session activity  
=inactive


62cdebe6180af89ba336df341a67eb17-49.jpg  
154) Which command generates a full backup of the Vault?

&. Which command generates a full backup of the Vault?  
B.PAPreBackup.exe.c :\PrivateArk\Server\ Conf\Vault.ini/ Backup/Asdf1234/full  
C.PARestore.exe Pair .ini /LogonFrormFile vault.ini /FullBackup

D. CAVaultManager.exe RecoverBackupFiles/BackupPoalName BkpSvrl1

29.What does the Export Vault Data (EVD) utility do?

B. generates a backup file that can be used as a cold backup

1. What does the Export Vault Data (EVD) utility do?

29.What does the Export Vault Data (EVD) utility do?

B. generates a backup file that can be used as a cold backup

C exports all passwords and imports them into another instance of CyberArk

D. keeps two active vaults In sync a  
CLASSES


62cdebe6180af89ba336df341a67eb17-50.jpg  
156) A user requested access to view a password secure by dual control and is unsure who to  
contact to expedite the apomval process, The Vault Admin has been account and identity who can  
approve their request What is the correct location to identify users or groups who can approve?

30.4 user requested access to view a password secured by dual control and is unsure who to  
contact to expedite the apomval process,The Vaut Admin has been account and identity who  
can approve their request

What is the correct location to identify users or groups who can approve?

4A. PVWA> Administration > Platform Configuration > Edit Platform > UL& Workflow > Dual  
Contral > Approvers

cc. PYWA > Account List > Edit> Show Advanced Settings > Dual Control > Direct Managers

> . PrivateArk > Admin Tools > Users and Groups > Auditors (Group

Membership} ete,

1. You have been asked to identify the up or down status of vault services. Which cyberark  
utility can you use to accomplish this task?

2. you have been asked to identify the up or down status of vault services,  
Which cyberark utility can you use to accomplish this task?

3. Privateark central Administration Console
4. PAS Reporter

D. Syslog

1. During a High Availability node switch you notice an error and the Cluster Vault Manager  
Utility fails back to the original node. Which log files should you check to investigate the cause of  
the issue?


62cdebe6180af89ba336df341a67eb17-51.jpg  
34. During a High Availability node switch you notice an error and the Cluster Vault Manager  
Utility fails back to the original node. Which log files should you check to investigate the  
cause of the issue? (Choose 3.)

A.CyberArk Webconscle.log

ne  
CRSER  
CLASSES

C.PM_Error.log  
D.ITALag. log

1. A new colleague created a directory mapping between the Active Directory groups and the  
Vault. Where can the newly configured directory mapping be tested?

36.A new colleague created a directory mapping between the Active Directory groups and  
the Vault. Where can the newly configured directory mapping be tested?

HY  
. . oe ae cvBE  
A. Connect to the Active Directory and ensure the organizational unit exists. CLASSES

B. Connect to Sailpoint (or similar tool) to ensure the organizational unit is correctly named,  
log in to the PVWA with "Administrator" and confirm aut  
C. Search for members that exist only in the mapping group to grant them safe permissions

through the PYWA

|

1. When an account is unable to change its own password, how can you ensure that password  
reset with the reconcile account is performed each times of a change


62cdebe6180af89ba336df341a67eb17-52.jpg  
38. When an account is unable to change its own password, how can you ensure  
that password reset with the reconcile account is performed each timed of a change

B.Set the parameter ChangePasswordinResetMode to Yes

C.Set the parameter IgnoreReconcileOQnMissing Account to No

D.Set the UnlockUserOnReconcile to Yes.  
39. Due to corporate storage canstraints, you have been asked to disable session  
monitoring and recording for 500 testing accounts used for your How do you  
accomplish this?

1. Which item is an option for PSM recording customization?

2. Which item is an option for PSM recarding customization? ce  
A. Windows events text recorder with automatic play-back

B.Windows events text recorder and universal ke rokes recording simultaneously

a

B.Custom audio recording for windows events.

1. You want to give a newly-created group rights to review security events under the Security  
pane. You also want to be able to update the status of these events. Where must you update the  
group to allow this?

41.You want to give a newly-created group rights to review security events under the  
Security pane. You also want to be able to update the status of these events. Where  
Must you update the group to allow this?

1. in the PTAAuthorization Groups parameter, found in Administration > Options > PTA

a  
B. in the PTAAuthorization Groups parameter, found in Administration >  
Options > General

|e

D.in the Security EventsFeedAuthorizationGroups parameter, found in Administration >  
Options > General


62cdebe6180af89ba336df341a67eb17-53.jpg  
170) What as the easiest way to duplicate an existing platform?

1. What as the easiest way to duplicate an existing platform?

A.From PrivateArk, copypaste the appropriate Policy.ini file, than rename it.

at  
CYBER  
GLASSES

C.From PrivateArk, copypaste the apprepriate settings in P�Configuration. xml, then update

the policyName variable.

O.From the PVWA ,navigate to the platforms page, select an existing platform that is similar to  
the new target account play,manually update the platform setting "Save as INSTEAD of save to  
duplicate and rename the platform

1. You are onboarding 5,000 UNIX root accounts for rotation by the CPM. You discover that the  
CPM is unable to log in directly with the root account and will need to a account. How can this be  
configured to allow for password management using least privilege?


62cdebe6180af89ba336df341a67eb17-54.jpg  
45. You are onboarding 5,000 UNIX root accounts for rotation by the CPM. You discover  
that the CPM is unable to log in directly with the root account and will need to a  
account.

How can this be configured to allow for password management using least privilege?

A.Configure each CPM to use the correct logon account  
B.Configure each CPM to use the correct reconcile account

O.Canfigure the UNIX platform to use the correct reconcile account.

1. You are creating a Dual Control workflow for a team�s safe. Which safe permissions must you  
grant to the Approvers group?

49 You are creating a Dual Control workflow for a team's safe. Which safe permissions must  
You grant to the Approvers group?

Kh. Retrieve accounts, Access Safe without confirmation  
c. Retrieve accounts, Authorize account request D.List

accounts, Unlock accounts eran  
CLASSES

1. You are troubleshooting a PVWA slow response. Which log files should you analyse first?

51, You are troubleshooting a PVWA slow response. Which log files should you analyze  
first? (Choose 2)

A.ITALog. log  
B.web.config

1. You are concerned about the Windows Domain password changes occurring during business  
hours Which settings must be updated to ensure passwords are only rotated outside of business  
hours?


62cdebe6180af89ba336df341a67eb17-55.jpg  
54. You are concerned about the Windows Domain password changes occurring during  
business hours Which settings must be updated to ensure passwords are only rotated  
outside of business hours?

i ee

b. In the Master Policy a  
Account Change Windew > ToHour & From Hour cLasses

C .Administration Settings  
CPM Settings> ToHaur & FromHour

D. On each individual account  
Edit> Advanced > ToHour & FromHour

1. The Active Directory User Configured for Windows Discovery needs which permissios(s) or  
membership?

2. The Active Directory User configured for Windows Discovery needs which permission(s}

or membership? a

A.Member of Domain Admin Group

Cc. Read and Write Permissions

1. What can you do to ensure each component server is operational?

B. Ping each component server to ensure connectivity.

C. Use the PrivateArk client to connect to the Vault server and validate all the services are running.  
D. Install the Vault Server interface on a remote machine to avoid interactive logon to the Vault OS  
and review the ITALog.log through the Vault Server interface.