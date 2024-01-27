---
aliases: 
tags: 
date created: Saturday, October 21st 2023, 8:30:27 pm
date modified: Wednesday, October 25th 2023, 8:12:10 am
---

## Start

1. Your customer has 5 main data centers with one PVWA in each Centre under different URLs. How can you make this setup fault-tolerant?
   - (a) This setup is already fault-tolerant
   - (b) Install more PVWA in each data center
   - (c) Continuously monitor the PVWA status and send users the link to another PVWA if issues are encountered
   - (d) Load balance all PVWA under the same URL

2. Which Pre-requisite step must be completed before installing Vault?
   - (a) Join the server to the domain
   - (b) Install a clean operating system
   - (c) Install Antivirus Software
   - (d) Copy the master CD to a folder in the vault server

3. You have been asked to design the number of PVWAs a customer must deploy. The customer has three data centers with a distributed vault in each, requires high availability and to use all Vault at all times, how many PVWAs does the customer need.
   - (a) 6
   - (b) 2
   - (c) 3
   - (d) 4

4. You are configuring Vault to send syslog data to your organization's SIM solution. What is a valid value for SyslogServer protocol parameter in dbparm.ini?
   - (a) TLS
   - (b) SSH
   - (c) SNMP
   - (d) SMTP
   

5. A customer installed multiple PVWAs in the production environment behind Balancer VIP. They subsequently observed that all the incoming traffic from the load balancer only hits one PVWA, even though all the PVWAs are up and running. What could be the likely situation?
   - (a) The load balancing algorithm is the least connections algorithm
   - (b) The certificate of the load balancer is not a wildcard cert
   - (c) The load balancing pool only has one PVWA server
   - (d) SSL passthrough is not configured on the load balancer

6. What is a requirement for setting fault tolerance for PSM?
   - (a) Use a load balancer
   - (b) Use a backup solution
   - (c) CPM must be in all data centers
   - (d) Install the vault HA cluster

7. Which Browser is supported by PSM web connectors developed using the CyberArk?
   - (a) Internet Explorer
   - (b) Opera
   - (c) Microsoft Edge
   - (d) Google Chrome

8. A customer asked you to help scope the company's PSM development. What should be included in the scoping conversation?
   - (a) Recording File path
   - (b) Recording Codec
   - (c) Recording retention period
   - (d) Recording File type

9. Which Parameter must be provided when registering a primary vault in Azure, but not in Amazon Web Service?
   - (a) /RecPub
   - (b) /AdminPass
   - (c) /MasterPass
   - (d) /RDPGateway

10. When creating a Distributed Vault environment Architecture, what is the Maximum number of Vault servers that can be deployed?
   - (a) 5 - Number of primary and satellite vaults can be specified during installation
   - (b) 3 - all primary
   - (c) 6 - 1 primary and 5 satellite
   - (d) 10 - 2 Primary and 8 satellite

1. You have been asked to install three additional PSMs after the initial PSM install. The first PSM was installed with a secondary Administrator Account. Which account should you use when installing the new PSM?
   - (a) Use the default vault administrator account
   - (b) Use the secondary administrator account
   - (c) You may use any user in the vault admin group
   - (d) Create a new administrator in the installation

2. You are installing PSM for SSH with AD-bridge in CyberArkSSHD mode for your customer, My Cyber Classes. What do you need to install to meet your customer's needs? (Choose 2)
   - (a) libssh
   - (b) CARKPSMP - Infra
   - (c) CARKpsmp
   - (d) CARKpsmp-ADBridge

3. You are responsible for installing a CPM. Which Vault authorization will your CyberArk user need to install the CPM? Choose the best one.
   - (a) Add Safes, Add/Update Users, Reset Users Password, Activate User Manage server file categories
   - (b) Add Safes, Add/Update Users, Manage Directory Mapping
   - (c) Manage directory, backup all safes, restore all safes
   - (d) Audit users, activate users, add network areas, Manage directory Mapping

4. Before the hardening process, your customer identified a PSM universal connector executable that will be required to run on the PSM. Which file should you update to allow this to run?
    - (a) PSMConfigureApplocker.xml
    - (b) PSMHardening.xml
    - (c) PSMAppConfig.xml
    - (d) PSMConfigureHardening.xml

5. After installing the first PSM server and before installing additional PSM servers, you must ensure the user performing the installation is not the direct owner of which safe?
    - (a) PSM Unmanaged Session Accounts Safe
    - (b) PSM Recordings Session Accounts Safe
    - (c) PSM Unmanaged Application Account Safe
    - (d) PSM Session Backup Account Safe

6. You are setting up HTML5 Gateway for PSM Sessions. Which servers need to be trusted by the Linux Host to secure communications through the gateway?
    - (a) PSM & PVWA
    - (b) PSM & CPM
    - (c) PVWA & Vault
    - (d) Vault & PSM

7. You need to recover an account "mcc-loc" for target server "host4.mcc.com" stored in "safe1". What do you need to recover and decrypt the object? (Choose 3)
    - (a) Recovery Private Key
    - (b) Recovery.exe
    - (c) Vault Data
    - (d) Recovery Public Key
    - (e) Server Key
    - (f) Master Password

