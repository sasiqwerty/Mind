---
aliases: LDAP authentication
tags: concept
date created: Wednesday, July 26th 2023, 3:29:24 pm
date modified: Monday, August 21st 2023, 1:00:00 pm
---
#todo  

## Introduction

### What is LDAP?

**Lightweight Directory Access Protocol ([[Lightweight Directory Access Protocol]])** is an internet protocol works on TCP/IP, used to access information from directories. LDAP protocol is basically used to access an active directory.

![[ldap.svg]]

### Why Do We Need LDAP?

### What Are the Limitations of LDAP?

### What Are the Features that Need to Be Installed before We Use LDAP?

### Who Has Access to LDAP Integration Tab in [[Password Vault Web Access|PVWA]]?

## Vault Authorizations

![[vault-auth-options.svg]]
1. activate [[Users]]
2. Add network areas
3. add safes
4. app update users
5. audit users
6. backup all safes
7. manage server file categories
8. reset user password
9. restore all safes

## Account Access and Suspension

#application  
CyberArk allows 5 wrong attempts before locking the account and requesting a CyberArk an admin to unsuspend the account.

The user gets suspended from the server they are trying to access after repeated wrong password entry, [[Password Vault Web Access]] prompts the user to contact the administrator.

![[Pasted image 20230726181009.png]]

![[Pasted image 20230726172932.png]]

*Authentication failure for user {name} from station {[[IP]]} address (code: -108)*

User Passwords are not changed in vault if they are from LDAP

![[Pasted image 20230821124457.png]]

![[Pasted image 20230821115414.png]]