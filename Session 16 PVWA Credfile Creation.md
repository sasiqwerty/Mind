---
aliases: 
tags: 
date created: Sunday, October 1st 2023, 3:32:28 pm
date modified: Monday, November 20th 2023, 11:47:17 am
---

## **General Instructions** For Creating Cred Files

1. **Pause Services:** Start the process by stopping the component's services.
2. **Unsuspend User:** If the component's user account is suspended, access the PrivateArk client to bring it back online.
3. **Change Password:** Modify the password in line with the company's security standards in the PrivateArk Client > Administration Tools > Users and Groups > {User} > Trusted Network Areas > Activate User.
4. **Credential File Creation:** On the server where the component is installed, go to the directory of the password file. Run the `createcredfile.exe` using the fitting command:

    - For versions **above 12.1**:  
      `CreateCredFile.exe user.ini Password /Username {username} /Password {password} /AppType {apptype} /EntropyFile /DPAPIMachineProtection`
    
    - For versions **12.1 and below**:  
      `CreateCredFile.exe user.ini`

5. **Service Restart:** Reactivate the relevant service for the component and ensure its regular function.

---

## **Specific Component Instructions**

### **CPM (Central Password Manager)**

- **Service to Halt:** Cyberark Password Manager Service.
- **File Directory:** `“<drive>:\Program Files (x86)\CyberArk\Password Manager\Vault”`.
- command (12.1 and Above ) : `CreateCredFile.exe user.ini Password /Username PasswordManager /Password {password} /AppType CPM /EntropyFile /DPAPIMachineProtection`
- `CreateCredFile.exe user.ini`

### **PVWA (Password Vault Web Access)**

- **Service to Halt:** IIS Services.
- **File Directories:** 
  - Password File Location: `C:\CyberArk\Password Vault Web Access\CredFiles`.
  - Credential Creation Tool: `C:\CyberArk\Password Vault Web Access\Env`.
  - command for PVWAAppUser
	  - (12.1 and Above ) : `CreateCredFile.exe appuser.ini Password /Username PVWAAppUser /Password {password} /AppType PVWAApp /EntropyFile /DPAPIMachineProtection`
	  - (12.1 below ) - `CreateCredFile.exe appuser.ini`
  - command for PVWAGWUser 
	  - (12.1 and Above ) : `CreateCredFile.exe gwuser.ini Password /Username PVWAGWUser /Password {password} /AppType PVWAApp /EntropyFile /DPAPIMachineProtection`
	  - (12.1 below ) - `CreateCredFile.exe gwuser.ini` 

**Important Notes for PVWA:**

- It's crucial to run the command for both user files. If one user is suspended, the other is also likely at risk.
- After executing the command in the 'env' directory, the generated credential files will reside there. You must transfer them to the 'credfiles' directory post-process.
---

## PVWA Safes

- During installation, all the required Safes, users, groups and properties are created in the Vault. This environment enables you to begin working with the PVWA immediately after installation .
- The following Safes are created for the PVWA environment.  

| Safe                        | Description                                                     |
|-----------------------------|-----------------------------------------------------------------|
| **PVWA Config**             | Configuration settings for PVWA.                                |
| **PVWA UserPrefs**          | User preference settings for PVWA interface.                    |
| **PVWA Ticketing System**   | Accounts for connecting to ticketing systems with PVWA.         |
| **VaultInternal**           | Accounts for LDAP directories; LDAP integration & auto-detection.|
| **PVWAPrivateUserPrefs**    | Stores user preferences.                                        |
| **Shared Auth_Internal**    | Credentials for communication between CyberArk components (e.g. LCD). |    

- **The following Safes are automatically created during installation.**  

| Safe                  | Description                                                                                     |
|-----------------------|-------------------------------------------------------------------------------------------------|
| **PVWAReports**       | Contains reports; segregated by user folders. Access restrictions apply. Configuration includes:|
|                       | - Object Level Access Control                                                                   |
|                       | - Automatic purge when retention period expires                                                  |
|                       | - Report retention: 30 days                                                                     |
|                       | - Safe activity retention: 90 days                                                              |
| **PWVATaskDefinitions** | Contains reports saved/scheduled by users.                                                     |
| **PVWAPublicData**      | Contains help documents accessed in PVWA.                                                      |          

## PVWA Users