8. You are installing multiple PVWAs behind the load balancer. Which statement is correct?
    - (a) Port 1858 must be opened between the load balancer and PVWAs.
    - (b) The Load balancer must be configured in DNS (Round Robin).
    - (c) The load balancer must support "sticky sessions".
    - (d) The LoadBalancerClientAddressHeader parameter in the PVWA.ini file must be set.

9. When running a privileged account Inventory report through the report page in PVWA on a specific safe, which permissions are required on that safe to show complete account inventory information?
    - (a) List account, view safe members
    - (b) Manage safe owners
    - (c) List account access safe without confirmation
    - (d) Manage safe, view audit- A company requires challenge/response multi-factor authentication for PSMP sessions which server must you integrate with CyberArk Vault?  
	- LDAP
	- PKI
	- SAML
	- RADIUS  
- Here are the formatted questions and options:

1. What is the default username for the PSM for SSH maintenance user?
   - (a) Proxymng
   - (b) Psmp_maintenance
   - (c) Psmpmaintenanceuser
   - (d) Proxymng_usr

2. Which CyberArk group does a user need to be part of to view recordings or monitor live sessions?
   - (a) Vault Admin
   - (b) Users
   - (c) Auditors
   - (d) Operator

3. How much disk space do you need on the servers for a PAReplicate?
   - (a) 500GB
   - (b) 1TB
   - (c) Same as disk size on Satellite Vault
   - (d) Same as disk size on Primary Vault

4. PAM solution provides an out-of-the-box target platform to manage SSH keys, called Unix Via SSH keys. How are these keys managed?
   - (a) CyberArk stores Private keys in Vault and updates Public key on Target System
   - (b) CyberArk stores Public keys in Vault and updates Private key on Target System
   - (c) CyberArk does not store Public or Private Key and instead uses a reconcile account to create keys on demand
   - (d) CyberArk stores both Private & Public Key and can update target systems with either key

5. In your organization, the "click to connect" button is not active by default. How can this feature be activated?
   - (a) Policies > Master Policy > Allow EPV transparent connection > Inactive
   - (b) Policies > Master Policy > Session Management - Require Privileged Session Monitoring and Isolation > Add Exception
   - (c) Policies > Master Policy > Allow EPV transparent connection > Active
   - (d) Policies > Policy Password Management

6. Status of Services when OF server is running on replication mode:
   - (a) CyberArk Windows Hardened firewall - Running
   - (b) PrivateArk Database - Running
   - (c) PrivateArk Server - Stopped
   - (d) CyberArk Vault Disaster Recovery - Running
   - (e) CyberArk Event Notification Engine - Stopped

7. Which option in PrivateArk Client is used to update a user's Vault Group Membership?
   - (a) Update > General Tab
   - (b) Update > Authorization Tab
   - (c) Update > Member of Tab
   - (d) Update > Group Tab

8. Which prerequisite is mandatory or not to run PSM Health Check?
   - (a) PSM Service Installed on Windows 2008R2, 2012R2, and 2016 — Mandatory
   - (b) PSM Service Installed on Windows 2012R2, 2016 & 2019 — Mandatory
   - (c) A Valid SSL cert installed on Web Server — Not Mandatory
   - (d) IIS Web Server — Not Mandatory

9. There is a requirement for a password change between 01:00 and 03:00 on Saturdays and Sundays, however, this doesn't work consistently. Which Platform settings do you need to check?
   - (a) The interval setting for the platform is incorrect and must be less than 120
   - (b) The immediate interval setting for the platform is incorrect and must be greater than or equal to 1
   - (c) The Days to Run setting for the platform is incorrect and must be set to Sat, Sun
   - (d) The HeadStartInterval setting for the platform is incorrect and must be set to 0

10. After installing the Vault, you need to allow Firewall access for Windows Time Service to sync with NTP server 10.1.1.1 and 10.2.2.2. What should you do?
   - (a) Edit dbparm.ini file and add AllowNonStandardFWAddresses=[10.1.1.1,10.2.2.2],Yes:outbound/udp
   - (b) Edit dbparm.ini file and add NTPServer=[10.1.1.1,10.2.2.2],Yes:outbound/udp
   - (c) Edit dbparm.ini file and add AllowNonStandardFWAddresses=[10.1.1.1,10.2.2.2],Yes:outbound/udp, 123:outbound/inbound udp
   - (d) Edit Windows Firewall to add a rule to allow port 123  
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
- **Question 68:** Match the built-in Vault user with the correct definition:
	- (A) This user appears on the highest level of the User hierarchy and has all the possible permissions. As such, it can create and manage other users on any level on the User's hierarchy → **Administrator**
	- (B) This user appears at the top of the user hierarchy, enabling it to view all the users in the safe. The user can produce reports of Safe activities and user activities which enables it to keep track of activity in the Safe and User requirements → **Auditor**
	- (C) This user is an internal user that cannot be logged onto and carries out internal tasks, such as automatically clearing expired user and safe history → **Batch**
	- (D) This user has all available Safe member authorizations except authorize password requests. This user has complete system control, manages a full recovery when necessary and cannot be removed from any safe → **Master**
