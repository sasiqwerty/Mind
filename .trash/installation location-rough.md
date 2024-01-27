---
aliases: 
tags: 
date created: Saturday, September 23rd 2023, 5:56:19 am
date modified: Saturday, September 23rd 2023, 8:04:58 am
---

## Final Draft

Based on the provided data, here's an explanation of the locations concerning their bitness and security:

### Bitness:

   - **32-bit Locations**:
     - `C:\Program Files (x86)\CyberArk\PSM`: This is the location for the PSM (Privileged Session Manager).
     - `C:\Program Files (x86)\CyberArk\Password Manager`: This location houses the CPM (Central Password Manager).
     - `C:\Program Files (x86)\PrivateArk\Client`: This directory contains the PrivateArk Client.
     - `C:\Program Files (x86)\PrivateArk\Server`: The Vault is situated here.
     
     These locations reside within the "Program Files (x86)" directory, which, as previously mentioned, is reserved for 32-bit applications and only appears on 64-bit Windows systems.
   

### PVWA

`C:\CyberArk\Password Vault Web Access` - PVWA Environment:
   - Houses PVWA's configuration and environment data.
   - Located outside "Program Files" to avoid potential permission issues in Windows.  
`C:\inetpub\wwwroot\PasswordVault` - PVWA Web Components:
   - Contains PVWA's web-related files.
   - Sits in the default directory for IIS-hosted web applications, ensuring smooth integration with IIS and streamlined web access.

In short, CyberArk's directory structure for PVWA combines functionality with security and seamless IIS integration.

## Rough Draft

`C:\Program Files (x86)\CyberArk\PSM` - PSM  
`C:\Program Files (x86)\CyberArk\Password Manager` - CPM  
`C:\CyberArk\Password Vault Web Access` - PVWA Environment  
`C:\Program Files (x86)\PrivateArk\Client` - PrivateArk Client  
`C:\Program Files (x86)\PrivateArk\Server` - Vault  
`C:\inetpub\wwwroot\PasswordVault` PVWA Web related stuff


1. **Program Files**: Used for 64-bit applications and is found on both 32-bit and 64-bit Windows, but mainly serves 64-bit apps on the latter.
2. **Program Files (x86)**: Reserved for 32-bit applications and only appears on 64-bit Windows systems.
 
**Installation Location**: The primary folder, `PasswordVault`, is by default located in `Inetpub\wwwroot`, which is the default directory for web applications hosted on IIS (Internet Information Services) on Windows systems.

The `PasswordVault` folder in IIS corresponds to the PVWA's URL access. To prevent permission conflicts, especially due to Windows' tight restrictions in the "Program Files" directory, CyberArk advises against installing there, ensuring PVWA's seamless operation.

## Data Dump

By default, the main folder, PasswordVault, is created under Inetpub\wwwroot. Although the location can be changed during installation, we recommend that the files remain in the default installation location due to potential permission problems. Specifically, we recommend that you don't install the application folder under Program Files.

This folder is used as the physical path of the virtual directory that is created under the selected website.

The following image shows the folder structure of the PasswordVault folder after installation in the default location.

The folder, Password Vault Web Access, is created for the configuration and connection files required by the PVWA to create its working environment. By default, this folder is created under C:\CyberArk. This location can be changed during installation, but the folders should not be copied to a different location after installation. We recommend that you do not install this folder under Program Files.

### Program Files and Their Story

1. **Program Files**:
    - **Purpose**: Meant for 64-bit versions of applications.
    - **Systems where it appears**: It's present on both 32-bit and 64-bit versions of Windows, but its primary role on 64-bit Windows is for 64-bit applications.
2. **Program Files (x86)**:
    - **Purpose**: Specifically for 32-bit versions of applications.
    - **Systems where it appears**: This directory is exclusive to 64-bit versions of Windows to differentiate and separate 32-bit applications from 64-bit ones.

### Companies CyberArk Acquired

1. **Viewfinity (Acquired in 2015)**
   - **Specialization**: Privilege management and application control software.
   - **Description**: Viewfinity's solutions help organizations manage user privileges and control applications on endpoints like desktops and servers. This ensures that only authorized applications run on company systems and that user privileges are elevated only when necessary, reducing the risk of malicious activities.

2. **Conjur Inc. (Acquired in 2017)**
   - **Specialization**: Securing access for software development and IT teams building cloud-based software.
   - **Description**: Conjur offers a solution to manage secrets used by machines (like API keys) and users in modern computing environments. This is especially crucial for DevOps environments where automated processes require access to sensitive keys, passwords, and tokens, which need to be secured.

3. **Vaultive (Assets Acquired in 2018)**
   - **Specialization**: Cloud security.
   - **Description**: Vaultive developed solutions for cloud data encryption to protect data stored in cloud applications, ensuring only authorized users could access and decrypt the data. Its focus was on ensuring that sensitive data remains secure even when stored in third-party cloud environments.

4. **Idaptive (Acquired in 2019)**
   - **Specialization**: Identity management.
   - **Description**: Idaptive delivered Next-Gen Access solutions, ensuring that the right people have the right level of access, to the right resources, in the right context, and that access is assessed continuously — all without adding friction for the user. Their solutions combined Single Sign-On, Multi-Factor Authentication, and Adaptive Authentication.
