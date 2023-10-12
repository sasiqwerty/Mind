---
aliases: 
tags: 
date created: Monday, August 14th 2023, 7:35:17 am
date modified: Monday, August 14th 2023, 7:38:20 am
---
Certainly! Here's a summary of the information I found about the Password Upload Utility in CyberArk:

1. **Password Upload Utility Overview**:
   - The Password Upload utility works in conjunction with the CyberArk Password Vault to create accounts from a list of passwords and store them in the Vault. This streamlines the Vault implementation process, making it faster and more automated.
   - The utility can upload multiple accounts to the Password Vault by importing passwords and their properties from a pre-prepared file. This process can be initiated from a command line whenever a password upload is needed.
   - The utility can also automatically set up the Vault environment required to store passwords in a Safe and begin working with them. This includes creating new Safes, adding the CPM user as a Safe owner, and sharing the Safe with the Password Vault Web Access.
   - The Password Upload utility can use Template Safes to automatically create Safes with specific properties. If a Safe doesn't exist when uploading passwords, the utility can create a new Safe based on a specified Template Safe or a default one from the utility configuration file.
   - The utility also has features to automatically add a CPM user to Safes and share Safes with the Password Vault Web Access.
   - [More details can be found here](https://docs.cyberark.com/PAS/11.1/en/Content/PASIMP/Password-Upload-Utility.htm).

2. **Password Upload Utility Parameter File**:
   - The utility has various parameters that can be configured, such as the operating system it will run on, the path to the Vault parameter file, the file containing passwords to upload, and many more.
   - These parameters can be set in the `conf.ini` file.
   - [More details on the parameters can be found here](https://docs.cyberark.com/PAS/11.1/en/Content/PASREF/Password%20Upload%20Utility%20Parameter%20File.htm).

3. **End of Support**:
   - As of June 30, 2022, CyberArk has ended support for the Password Upload Utility. This tool was based on older technology and was previously used to upload multiple accounts to the Password Vault.
   - [More details can be found here](https://cyberark-customers.force.com/s/article/Support-for-Password-Upload-Utility-PUU).

4. **Installation and System Requirements**:
   - The Password Upload utility can be installed on various platforms, including Windows 2008 R2 (64-bit), Windows 7 (64-bit), Windows 2003 (32-bit), and Windows XP (32-bit).
   - It requires the PrivateArk Command Line Interface (PACLI), version 4.1 or later. PACLI should be installed in the same folder as the Password Upload utility or in a folder specified in the Path.
   - [More details on system requirements can be found here](https://docs.cyberark.com/PAS/11.7/en/Content/PAS%20SysReq/System%20Requirements%20-%20Password%20Upload.htm).

## PACLI

CyberArk's Command Line Interface (PACLI) is a tool that allows users and applications/scripts to interact with the CyberArk Digital Vault server from a command line environment. Here's a detailed overview:

1. **Purpose and Usage**:
   - PACLI is used to perform quick Vault-level functions.
   - It is recommended to use PACLI only if the task cannot be performed using the REST Web services.
   - Examples of tasks you can perform with PACLI include:
     - Adding or deleting Vault users.
     - Managing Safes.
     - Managing network areas.
     - Managing requests.

2. **PACLI Package Contents**:
   - The PACLI package includes several files such as:
     - `Pacli.exe`
     - `libeay64.dll`
     - `ssleay64.dll`
     - `icudt58l.dat`
     - A folder named `CreateCredFile` which contains `CreateCredFile.exe`, `libeay64.dll`, and `ssleay64.dll`.
   - The `icudt58l.dat` file must be placed in a specific folder (`c:/windows/syswow64`).

3. **How to Use PACLI SDK**:
   - Most PACLI command lines begin with a definition of the Vault in which the activity will take place and the username of the user issuing the command. This ensures that only authorized users can perform the specified task.
   - PACLI commands are not case-sensitive.
   - For instance, a basic script to log in to a Vault would look like:
     ```
     PACLI INIT
     PACLI DEFINEFROMFILE VAULT=NewCo PARMFILE=C:\VAULT.INI
     PACLI LOGON VAULT=NewCo USER=Judy
     PACLI LOGOFF VAULT=NewCo USER=Judy
     PACLI TERM
     ```

4. **End of Support**:
   - It's important to note that as of June 30, 2022, CyberArk has ended support for the Password Upload Utility, which was based on older technology and was previously used to upload multiple accounts to the Password Vault.

5. **System Requirements**:
   - PACLI can be installed on platforms like Windows 2008 R2 (64-bit), Windows 7 (64-bit), Windows 2003 (32-bit), and Windows XP (32-bit).
   - It requires the PrivateArk Command Line Interface (PACLI), version 4.1 or later. PACLI should be installed in the same folder as the Password Upload utility or in a folder specified in the Path.

For more detailed information, you can refer to the [official documentation](https://docs.cyberark.com/PAS/Latest/en/Content/PACLI/Introduction.htm).
