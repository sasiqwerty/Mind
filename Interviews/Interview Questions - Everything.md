---
aliases: 
tags: 
date created: Monday, August 28th 2023, 5:58:37 pm
date modified: Sunday, November 5th 2023, 7:54:24 pm
---

## What is CyberArk and why is it Important?

CyberArk offers centralized and tamper-proof audit logs for all privileged access activities, ensuring individual accountability for any actions involving shared privileged accounts.

CyberArk introduces a unique layer of internal security named privileged account security. This layer monitors, controls, and detects all activities related to credentials and privileged accounts. Since privileged accounts are integral to every IT infrastructure and are frequently the target in advanced cyberattacks, safeguarding them is crucial. Attackers, once they infiltrate a system, require these credentials to navigate and access valuable data. CyberArk provides users with the means to exert control over these credentials, securing the privileged accounts and enhancing the overall cybersecurity posture.

## What is a Privileged Account?

A privileged account is a user account that possesses greater permissions compared to regular users. These accounts grant elevated rights and capabilities, allowing them to perform tasks such as software installation or removal and configuration adjustments. Commonly referred to as "super user" accounts, they are found across different platforms and systems. Examples include:

- Root for Linux
- Administrator for Windows
- SA for Oracle
- Enable for Cisco

## What Are the Different Types of Privileged Accounts?

Privileged accounts come in various forms, and some of the primary types include:

1. **Local account**: This type of account controls access to a single, physical computer. The credentials (username, password, and SID/UID) for a local account are stored on the computer's hard drive. When someone logs in using a local account, the computer validates the login by checking its own stored credentials. Essentially, a local account grants a user a certain level of access to that individual computer.

2. **Domain account**: A domain account refers to a user whose credentials are stored on a domain controller instead of the computer they are accessing. When logging in as a domain user, the computer queries the domain controller to determine the privileges granted to that user.

3. **Service account**: Service accounts are specialized user accounts used by applications or services to interact with the operating system. These accounts allow services to make changes to the OS or its configuration. By assigning specific permissions, one can regulate the actions a service can execute using the service account.

4. **Shared account**: Shared accounts utilize a single set of credentials to authenticate multiple users. This type of account can present challenges for IT because it can be difficult to track individual activity and ensure visibility. The foundation of identity and access management (IAM) is knowing which user accessed which resource, a task that becomes complex with shared accounts.

## What is Identity and Access Management (IAM)?

Identity and access management (IAM) refers to the security discipline that manages and ensures the appropriate access of users to technology resources. It encompasses both the process of defining and controlling user roles and their respective access privileges, as well as the circumstances under which these privileges are granted or denied. Here's a breakdown:

- **Authentication**: IAM systems authenticate users, verifying their identity. Once a user's identity is successfully authenticated, the IAM system then determines their authorization levels to ensure they can perform the requested activity.
    
- **Enterprise IT roles**: IAM not only applies to employees through employee identity management but also to customers via customer identity management.
    
- **Digital Identity**: The primary aim of IAM systems is to ensure one distinct digital identity per individual. This identity then serves as the basis for all permissions and rights assigned to that user.
    
- **Access Lifecycle**: After establishing a digital identity, it needs continuous management. This includes monitoring, updating, and adjusting access rights throughout the user's association with the organization.
    

In essence, IAM is the framework that ensures users have the appropriate access to resources, improving security, and enhancing operational efficiency.

## What is EPV?

EPV, or Enterprise Password Vault, is a product offered by CyberArk. It is designed to help organizations secure, manage, automate changes for, and log all activities associated with various types of privileged passwords. Here's a breakdown:

- **Central Repository**: EPV utilizes a highly secure central repository to store and safeguard SSH keys as well as passwords. This makes it applicable in various settings, including on-premises, hybrid, and cloud environments.
    
- **Auditing and Control**: The system's auditing and control features allow organizations to monitor and pinpoint any misuse of privileged accounts, ensuring enhanced security and accountability.
    
- **Main Functions**: The primary roles of EPV are to administer, secure, rotate, and control access to privileged account passwords, thereby minimizing risks associated with unauthorized access or breaches.
    

Essentially, EPV streamlines the management of privileged passwords, making it easier and more secure for organizations to handle sensitive credentials

## What Are the Vault Security Layers? #defcon1

CyberArk's Vault employs a multi-layered security approach to ensure the utmost protection for stored credentials and other sensitive data. Here's a breakdown of these layers:

1. **Session Encryption**:
    - **Proprietary Protocol**: The Vault requires a dedicated server to operate, a mandate enforced by the CyberArk firewall. This firewall restricts communication to and from the server, only allowing its proprietary authenticated protocol, known as the Vault protocol.
    - **OpenSSL Encryption**: All passwords and files within the Vault are encrypted, utilizing an encryption framework that remains transparent to the end-user. Consequently, neither users nor administrators have to manage or address key-related issues.

2. **Firewall**:
    - **Hardened built-in Windows Firewall**: CyberArk's firewall ensures that the Vault's code is the sole executable on its dedicated server, guaranteeing a pristine environment and enabling the security system's total control over the server.

3. **Authentication**:
    - **Single or Two Factor Authentication**: Access to the Vault mandates authentication via a robust bi-directional authentication protocol. Methods include Passwords, PKI digital certificates, RSA SecurID tokens, RADIUS protocol, USB Tokens, or Windows authentication. The Privileged Account Security solution can also integrate third-party authentication tools.

4. **Discretionary Access Control**:
    - **Granular Permissions**: The Privileged Account Security solution has an intrinsic access control system. Users are shielded from passwords or details not meant for them. Permissions include reading, writing, deleting, or administrating based on access control rules.
    - **Role-Based Access Control**: The Vault's Visual Security offers a unique way for users to monitor the activities performed in their Safes by peers. They can observe real-time interactions, including logins and data retrievals.

5. **Mandatory Access Control**:
    - **Subnet-Based Access Control**: Restrictions based on specific subnets.
    - **Time Limits and Delays**: Access can be restricted or delayed based on specific timings.

6. **Auditing**:
    - **Tamperproof Audit Trail**: Visual Security functionalities notify users of any Vault activities and instantly highlight accessed passwords and files.
    - **Event-Based Alerts**: Automatic notifications for specific events.

7. **File Encryption**:
    - **Hierarchical Encryption Model**: An organized encryption structure.
    - **Every Object Has a Unique Key**: Each password and file within the Vault gets encrypted with its unique key, leveraging an encryption infrastructure invisible to the end user, freeing them from key management issues.

This multi-layered approach ensures the Vault provides the highest level of security for privileged credentials and other sensitive information.

## What is the Latest Version of CyberArk and Its Key Features?

The most recent version of CyberArk as of this data is version 12.1. Below are its notable features:

1. **Privileged Session Manager for SSH**:
   - Allows SSH connections with modern authentication methods, including SAML, combining single multi-factor authentication for multiple targets.

2. **CyberArk Telemetry Tool**:
   - A new tool for on-premises deployments that provides insights regarding the usage and adoption of CyberArk PAS components.

3. **Vault Enhancements**:
   - Improved syslog integration robustness, accommodating high loads and handling slow or interrupted communication with syslog servers.

4. **Password Vault Web Access (PVWA)**:
   - Platform Management now offers better visibility into access workflow policies and their settings for each platform.

