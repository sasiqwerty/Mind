---
tags: Interface
aliases: Change, Verify, Edit
date created: Saturday, July 29th 2023, 12:18:20 pm
date modified: Saturday, July 29th 2023, 5:05:25 pm
---
These are some settings that show up in the Account details section of [[Password Vault Web Access]] page.

## Account Details > Change

![[Pasted image 20230729144718.png]]  
*This is for changing passwords, the password gets changed in the [[Target Server|target server]] and [[Vault|vault]]*.

### Change the Password Immediately by the [[CPM|CPM]]

- The password is marked immediate change the [[CPM|CPM]] will try to login and if its successful the password is changed according to the password policy, this will be updated in the Activities tab in the Account Details page.
- The passwords are stored in the versions tab up to maximum of 5 versions of the passwords and this can be changed at the safe level to a number of your choice.

### Specify the Password for the next [[CPM|CPM]] Change

- This tab contains the rules that the new password is supposed to follow, the user has to manually enter the password.
- This option also has the ability to update the password immediately.  
![[Pasted image 20230729144617.png]]  
Go here for more information on password change policy - [[Password Change Policy|Change Passwords]]

### Change the Password only in the [[Vault|vault]]

- The password is only updated in the vault.
	- for any reason if the password was updated on the [[Target Server]] and the activity was considered to be legal, the password can manually updated in the [[Vault|vault]] to ensure connectivity.

## Account Details > Verify
- If the passwords at the [[Target Server|target server]] account and the [[Vault|vault]] are not synchronized, we first verify it.
- 


## Account Details > Edit