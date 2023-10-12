---
aliases: 
tags: 
date created: Thursday, July 27th 2023, 5:29:24 pm
date modified: Saturday, July 29th 2023, 1:39:28 pm
---

- What is the function of the in terms of storing and accessing users and accounts ? [[Active Directory]] #learn
- What is the function of a [[Domain Controller]] #learn ?

## Points to Understand

- [[Target Server]] is the place where most of the companies main activities are performed. These servers need to be secure and provided with secure access to the end user and that's where CyberArk comes in.
- [[Organizational Unit]]s are also called [[Groups]] in windows servers.

we are talking about a target server

we need an account to access the critical account, there are different reasons to access the server and it can have many accounts and they need admin rights and they are called privileged accounts

creating a privileged account in the target server  
when a new account is created its not privileged account  
it has to be given the privileged access and then it becomes a privileged account  
once that done the account needs to be onboarded  
when that happens we select the platform and the safe  
the [[IP]] address of the account should be known beforehand

to secure the account we onboard  
the target server is not part of CyberArk, hence the target server has to be secured by onboarding  
slate and pencil? wtf lol  
that account was an outside account that was from an active directory LDAP integration was done  
once the user is added to the safe the user gains access to list of accounts present in the safe  
the vault admin is responsible for giving access to the end user.  
as ajith is an external user he cannot access to other account as his account is LDAP integrated he can access the pvwa page

## Steps to Give Access to the End User

- the vault admin should login and create an account in the target server.
- once the account is created in the server, it has to be onboarded.
    - while onboarding its important to note down the name of the server [[IP]] and to what safe was the account added.
    - when the end user account is added to that safe the user is able to access the accounts in that target server.





#website  
[How to locate privileged accounts in Active Directory | TechTarget](https://www.techtarget.com/searchwindowsserver/tip/How-to-locate-privileged-accounts-in-Active-Directory)