5. **REST APIs**:
   - Expanded web services in the Accounts, Safes, and User Management areas, with new APIs such as "Get secret versions," "Link an account," "Delete Safe," "Add member," and "Delete discovered accounts."

6. **Security Enhancements**:
   - Upgraded internal components for improved security, technological advancements in the PVWA Server's OS, and third-party components.

7. **Central Policy Manager**:
   - The installation process now supports incremental hardening, allowing customers more flexibility in managing their configurations.

8. **PSM for SSH Deployment**:
   - PSM for SSH can now be set up on Amazon Linux 2.

9. **On-Demand Privileges Manager**:
   - OPM and OPM-PAM support deployment on various Ubuntu versions (16.04, 18.04, 18.10, 20.04, and 20.10).

10. **Privileged Threat Analytics**:
   - Enhanced server performance, capable of handling 4000 audits per second, thanks to internal component optimizations.

1. **Support for Multi-Factor Authentication (MFA)**:
   - Azure and AWS PSM connectors now accommodate cloud console login using IAM user credentials enforced with MFA.

2. **Application Access Manager - Credential Providers**:
   - The Credential Provider supports Centos 8 and AIX 7.2 TL5.
   - The new Credential Provider for z/OS version offers bug fixes and a revised end-user license agreement.
   - Updated components include Java Provider, C SDK, and Java SDK.

This version of CyberArk introduces a plethora of new features and improvements, ensuring a secure, efficient, and user-friendly privileged access management experience.

## What Do the Master CD and Operator CD Contain? #defcon2

1. **Master CD contains**:
   - Recovery private key
   - Recovery public key
   - Random database key
   - Server key

Purpose : The Master CD keys are reserved for emergencies, such as logging in as Master, recovering the Vault, or re-keying the Vault.  


1. **Operator CD contains**:
   - Recovery public key
   - Random database key
   - Server key

Purpose : The Operator CD keys are required to install and start the vault server.

These CDs are essential for system recovery and operational purposes within certain system architectures.

![[Pasted image 20230828184148.png]]

## What is RCA and how Can You Monitor the Digital Vault with It? #defcon4

**Answer**:

**RCA** stands for **Remote Control Agent**. The Enterprise Remote Control Agent is a software component that facilitates remote control and management of a computer system.

In the context of CyberArk, the RCA, specifically the **CyberArk Vault Remote Control** feature, empowers users to execute various operations on Vault components from a distance, without direct access to the server where the Vault resides. This ensures that privileged operations can be performed securely even when administrators are not physically present at the server location.

**Monitoring the Digital Vault with RCA**:

To manage and monitor the Digital Vault and its associated components (like the DR Vault, ENE, and CVM) from a remote location, you would use the **PARClient utility**. This utility offers a range of commands that facilitate remote operations.

For instance, to manage the Vault, DR Vault, ENE, and CVM remotely, the PARClient utility provides specific commands tailored for each operation. These might include commands to start or stop services, view logs, or even trigger specific administrative actions.

![[Pasted image 20230828184532.png]]

## What is the Purpose of the Administrator account and Master Account?

The **Administrator account** is a critical account typically used for managing and maintaining systems, applications, or platforms. It possesses elevated privileges that allow the user to perform tasks that a regular user cannot, such as installing software, managing user accounts, and altering configuration settings. Given its elevated rights, it's crucial to ensure the security of this account to prevent unauthorized access.

The **Master account**, on the other hand, acts as a safeguard or backup mechanism for the Administrator account. In the event that the Administrator account is locked out, compromised, or suspended, the Master account can be used to restore access. The primary purpose of the Master account is to retrieve or reactivate the Administrator accounts. By doing so, it ensures continuity of operations and access, especially in scenarios where the primary administrative account is unavailable.

In essence:

- **Administrator account**: For day-to-day administrative tasks and system management.
- **Master account**: Primarily for recovery and restoration of the Administrator account when it's inaccessible.  
![[Pasted image 20230828184721.png]]

## What Are the Services of the Digital Vault Server? #defcon1

**Answer**:

The Digital Vault server, as part of CyberArk's Privileged Account Security Solution, offers a range of services to ensure the security, management, and monitoring of privileged accounts. Here are some of the key services:

1. **CyberArk Event Notification Engine (ENE)**: This service manages the communication between the components in the CyberArk suite. It ensures that critical events, such as privileged account access or configuration changes, are properly logged and notifications are sent to relevant stakeholders or systems.
    
2. **CyberArk Logic Container**: A service that contains the business logic of the Vault. It interprets and processes commands, ensuring that operations like retrieval, storage, and management of secrets happen securely and correctly.
    
3. **CyberArk Windows Hardened Firewall**: This is a specialized firewall tailored for the Digital Vault server. It ensures that only authorized traffic can communicate with the Vault, minimizing the potential attack surface.
    
4. **PrivateArk Database**: This is the central repository where all the privileged account information, secrets, and metadata are stored. The data within this database is encrypted, ensuring the confidentiality and integrity of the privileged information.
    
5. **PrivateArk Remote Control Agent (RCA)**: This component allows administrators to manage and control the Vault remotely. Through RCA, admins can perform various operations without having to be physically present at the server location.
    
6. **PrivateArk Server**: This is the main server component of the CyberArk solution. It handles client requests, manages encryption keys, and interacts with the PrivateArk Database to store and retrieve privileged account information.
    

Together, these services ensure that the Digital Vault server provides a robust, secure, and efficient solution for privileged account management.

![[Pasted image 20230828184829.png]]

## What Are the Configuration Files of the Vault Server? #defcon1

**Answer**:

The Vault server, which is part of the CyberArk Privileged Account Security Solution, uses several configuration files to determine how it should operate and interact with other components. Here are some of the key configuration files:

1. **Dbparm**: This file is associated with the settings and configuration of the PrivateArk Database. It dictates how the Vault communicates with the database, including settings for database maintenance, backups, and other related operations.

2. **Paragent**: This configuration file is related to the PrivateArk Remote Control Agent (RCA). The file generally contains settings that dictate how remote control operations are handled. The mentioned port `9022` is commonly associated with RCA's communication. #ports

3. **Passparm**: This file pertains to password management within the Vault. It can contain configurations related to password policies, generation criteria, expiration settings, and other password-related parameters.

4. **Tsparm**: This file deals with the 'safes' within the CyberArk Vault. Safes are logical containers where privileged account details are stored. The `Tsparm` file contains configurations related to the creation, deletion, and management of these safes, including settings for their physical storage directories.

5. **Vault**: This is the primary configuration file for the Vault server. It encompasses a broad range of settings, including general operational parameters, communication settings, logging options, and more.

Each of these configuration files is vital to the Vault's operation, ensuring that the system behaves as intended and adheres to the security and operational policies set by the organization.

## What Does the `license.xml` File Contain?

The `license.xml` file is a crucial configuration file for many software applications, including the CyberArk Vault, which contains the licensing information for the product. Here's what the `license.xml` file typically contains for the CyberArk Vault:

1. **Customer’s Unique ID**: This ID is specific to each customer and helps in identifying the legitimate holder of the software license.

2. **Type of Vault Installed**: This indicates which variant or edition of the Vault is currently installed (e.g., standard, enterprise).

3. **License Version**: Specifies the version of the licensing terms.

4. **License Key**: A unique alphanumeric string that validates and activates the software.

5. **Licensed Components**: Lists the specific components or modules of the software that are licensed for use.