- **Q69:** A new HTML5 Gateway has been deployed in your organization.  
Where do you configure the PSM to use the HTML5 Gateway?
	- (A) Administration > Options > Privileged Session Management > Configured PSM Servers > Connection Details > Add PSM Gateway
	- (B) Administration > Options > Privileged Session Management > Add Configured PSM Servers
	- (C) Administration > Options > Privileged Session Management > Add PSM Gateway
	- (D) Administration > Options > Privileged Session Management > Connection Details
- **Question 70:** A Vault Administrator team member can log in to CyberArk, but for some reason, is not given Vault Admin rights. Where can you check to verify that the Vault Admins directory mapping points to the correct AD group?
	- (A) PVWA > User Provisioning > LDAP Integration > Mapping Criteria
	- (B) PVWA > User Provisioning > LDAP Integration > Map Name
	- (C) PVWA > Administration > LDAP Integration > Mapping groups
	- (D) PVWA > Administration > LDAP Integration > AD groups  

**Question 71:** In the privateArk Client, how do you add an LDAP group to a CyberArk group?
- (A) **Select Update on the CyberArk group, and then click Add > LDAP Group**
- (B) Select Update on the LDAP Group, and then click Add > LDAP Group
- (C) Select Member of the CyberArk Group, and then Click Add > LDAP Group
- (D) Select Member of the LDAP group and then Click Add > LDAP Group

**Q72:** What are the basic network requirements to deploy a CPM server?
- (A) **Port 1858 to vault and port 443 to PVWA**
- (B) Port 1858 only
- (C) All ports to the vault
- (D) Port UDP/1858 to vault and all required ports to targets and port 389 to the PSM

**Question 73:** You have been asked to identify up or down status of Vault services. Which CyberArk utility can you use to accomplish this task?
- (A) Vault Replicator
- (B) PAS Reporter
- (C) **Remote Control Agent**
- (D) Syslog

**Question 74:** Which is mandatory for a PVWA installation? A DNS entry for the PVWA URL must be created.
- (A) A company signed TLS certificate must be imported into the server
- (B) **A vault administrative user must be used to register the PVWA**
- (C) Data Execution Prevention must be disabled  

**Question 76:** You are helping a customer prepare a Windows Server for PSM Installation. What is required for a successful installation?
- (A) Windows 2012 KB4558843
- (B) **Remote Desktop Services(RDS) Session Host Role**
- (C) Windows 2016 KB4558843
- (D) Remote Desktop Services (RDS) Session Broker

**Question 78:** In addition to bit rate and estimated total duration of recordings per day, what is needed to determine the amount of storage required for PSM recordings?
- (A) **retention period**
- (B) Number of PSMs
- (C) Number of users
- (D) Number of targets

**Question 79:** CyberArk user XYZ is trying to connect to the Target Linux server 192.168.1.164 using a domain account MCC/linuxuser01 on domain mycyberclasses.com PSM for SSH server 192.168.65.145. What is the correct syntax?
- (A) ssh xyz@linuxuser01@mycyberclasses.com@192.168.1.164@192.168.65.145
- (B) sshxyz@linuxuser01@mycyberclasses.com@192.168.1.164@192.168.65.145
- (C) **ssh xyz@linuxuser01@192.168.1.164@192.168.65.145**
- (D) ssh xyz@linuxuser01@mycyberclasses.com@192.168.1.164@192.168.65.145

**Question 80:** Which component must be installed on the vault if distributed vaults is used with PSM?  
	- (A) **RabbitMQ**  
	- (B) Disaster Recovery  
	- (C) Remote Control Client  
	- (D) Distributed Vault Server


1. Which tools are used during a CPM renaming process?
   - (a) API key Manager utility
   - (b) CreateCredFile Utility
   - (c) CPM/nDomain_Hardening.ps1 CLASSES
   - (d) PMTerminal.exe
   - (e) Data Execution Prevention

2. If a customer has one data center and requires high availability, how many PVWAs should be deployed?
   - (a) Two
   - (b) One PVWA Cluster
   - (c) One
   - (d) Two PVWA Cluster

3. In addition to disabling Windows services or features not needed for PVWA operations, which tasks does PVWA_Hardening.ps1 perform when run?
   - (a) Performs IIS hardening; imports the CyberArk INF configuration
   - (b) Performs IIS hardening; configures all group policy settings
   - (c) Performs IIS hardening; renames the local Administrator Account
   - (d) Configures Windows Firewall; removes all installation files  
**Question 85:** Refer to the exhibit - A customer is building a development environment in the Amazon Public Cloud through Amazon Web Services.

| EC2 instance | vCPU | Memory (GB) | Purpose            |
|--------------|------|-------------|--------------------|
| T2.micro     | 1    | 1           | General Purpose    |
| T3.medium    | 2    | 4           | General Purpose    |
| **M5.large**     | 2    | 8           | General Purpose    |
| C5.large     | 2    | 4           | Computer Optimized |                                                                                  
What is an ideal specification for the vault if it will only hold less than 1000 accounts?  
	- (A) t2.micro  
	- (B) T3.medium  
	- (C) **M5.large**  
	- (D) C5.large  

