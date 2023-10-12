---
aliases: 
tags: 
date created: Friday, August 18th 2023, 2:37:15 pm
date modified: Saturday, August 19th 2023, 1:39:19 pm
---
1. Why do we create backups?
2. How to create backups in first place?
3. What are the types of backup?
4. When do we take backup? What is the right time? how to avoid interruptions for the working environment ?
5. Destination IP address ([[Vault]]) is provided to the other components at the time of installation.
6. the vault.ini file contains the vault ip address and the port number 1858
	1. this is present in every component server
7. backup user is used for creating backups
8. The name of the Vault Backup utility is [[PrivateArk Replicator]]. It is installed in the Replicate subfolder of the Server installation folder.
9. the backup user is a member of every safe in the vault by default, this ensures that every safe is backed up at the stipulated time.
	1. the backup user is present in the vault under the users and groups. 
	2. the backup user needs a cred file to authenticate to the vault server constantly and it requires a cred file present in the backup server.
	3. 

![[Pasted image 20230819132140.png]]