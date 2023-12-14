---
aliases: 
tags: 
date created: Monday, August 28th 2023, 1:00:51 pm
date modified: Wednesday, December 13th 2023, 9:53:22 pm
---

## Safes and Safe Members

This topic describes Safes and Safe members, and how authorizations affect access to a Safe or the actions that can be performed to Safes, Safe members, and accounts.

## Safes Overview

Safes enable you to store and organize authorized user accounts according to your organization's requirements. For example, you can create a Safe for each department such as Finance or HR, and store the accounts for that department in the relevant Safe. Or you can create Safes for accounts based on operating systems such as Windows or Unix.

Organizing accounts in different Safes enables you to limit access to accounts. For example, only the administrator of Windows accounts would have access to the Windows accounts Safe, and only the administrator of the Unix accounts would have access to the Unix accounts Safe.

Users who have the relevant permissions can add Safes in the PVWA and modify their properties, as well as manage Safe members and their permissions.

The entire account management process benefits from all the security and tracking features of the Vault.

## Safe Members Overview

Authorized users with the relevant permissions have access to Safes and accounts. Each user is a member of a Safe and is assigned a specific set of permissions. Permissions give you the flexibility to grant different permissions to different users. For example, some users can only view an account, while others can modify an account's properties or perform tasks on accounts and files in a Safe.

## Add a Safe

This topic describes the authorizations a user must have to add a Safe or view the Safes page, and how to add a Safe in the PVWA.

### Add Safe Authorizations

To add a Safe, users must have the following authorization in the Vault:

|Authorization|Description|
|---|---|
|Add Safes|This authorization is given at the user level, as part of the PrivateArk User management.<br><br>It enables the user to perform the following actions:<br><br>- Add Safes<br>    <br>- Rename a Safe|

Users who do not have the Add safes authorization can view the Safes page with one of the following authorizations:

|Authorization|Description|
|---|---|
|Manage safe|Enables the user to view the safes page and manage the properties of existing safes.|
|Manage safe Members|Enables the user to view the safes page and manage safe members’ authorizations.|

### Add a Safe

Safes that are created in the PVWA are based on default properties. For more information about the default Safe properties, see [Default Safe properties](https://docs.cyberark.com/PAS/Latest/en/Content/PASIMP/Safes-default-properties.htm#_Ref364596841).

1. In the PVWA, click Policies > Safes.  
	1. The Safes that appear in the list are either Safes created by your user, or Safes for which you have one of the required permissions.
2. Click Create Safe.
    
    The Add Safe page appears.
    
3. Enter a name for the new Safe.
    
4. (Optional) Enter a description.
    
5. To set different permissions for individual accounts in the Safe, select Enable Object Level Access Control. For more information, see [Use Object Level Access Control in Safes](https://docs.cyberark.com/PAS/Latest/en/Content/PASIMP/Safes-Object-Level-Access-Control.htm#OLE_LINK3).
    
6. Select the account (password) version management for the Safe:
    
    - Save the last <number> account versions – The number of previous password versions that you want to save for each account. These versions are stored in the Safe indefinitely. A new version replaces the oldest version.
        
    - Save account versions from the last <number> days – The number of days that password versions are saved in the Safe.
        
        You can view saved password versions in the Account Details page, in the Versions tab. By default, the last five password versions are stored. For more information, see [Passwords](https://docs.cyberark.com/PAS/Latest/en/Content/PASIMP/Password-Version-Control.htm#_Ref323117966).
        
7. In the Assigned to CPM drop-down list, select the relevant CPM.
    
8. Click Save.
    
    The Safe is created in the Vault, and the Safe Details page appears.
    
    | | |  
    |---|---|  
    ||Reports Safes and PSM Recording Safes are created automatically with the Auto-purge is enabled setting, which means that files in these Safes will automatically be purged after the Object History Retention Period defined in the Safe properties. In addition, these Safes cannot be managed by the CPM.|
    
    The Members tab contains the Safe members and their authorizations in the Safe. By default, all predefined users and groups are hidden. To display them, clear the Hide predefined users and groups check box.
    
    For more information about Safe members and their authorizations, see [Add a Safe member](https://docs.cyberark.com/PAS/Latest/en/Content/PASIMP/Safes-add-a-safe-member-ClassicUI.htm).