1. A customer is deploying PVWAs in Amazon Web Services Public Cloud. Which load balancing option does CyberArk recommend?
   - (a) Network Load Balancer
   - (b) Classic Load Balancer
   - (c) HTTPS Load Balancer
   - (d) Public Standard Load Balancer

2. Due to network activity, My Cyber Classes PrivateArk Server became active on the DR Vault while the primary vault was also running normally. All the components continue to point to the Primary Vault. Which steps should you perform to restore DR replication to normal?
   - (a) Replicate data from DR Vault to Primary Vault > Shutdown PrivateArk Server on DR Vault > Start Replication on DR Vault

   - (b) Shutdown PrivateArk Server on DR Vault > Start Replication on DR Vault

   - (c) Shutdown PrivateArk Server on Primary Vault > Replicate Data from DR Vault to Primary Vault > Shutdown PrivateArk Server on DR Vault > Start Replication on DR Vault

   - (d) Shutdown PrivateArk Server on DR Vault > Replicate Data from DR Vault to Primary Vault > Shutdown PrivateArk Server on DR Vault > Start Replication on DR Vault

3. Which authentication method does PSM for SSH support?
   - (a) CyberArk password, LDAP, RADIUS, SAML
   - (b) LDAP, Windows Authentication, SSH Keys
   - (c) RADIUS, Oracle, SSO, CyberArk Password
   - (d) CyberArk Password, LDAP, RADIUS

4. To ensure all sessions are being recorded, a CyberArk Administrator goes to the master policy and makes configuration changes.
   - (a) Require privileged session monitoring and isolation—inactive; Record save session activity=active
   - (b) Require privileged session monitoring and isolation—inactive; Record save session activity—inactive
   - (c) Require privileged session monitoring and save session activity—active; Record save session activity=active
   - (d) Require privileged session monitoring and isolation—active; Record save session activity—inactive

5. Refer to the exhibit. To Enable PKI Authentication for PVWA (Version 10 and above), which web server config file must be updated and appended with the displayed settings?
   - (a) %WinDir%\System32\Inet\Serv\Config\Applicationhost.config
   - (b) C:\inetpub\adminscripts\web.config
   - (c) PasswordVault\CustomAuthenticationDLs\CyberArk.Authentication.CustomPKIPN.dll
   - (d) C:\inetpub\wwwroot\PasswordVault\Env

6. To use PSM Connections while in the PVWA, what are the minimum safe permissions a user or group will need?
   - (a) List Accounts, Use Accounts
   - (b) List Accounts, Retrieve Accounts
   - (c) Use Accounts
   - (d) List Accounts, Use Accounts, Retrieve Accounts, Access Safe without Confirmation

  

- Here are the formatted questions and options:

1. Which is a valid combination of primary and secondary layers of authentication for a company's two-factor authentication policy?
   - (a) RSA SecureID Authentication (in PVWA) and LDAP Authentication.
   - (b) CyberArk Authentication and RADIUS Authentication.
   - (c) Oracle SSO (In PVWA) and SAML Authentication.
   - (d) LDAP Authentication and RADIUS Authentication.

2. A customer wants to implement a multi-cloud strategy for a vault deployment. Which architecture should you recommend?
   - (a) Primary Vault in AWS, DR Vault in Azure. Both Primary and DR Vault integrate with AWS Key Management Service.
   - (b) Primary Vault in Azure, DR Vault in AWS. Both Primary and DR Vault integrate with Azure Key Management Service.
   - (c) Primary Vault in AWS, DR Vault in Azure. The primary vault will be integrated with Azure Key Management Service, while the DR Vault will be integrated with Azure Key Vault.
   - (d) Primary Vault in Azure, DR Vault in AWS. Neither will integrate with Cloud Native key management systems. The server will reside on the Operating system.

3. You have been asked to configure SNMP remote monitoring for your organization's vault servers. In the PARAgent.ini, which parameter specifies the destination of the Vault SNMP traps?
   - (a) SNMPHostIP
   - (b) SNMPTrapPort
   - (c) SNMPCommunity
   - (d) SNMPVersion

4. Which component must be installed before the first CPM installation?
   - (a) PTA
   - (b) PSM
   - (c) PVWA
   - (d) EPM

5. In a default CyberArk installation, which group must a user be a member of to view the reports page in PVWA?
   - (a) PVWA Monitor
   - (b) Report Users
   - (c) PVWA Reports
   - (d) Operators

6. You are creating a new RestAPI user that utilizes CyberArk Authentication. What is the correct process to provision this user?
   - (a) PrivateArk Client > Tools > Administrative Tools > Users & Groups > New > User
   - (b) PrivateArk Client > Tools > Administrative Tools > Directory Mapping > Add
   - (c) PVWA > User Provisioning > LDAP integration > Add mapping
   - (d) PVWA > User Provisioning > Users and Groups > New > User