6. **Number of EPV Users**: Specifies how many Endpoint Privilege Manager (EPM) users are permitted to access and work with the CyberArk Vault.

7. **High Availability Clustering**: Indicates whether the high availability feature is enabled, allowing for failover mechanisms and redundancy.

8. **External Directory Connection**: Specifies whether the Vault is allowed to connect to external directories for user and group management.

9. **Disaster Recovery Features**: Indicates if features meant to recover data and configurations after a disaster are enabled.

10. **Remote Monitoring in the Vault**: Specifies if remote monitoring capabilities, essential for centralized monitoring and management, are enabled.

11. **Backup by Third Party Software**: States whether the Vault's data can be backed up using third-party backup solutions.

12. **Permitted Authentication Types**: Lists the methods of authentication (like password, token, biometric, etc.) that the Vault supports and allows.

13. **Recognized Client Types**: Specifies which client applications or systems the Vault will recognize and interact with.

The `license.xml` file is essential for software compliance and ensuring that the CyberArk Vault operates within the stipulated terms and conditions set by CyberArk. Modifying or tampering with this file without proper authorization can lead to software malfunctions and legal repercussions.

![[Pasted image 20230828185122.png]]

## What is the `Dbparm.ini` File, and what Does it Contain? #defcon1

**Answer**:

The `Dbparm.ini` file is a primary initialization file for the CyberArk Vault Server. It governs various parameters essential for the functioning and interaction of the vault with its environment.

Here's a breakdown of the typical contents of the `Dbparm.ini` file:

1. **Server Keys Information**: 
    - **Recovery Private Key**: Essential for recovery scenarios. 
    - **Backup Key**: Used during backup operations.
    - **Recovery Public Key**: Corresponding public key for the recovery private key.

2. **Debug Levels**: Specifies the levels of debugging, which can be useful for troubleshooting or when monitoring specific activities in the Vault.

3. **Timestamps**: Might contain settings related to how timestamps are managed or formatted within the Vault, crucial for tracking activities and changes.

4. **Syslog Server Info**: Details about the syslog server if the Vault is configured to send its logs to an external syslog server for centralized logging and monitoring.

5. **RADIUS Server Info**: If the Vault uses RADIUS for two-factor authentication, the `Dbparm.ini` file will have configurations related to the RADIUS server, such as its address, port, and other necessary parameters.

6. **Non-standard Firewall Addresses**: If the CyberArk Vault is running behind a firewall or if there are specific firewall configurations necessary for its operation, those details might be specified in this file.

7. **Database Settings**: The file might also contain details related to the database used by the Vault, such as connection strings, timeouts, and other relevant parameters.

8. **Other Miscellaneous Settings**: These could include network configurations, settings related to integrations with other CyberArk components, or any other custom settings specific to the Vault's deployment.  
![[Pasted image 20230828185251.png]]  
Proper care should be taken when editing the `Dbparm.ini` file, as incorrect configurations can disrupt the functioning of the CyberArk Vault. Any modifications should be documented, and backups of original configurations should be maintained.

## What is a Safe, and what Does it Contain?

A safe in CyberArk is a logical entity designed to securely store, manage, and organize privileged credentials and sensitive data. It is equivalent to a digital safe deposit box, ensuring that only authorized users can access its contents.

A safe contains the following:

1. **Privileged Account Credentials**: These are the passwords for privileged accounts, such as root on a UNIX server, administrator on a Windows workstation, or a high-level database user. This could be for operating systems, databases, applications, and more.
    
2. **Access Control Lists (ACLs)**: ACLs determine who can access a particular safe and what actions they can perform once they have access. This might include actions like retrieve, list, add, update, or delete credentials.
    
3. **Audit Records**: Every action performed on items within the safe is logged. This audit trail provides a detailed history of who accessed which credentials, when they were accessed, and what operations were performed.
    
4. **Files and Documents**: Beyond just credentials, safes can also store important files or documents, like configuration files, license keys, or any sensitive data that needs protection.
    
5. **Metadata**: Each set of credentials might also have associated metadata, like the type of device or application the credentials are for, the IP address, the owner of the credentials, and more.
    
6. **Retention Policies**: Safes can be configured to retain old passwords for a specified period. This helps in scenarios where one might need to revert to a previous password.
    
7. **Access Workflow Policies**: These define any workflows or additional steps required for a user to access a particular credential. For instance, a manager might need to approve a user's request before they can access a specific password.
    
8. **Notifications**: Safes can be set up to send notifications for various events, such as when a password is accessed or changed, or if a safe reaches a certain threshold of activity.

## Why Should the Vault Server not Be part of a Domain?

**Answer**:

The primary reason the Vault server should not be part of a domain is to enhance its security posture by minimizing potential attack vectors and limiting its exposure to threats. Here are the main reasons:

1. **Isolation**: By keeping the Vault server off the domain, you ensure it is isolated from other systems. This reduces the risk of lateral movement by attackers who might have compromised another system on the domain.
    
2. **Limited Exposure**: If the Vault server is part of the domain, it might be discoverable or accessible using domain credentials or domain-based attacks. Keeping it off the domain ensures it remains hidden from potential attackers.
    
3. **Reduced Attack Surface**: Domain-connected servers are often subject to Group Policies, domain scripts, and other configurations pushed from the domain controllers. Any of these could inadvertently introduce vulnerabilities to the Vault server.
    
4. **Mitigation against Domain-level Compromises**: In the event that the domain itself is compromised (e.g., through techniques like "Golden Ticket" attacks using Mimikatz), a non-domain-joined Vault server remains unaffected.
    
5. **Avoidance of Domain-related Outages**: Keeping the Vault server off the domain ensures that any issues or outages related to domain services (like Active Directory outages) won't impact the Vault's availability.
    
6. **Reduced Complexity**: The less integration and dependencies the Vault has with other systems, the simpler its architecture and the easier it is to secure, manage, and troubleshoot.
    
7. **Compliance and Best Practices**: Many regulatory guidelines and industry best practices recommend or mandate the isolation of highly sensitive systems, especially those that store and manage critical credentials like the CyberArk Vault.

## What is PrivateArk Client?

**Answer**:

PrivateArk Client is a graphical user interface (GUI) application provided by CyberArk to manage and administer the Privileged Account Security (PAS) Solution. It serves as the primary management tool for Vault administrators, allowing them to manage user access, policies, safes, and many other aspects of the system. Here are some of its main features and functionalities:

1. **User Authentication**: Before accessing any vault functions, users must authenticate to the PrivateArk Client. The authentication methods supported include password, certificate-based authentication, and other multi-factor authentication methods.

2. **Safe Management**: Safes are logical containers within the vault where privileged account information, such as passwords, SSH keys, and documents, are stored. Administrators can create, modify, or delete safes using the PrivateArk Client.

3. **User and Group Management**: The client allows administrators to define and manage user and group permissions. This includes setting up individual user roles and access levels, and grouping users to streamline permissions management.

4. **Password Retrieval and Rotation**: Users with the necessary permissions can retrieve passwords for various accounts. Additionally, administrators can force a password change for any account stored in the vault.

5. **Audit and Activity Logs**: PrivateArk Client provides access to audit trails. Administrators can review activities and operations performed within the vault, ensuring compliance and monitoring for any suspicious activities.

6. **Policy Management**: The client enables administrators to define and enforce policies related to password complexity, rotation frequency, session management, and more.

