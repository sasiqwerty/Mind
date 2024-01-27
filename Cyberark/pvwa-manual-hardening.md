---
aliases: 
tags: 
date created: Sunday, September 17th 2023, 7:11:52 am
date modified: Saturday, January 27th 2024, 7:02:42 pm
---
Certainly, I'll include the instruction to update SSL/TLS settings as the 6th point:

## **IIS Hardening**

1. Disable Default Shares
   - Perform IIS reset after this change.
2. Remove Unneeded Application Pools
   - Keep "DefaultAppPool" and "PasswordVaultWebAccessPool."
   - Perform IIS reset after this change.
3. Disable Web Distributed Authoring and Versioning (WebDAV).
   - Perform IIS reset after this change.
4. Edit applicationhost.config for PVWA
   - Locate and edit the "applicationhost.config" file related to PVWA for MIME map configuration.
   - Perform IIS reset after this change.
5. Unchecking WebDAV Publishing in Server Manager
   - Open Server Manager.
   - Navigate to "Manage" > "Add Roles and Features."
   - Find "Common HTTP Features."
   - Uncheck "WebDAV Publishing."
   - Perform IIS reset after this change.
6. Update SSL/TLS Settings.
   - Perform necessary updates to SSL/TLS settings.
   - Perform IIS reset after this change.

**Registry Edit**
- Open the registry editor and navigate to HKLM > System > CurrentControlSet > Services > LanmanServer > Parameters
- Add "AutoShareServer" with a value of 0.
- Perform IIS reset after this change.