7. You want to generate a license capacity report. Which tool accomplishes this?
   - (a) Password Vault Web Access
   - (b) PrivateArk Client
   - (c) DiagnosisDB Report
   - (d) RestAPI

8. For a digital Vault cluster in a high availability configuration, how do you determine if a node is down?
   - (a) The heartbeat is no longer detected on Private Network
   - (b) The shared storage array is offline
   - (c) An alert is generated in the Windows Event Log
   - (d) The Digital Vault cluster does not detect a node failure.


9. You want to generate a license capacity report. Which tool accomplishes this?
   - (a) Password Vault Web Access
   - (b) PrivateArk Client
   - (c) DiagnosisDB Report
   - (d) RestAPI

10. For a Digital Vault cluster in a high availability configuration, how do you determine if a node is down?
   - (a) The heartbeat is no longer detected on Private Network
   - (b) The shared storage array is offline
   - (c) An alert is generated in the Windows Event Log
   - (d) The Digital Vault cluster does not detect a node failure.  

**Question 102:** You need to move a platform from using PMTerminal to using Terminal Plugin Controller (TPC). What must you do?

- (A) **Within PVWA**  
    - Click `Administration > Platform Management`  
    - Select the platform, and then click `Edit`  
    - In the left pane, click `Automatic password management > CPM Plug-in`  
    - Set the `ExeName` parameter value to `CyberArk.TPC.exe`  
- (B) Using PrivateArk, select the `PasswordManager_Shared` safe and then select open. Locate the ini file relating to the platform you wish to change, and double click. At the bottom of the file, insert a line "`UseTPC=True`". Remove any lines that reference "PMTerminal" and save. Return the ini file to safe. Restart CPM for this change to take effect.  
- (C) Open the process file of the platform you wish to configure to use TPC. Add the following parameter under the platforms section "use TPC =yes". It is not possible to change a state from using PMTerminal to using TPC. You must locate a new version of the platform that supports TPC and import the new platform over writing the existing platform.


1. Users are unable to launch Web Type Connection components from the PSM Server. Your manager asked you to open the case with CyberArk Support. Which logs will help the CyberArk Support Team debug the issue? (Choose 3)
   - (a) PSM Console.log
   - (b) PSMDebug.log
   - (c) PSMTrace.log
   - (d) `<Session_ID>.Component.log`
   - (e) PM.Console.log
   - (f) ITA.log

2. Which of the following properties are mandatory when adding accounts from a file? (Choose 3)
   - (a) Safe Name
   - (b) Platform ID
   - (c) All required properties specified in the Platform
   - (d) Username
   - (e) Address
   - (f) Hostname

3. Which Automatic Remediation is configurable for a PTA detection of a Suspected Credential Theft?
   - (a) Add to Pending
   - (b) Rotate Credentials
   - (c) Reconcile Credentials
   - (d) Disable Accounts

4. A customer has two data centers and requires a single PVWA URL. Which deployment provides the best performance and the most redundancy?
   - (a) Deploy two PVWAs behind a global traffic Manager
   - (b) Deploy one PVWA only
   - (c) Deploy two PVWAs in an active/standby mode.
   - (d) Deploy two PVWAs using DNS RoundRobin

5. Arrange the steps to install the Password Vault Web Access (PVWA) in the correct sequence. Correct Ordered Response:
   - (1) Run the PVWA_Prerequisites.ps1 file as an administrator
   - (2) Run the PVWAInstallation.ps1 script as Administrator
   - (3) Run the PVWARegisterComponent.ps1 script with Vault password
   - (4) Run the PVWA Hardening.ps1 script in PowerShell as Administrator

6. Which SMTP address can be set on the notification settings page to re-invoke the ENE.setup wizard after the initial vault installation?
   - (a) 255.255.255.255
   - (b) 8.8.8.8
   - (c) 192.168.1.1
   - (d) 1.1.1.1

7. Which file does the Vault installation Wizard prompt you for during the vault install?
   - (a) Operator CD and License file
   - (b) Master CD and License file
   - (c) Operator CD and Vault Certificate
   - (d) Master CD and DBparam.ini

**Question 111:** Your customer, My Cyber Classes, wants to store the safes data in Drive D instead of Drive C.
- (A) **TSParm.ini**
- (B) DBParm.ini
- (C) Vault.ini
- (D) User.ini

**Question 112:** In a rule using “Privileged Session Analysis and Responses” in PTA, which session options are available to configure as responses to activities?
- (A) **Suspend,Terminate,None**
- (B) Suspend,Terminate,Lock Account
- (C) Pause,Terminate,None
- (D) Suspend,Terminate

**Question 113:** Which configuration file & Vault utility are used to migrate the server key to an HSM?
- (A) **DBParm.ini & CAVaultManager.exe**
- (B) Vaultkeys.ini & CAVaultManager.exe
- (C) DBParm.ini & Changeserverkeys.exe
- (D) Vaultkeys.ini & Changeserverkeys.exe

