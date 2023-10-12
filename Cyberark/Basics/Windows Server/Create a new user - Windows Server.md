---
aliases: 
tags: 
date created: Tuesday, July 25th 2023, 5:25:38 pm
date modified: Monday, July 31st 2023, 3:21:51 pm
---

## How to Create a New Privileged User in Windows Server?

1. Log in to your Windows Server as an administrator.
2. Open the **Computer Management** console. You can do this by pressing **Windows**+**X** and selecting **Computer Management**.
3. In the **Computer Management** console, expand the **Local Users and Groups** node.
4. Right-click the **Users** folder and select **New User**.
5. In the **New User** dialog box, enter the following information:
    - **Username:** The name of the new user account.
    - **Full name:** The full name of the user.
    - **Password:** The password for the new user account.
    - **Confirm password:** Re-enter the password for the new user account.
    - **Account type:** Select the type of account you want to create. The default is **Standard user**.
6. Click **Create**.

The new user account will be created and added to the **Users** folder. You can now log in to your Windows Server using the new user account.

Here are some additional tips for creating a new user in Windows Server:

- You can create a user account with a password that never expires. This is useful for accounts that need to be accessed by automated processes.
- You can assign the new user account to a group. This will give the user the permissions of the group.
- You can enable or disable the new user account. This is useful if you want to create a user account that is not yet ready to be used.

## [[PowerShell]] Script

*Script to create a new user and add it to a group in the server.*  
#script #important #practice 

```powershell
New-LocalUser -Name "NewUsername" -Description "User's Full Name"
Set-LocalUser -Name "NewUsername" -Password (ConvertTo-SecureString "NewUserPassword" -AsPlainText -Force)
Add-LocalGroupMember -Group "Administrators" -Member "NewUsername"

```
Creating a new account from PowerShell typically involves adding a new user to the system. To achieve this, you can use the `New-LocalUser` cmdlet in Windows PowerShell (works on Windows 8/Windows Server 2012 and newer versions). If you're using PowerShell Core (cross-platform), you can use the `New-LocalUser` cmdlet as well. Here's how to create a new account:

1. Open PowerShell with administrative privileges. To do this, search for "PowerShell," right-click on "Windows PowerShell," and choose "Run as administrator."

2. Use the `New-LocalUser` cmdlet to create the new account. You'll need to provide a username and optionally a full name and description. Here's the basic syntax:

```powershell
New-LocalUser -Name "NewUsername" -Description "User's Full Name"
```

Replace "NewUsername" with the desired username and "User's Full Name" with the actual full name you want to assign to the new account.

3. Set a password for the new user account using the `Set-LocalUser` cmdlet:

```powershell
Set-LocalUser -Name "NewUsername" -Password (ConvertTo-SecureString "NewUserPassword" -AsPlainText -Force)
```

Replace "NewUsername" with the username you used in step 2 and "NewUserPassword" with the desired password for the new account.

4. (Optional) If you want to add the new user to a specific group, such as Administrators, use the `Add-LocalGroupMember` cmdlet:

```powershell
Add-LocalGroupMember -Group "Administrators" -Member "NewUsername"
```

Replace "NewUsername" with the username of the account you created in step 2.

After following these steps, you will have successfully created a new user account in PowerShell. Make sure to remember the username and password for future logins.

Remember to use administrative privileges responsibly and only create accounts if necessary for security reasons or to grant specific access to certain individuals.