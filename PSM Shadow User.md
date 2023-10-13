---
aliases: 
tags: 
date created: Friday, October 13th 2023, 3:31:57 pm
date modified: Friday, October 13th 2023, 3:52:35 pm
---

## Dump

How does PSM shadow user profile works?

How does PSM shadow user profile works? And how is it created? Noticed that there are many shadow user profile in Computer Management - - >User and Groups, but some of the users are not found in [C:\Users](file:///C:/Users) folder

Shadowusers are the local PSM users that are used to actually start and run applications, mostly for RemoteApp apps.

The reason you dont see their profile is because on a default installation of PSM/RDS local profiles are disabled and therefore deleted after a session ends

PSMShadow users are those which represent the person connecting to the target , but from the PSMServer to the target.

So it is the PSMConnect that will take you upto the PSM Component Server and from then to the target server is the PSMShadow user who lives as long as the session is active.

When users initiate a connection (session) to a target machine via PSM, a PSM Shadow user is automatically created on the PSM machine and that's the user that is used to log on to the target machine and perform actions.

The purpose of the Shadow user is to isolate the session. This enables programs launched on the same server by different Vault users to run under different identities without the risk of information leaking between these sessions.

## Operational Aspects of PSM Shadow User Accounts

**Q1: What are PSM Shadow User accounts and how do they work?**  
**A1:**  
A PSM Shadow user is an account created automatically during a PSM (Privileged Session Manager) connection. They serve to sandbox, or isolate, the client session, ensuring that programs initiated by different vault users on the same server run under distinct identities. This prevents information leakage between sessions. These shadow users have no privileges and are created by the SYSTEM user. Their credentials are managed internally by the PSM server, which resets the shadow user's password with each new connection. The PSM server's hardening procedure, detailed in the PIM Suite Installation Guide, restricts the use of these users and limits their permissions.

**Q2: What is their purpose?**  
**A2:**  
Starting from version 6.0, PSM allowed various clients on the server (e.g., Toad, SQL+). To enhance security and scalability, version 7.0 introduced sandboxed client sessions through PSM Shadow users. A unique shadow user account is generated for each Vault user, existing as a local user on the PSM machine. During a PSM connection, the primary connection is made using the PSMConnect user. However, the client software is executed under the shadow user's context, ensuring full session separation. Each user benefits from distinct permissions, files, and registry entries, which protects against interference with other users' sessions.

**Q3: When do these accounts get deleted?**  
**A3:**  
Shadow user accounts and profiles are deleted based on a configurable parameter named `ClearUserProfilesInterval`. This can be accessed in PVWA via:
   1. Administration Tab  
   2. System Configuration - Component Settings - Options  
   3. PIM Suite Configuration - Privileged Session Management - General Settings - Server Settings  
By default, this parameter is set to 30 days. If the associated Vault User is no longer present in the vault, the shadow user account and profile are deleted during this interval.

**Q4: What is the recommended method for cleaning up unused accounts/profiles?**  
**A4:**  
For shadow users tied to existing vault users, it's advisable to retain their accounts. If the vault user is deleted, the associated shadow user will be automatically cleaned up during the next `ClearUserProfilesInterval` cycle. If there's a need to manually delete a shadow user account without removing the vault user:
   1. Navigate to Control Panel -> System -> Advanced system settings.
   2. Under the Advanced tab, within the User Profiles section, click on the Settings button.
   3. Select the desired user name and click the Delete button.

**Q5: Why do RDP sessions not require or use a PSM Shadow User account to connect through PSM?**  
**A5:**  
The PSMRdpClient is unique in that it uses PSMConnect and not a shadow user. Using a shadow user for this purpose would inhibit certain features, like the ability to copy-paste between the client and target machine. There's also no security necessity for using shadow users with RDP sessions, unlike with other connection clients.

**Q6: How does password rotation on PSM Shadow User accounts work?**  
**A6:**  
PSM Shadow User accounts do not have an automatic password rotation mechanism. However, it's worth noting that these accounts are considered low-risk. They are weak users, unable to remotely log into the PSM server. For added security, a new password is generated for each session.

**Additional Notes**:  
Shadow Users are designed with security as a priority. They cannot remotely access the PSM server, and their passwords are regularly reset, minimizing potential risks.  

### Summary

PSM Shadow User accounts are automatically generated during a PSM (Privileged Session Manager) connection to ensure isolated client sessions. This isolation prevents any interference or information leakage between different users' sessions on the same server. The purpose behind introducing PSM Shadow users in version 7.0 was to heighten security and scalability when multiple client software operates on the PSM server. Each shadow user has a unique identity, with its permissions, files, and registry entries distinct from others. They get deleted based on the `ClearUserProfilesInterval` parameter, typically set to 30 days by default. While RDP sessions don't use PSM Shadow Users, these accounts prioritize security, disallowing remote access to the PSM server and frequently resetting their passwords.

## Preparatory Steps for Installing PSM (related to Shadow users)

Before you install PSM (Privileged Session Manager), it's essential to ensure that a specific Windows permission, "Allow Logon Locally", is granted to the "Users" group. This step guarantees that a new group, created during the PSM installation called "PSMShadowUsers", will inherit the necessary permissions. If this isn't done before installation, you can still grant this permission to the "PSMShadowUsers" group directly afterward.

**Details**:
1. **Allow Logon Locally Windows Permission**: 
   - This is a specific permission in Windows that permits a user or group to log on to a device. It's necessary for the PSM system to function correctly.

2. **Users Group**: 
   - A default group in Windows that typically includes all users who will be using the system. By ensuring this group has the 'Allow Logon Locally' permission, you make sure any subsequent groups or users you add (like PSMShadowUsers) will also have this permission.

3. **PSMShadowUsers Group**: 
   - This is a specialized group that gets created when you install PSM. It requires the 'Allow Logon Locally' permission to operate correctly within the PSM environment.

4. **Setting Permissions**: 
   - If the "Users" group already has the required permission before PSM installation, then the "PSMShadowUsers" group will automatically inherit it. If not, you'd have to manually set this permission for the "PSMShadowUsers" group after you've installed PSM. 

In simpler terms, this instruction is a preventative measure to ensure smooth operation of PSM post-installation.