**Question 114:** What is the configuration file used by CPM scanner when scanning Unix/Linux Machine?
- (A) **UnixPrompts.ini**
- (B) Plink.exe
- (C) DBParm.ini
- (D) PVConfig.xml

**Question 116:** A customer is moving from On-Premise to public cloud deployment, what is the best and most cost-effective way to secure the server key?
- (A) Install the Vault in the cloud the same way that you would in an On-premise environment. Place the server key in a password protected folder on the operating system.
- (B) Install the Vault in the cloud the same way that you would in an On-premise environment. Purchase a Hardware Security Module to secure the server key.
- (C) **Install the Vault using Amazon Machine Images and secure the server key using native cloud key management system.**
- (D) Install the Vault using Amazon Machine Images and secure the server key with a Hardware security model.

**Question 117:** In PVWA, you are attempting to play a recording mode a session by user mycyberclasses, but there is no option to “Fast Forward” within the video. It plays and only allows you to skip between commands instead. You are also unable to download the video. What could be the issue?
- (A) **Recording is of PSM for SSH Session**
- (B) The browser you are using is out of date and needs to update to be supported
- (C) You don’t have view audit permission on safe where the account is stored
- (D) You need to update the recorder settings in the platform to enable secure capture every 1000ms or less.

**Question 118:** A newly created platform allows users to access a Linux endpoint. When users click to connect, nothing happens which piece of platform is missing?
- (A) **PSM-SSH Connection Component**
- (B) UnixPrompts.ini
- (C) UnixProcess.ini
- (D) PSM-RDP Connection component

**Question 119:** A new domain controller has been added to your domain. You need to ensure the CyberArk Infrastructure can use the new domain controller for authentication, which location you must update?
- (A) **On Vault Server \Windows\System32\etc\Hosts and in PVWA Application under Administration > LDAP Integration > Directories > Hosts**
- (B) On Vault Server \Windows\System32\etc\Hosts and in PVWA \Windows\System32\etc\Hosts
- (C) In Private Ark client under tools > Administrative tool > Directory Mapping
- (D) On the Vault Server in the Certificate store and on PVWA Server in Certificate store.

**Question 120:** Arrange the steps to complete CPM Hardening for Out of Domain deployment in the correct sequence:
1. **Locate the CPM_hardening.ps1 scripts in the installation media**
2. **Open Powershell as Administrator and run the script**
3. **Review the script log called HardeningScript.log**
4. **Review the script log called CYBR_Hardening_secedit.log**

**Question 121:** What is the last step to ensure that a stand-alone Vault is synchronized with Organization’s NTP server?
- (A) Restart the Vault Application using PrivateArk Client
- (B) Restart the Organizations NTP Server
- (C) **Restart the Vault Application using the PrivateArk Central Administration Console**
- (D) Restart the Vault event Notification Engine Service  
**Question 121** : A customer wants to store PSM recordings for 100 days. They estimate they will have 10 Windows Sessions per day for 100 minutes each. How much storage is required for vault and PAReplicate for the PSM Storage?
- (A) 25 GB
- (B) 250
- (C) 500 GB
- (D) 5GB  


**Question 123:** You are logging into CyberArk as Master User to recover an orphaned safe, which items are required to login as master?
- (A) **Master CD, Master Password, Console Access to Vault Server, Private Ark Client**
- (B) Operator CD, Master Password, Console Access to PVWA Server, PVWA Access
- (C) Operator CD, Master Password, Console Access to Vault Server, Recover.exe
- (D) Master CD, Master Password, Console Access to PVWA, Recover.exe

**Question 124:** A user requested to view a password secured by dual control & is unsure who to contact to expedite the approval process. Vault Admin has been asked to look at the account and identify who can approve the request? What is the correct way to identify users & groups who can approve?
- (A) PVWA > Administration > Platform Management > Ui & Workflow > Dual Control > Approver
- (B) **PVWA > Policies > Access Control (Safes) > Safe Members > Workflow > Authorize Password Request**
- (C) PVWA > Account list > Edit > Show passwords > Dual Control > Direct Managers
- (D) PrivateArk > Admin tool > Users & groups > Auditors (Group Membership)

**Question 125:** Which parameter must be identical for both the identity provider(idp) and PVWA?
- (A) **Idp “EntityID” and “PartnerIdentityProvider Name” in PVWA Saml.config file**
- (B) Idp “username” and “SingleSignOnServiceURL” in PVWA saml.config file
- (C) Idp “audience” and “ServiceProviderName” in PVWA saml.config file
- (D) Idp “secure hash algorithm” and “certificate” in PVWA saml.config file

**Question 126:** Match each PTA Alert category with the PTA sensors that collect the data for it:
- (A) Unmanaged Privileged Account — **Logs, Vault, AD (Optional), AWS (Optional)**
- (B) Anomalous access to multiple machine — **Network Sensor, PTA Windows Agent**
- (C) Suspicious activities detected in a privileged session — **Vault**
- (D) Suspected Credential Theft — **Logs, Vault, AWS (Optional)**

