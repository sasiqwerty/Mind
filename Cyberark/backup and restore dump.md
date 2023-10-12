---
aliases: 
tags: 
date created: Saturday, August 19th 2023, 4:14:57 pm
date modified: Monday, October 9th 2023, 9:41:28 pm
---
#dump

## Backup and Restore

- **Backup Types**: There are two main types of backups: incremental and full. After a full backup is taken, subsequent backups only capture changes made since the last backup.
    
- **Replication**: Data isn't merely copied; it undergoes a process called replication. The term to remember here is "replication."
    
- **Backup Process**: The `PAreplicate` utility is used to perform backups. Daily backups are typically incremental. Larger organizations might have a dedicated backup server, while smaller ones might use the same server for multiple components. The `pareplicate` utility is installed on the backup server.
    
- **Important Note**: The `vault.ini` file is a common configuration file for all components. This is a crucial point to remember.
    
- **Cred File**: The password in the vault and the cred file password should be identical. The purpose of a cred file will be addressed later.
    

## Ports

- **Backup and Restore Ports**: The specific ports used during backup and restore processes need to be identified and documented later.

## PA Restore

- **Restoration Needs**: If certain safes are deleted, the `parestore` utility is used to restore that data.
    
- **User Roles**: The `parestore` utility and the operator user work in tandem, with the `vault.ini` file assisting the operator user in authenticating with the vault.
    
- **Restoration Types**:
    
    - **Full Restore**: This is done when the vault database is empty.
    - **Targeted Restore**: If only specific files or safes need restoration, it's achievable with `parestore`. Safes must be renamed during restoration to avoid conflicts with existing safes. Safes are logical containers, and their names can be changed without affecting the accounts within them.
- **Data Storage**: Data within safes is stored in the installation directory of the vault, whether on the C drive or another drive. The PrivateArk client acts as an interface, decrypting data in safes for users to view and modify.
    
- **Additional Information**:
    
    - **Metadata**: The vault uses MySQL as its database. It's recommended to learn some basics about the MySQL language.
    - **Bin Files**: It's essential to understand bin files and identify the most common types that get corrupted.
    - **Full Restore Process**: The procedure for a full restore needs further elaboration.

## Practical

- **Metadata Replication**: Understand where replication occurs.
    
- **Installation**: Determine the typical installation location for the `pareplicate` utility and the `PAReplicate.exe` within the Replicate Folder.
    
- **Vault Downtime**: If the vault is down, data restoration is impossible.
    
- **Vault's Distinguished Name**: Identify the distinguished name of the vault present in the `vault.ini` file.
    
- **PVWA Communication**: PVWA consistently communicates with both the DR vault and the primary vault.

1. **What is the purpose of a cred file?**
    
    - A cred file (or credentials file) typically stores authentication information required to access a system or service. In the context of backup and restore operations, especially with systems like CyberArk's PrivateArk, the cred file ensures that only authorized processes or users can perform backup or restore actions. It adds an additional layer of security by requiring matching credentials between the vault and the backup or restore utility.
2. **What are bin files, and which types are most prone to corruption?**
    - Bin files, short for binary files, are non-text files that might contain software, data, or other information in a binary format. These files can be any type of data, from images to executable programs. In the context of backup and restore, bin files might represent chunks of data or database segments. As for which types are most prone to corruption, it can vary based on the system, usage patterns, and external factors like hardware reliability. However, frequently accessed or written-to files, or those stored on unreliable hardware, might be more susceptible.

CreateCredFile.exe  
![[Pasted image 20230819165115.png]]  
The TSParm.ini file, in the Server\Conf installation folder, contains the list of directories that can store Safes databases.  
![[Pasted image 20230819173130.png]]