7. **Integration with Other CyberArk Components**: Through the PrivateArk Client, administrators can integrate and manage other components of the PAS Solution, such as Privileged Session Manager, Central Policy Manager, and more.

8. **Backup and Recovery**: Vault administrators can initiate backups and, in case of emergencies, perform recoveries using the client.

9. **DR (Disaster Recovery) Configuration**: The client allows configuration and management of the Disaster Recovery settings, ensuring that there's a proper backup vault ready to take over in case of a primary vault failure.

In essence, the PrivateArk Client is the central hub from which administrators control and oversee the security and operations of the CyberArk PAS environment.

## What is `tsparm.ini`?

The `tsparm.ini` file, located within the `Server\Conf` directory of the CyberArk installation, is a configuration file primarily related to the storage and management of Safes within the CyberArk Privileged Account Security solution.

The Safes within CyberArk are logical entities where privileged account credentials and other sensitive information are stored. To ensure efficient management and optimal performance, the actual databases of these Safes can be distributed across different directories or storage locations.

The `tsparm.ini` file contains:

1. **Directories List**: It specifies the directories or paths where the actual databases of the Safes are stored. This allows the Vault to know where to look when accessing or saving information to a specific Safe.

2. **Storage Management**: It helps distribute the storage of Safes across multiple directories, especially in large deployments where a single directory might become a performance bottleneck.

3. **Backup and Recovery Paths**: It might also contain paths relevant to backup and recovery operations.

By managing and configuring the `tsparm.ini` file, administrators can optimize storage, ensure efficient performance, and manage the distribution of Safes across the enterprise environment. It's crucial to handle this file with care to ensure the consistent operation of the CyberArk solution.

## What Are Default Built-in Users & Groups that Are Created for CyberArk Implementation?

Default built-in users and groups in CyberArk include:

### Users

1. Auditor
2. Administrator
3. Batch
4. Master
5. NotificationEngine
6. PSMApp_WIN
7. PVWAAppUser
8. PVWAGwUser

### Groups

1. Auditors
2. Notification Engines
3. PSMAppUsers
4. PSMLiveSessionTerminators
5. PSMMaster
6. PVWAGWAccounts
7. PVWAMonitor
8. PVWAUsers

These users and groups are fundamental for managing roles, permissions, and functions within the CyberArk environment.

## What is CPM?

**Answer:** CPM stands for Central Policy Manager in the context of CyberArk's Privileged Access Security solution. 

It's responsible for:
1. **Automated Password Management:** CPM can change passwords automatically on various remote machines, following the organization's policies, ensuring that privileged account passwords are regularly rotated.
2. **Password Verification:** It can verify if passwords stored in the vault match those on the target devices.
3. **Reconciliation:** If discrepancies are found, CPM can reconcile or reset passwords to ensure consistency.
4. **Enforcing Organizational Policies:** CPM ensures that passwords adhere to enterprise-wide security policies, improving overall security hygiene.
5. **Scalability:** In larger setups with complex networks, multiple CPMs can be deployed while having all passwords stored in a centralized vault.

The Central Policy Manager plays a critical role in ensuring that privileged credentials are both secure and available, mitigating potential risks associated with static or widely-known passwords.

## What is the Default Port by Which All Components of Servers Will Be Able to Connect to the Vault Server? Can it Be Altered?

- The default port for CyberArk Vault TCP/IP connectivity is 1858.  
- No, the 1858 port cannot be altered directly. If there's a need for alteration, it's advised to consult with CyberArk's original equipment manufacturers (OEMs).

## What Are the Services Related to CPM?

**Answer:** The services related to CPM (Central Policy Manager) are:
1. CyberArk Password Manager
2. CyberArk Central Policy Manager Scanner.  
![[Pasted image 20230828190428.png]]

## What is the Purpose of CyberArk Password Manager Service?

**Answer:** The CyberArk Password Manager service, part of the Central Policy Manager (CPM), is responsible for automatically enforcing enterprise policies related to password management. It generates new random passwords, replaces existing passwords on remote machines, and ensures adherence to organizational password policies.

## What is the Default Username of CPM?

**Answer:** The default username for the Central Policy Manager (CPM) is "Password Manager", which is tasked with handling password management operations

## What is Password Vault Web Access?

**Answer:** Password Vault Web Access (PVWA) is a web-based interface of the CyberArk Privileged Account Security Solution. PVWA provides users and administrators with a single console for requesting, accessing, and managing privileged account credentials throughout the enterprise. It facilitates a centralized location for password management tasks, approval workflows, and audit functionalities.

## What Are the Services Related to PVWA?

**Answer:** The services related to Password Vault Web Access (PVWA) include:
- IIS Admin Service (IIS ADMIN)
- Windows Process Activation Service
- World Wide Web Publishing Service

## What is HTTP & HTTPS Connections and Their Port Numbers?

**Answer:** HTTP (Hypertext Transfer Protocol) is an unsecured protocol used for transferring web content, and its default port number is 80. HTTPS (Hypertext Transfer Protocol Secure) is a secured version of HTTP that uses encryption for data transfer, and its default port number is 443.

## **Question:** What is the Functionality of PSM?

Answer: PSM, or Privileged Session Manager, serves as a protective layer between users and sensitive systems, offering three main functionalities:

1. **Isolate:** PSM safeguards sensitive target machines by isolating end-user environments and desktops, preventing direct access and reducing the risk of cyberattacks.
  
2. **Control:** It provides robust access control mechanisms to ensure that only authorized users can access sensitive systems. This includes enforcing access policies, implementing workflows, and offering privileged single sign-on, all of which create a clear accountability trail.

3. **Monitor:** PSM facilitates continuous oversight of privileged sessions. It records every session, allowing for comprehensive auditing and compliance checks. This recording happens without any footprint on the target machines, ensuring that system performance remains uncompromised.  
![[Pasted image 20230828191112.png]]

![[Pasted image 20230828191119.png]]

## Question: What Are the Log Files Related to PSM?

Answer: The log files associated with PSM (Privileged Session Manager) are primarily:
- **PSMConsole.log**: This captures events and activities related to the PSM Console operations.
- **PSMTrace.log**: This file provides detailed trace logs for troubleshooting and deep analysis of PSM sessions and interactions. 

It's essential to monitor and regularly review these logs to ensure the secure operation of PSM and to troubleshoot any issues that may arise

![[Pasted image 20230828191234.png]]

## Question: What Are the Services Related to PSM?

Answer: The primary service associated with PSM (Privileged Session Manager) is:
- **CyberArk Privileged Session Manager**: This service manages and oversees the initiation, monitoring, and termination of privileged sessions, ensuring that they conform to organizational policies and providing a secure environment for accessing sensitive systems.

![[Pasted image 20230828191327.png]]

## Question: What is the Configuration File for PSM?

Answer: The configuration file for PSM (Privileged Session Manager) is `basic_psm`.

![[Pasted image 20230828191344.png]]

## Question: How Will You Grant Report Permission to a User or Group?

Answer: To grant report permission to a user or group, the user or group should be added to the `PVWAmonitor` group and be assigned the `Auditor` role

## Question: What Are the Default Ports for LDAP?

Answer: 
- For standard LDAP: 389 
- For LDAP over SSL (LDAPS): 636 
- For Global Catalog over SSL (Multiple Domains in a Single Farm): 3269

## Question: How Will You Do Active Directory Integration with CyberArk?

