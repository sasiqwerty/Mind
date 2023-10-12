---
aliases: 
tags: 
date created: Sunday, October 1st 2023, 3:30:11 pm
date modified: Sunday, October 1st 2023, 11:08:45 pm
---

## Hardening - Automatic

The hardening script file performs the following tasks:

- Imports the INF configuration
- Validates server roles
- Sets policy configuration
    - Enables screen saver policies
    - Configures advanced audit policies
    - Configures Remote Desktop Services policies
- Sets EventLog size and retention
- General auditing, registry, and file system configuration 
    - Registry audits
    - Registry permissions
    - FileSystem permissions
    - FileSystem audit
- Creates three local Windows users that run the CPM services
- Disables services
- Disables DEP on files used by the CPM  

## Steps to Remove Permissions

### Inheritance

In the context of file and folder permissions in Windows, inheritance refers to the automatic propagation of permissions from parent objects (like folders) to child objects (like sub-folders and files) within them. When a folder has permission inheritance enabled, any permissions assigned to that folder will also apply to all the contents inside it.  

### Instructions

**Stopping Services**:
1. Open `Services` (from Start menu search).
2. Locate and stop these services: `CPM`, `CPMScanner`, `Scheduled Task`.

**Removing User/Groups from a Folder**:
1. Right-click folder → `Properties` → `Security` → `Advanced`.
2. Either uncheck "Include inheritable permissions..." or click "Disable inheritance".
3. Remove desired user/group.

![[Pasted image 20231001223327.png]]

![[Pasted image 20231001223343.png]]

![[Pasted image 20231001223412.png]]  

**Setting Reader Permissions**:
1. Right-click folder → `Properties` → `Security` → `Edit`.
2. For desired user/group, select: 
   - `Read & Execute`
   - `List folder contents`
   - `Read`

**Setting Full Permissions**:
1. Right-click folder → `Properties` → `Security` → `Edit`.
2. For desired user/group, select:
   - `Full Control`
   - `Read & Execute`
   - `List folder contents`
   - `Read`
   - `Modify`
   - `Write`

## Clipboard Redirection

Clipboard redirection is a feature that allows users to copy and paste data between a remote desktop session and a local desktop session1. By default, Remote Desktop Services allows Clipboard redirection, but it can be disabled by a Group Policy setting.  

1. Go to **Windows > Start button > gpedit.msc**.
2. Open U**set Configuration > Administrative Templates >Windows Components > Remote Desktop Services > Remote Desktop Session Host > Device and Resource Redirection** and set **Do not allow clipboard redirection** to **Disabled**.
3. Restart the machine.

![[Pasted image 20231001155320.png]]

## Access and Folder Permissions

_Points to Consider_  
- Sometimes the `PasswordManagerUser` wont be created in the local server, if that's the case one can create the user and assign the right permissions.
- Create a domain/local user to use in the "PMEngine" (CPM) service

1. **Local Folder Permissions**:
   - Grant permissions for: `CPM user`, `Administrators group`, and `SYSTEM`.
   - Remove all other unnecessary permissions.
2. **Reader Permissions** for:
   - `C:\Python27`
   - `C:\Oracle`
   - `C:\Program Files (x86)\CyberArk`
3. **Full Permissions** for:
   - `C:\Program Files (x86)\CyberArk\PasswordManager\Logs`
   - `C:\Program Files (x86)\CyberArk\PasswordManager\tmp`
   - `C:\Program Files (x86)\CyberArk\PasswordManager\bin`
   - `C:\Program Files (x86)\CyberArk\PasswordManager\Vault`
   - `C:\Program Files (x86)\CyberArk\PasswordManager\Scanner\Log`
4. **Remove "users" permissions**:
   - From all the above folders.
   - From all other unnecessary users/groups.  

## [[Password Vault Web Access|PVWA]] Permissions

- Create a domain/local user to use in the "CyberArk Scheduled Task" service (installed by the PVWA)  
- Remove unnecessary permissions from PVWA folders Remove all except SYSTEM and Administrators group from `[Drive:]\CyberArk`.  
	- Note: Default location is `C:\CyberArk` unless changed during installation. 

**CyberArk Scheduled Task Service Permissions**:
1. For service user: Grant reader permissions to `[Drive]:\CyberArk\PasswordVaultWebAccess\Services`.
2. Grant full permissions to `[Drive]:\CyberArk\PasswordVaultWebAccess\Services\Logs`.
3. Remove "users" and other unnecessary permissions from the mentioned folders.

## Log on as a Service

"Log on as a service" is a Windows privilege that lets specific user accounts, like those for CyberArk's CPM and "CyberArk Scheduled Task" services, start services automatically with the OS. These specialized accounts ensure services like SQL Server or IIS run securely without needing regular user intervention.

Allows CPM and "CyberArk Scheduled Task" service users to "Run as a service".  

**Group policy object**: Computer Configuration/Policies/ Windows Settings/Security Settings/Local Policies/User Rights Assignment.

Add the following users:

- NT SERVICE\ALL SERVICES
- CPM service user
- Scheduled Task service user

Remove any other users from the list.

## Changing the Default Admin Username

The default administrator name in many systems is known to be a high-risk target for hacking attempts. For enhanced security:

- **Group policy object**: 
  - Computer Configuration > Policies > Windows Settings > Security Settings > Local Policies > Security Options
- **Vulnerability**: 
  - The administrator's default name is known as a high target for hacking attempts. It's suggested to rename the administrator's account for security measures.
- **Recommendation**: 
  - It's recommended to change the administrator's name and password and to ensure that permissions transfer to the new account. For an added layer of protection, consider using the renamed administrator as a backup.

## Disabling Protocols That Are Not Needed

Unnecessary protocols can open your system to vulnerabilities. Limit your exposure by deactivating what you don't need:

- **Group policy object**:
  - Computer Configuration > Policies > Windows Settings > Security Settings > Local Policies > Security Options
- **Only the Following Protocols/Services/Clients are required for a CPM PVWA machine**:
  - Client for Microsoft Network
  - File and Printer Sharing for Microsoft Network
  - Internet Protocol Version 6 (TCP/IPv6)
- **Comments**: 
  - Unless specifically required, disable IP v6 too.
  - The following were removed and tested: QoS Packet Scheduler, Link-Layer Topology Discovery Mapper I/O Driver, Link-Layer Topology Discovery Responder

## Disabling Services That Are Not Needed

Reducing unnecessary services enhances system performance and security:

- **Services**: 
  - By default, all these services are disabled. Only enable services that are required.
  - Services to consider: 
    - Routing and Remote Access
    - Smart Card
    - Smart Card Removal Policy
    - SNMP Trap
    - Special Administration Console Helper
    - Windows Error Reporting Service
- **Comments**:
  - Check whether all enabled services are required. For example, Smart Card might be in use but isn't often used by most customers.
  - If you disable the Windows Error Reporting Service, your system will not be able to collect dumps.
