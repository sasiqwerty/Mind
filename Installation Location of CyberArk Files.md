---
aliases: 
tags: 
date created: Saturday, September 23rd 2023, 8:06:09 am
date modified: Monday, October 2nd 2023, 9:04:55 pm
---

## Locations of CyberArk Components

Before 2014, CyberArk primarily provided privileged account security solutions like the Vault and PrivateArk Client under the "PrivateArk" name. As their offerings expanded, newer applications adopted the "CyberArk" label, indicating a broader range of products.

| Path                                                  | Description                                                       |
|-------------------------------------------------------|-------------------------------------------------------------------|
| `C:\Program Files (x86)\CyberArk\PSM`                 | PSM (Privileged Session Manager)                                  |
| `C:\Program Files (x86)\CyberArk\Password Manager`    | CPM (Central Password Manager)                                    |
| `C:\Program Files (x86)\PrivateArk\Client`            | PrivateArk Client                                                 |
| `C:\Program Files (x86)\PrivateArk\Server`            | Vault                                                             |
| `C:\CyberArk\Password Vault Web Access`               | PVWA Environment: Configuration and environment data.             |
| `C:\inetpub\wwwroot\PasswordVault`                    | PVWA Web Components: Web-related files for IIS-hosted application|
   - **32-bit Locations**:
     - `C:\Program Files (x86)\CyberArk\PSM`: This is the location for the PSM (Privileged Session Manager).
     - `C:\Program Files (x86)\CyberArk\Password Manager`: This location houses the CPM (Central Password Manager).
     - `C:\Program Files (x86)\PrivateArk\Client`: This directory contains the PrivateArk Client.
     - `C:\Program Files (x86)\PrivateArk\Server`: The Vault is situated here.
     
     These locations reside within the "Program Files (x86)" directory, which, as previously mentioned, is reserved for 32-bit applications and only appears on 64-bit Windows systems.
   

## PVWA

 `C:\CyberArk\Password Vault Web Access` - PVWA Environment:

   - Houses PVWA's configuration and environment data.
   - Located outside "Program Files" to avoid potential permission issues in Windows.  

### `C:\inetpub\wwwroot\PasswordVault` - PVWA Web Components:

   - Contains PVWA's web-related files.
   - Sits in the default directory for IIS-hosted web applications, ensuring smooth integration with IIS and streamlined web access.

In short, CyberArk's directory structure for PVWA combines functionality with security and seamless IIS integration.