Answer: To integrate Active Directory with CyberArk:

1. **LDAP Bind Account**: Create an LDAP bind account in the Active Directory that has READ ONLY access. This account will be used by CyberArk to communicate with AD.
    - Note down the User Name, Password, and Distinguished Name (DN) of this account.

2. **LDAP Groups**: Create three LDAP groups in Active Directory to control access to the vault:
    - **CyberArk Administrators**: This group will have administrative rights in CyberArk.
    - **CyberArk Auditors**: Members of this group can audit activities in CyberArk.
    - **CyberArk Users**: Regular users who will access CyberArk.

3. **Configuration in CyberArk**:
    - Open the CyberArk admin console.
    - Navigate to the LDAP integration settings.
    - Enter the details of the LDAP bind account (User Name, Password, DN).
    - Specify the LDAP server details.
    - Map the three LDAP groups to their corresponding roles in CyberArk (Administrator, Auditor, User).

4. **Test the Integration**: Add a few users to the LDAP groups created in step 2, and then test to ensure that they can access CyberArk with the appropriate permissions based on their group membership.

5. Monitor and Audit regularly to ensure everything works as expected. 

Remember to follow CyberArk's best practices and always maintain a backup before making any changes to your environment.

![[Pasted image 20230828191612.png]]

![[Pasted image 20230828191618.png]]

![[Pasted image 20230828191626.png]]

## How Will LDAP/S Integrate with CyberArk via 636 Port?

**Answer**: LDAP/S is the secure version of LDAP, where communications between the client and server are encrypted using SSL/TLS. The default port for LDAP/S is 636. To integrate CyberArk with LDAP/S via port 636:

1. **Certificate**: Ensure you have the appropriate SSL certificate installed on the Domain Controller or LDAP server. 
2. **Install Root Certificate**: On the CyberArk Vault servers, install the Root Certificate for the Certificate Authority (CA) that issued the LDAP server's certificate.
3. **Hosts File**: For resolving directory server names, you might need to create or update the hosts file on the Vault servers.
4. **Configure CyberArk**: 
    - Open CyberArk's administrative console.
    - Navigate to the LDAP integration settings.
    - Specify the LDAP/S server details, ensuring to specify port 636.
    - Enter details for the LDAP bind account.
5. **Test the Integration**: Validate the secure connection and ensure that user authentication via LDAP/S is working correctly.

## What is the Purpose of BINDUSER Account?

**Answer**: The BINDUSER account, commonly referred to as the "Bind User," serves as a service account for the Vault to authenticate itself to the Active Directory or any LDAP server. The main purposes of the BINDUSER account are:

1. **Authentication**: The Vault uses the BINDUSER account credentials to authenticate itself to the LDAP server. 
2. **Read Access**: The BINDUSER account is typically granted read-only access to the LDAP directory to fetch user attributes and group memberships.
3. **Establish Session**: Once authenticated, the BINDUSER account helps establish a session between the Vault and the LDAP server, allowing for user authentication and other LDAP-related tasks.
4. **Security**: The BINDUSER account is only meant to have minimal permissions, ensuring that even if the credentials are compromised, malicious users can't make significant changes to the directory.

In essence, the BINDUSER account acts as a bridge between CyberArk and the LDAP directory, facilitating secure and controlled communications.

## What Are the Directories Supported by CyberArk?

Answer: CyberArk supports integration with several directory services, including but not limited to:

1. **Active Directory (AD)**: A directory service developed by Microsoft for Windows domain networks.
2. **Oracle Internet Directory (OID)**: A LDAP directory that uses an Oracle database as a datastore.
3. **Novell eDirectory**: A X.500-compatible directory service software product from NetIQ.
4. **IBM Tivoli Directory Server (TDS)**: IBM's implementation of a lightweight directory access protocol (LDAP) server.

These directory services allow CyberArk to authenticate and authorize users based on their group memberships and other attributes stored within these directories.

## In how Many Ways Can Safes Be Created in CyberArk?

Answer: Safes in CyberArk can be created through several methods:

1. **PrivateArk Client**: A graphical user interface that allows administrators to manage the CyberArk Vault, including creating and managing safes.
2. **PVWA (Password Vault Web Access)**: A web interface that provides a centralized console for managing privileged account passwords and enables the creation of safes.
3. **Pacli script**: The Command-Line Interface for CyberArk that can be used for automation tasks, including creating safes.
4. **RestAPI**: CyberArk's RESTful API which allows developers and administrators to programmatically perform various operations, including creating safes.

## What is Object Level Access Control (OLAC)?

Answer: Object Level Access Control (OLAC) is a security feature that provides granular access control to specific objects within a storage or system. In the context of CyberArk's Privileged Access Security solution, OLAC allows administrators to define and control who can retrieve and use specific passwords and files stored in a Safe, irrespective of the permissions set at the Safe level. This adds an additional layer of security by ensuring that only authorized users have access to specific resources or data, even if they have broader permissions in the encompassing Safe.

## How Will You Assign CPM to the Safes?

Answer: To assign the Central Policy Manager (CPM) to a safe in CyberArk:
1. Open the PVWA.
2. Navigate to the specific safe you want to manage.
3. Access the safe's properties or settings.
4. Under the "Password Management" or a similar section, you'll see an option for "Password Manager" or "Manage passwords with CPM."
5. Checkmark or enable this option.
6. Save or apply the changes.

This will ensure that the CPM is responsible for managing the passwords within that particular safe.

## What is Safe Retention Period?

**Answer**: The safe retention period in CyberArk refers to the duration for which historical versions of objects within a safe are retained. Essentially, it's a setting that determines how long the history of changes made to objects (like passwords) within a safe are kept before being purged.

## How Will You Change the Quota for a Safe?

Answer: To change the quota for a safe in CyberArk:

1. Open the PrivateArk client .  
2. Navigate to the specific safe whose quota you want to adjust.  
3. Access the safe's properties or settings.  
4. Locate the "Quota" section or setting.  
5. Set the desired quota, usually in MB (megabytes).  
6. Save or apply the changes.

Make sure to monitor the space utilization of safes periodically and adjust quotas as necessary to prevent safes from running out of allocated space.

## What Are the Roles and Permissions that You Can Assign at the Safe Level in CyberArk?

Answer: At the safe level in CyberArk, you can assign various roles and permissions, such as:

**Access Roles:**
1. Use accounts
2. Retrieve accounts
3. List accounts

**Account Management Roles:**
1. Add accounts (which includes the ability to update properties)
2. Update account content
3. Update account properties
4. Initiate CPM account management operations
5. Specify the next account content
6. Rename accounts
7. Delete accounts
8. Unlock accounts

**Safe Management Roles:**
1. Manage the safe
2. Manage safe members
3. Backup the safe

**Monitoring Roles:**
1. View the audit log
2. View safe members

**Workflow Roles:**
1. Authorize account requests (can be at multiple levels, such as Level 1, Level 2)
2. Access the safe without confirmation

**Advanced Roles:**
1. Create folders within the safe
2. Delete folders within the safe
3. Move accounts or folders within the safe

These roles allow organizations to granularly control who has access to certain operations within a safe, ensuring the right balance between security and functionality.

## What Are the Default Ports that Need to Be Enabled from the CPM Server to the Target Server?

Answer: For the Central Policy Manager (CPM) in CyberArk to manage passwords on target hosts, certain default ports need to be opened depending on the target system. Here's a list of default ports from CPM to various common target hosts:

