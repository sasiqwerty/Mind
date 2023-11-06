---
aliases: 
tags: 
date created: Wednesday, August 9th 2023, 3:35:16 pm
date modified: Monday, November 6th 2023, 12:03:10 am
---

## What is Refresh Period in PVWA ? What it Does and what is it Purpose?

The refresh period in PVWA is the amount of time between automatic updates of the accounts and files lists in the PVWA. The default refresh period is 20 minutes. This means that every 20 minutes, the PVWA will check with the Privileged Session Manager (PSM) to see if there are any new or updated accounts or files. If there are, the PVWA will update its lists accordingly.

The refresh period is important for ensuring that the PVWA always has the most up-to-date information about the accounts and files that users can access. This helps to prevent users from trying to access accounts or files that they no longer have permission to access, and it also helps to ensure that users are aware of any new accounts or files that have been created.

The refresh period can be configured in the PVWA's administration console. To do this, open the administration console and navigate to the **Configuration Options** page. In the **PIM Suite Configuration** section, you will see the **Refresh Period** setting. 

Its the frequency in minutes at which the PVConfiguration.xml, Policies.xml,SafeTemplate.xml, CPM.ini and Policy.ini configuration files in the server are read.  
![[Pasted image 20230809153425.png]]
- It is important to note that the refresh period is only for automatic updates. 
- This is useful if you need to make sure that the PVWA has the most up-to-date information immediately.

## What is Vault Id in CyberArk? Where We Can See and what is it Purpose?

The vault ID and server ID are unique identifiers for a CyberArk vault and server, respectively. They are used to identify the vault and server in various CyberArk products and services, such as the Privileged Access Manager (PAM), the Password Vault Web Application (PVWA), and the CyberArk Management Console (CMC).

The vault ID is a 32-character alphanumeric string that is assigned to each vault when it is created. The server ID is a 16-character alphanumeric string that is assigned to each server when it is added to a vault.

The vault ID and server ID can be found in the following places:

- In the CyberArk vault configuration file, `dbparm.ini`  
![[Pasted image 20230809153906.png]]

The vault ID and server ID are used for a variety of purposes, including:

- Identifying the vault or server in logs and other diagnostic output.
- Filtering and searching for vaults and servers.
- Authenticating to the vault or server.
- Managing the vault or server.