| File          | Description                                                                                                             |
|---------------|-------------------------------------------------------------------------------------------------------------------------|
| **PWVAGWUser**| Gateway user for Vault access. Credentials: `PWVAGWUser.ini`. Member of `PWVAGWAccounts`. Refer to PWVA groups for Safes.|
| **PWVAAppUser**| Used for internal processing. Credentials: `PWVAAppUser.ini`. Only this user type can run PWVA. Member of `PWVAAppUsers` and has access to `PasswordManagerShared` Safe. Authorizations: `Audit Users`, `Add Safes`.|

| Group              | Description                                                                                                                                 |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **PWVAMonitor**    | Monitoring group; can view CPM activities. Added to `PWVAUserPrefs Safe` and `PasswordManager_Info Safe` with various authorizations. Users added manually.|
| **PWVAUsers**      | Users group for PWVA; can modify PWVA preferences. Added to `PWVAUserPrefs Safe` and `PasswordManager_Info Safe` with various authorizations.|
| **PWVAAppUsers**   | Group for PWVAAppUser. Shared with Safes: `CPM/Scanner`, `PasswordManager_Info`, `PasswordManagerShared`, `PWVAConfig`, `PWVAPrivateUserPrefs`, `PWVAPublicData`, `PWVAReports`, `PWVATaskDefinitions`, `PWVATicketingSystem`, `SharedAuth_Internal` with various authorizations. App user is in `PasswordManagerShared Safe`.|
| **PVWAGWAccounts** | Gateway accounts group. All Safes added in PVWA are auto-shared with this group. Shared with Safes: `CPM/Scanner`, `AccountsFeedADAccounts`, `AccountsFeedDiscoveryLogs`, `PasswordManager`, `PasswordManager_Info`, `PasswordManager_Pending`, `PasswordManagershared`, `PWVA`, `PWVAConfig`, `PWVAPublicData`, `PWVAReports`, `PWVATaskDefinitions`, `PWVATicketingSystem`, `PVWAUserPrefs`.|      

### Safes and Their User's Permissions

| Safe                  | User & Authorizations                                                                                               |
|-----------------------|---------------------------------------------------------------------------------------------------------------------|
| **PVWAConfig**        | `PVWAAppUsers`: Retrieve, List passwords. `PVWAGWAccounts` shared.                                                   |
| **PVWAUserPrefs**     | `PVWAMonitor`, `PVWAUsers`: List, Add, Retrieve, Update values & properties. `PVWAGWAccounts` shared.                 |
| **PVWAPrivateUserPrefs** | `PVWAAppUsers`: List, Retrieve, Create, Update files & properties.                                                  |
| **PVWATicketingSystem**  | `PVWAAppUsers`, `PVWAGWAccounts`: Retrieve, List passwords.                                                          |
| **PasswordManager_Info** | `PVWAMonitor`, `PVWAUsers`, `PVWAAppUsers`: Retrieve, List, View Audit, View Safe Members. `PVWAGWAccounts` shared.  |
| **PVWAReports**       | `PVWAAppUsers`: List, Retrieve, Add, Update, Delete, Manage & View Safe members, Create/rename folder.                |
| **PVWATaskDefinitions**  | `PVWAAppUsers`: All authorizations.                                                                                 |
| **PVWAPublicData**    | `Vault Admins`: All authorizations. Installer (default `Administrator`): All. `PVWAAppUsers`: Retrieve, List.        |
| **SharedAuth_Internal** | `PVWAAppUsers`: List, Retrieve, Create, Update, Delete files, View owners, Create/Rename folders, Manage Safe owners.|

**Note**: Specific authorizations for each safe include actions such as List Files, Retrieve Files, View Audit, etc.

## Configuration Files

Important Files :  
![[Pasted image 20231002171059.png]]  

| File                   | Description                                                                |
|------------------------|----------------------------------------------------------------------------|
| **PVConfiguration.xml**| Contains parameters for different PVWA configurations. <br> ** The main config File, the most important file related to PVWA**                      |
| **SafeTemplate.xml**   | Contains parameters for default Safe properties; applied to PVWA-created Safes. |
| **Policies.xml**       | Contains parameters for platforms.                                         |
| **EPMConfiguration.xml**| Contains parameters for integration with EPM.                               |

## Safes List and Their Images

![[Pasted image 20231002165912.png]]  
![[Pasted image 20231002163942.png]]  
![[Pasted image 20231002165629.png]]  
![[Pasted image 20231002165643.png]]  
![[Pasted image 20231002165723.png]]  
![[Pasted image 20231002165749.png]]  
![[Pasted image 20231002165943.png]]  
![[Pasted image 20231002165958.png]]  
![[Pasted image 20231002170021.png]]