**Question 129:** When are external vault users and groups synchronized by default?
- (A) **They are synchronized once every 24 hours between 1 AM and 5 AM**
- (B) They are synchronized once every 24 hours between 7 PM and 12 AM
- (C) They are synchronized every 2 hours.
- (D) They are not synchronized according to a specific schedule

**130) Which file must be edited on the vault to configure it to send date to PTA?**
1. `dbparm.ini`
2. `PARAgent.ini`
3. `my.ini`
4. `padr.ini`

---

**132) You created a new safe and need to ensure the user group cannot see the password, but can connect through PSM, which safe permissions must you grant to the group?**
1. List accounts
2. Use accounts
3. Access safe without confirmation
4. Retrieve files
5. Confirm requests

---

**133) You receive this error “Error in change password to user domain\ user on domain server \(domain(winRc=5) Access is denied” which could be the cause?**
1. The account does not have sufficient permissions to change its own password
2. The domain controller is unreachable
3. The password has been changed recently and minimum password age is preventing the change
4. The CPM service is disabled and will need to be restarted

---

**135) You want to built a connector that connects to a website through the web applications for PSM framework. Which default connector do you duplicate and modify?**
1. PSM-Chrome sample
2. PSM- Webform
3. psm-webapp
4. Psm-WebAppSample

---

**136) Where can you assign a Reconcile account?**
1. In PVWA at the account level
2. PVWA in the platform configuration
3. In the Master policy of the PVWA
4. At the Safe level
5. In the CPM settings

---

**11. Privileged Access Management Solution Management of SSH Keys**

The Privileged Access Management solution provides an out-of-the-box target platform to manage SSH keys called UNIX Via SSH Keys. How are these keys managed?
- A. CyberArk stores Private keys in the Vault and updates Public keys on target systems.
- B. CyberArk stores Public keys in the Vault and updates Private keys on target systems.
- C. CyberArk does not store Public or Private keys and instead uses a reconcile account to create keys on demand.
- D. CyberArk stores both Private and Public keys and can update target systems with either key.

**12. Integration of PTA with Supported SIEM Solution**

If PTA is integrated with a supported SIEM solution, which detection becomes available?
- A. Unmanaged privileged account
- B. Privileged access to the Vault during irregular days
- C. RiskySPN
- D. Exposed credentials

**15. Configuration of PTA for Sending Alerts**

Where can PTA be configured to send alerts? (Choose 2)
- A. SIEM
- B. Email
- C. Google Analytics
- D. EVD
- E. PAReplicate

**16. Methods to Add User to the Vault Admin Group**

Which method can you use to add a user directly to the vault Admin Group? (Choose 3)
- A. Rest API
- B. Private Ark Client
- C. PACLI
- D. PVWA
- E. AD
- F. Sailpoint

**17. Default CyberArk Installation Group Requirement**

In a default CyberArk Installation, which group must a user be a member of to view the reports page in a pvwa?
- A. PVWA MONITOR
- B. REPORTS USER
- C. PVWA REPORTS
- D. PERATORS

**20. Automatic Remediation for PTA Detection**

Which Automatic Remediation is configurable for a PTA detection of a "Suspected Credential Theft"?
- A. Add to Pending
- B. Rotate Credentials
- C. Reconcile Credentials
- D. Disable Account

---
**147) Match each permission to where it can be found**
- Add Accounts
- Initiate CPM account management operations
- Add/Update Users
- Add Safes


**149) What do you need on the vault to support LDAP over SSL?**
- **A.** CA Certificate(s) used to sign the External Directory certificate
- **B.** RECPRV.key
- **C.** a private key for the external directory
- **D.** self-signed Certificate(s) for the Vault

---

**24) You have been asked to create an account group and assign three accounts which belong to a cluster. When you try to create a new group, you receive an unauthorized error. You are able to edit other aspects of the account properties. Which safe permission do you need to manage account groups?**
- **A.** create folders
- **B.** specify next account content
- **C.** rename accounts
- **D.** manage safe

---

**151) Users are unable to launch Web Type Connection Components from the PSM server. Your manager asked you to open the case with CyberArk Support. Which logs will be most useful for the CyberArk Support Team to debug the issue? (Choose 3)**
- **A.** PSMConsole.log
- **B.** PSMDebug.log
- **C.** PSMTrace.log
- **D.** <Session_ID> Component.log
- **E.** PMConsole.log
- **F.** ITALog.log

---

**152) According to CyberArk, which issues most commonly cause installed components to display as disconnected in the System Health Dashboard?**  
network instabilities/outages  
vault license expiry  
credential de-sync  
browser compatibility issues  
installed location file corruption


**53) Your Organization's Requirement**:
> Your organization has a requirement to allow only one user to "check out passwords" and connect through the PSM securely. What needs to be configured in the Master policy to ensure this will happen?

- A. Enforce check-in/check out exclusive access active; Require privileged session monitoring and isolation = active
- B. Enforce check-in/check-out exclusive access = inactive; Require privileged session monitoring and isolation = inactive
- C. Enforce check-in/check-out exclusive access = inactive; Record and save session activity = active
- D. Enforce check-in/check-out exclusive access = active; Record and save session activity = inactive

