---
aliases: 
tags: 
date created: Thursday, September 28th 2023, 3:45:48 pm
date modified: Sunday, November 5th 2023, 8:49:11 pm
---
**Date : 28-09-23 Thursday**

## [[CPM|Central Policy Manager]]

### Prerequisites for CPM Install

#### .NET Framework

1. Developed by Microsoft for Windows applications.
2. Based on the Common Language Runtime (CLR).
3. Supports multiple programming languages.
4. Includes the .NET Class Library for developers.
5. Evolved into .NET Core and .NET 5+.

#### IIS-TLS

IIS (Internet Information Services) uses TLS (Transport Layer Security) to encrypt and secure web communications. Configuration involves setting up server certificates and choosing TLS versions in IIS Manager.

#### System Requirements

| Implementation Size | Processor | RAM | Drives | Other |
|---------------------|-----------|-----|-------|-------|
| Small (<1k passwords) | Quad core | 8GB | 2x 80GB SATA/SAS | RAID, 1Gb Network, DVD ROM |
| Mid-range (1k-20k passwords) | 2x Quad core | 16GB | 2x 80GB SATA/SAS | RAID, 1Gb Network, DVD ROM |
| Large (20k-100k passwords) | 2x Eight core | 32GB | 2x 80GB SAS | RAID, 1Gb Network, DVD ROM |
| Very Large (>100k passwords) | 4x Eight core | 64GB | 2x 80GB SAS | RAID, 1Gb Network, DVD ROM |

**Software Prerequisites:**
- Windows: 2022, 2019, 2016
- .NET Framework: 4.8

### Default Users

Before the **12.2.4 update**, CPM had a default user named "**PasswordManager**." However, after the **12.2.4 update**, CPM introduced additional default users: "**PasswordManager**," "**PluginManagerUser**," and "**ScannerUser**."  

_Important Note_
- All PMTerminal-based plugins must be migrated to Terminal Plugin Controller (TPC) to work properly. 
- Some of the custom plugins might also be affected.

| CPM Version | Default Users |
|-------------|---------------|
| Before 12.2.4 | PasswordManager |
| After 12.2.4  | PasswordManager, PluginManagerUser, ScannerUser |

#### Users and Their Functions

| User            | Permissions                                                                                                                    |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| PasswordManager | - Manage CPM settings, objects (policies, platforms, safes), users & groups<br>- Configure CPM replication, logging & auditing <br> - The local Windows user that runs the CyberArk Password Manager service. |
| Pluginmanager   | - The local Windows user used by the CyberArk Password Manager service to execute plugins. <br> - Manage CyberArk plugins (install, update, uninstall)<br>- Configure CyberArk plugins<br>- View plugin logs                   |
| Scanneruser     | - The local Windows user used by the CyberArk Password Manager service to execute plugins.<br> - Read-only access: CPM safes, policies, platforms, users & groups<br>- Report on CPM object status                            |

### Default Safes

| Safe Name | Description |
|-----------|-------------|
| PasswordManager Safe | Contains `CPM.ini` (main settings) & `ADConfiguration.xml` (auto-detection parameters). |
| `<CPM name>_workspace Safe` | Internal use, not user-accessible. Default: `PasswordManager_workspace`. Size: 5000 MB. |
| `<CPM name>_info Safe` | Stores CPM activity notifications. Readable by PVWAAppUser for display in PVWA. Default: `PasswordManager_info`. |
| `<CPM name>_ADInternal` | Internal use during auto-detection, not user-accessible. Default: `PasswordManager_ADInternal`. |
| PasswordManagerShared Safe | Repository for all CPM platforms. Default size: 500 MB. |  

### Common Safes

Safes that are shared between CPMs in the infrastructure of the company.  
![[Pasted image 20231006005229.png]]  
#todo 

### CPM.ini

CPM's primary config file, located in the `passwordmanager` Safe in the vault. Typically fetched from the safe at runtime and temporarily found at:  
`C:\Users\{Username}\AppData\Local\Temp`.

_The CPM settings mentioned in the CPM.ini can be changed in the following way._  
![[Pasted image 20230928175548.png]]  
![[Pasted image 20230928180250.png]]

![[Pasted image 20230928180912.png]]

### The CPM User

During installation, a unique CPM user is created to access accounts and manage them. This user is created as a CPM user type, and can only interact with the CPM component. By default, it is the only user type in the Vault who can run the CPM.

This user is automatically given access to the CPM Safes with the following authorizations:

#### Common Authorizations

