---
aliases: 
tags: 
date created: Thursday, August 3rd 2023, 3:43:21 pm
date modified: Friday, August 11th 2023, 10:06:57 pm
---

## Root Access via SSH

The root account is the most powerful account on a Linux system, and it has complete access to the system. If a hacker were to gain access to the root account, they could do almost anything they wanted to the system, including installing malware, stealing data, or destroying the system. By preventing root accounts from accessing servers via SSH, it makes it more difficult for hackers to gain access to the root account.

When a user logs in to a server via SSH, their username and IP address are logged. This information can be used to track down hackers who have gained unauthorized access to the system. However, if the root account is allowed to log in via SSH, their username will always be "root", and their IP address will not always be logged. This makes it more difficult to track down hackers who have gained access to the root account.

In some cases, it may be necessary to allow the root account to log in via SSH. For example, if the server is not connected to the internet, then there is no way to log in as a different user and use the `sudo` command. In these cases, it is important to take steps to secure the root account, such as using a strong password and enabling two-factor authentication.

Keeping security threats in mind, root access is not permitted via SSH.

## Linked Accounts

1. Reconcile Account  
2. Logon Account  
We can define/link the linked accounts in two ways  
- At account level  
- At platform level