1. **CPM to Linux, VMware hosts, and Cisco devices**: Port 22 (SSH)
2. **CPM to Windows Targets**: 
   - Port 135 (RPC)
   - Port 139 (NetBIOS)
   - Port 445 (SMB)
3. **CPM to Oracle Database**: Port 1521-1526 (Range typically used by Oracle Listener)
4. **CPM to MySQL Database**: Port 3306 
5. **CPM to MS SQL Server**: Port 1433 (TCP/IP connection)

These ports allow CPM to communicate with the target servers for operations like password rotation, verification, and reconciliation. Proper firewall configurations are necessary to ensure the security of these communications.

         

## What Are the Default Platforms that CyberArk Supports?

![[Pasted image 20230829221137.png]]

## Why Do We Need to Duplicate Platforms in CyberArk?

Answer: Duplicating platforms in CyberArk serves several purposes:

1. **Customization**: By duplicating an existing platform, administrators can tailor the settings and behavior to meet specific organizational or technical requirements without altering the original platform.
2. **Granularity**: Different systems or applications within an organization might have variations in how they handle credentials. Duplicating platforms allows for fine-tuned control over each distinct setup.
3. **Safety**: It's a best practice not to modify the out-of-the-box platforms directly to avoid potential issues. By duplicating and then customizing, the original remains intact as a fallback.
4. **Ease of Management**: As systems evolve or when managing a diverse environment, having multiple platforms makes it easier to handle unique requirements for each system or application.
5. **Version Control**: Duplicating platforms can also serve as a versioning mechanism, allowing administrators to test changes on a duplicate before applying them to a production platform.

Overall, duplicating platforms provides flexibility, ensures a safer environment, and enhances the management of privileged accounts across various systems.

## What is the Purpose of "user Lock out in minutes" in dbparm.ini?

Answer: The "user lock out in minutes" setting in dbparm.ini specifies the duration for which a user account remains locked out after exceeding the permitted number of failed login attempts. Once this time has elapsed, the account is automatically unlocked, allowing the user to attempt to log in again. This feature enhances security by preventing brute force attacks while also offering a way for users to regain access after a certain period without administrator intervention.

![[Pasted image 20230829221800.png]]

## In how Many Ways Can Accounts Be Onboarded in CyberArk?

Answer: Accounts in CyberArk can be onboarded in various methods:

1. PUU (Password Upload Utility) - A tool provided by CyberArk to bulk upload accounts.
2. Manually - Adding accounts directly via the PrivateArk Client or PVWA.
3. REST API (ReSTAPI) - Automating account onboarding by integrating with other systems or scripts using CyberArk's RESTful API.
4. Auto-Discovery - CyberArk can automatically discover and onboard privileged accounts across the network based on certain rules and configurations.

Choosing the right method depends on the specific requirements and scale of the onboarding process.

## How Will You Onboard Accounts Using PUU in CyberArk?

Answer: To onboard accounts using the Password Upload Utility (PUU) in CyberArk:

1. **Prepare the CSV File**: Create a CSV file with the details of the accounts you want to onboard. This file should follow the format specified by CyberArk, with appropriate headers and details for each account.

2. **Configure the Vault Address**: Edit the `vault.ini` file to specify the address of the vault you are connecting to.

3. **Set Up Credentials**: Use the `createAuthFile.exe` utility to create a credentials file (`user.ini`). This file will contain the encrypted credentials that PUU will use to authenticate to the vault.

4. **Specify CSV File in Configuration**: Edit the `conf.ini` file and specify the name and path of the CSV file you prepared in step 1.

5. **Run PUU**: Execute the command `passwordupload.exe conf.ini` to begin the onboarding process. PUU will read the `conf.ini`, authenticate to the vault using the credentials from `user.ini`, and onboard the accounts from the CSV file.

6. **Monitor and Verify**: After running the utility, you should verify in the CyberArk PVWA or PrivateArk Client that the accounts have been onboarded correctly.  
![[Pasted image 20230829222151.png]]  
![[Pasted image 20230829222156.png]]  
![[Pasted image 20230829222204.png]]  
![[Pasted image 20230829222213.png]]  
![[Pasted image 20230829222223.png]]  
Note: Always take care when handling the CSV file and `user.ini`, as these can contain sensitive information. Ensure you follow your organization's best practices for data handling and security.

## What is the Configuration File of PUU in CyberArk?

Answer: The configuration file for the Password Upload Utility (PUU) in CyberArk is `conf.ini`. This file guides the utility on how to onboard accounts. Inside `conf.ini`, you will typically find:

- `Os`: Specifies the type of operating system, like Windows.
- `VaultFile`: Points to the `vault.ini` file which contains details about the CyberArk Vault address and other vault-specific configurations.
- `CredFile`: Refers to the `user.ini` file which contains encrypted credentials that the PUU uses to authenticate against the CyberArk Vault.
- `PasswordFile`: Indicates the location and name of the `passwords.csv` file, which contains the details of the accounts you wish to onboard.

Always ensure to correctly configure these parameters in `conf.ini` before running the PUU to onboard accounts.  
![[Pasted image 20230829222405.png]]

## What is the Purpose of Default Templates Safes in CyberArk?

Answer: The purpose of default template safes in CyberArk is to provide a standardized set of configurations and permissions that can be applied to newly created safes. These templates ensure consistency across safes, simplify the creation process, and reduce the potential for errors. By using a template, administrators can quickly apply a predefined set of access controls and configurations, without having to manually set each parameter for every new safe. The "SafeTemplate" in CyberArk stores these default values for safes created through the Password Vault Web Access (PVWA). When a new safe is created, it inherits the configurations and permissions set in the template, unless specifically overridden by the administrator.

## What Are the Fields or Values that Need to Be Mentioned in the CSV Template for CyberArk?

Answer: For onboarding accounts to CyberArk using a CSV template, the following fields are commonly required:

- `Password_name`: The unique name for the account.
- `Safe`: The name of the safe where the account will be stored.
- `Folder`: The specific folder within the safe for the account.
- `Password`: The actual password for the account.
- `DeviceType`: The type of device or system the account belongs to (e.g., Windows, Linux, Database).
- `PolicyID`: The ID of the policy that should be applied to the account.
- `Address`: The address or hostname of the system where the account is located.
- `UserName`: The username associated with the account.

## What is the Command for Executing the Password Upload Utility in CyberArk?

Answer: The command to execute the Password Upload Utility in CyberArk is:
```
PasswordUploadUtility.exe conf.ini
```
Note: Ensure that you're in the correct directory where the utility and `conf.ini` file are located, or provide the full path to the files when executing the command.

## How Do You Generate the Credential File for the Password Upload Utility to Communicate with the CyberArk Vault?

Answer: To generate the credential file that allows the Password Upload Utility (PUU) to communicate with the CyberArk Vault, you use the `CreateAuthFile.exe` tool. The command is:
```
CreateAuthFile.exe user.ini
```
Note: The `user.ini` file contains the necessary credentials. After executing the above command, a credential file will be generated, which is then used by the PUU for authentication with the vault. Ensure that `user.ini` has the correct user details and permissions.

## What is the Log File Associated with the Password Upload Utility (PUU)?

Answer: The log file for the Password Upload Utility (PUU) is named "PasswordUploadError.log". This file captures any errors or issues that occur during the operation of the PUU, aiding in troubleshooting and diagnostics.