| Authorization Category      | Description                                 |
|-----------------------------|---------------------------------------------|
| Use Password/Use accounts   | Allows users to utilize passwords/accounts  |
| Retrieve Files/Retrieve     | Allows retrieval of account files           |
| List Files/List accounts    | Allows listing of accounts or files         |
| Create Files/Add accounts   | Allows account or file creation             |
| Update Files/Update password value | Allows password value updates for accounts |
| Update File Properties/Update password properties | Allows updates to password properties   |
| Initiate password management operations/Initiate CPM password management operations | Starts password management operations for CPM |
| Rename Files/Rename accounts | Allows renaming of accounts                |

#### Exceptions

| Safe Name                 | Unique Authorizations                          |
|---------------------------|------------------------------------------------|
| PasswordManagerShared    | - View Audit/View audit log <br> - View Owners/View Safe Members <br> - Create/Rename Folder/Create folder <br> - Move Files/Folders/Move accounts/folders |
| PasswordManager          | - Initiate CPM Change with Manual Password/Specify next password value |
| PasswordManager_workspace | - Delete Folder/Delete accounts <br> - Delete Folder/Delete folders |
| PasswordManager_info     | *None identified*                              |

## CPM Role in [[Just in Time Access  - Instructions]]

![[Pasted image 20230928173606.png]]

### Steps:

1. **Requesting Access:** The end user initiates a request for access to the target machine from their own machine.
2. **Adding to Admin Group:** Once the request is made, the end user is added to the local administrators group on the target machine. This step is facilitated by the CyberArk CorePAS (Central Policy Manager or CPM), utilizing a configured account as the reconcile account on the platform.
3. **Notification of Access:** After being added to the admin group, the end user receives a notification that access has been granted.
4. **Actual Access:** The end user can then access the target machine using their own login credentials and tools.
5. **Removal from Admin Group:** After a specified duration (N hours), the end user is automatically removed from the local administrators group on the target machine. This ensures that the elevated access is temporary and aligns with the principle of least privilege. 

### Role of CPM in JIT

The CPM, in this process, plays a critical role in managing the temporary access privileges. Specifically:
- It's responsible for adding the end user to the local administrators group on the target machine (Step 2).
- After a set duration (N hours), the CPM ensures that the end user is removed from this group, revoking the temporary access (Step 5).

In essence, the CPM automates the provisioning and deprovisioning of access rights, ensuring that users only have the permissions they need for the time they need them. This ensures security while also providing flexibility.

## **Cred File Creation Process in CyberArk**

### **General Instructions**

1. **Pause Services:** Start the process by stopping the component's services.
2. **Unsuspend User:** If the component's user account is suspended, access the PrivateArk client to bring it back online.
3. **Change Password:** Modify the password in line with the company's security standards in the PrivateArk Client > Administration Tools > Users and Groups > {User} > Trusted Network Areas > Activate User.
4. **Credential File Creation:** On the server where the component is installed, go to the directory of the password file. Run the `createcredfile.exe` using the fitting command:

    - For versions **above 12.1**:  
      `CreateCredFile.exe user.ini Password /Username {username} /Password {password} /AppType {apptype} /EntropyFile /DPAPIMachineProtection`
    - For versions **12.1 and below**:  
      `CreateCredFile.exe user.ini`

5. **Service Restart:** Reactivate the relevant service for the component and ensure its regular function.

### **Specific Component Instructions**

#### **CPM (Central Password Manager)**

- **Service to Halt:** Cyberark Password Manager Service.
- **File Directory:** `“<drive>:\Program Files (x86)\CyberArk\Password Manager\Vault”`.
- command (12.1 and Above ) : `CreateCredFile.exe user.ini Password /Username PasswordManager /Password {password} /AppType CPM /EntropyFile /DPAPIMachineProtection`
- `CreateCredFile.exe user.ini`

_[[credfile creation common process]] - refer to this file for more details_


| Shortcut      | Description                                                  |
|---------------|--------------------------------------------------------------|
| services.msc  | Displays the Services Management Console.                    |
| gpedit.msc    | Opens the Local Group Policy Editor.                         |
| compmgmt.msc  | Opens the Computer Management Console.                       |
| devmgmt.msc   | Directly opens the Device Manager.                           |
| diskmgmt.msc  | Opens Disk Management.                                       |
| eventvwr.msc  | Opens the Event Viewer.                                      |
| lusrmgr.msc   | Opens the Local Users and Groups Manager.                    |
| secpol.msc    | Opens the Local Security Policy Editor.                      |
| certmgr.msc   | Opens the Certificate Manager.                               |
| perfmon.msc   | Opens the Performance Monitor.                               |
| wmimgmt.msc   | Opens the Windows Management Instrumentation (WMI) Console.  |
| msconfig      | Opens the System Configuration Utility.                      |