---

**154) Full Backup of the Vault**:
> Which command generates a full backup of the Vault?

- A. PAReplicate.exe.Vault .ini/Logon from file user.ini/Fullbackup
- B. PARepBackup.exe.C:\PrivateArk\Server\Conf\Vault.ini/ Backup/Asdf1234/full
- C. PARestore.exe PADR .ini /LogonFromFile vault.ini /FullBackup
- D. CAVaultManager.exe RecoverBackupFiles/BackupPoolName BkpSvr1

---

**29 & 155) Export Vault Data Utility**:
> What does the Export Vault Data (EVD) utility do?

- A. Exports data from the Vault to TXT or CSV files, or to MSSQL databases
- B. Generates a backup file that can be used as a cold backup
- C. Exports all passwords and imports them into another instance of CyberArk
- D. Keeps two active vaults in sync

---

**156)** A user requested access to view a password secure by dual control and is unsure who to contact to expedite the approval process. The Vault Admin has an account and identity. What is the correct location to identify users or groups who can approve the request?

- **A.** PVWA > Administration > Platform Configuration > Edit Platform > UI & Workflow > Dual Control > Approvers
- **B.** PVWA > Policies > Access Control (Safes) > Select the safe > Safe Members > Workflow > Authorize Password Requests
- **C.** PVWA > Account List > Edit > Show Advanced Settings > Dual Control > Direct Managers
- **D.** PrivateArk > Admin Tools > Users and Groups > Auditors (Group Membership)

---

**159)** You have been asked to identify the up or down status of vault services. Which CyberArk utility can you use to accomplish this task?

- **A.** Privateark central Administration Console
- **B.** PAS Reporter
- **C.** PrivateArk Remote Control Agent
- **D.** Syslog

---

**160)** During a High Availability node switch, you notice an error and the Cluster Vault Manager Utility fails back to the original node. Which log files should you check to investigate the cause of the issue? (Choose 3.)

- **A.** CyberArk Webconsole.log
- **B.** VaultDB.log
- **C.** PM_Error.log
- **D.** ITALog.log
- **E.** ClusterVault.console.log
- **F.** logiccontainer log

---

**162)** A new colleague created a directory mapping between the Active Directory groups and the Vault. Where can the newly configured directory mapping be tested?

- **A.** Connect to the Active Directory and ensure the organizational unit exists.
- **B.** Connect to Sailpoint (or similar tool) to ensure the organizational unit is correctly named, log in to the PVWA with "Administrator" and confirm aut
- **C.** Search for members that exist only in the mapping group to grant them safe permissions through the PVWA
- **D.** Connect to the PrivateArk Client with the Administrator Account to see if there is a user in the Vault Admin Group

---

**166)** Which item is an option for PSM recording customization?

- **A.** Windows events text recorder with automatic play-back
- **B.** Windows events text recorder and universal keystrokes recording simultaneously
- **C.** Universal keystrokes text recorder with windows events text recorder disabled
- **D.** Custom audio recording for windows events.

---

**167)** You want to give a newly-created group rights to review security events under the Security pane. You also want to be able to update the status of these events. Where must you update the group to allow this?

- **A.** in the PTA Authorization Groups parameter, found in Administration > Options > PTA
- **B.** in the PTA Authorization Groups parameter, found in Administration Options > General
- **C.** in the SecurityEventsAuthorization Groups parameter, found in Administration > Security > Options
- **D.** in the Security EventsFeedAuthorizationGroups parameter, found in Administration > Options > General

---

**170) What is the easiest way to duplicate an existing platform?**

- A. From PrivateArk, copy paste the appropriate Policy.ini file, then rename it.
- B. From the PVWA, navigate to the platforms page, select an existing platform that is similar to the new target account platform and then click duplicate, name the platform.
- C. From PrivateArk, copy paste the appropriate settings in PVConfiguration.xml, then update the policyName variable.
- D. From the PVWA, navigate to the platforms page, select an existing platform that is similar to the new target account play, manually update the platform setting "Save as" INSTEAD of "save to" duplicate and rename the platform.

---

**45. You are onboarding 5,000 UNIX root accounts for rotation by the CPM.** You discover that the CPM is unable to log in directly with the root account and will need to a account. How can this be configured to allow for password management using least privilege?

- A. Configure each CPM to use the correct logon account
- B. Configure each CPM to use the correct reconcile account
- C. Configure the UNIX platform to use the correct logon account
- D. Configure the UNIX platform to use the correct reconcile account.

---

**175) You are creating a Dual Control workflow for a team’s safe. Which safe permissions must you grant to the Approvers group?**

- A. List accounts, Authorize account request
- B. Retrieve accounts, Access Safe without confirmation
- C. Retrieve accounts, Authorize account request 
- D. List accounts, Unlock accounts

---

**177) You are troubleshooting a PVWA slow response. Which log files should you analyze first? (Choose 2)**

- A. ITALog.log
- B. web.config
- C. CyberArk WebApplication.log
- D. CyberArk.WebConsole.log