## What is a Reconciliation Account, and why is it Important?

Answer: A reconciliation account is a privileged account that is granted sufficient permissions to manage and update other accounts on the target system. In the context of CyberArk, if the password of a privileged account becomes unsynchronized between the Vault and the target system, the reconciliation account can be used to reset the password on the target system and synchronize it back to the Vault. This ensures that there is always a mechanism to bring accounts back into synchronization and avoid lockouts or loss of control over critical accounts.

## What Distinguishes a Password Change from Reconciliation?

Answer: 

**Password Change:** 
- The CPM (Central Password Manager) is aware of the current password.
- It can initiate an immediate password alteration, where the CPM updates the password to a newly generated random one.
- Alternatively, one can specify the desired password for the CPM to utilize during its next password update.

**Reconcile:** 
- The CPM does not have knowledge of the current password.
- Reconciliation involves synchronizing the password on the target machine with the password stored in the Vault, ensuring they match.

## What is a Logon account and Its Primary Function?

Answer:  
A logon account is designed to facilitate sessions on devices that don't allow direct user login. When paired with a privileged account, the logon account first logs into the remote device and then elevates its permissions to assume the role of the privileged user.

## What Does Dual Control Password Access Approval Entail?

Answer:  
Dual control is a mechanism set up to ensure that users can only connect to a target device after obtaining authorization or validation from an approved safe owner.

## How Do You Assign Approval Permissions for the Dual Control Process? Answer:

The dual control security procedure involves the following steps:

1. **User Request Creation:** In a system where the Master Policy enforces Dual Control, a user desiring account access must initiate a request. This request encompasses:
    
    - The motive for account access.
    - The frequency of access (once or multiple times).
    - The specific timeframe for the access. Upon creation, a notification about this request gets forwarded to those authorized to approve it.
2. **Authorization by Confirmed Users:** The authorized users receive and review the request details via the notification. Depending on the provided information, they can either confirm or decline the request. The necessary number of confirmations is dictated by the Master Policy.
    
3. **User Gains Access:** Every time an approval or rejection is given by an authorized user, the initial requester is notified. Once the predetermined number of confirmations is achieved, the requester receives a final notification and can then activate the approval, granting them access based on the conditions they specified in the initial request.

## What Does the "access Safe without confirmation" Parameter at the Safe Level Mean?

Answer:  
The "access safe without confirmation" parameter at the safe level allows a user to bypass the usual procedures and perform tasks directly, even in environments where the dual control password access approval is active. In other words, when a user is granted this privilege, they aren't required to seek any approvals or confirmations and can directly access the safe.

## What is the Concept of check-in/check-out Exclusive Access?

Answer:

**Check-in/Check-out Exclusive Access:**  
This feature ensures that only one user at a time has access to a particular privileged account, enhancing security and accountability.

**Key Aspects:**

1. **Exclusive Locking:** When a user checks out an account, it's locked, preventing other users from retrieving it simultaneously. This guarantees that a single user is accessing the privileged account at any given moment.

2. **Accountability and Usage:** After utilizing the password, the user checks it back into the Vault. This process ensures exclusive use of the privileged account, offering clear accountability of who accessed the account and when.

3. **One-Time Password Option:** In addition to the exclusive access, the Master Policy can be configured to permit a one-time password use. Once the user completes their session, the password is required to be checked back into the Vault.

4. **Automatic Password Rotation:** If organizational policy dictates that a password should only be used once, the Master Policy can be set up to automatically change the password value after its use, ensuring it remains locked and unavailable to other users until its value is altered. This automatic process requires the installation of a Central Password Manager (CPM).  
![[Pasted image 20230829223950.png]]  
By default, the check-in/check-out rule is inactive but can be activated to strengthen security measures and ensure full accountability for privileged account access.

## How Do You Release an account when Exclusive Access is Configured?

Answer:

To release an account when exclusive access is configured:

1. Navigate to **Account Details**.
2. Locate and select the **Release Option** or opt for **Edit Account**.
3. Go to the **Advanced** section and choose the option to release the account.

Additionally, the Central Password Manager (CPM) can auto-release the account based on the "minimum validity period" that's configured at the platform level.

## What Does "one-time Password access" Refer To?

Answer:

One-time password access is a security rule designed to ensure that passwords are used just once and then changed. Upon retrieval of an account by a user, a process to change the password is triggered. This change will automatically take place after a predetermined duration.  
![[Pasted image 20230829223956.png]]  

## What is the Objective of the "Allow EPV Transparent Connection Policy"?

Answer:

The "Allow EPV Transparent Connection Policy" aims to facilitate a seamless connection to remote devices for users, bringing forth several advantages:

1. **Ease of Connection:** The policy enables users to swiftly connect to remote devices, known as 'click to connect', without the necessity to be aware of or enter the corresponding password.
    
2. **Enhanced Security:** By not disclosing the password to users, the potential for exposure is minimized.

## What is the Objective of Requiring Users to Specify Reasons for Access and how Can it Be Turned Off?

Answer:

**Purpose of Requiring Reasons for Access:** The policy to have users specify reasons for accessing an account serves as part of the audit trail.

**Disabling the Requirement:** To disable the prompt asking users to provide a reason for their access:

1. Navigate to the platform settings.
2. Add exceptions for the specific platform or user to bypass the reason requirement.

By implementing these steps, the pop-up message asking for a reason will no longer appear for the defined exceptions.

## What is the "audit Retention period" Policy?

Answer:

The "audit retention period" policy is governed by the Master Policy and determines the duration for which Safe activities audits are preserved. By default, these activity audits are retained for a span of 90 days.

## How Will You Monitor the PSM Live Session?

Answer:  
The MONITORING page provides a user-friendly interface to view all privileged session recordings. Authorized users can see this page once the initial recording has been uploaded to the Vault. For a more detailed examination of a specific session, the Recording Details page can be accessed. Additionally, the Account Details page offers access to recordings related to specific passwords.

## How Will You Grant Permission for an Auditor to Monitor Live Sessions?

Answer:  
To grant permissions for an auditor to monitor live sessions, the user should be added to both the "auditors" group and the "psmmaster" group.

## How Will You Grant Permission for an Auditor to Terminate Live Session?

Answer:  
To grant permissions for an Auditor to terminate a live session:
1. Log on to PrivateArk.
2. Navigate to Tools > Administrative Tools.
3. Select "Users and Groups".
4. Choose "PSM Live Session Terminators".
5. Click "Update".
6. Add the desired user to the list.

## How & where is the PSM Record Generated & Stored?

Answer:  
Initially, all the records are stored on the PSM Server at the path `<C:\Program Files (x86)\CyberArk\PSM\Recordings>`. After a specific duration, these records are automatically uploaded to the Vault, where they are stored in the default safe named "PSMRecordings".

## Which User is Responsible for Monitoring the Live Sessions?

Answer:  
The "PSMAdmin connect" user is responsible for monitoring the live sessions for an Auditor.

## Is it Possible to Customize the PSM Recordings?

Answer:  
Yes, it is possible. Custom recording safes can be defined at the platform level. These safes are automatically created by the PSM when it uploads the initial recordings to the Vault.

## How Will You Enable Default Users or Built-in Users when They Are Suspended?

Answer:  
To enable a default or built-in user that has been suspended:
1. Run the cred file from the specified installation path.
2. Update the password for that user in PrivateArk.

