---
aliases: 
tags: 
date created: Wednesday, July 26th 2023, 12:42:50 pm
date modified: Sunday, September 17th 2023, 10:55:14 pm
---
A password is a secret combination of characters that is used to verify the identity of a user. It is typically paired with a username to provide authentication. Passwords are used to protect access to computer systems, websites, and other online resources.

Passwords typically tend to have their history saved, they are stored as versions.

CyberArk allows 5 wrong attempts before locking the account and requesting a CyberArk an admin to unsuspend the account.

## Linux Passwords

[Understanding the /etc/passwd File - GeeksforGeeks](https://www.geeksforgeeks.org/understanding-the-etc-passwd-file/)
- Commands to create a new user in Linux  
	adduser {username}  
	passwd {password}

The **/etc/passwd** file is the most important file in Linux operating system. This file stores essential information about the users on the system. This file is owned by the root user and to edit this file we must have root privileges. But try to avoid edit this file. Now let’s see actually how this file look

This file contains one entry per line. That means it stores one user’s information on one line. The user information contains seven fields and each field is separated by the colon ( **:** )symbol.

Each entry in the /etc/passwd file looks like this:  
![[Pasted image 20230726133218.png]]
1. **Username:** This field stores the usernames which are used while login into the system. The length of this field is between 1 and 32 characters.
2. **Password**: This field store the password of the user. The **x** character indicates the password is stored in /etc/shadow file in the encrypted format. We can use the **passwd** command to update this field.
3. **User ID(UID)**: User identifier is the number assigned to each user by the operating system to refer the users. The 0 UID is reserved for the root user. And 1-99 UID are reserved for other predefined accounts. And 100-999 are reserved by the system for administrative and system accounts/groups.
4. **Group ID(GID)**: Group identifier is the number indicating the primary group of users. Most of the time it is the same as the UID.
5. **User ID Info (GECOS)**: This is a comment field. This field contain**s** information like the user phone number, address, or full name of the user. This field is used by the [**finger**](https://www.geeksforgeeks.org/finger-command-in-linux-with-examples/) command to get information about the user.
6. **Home directory**: This field contains the absolute path of the user’s home directory. By default**,** the users are created under the /home directory. If this file is empty**,** then the home directory of that user will be /
7. **Login shell**: This field store the absolute path of the user shell. This shell is started when the user is log in to the system.