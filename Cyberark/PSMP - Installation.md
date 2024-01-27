---
aliases: 
tags: 
date created: Saturday, November 4th 2023, 2:13:17 pm
date modified: Saturday, November 4th 2023, 6:44:47 pm
---
The standard PSM for SSH installation installs the PSM for SSH  server and registers the server to the Vault.

## - [PSM for SSH pre-installation tasks](https://docs.cyberark.com/PAS/Latest/en/Content/PAS%20INST/Before-Installing-PSMP.htm)

PSM for SSH can be installed on the following operating systems:

- Red Hat Enterprise Linux version 7 including all minor versions
- Red Hat Enterprise Linux version 8 including all minor versions
- Rocky Linux 8 including all minor versions
- CentOS Linux version 7.9
- SUSE Linux Enterprise Server 12.4, 12.5
- PSM for SSH can be installed on Amazon Web Services (AWS), Microsoft Azure, and Google Cloud platforms

### Minimum Server Requirements

| Minimum Server Requirements  | Details  |
|---|---|
|Platform:|Quad core processor (Intel compatible)|
|Disk space:|10 GB free disk space for installation, and additional 40 GB space for temporary workspace|
|Minimum memory:|8 GB|
|Communication:|TCP/IP connection to the Digital Vault Server|

Unix, Linux and Network devices using the following protocols:

- SSH (including SSH-Tunneling)
- Telnet
- PSM for SSH allows access from any SSH client that can connect to an OpenSSH 7.7 server.
- PSM for SSH supports connections to remote machines using IPv4 and IPv6 addresses.

### Storage Requirement on the Digital Vault Server

PSM for SSH stores the session recordings on the Digital Vault server. The estimated storage requirement is approximately 1-5 KB for each minute of a recording session. The recording size is affected by the number of activities that are performed during the session.

For example, 5 GB of storage will be sufficient for recording 10 hours of activities per day retained for 5 years.

PSM for SSH is compatible with the following CyberArk components:

- Digital Vault server
- Password Vault Web Access
- Privileged Session Manager
- CPM  
Each version of PSM for SSH is compatible with all versions of these components that have not reached their [End of Development](https://docs.cyberark.com/Portal/Legal/en/Content/EndOfLifePolicy.htm#PrivilegedAccessSecurity) date at the time the PSM for SSH version was released.

For example, PSM for SSH 11.7 was released in October 2020 and is compatible with version 10.6 and higher of these components, but PSM for SSH 11.5, which was released in June 2020, is compatible with version 10.4 and higher of these components.

### AD Bridge Capabilities

|Platform|Supported Versions|
|---|---|
|AIX|5.3, 6.1, 7.1|
|RHEL|7.8, 8.0 - 8.6|
|Solaris Intel|5.9, 5.10, 5.11|
|Solaris Sparc|5.9, 5.10, 5.11|
|SUSE|10.x, 11.x, 12.x, 13.x|
|HP-UX|11.x|

#### User Permissions before Install

The user who will create the environment for PSM for SSH in the Vault during the installation process must have the following permissions in the Vault:

- Add Safes
- Audit Users
- Add/Update Users
- Manage Server File Categories

This user must be an owner of the PVWAConfig Safe with the following permissions:

- List accounts
- Retrieve accounts
- View Owners
- Manage Safe Owners

### Pre-installation Steps

#### Verify Signature

The RPM installation packages for Red Hat operating system are digitally signed, to protect them from alteration after publication. To verify the digital signature of an RPM package, do the following:

1. Import the RPM-GPG-KEY-CyberArk public key that is provided with the installation package, by running the following command:  
   ` rpm --import RPM-GPG-KEY-CyberArk`
2. Verify the signature of the RPM package, by running the following command:  
    `rpm -K -v <package_name.rpm>`  

Configure LDAP integration so that users and groups will be provisioned in the Vault automatically. For more information about integrating PSM for SSH with LDAP, refer to [Integrate PSM for SSH with LDAP authentication](https://docs.cyberark.com/PAS/Latest/en/Content/PAS%20INST/Following-Installation-of-PSMP.htm#_Ref407814956).

#### Prepare the Installation Environment

1. On the PSM for SSH machine, create a new directory for the installation files. This directory is where the installation files will be located, for example `/opt/CARKpsmp`.
2. From the PSM for SSH installation package, copy the Privileged Session Manager for SSH installation package to the new directory. Make sure you copy the folder and all its contents, including its subfolders.

#### Configure the vault.ini File

- Open the vault.ini file and specify the parameters of the Vault that will be accessed by PSM for SSH.
	- `vi vault.ini` `Address=1.1.1.102`
- For high availability implementations and DR, you can specify more than one Vault IP address, separated by commas, as shown in the following example
	- `Address=1.1.1.102,1.1.1.232`
	- The first Vault IP address that is specified is used when creating the PSM for SSH environment during installation.
	- When PSM for SSH is running, if it cannot access the first Vault IP address, it automatically tries to access the next Vault IP address transparently, and no human intervention is required.

#### Create the Credentials File for Installation

- If you need to add execute permission for the CreateCredFile file, first run the following command
	- `chmod 755 CreateCreFile`
- Then, run CreateCredFile to create a credentials file for the user that will create the Vault environment during installation. This file must be called user.cred
	- `./CreateCredFile user.cred`

#### **InstallCyberArkSSHD** Parameter

When you install PSM for SSH, you configure how to handle the installation of the SSHD service. You can select from one of the following options: (integrated, yes and no)

#### Disable NSCD

On all Linux-based operating systems, NSCD is a daemon that provides a cache for the most common name service requests. Disable it to prevent unexpected behavior.  
`systemctl stop nscd.service nscd.socket` and `systemctl disable nscd.service nscd.socket`

## - [PSM for SSH installation](https://docs.cyberark.com/PAS/Latest/en/Content/PAS%20INST/Installing-the-PSMP.htm)

## - [PSM for SSH post-installation tasks](https://docs.cyberark.com/PAS/Latest/en/Content/PAS%20INST/Following-Installation-of-PSMP.htm)

## Later

[PSM for SSH Administration | CyberArk Docs](https://docs.cyberark.com/PAS/Latest/en/Content/PASIMP/Administrating-the-PSMP.htm)  
- proxymng user for psmp ( for every psmp)
- what are the services in PSMP?
- `useradd {username}`
- [Linux file permissions explained | Enable Sysadmin (redhat.com)](https://www.redhat.com/sysadmin/linux-file-permissions-explained)
- psmpparms - main config file for PSMP
- The installation input file for Privileged Session Manager for SSH is called psmpparms. It specifies the parameters that determine how and wherePrivileged Session Manager for SSH is installed. This file is included in the installation package as psmpparms.sample, and must be moved to the /var/tmp directory and renamed to psmpparms before starting installation.
- [Privileged Session Manager for SSH installation file | CyberArk Docs](https://docs.cyberark.com/PAS/12.6/en/Content/PASREF/PSMP%20Installation%20File.htm)
- var tmp in linux - what is the function ?
- install the infra package first, then the main package
	- during the installation, the safes, users and groups are created
	- locally in the server, services are created.
	- PSM SSH Proxy and PSMP ADBridge are the services created after the PSMP is created
- `service psmpsrv status` to check the status of running services
	- `service psmpsrv start` and `service psmpsrv stop`
	- `cat /var/tmp/psmp_install.log` this is used to check the log
	- hardening is part of the installation. 