## How Will You Logon to the Vault via Master Account?

Answer:  
There are two methods to logon to the vault using the master account:

1. From the Server Administrator or terminal: The Recovery Private Key path should be mentioned in the `DBParm.ini` file.
2. Using the Emergency Station IP: This is applicable when the Emergency Station IP is specified in the `DBParm.ini` file.

## Is it Possible to Logon into PVWA via Master Account?

Answer:  
No, it is not possible. The Master account cannot be impersonated.

## What is Disaster Recovery in CyberArk?

Answer:  
Disaster Recovery (DR) in CyberArk refers to the backup and restoration capabilities to ensure the continuous availability of the system. If the primary CyberArk Vault server fails, the DR Vault server can be brought online to take over its responsibilities. In essence, the DR is a backup server that stands ready to assume operations.

Key features of DR in CyberArk:

1. **Data Replication:** The DR Service replicates external files, which includes Safe files and Safe folders, from the CyberArk Production Vault to the DR Vault. This replication is governed by settings in the Disaster Recovery configuration file, `PADR.ini`.

2. **Metadata Replication:** The service also replicates metadata files based on two mechanisms:
   - Exports (full backup)
   - Binary logs (incremental backups)
   
   This means that after each action in the Vault, a metadata replication to the DR Vault takes place.

3. **Syncing Password Objects:** Password objects, being part of the metadata, are always in sync between the production and DR servers. Any change or addition in password objects on the primary server is immediately replicated to the DR server.

The above mechanisms ensure that in the event of a system failure or other catastrophic event, CyberArk can quickly recover with minimal disruption to its operations.

## How Will You Perform a DR Drill in Your Organization?

Answer:  
Performing a DR (Disaster Recovery) drill is crucial to ensure that the backup systems and processes work correctly. Here are the steps to conduct a DR drill:

1. **Backup:** Before initiating the DR drill, take a complete backup of the current Vault server. Ensure that all data has been replicated to the DR server up to the date of the DR drill.

2. **Planning and Communication:**
   - **Downtime:** Plan and communicate the expected downtime during the DR drill.
   - **Change Freeze:** Ensure no changes or updates are made to the system during the DR drill.
   - **Customer Notification:** Inform customers or internal users about the DR drill activity. Advise them to use the DR PVWA (Password Vault Web Access) during the drill.

3. **Initiate the Drill:** Stop the production Vault server to simulate a failure.

4. **Configuration Check:** Review the `PADR.ini` file and confirm that the "enable failover mode" is set to "yes."

5. **DR Activation:** After a pre-defined number of retries (e.g., 5 attempts), the DR Vault server should automatically become active and operational.

6. **Monitoring:** Keep an eye on the `PADR.log` for any irregularities and to confirm the successful switch-over to the DR server.

7. **Validation:** Ensure that all services are running as expected on the DR server and test access through DR PVWA to validate that everything is functioning correctly.

8. **Revert:** Once the DR drill is complete and validation is successful, you can revert back to the production environment by restarting the production Vault server and ensuring DR is back in standby mode.

9. **Review and Document:** After the DR drill, conduct a review to identify any gaps or issues faced during the drill. Document lessons learned, and make necessary modifications to your DR plan based on your findings.

It's important to remember that the goal of a DR drill is not just to test the technology but also the team's response and coordination during a crisis.

## What Are the Pre-requisites or Prechecks that Will You Do before while Going for a DR Drill?

Answer:
1. **User Authentication:** Ensure that the DR user is enabled and that the password is set and verified.
   
2. **Client/User Communication:** Notify the clients or internal users about the DR drill and inform them of the expected downtime. Ensure they are aware of the change freeze period and its duration.

3. **DR Server Configuration:** Confirm that the DR server is correctly pointed to the primary Vault and all other component servers, with the exception of CPM (Central Password Manager).

4. **Data Integrity Check:** Ensure that all data has been successfully replicated to the DR server and that there is no data discrepancy between the primary and DR servers.

5. **Network Check:** Verify that the DR server can communicate without issues with all related infrastructure components. 

6. **Backup:** Before starting the drill, take a comprehensive backup of the primary Vault server.

7. **System Health Check:** Ensure that both the primary Vault server and the DR server are healthy and that there are no underlying issues that might affect the DR drill.

8. **Documentation:** Have all relevant documentation, such as DR procedures, contact lists, and system configurations, readily available.

9. **Test Access:** Before initiating the DR drill, test access to all systems and applications through the DR environment to ensure smooth operation once the drill begins.

10. **Rollback Plan:** Always have a rollback plan in place. In case the DR drill does not go as expected, you should have a clear and defined method to revert to the primary environment without any data loss or extended downtime.

11. **Team Availability:** Ensure that all key personnel, including system administrators, network engineers, and other essential staff, are available and informed about the DR drill's schedule and their roles.

12. **Review Monitoring and Alerting Tools:** Ensure that all monitoring and alerting tools are correctly configured to notify relevant stakeholders if any issues arise during the DR drill.

Executing these pre-requisites or prechecks ensures a smooth DR drill and minimizes potential disruptions and issues.

## Which User is Responsible for Replicating the Data?

The DR user and Backup User are responsible for replicating the Vault data.

## Which Service is Responsible for Replicating the Data?

The DR Service is responsible for replicating the external files, including Safes files and Safes folders, from the CyberArk Production Vault to the DR Vault. The replication process is governed by the settings found in the Disaster Recovery configuration file (PADR.ini).

## What is the Configuration File of DR & what Does it Contain?

The configuration file for DR in CyberArk is named "PADR.ini". This file contains various settings and parameters related to the disaster recovery process, guiding how data is replicated from the Production Vault to the DR Vault.

![[Pasted image 20230829225838.png]]

## What is the Log File for DR?

The log file for DR in CyberArk is named "PADR.log". This file captures events, errors, and other relevant information related to the disaster recovery process.

![[Pasted image 20230829225848.png]]

## What Configurations to Be Checked in the Config File in DR when Automatic Failover is Enabled?

In the PADR.ini configuration file for DR in CyberArk, ensure that the "EnableFailOver Mode" parameter is set to "Yes" to enable automatic failover.

## What Are the Services that Will Be up & Running when Replication is Initiated?

The "CyberArk Vault Disaster Recovery" service will be up and running when replication is initiated.

## What Are the Services that Will Be up & Running after Failover from Primary to DR?

After failover from primary to DR, all the services related to the vault will be up and running except for the "CyberArk Vault Disaster Recovery" service.

## Why Do We Need to Do Reverse Replication from DR to Primary Vault?

Reverse replication from DR to Primary is necessary to ensure data consistency and to avoid any data loss, especially if any changes or updates were made while the DR was active.

## What Are Reports & Its Types Available in CyberArk?

Reports in CyberArk are categorized into two types:

1. **Operational reports:**
   - Privileged account inventory
   - Applications inventory

2. **Audit and compliance reports:**
   - Privileged accounts compliance status
   - Activity log
   - Entitlement

![[Pasted image 20230829230134.png]]

## How Will You Generate Reports or in how Many Ways Reports Can Be Generated?

Reports in CyberArk can be generated in two ways:

1. Via the PVWA webpage under the reports tab.
2. Through the PrivateArk client.  
![[Pasted image 20230829230208.png]]  
![[Pasted image 20230829230216.png]]  
![[Pasted image 20230829230222.png]]
