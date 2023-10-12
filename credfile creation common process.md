---
aliases:
  - cred file creation process for PVWA and CPM
tags:
  - credfiles
  - timeline
date created: Tuesday, September 19th 2023, 7:48:07 pm
date modified: Thursday, October 5th 2023, 10:49:20 pm
---

## **General Instructions**

1. **Pause Services:** Start the process by stopping the component's services.
2. **Unsuspend User:** If the component's user account is suspended, access the PrivateArk client to bring it back online.
3. **Change Password:** Modify the password in line with the company's security standards in the PrivateArk Client > Administration Tools > Users and Groups > {User} > Trusted Network Areas > Activate User.
4. **Credential File Creation:** On the server where the component is installed, go to the directory of the password file. Run the `createcredfile.exe` using the fitting command:

    - For versions **above 12.1**:  
      `CreateCredFile.exe user.ini Password /Username {username} /Password {password} /AppType {apptype} /EntropyFile /DPAPIMachineProtection`
    
    - For versions **12.1 below(not 12.1)**:  
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
