---
aliases: 
tags: 
date created: Sunday, October 1st 2023, 3:30:48 pm
date modified: Sunday, November 5th 2023, 10:56:45 pm
---

## How the PVWA URL Will Form?

- We provided an ID during installation.
	- ![[Pasted image 20231005222917.png]]
- This ID refers to the load balancer farm.
- Each PVWA can be accessed via its URL or IP address.
- For multiple PVWAs, this approach helps identify operational ones.
- The load balancer lists URLs of all PVWAs.
- The shared IP is termed the virtual IP or load balancer farm id.
- Using the FQDN, we can determine the IP and ping the server.
- Every server has a unique IP for access.

**we can access the PVWA using the following values**
1. PVWA FQDN
2. IP address
3. Load balancer farm id  
4. server name  
***Note** : we will not share the individual PVWA URLs to the end user*

[[ns-lookup]] - `nslookup` `nslookup` is a network administration command-line tool available in many computer operating systems for querying the Domain Name System (DNS) to obtain domain name or IP address mapping or for any other specific DNS record.

![[Pasted image 20231005223413.png]]  
when `nslookup` is used with the load balancer id we get all the ip addresses that the load balancer is handling.

### Problem Identification

- Ping all PVWA IP addresses or try accessing their URLs to identify any non-operational ones.
- Note down any PVWA that's down.
- Examine the logs to diagnose issues.
- Use each PVWA's URL to confirm its functionality.
- If there's an issue at the load balancer, it needs checking.
- A non-functional PVWA could result from a downed vault.
- If the vault operates but a PVWA doesn't, test each PVWA separately.

### PVWA Upgrade Activity

**Guide to Upgrading Multiple PVWAs**

**Precautions**:
- Monitor CyberArk Security bulletins for updates.
- Review security updates to determine necessary component upgrades to mitigate vulnerabilities.

**Common Steps for All Components**:
1. Install PVWAs closer to the user's location.
2. Seek approval from the change review board or client if there isn't one.
3. Remove the server set for upgrade from the Virtual IP or farm.
4. Strategically plan the upgrade waves.

| Component | Old Version | New Version | Region | Change No | Wave No | Execution Date | Status of the Upgrade   |
|-----------|---------|-------------|--------|-----------|---------|----------------|-------------------------|
| PVWA1     | 12.2.4  | 12.2.12     | HKG    |           | Wave 1  | 20-Sep         | Complete / Report Error |
| PVWA2     | 12.2.4  | 12.2.12     | HKG    |           | Wave 2  | 21-Sep         | Complete / Report Error |
| PVWA3     | 12.2.4  | 12.2.12     | LDN    |           | Wave 2  | 21-Sep         | Complete / Report Error |
| PVWA4     | 12.2.4  | 12.2.12     | LDN    |           | Wave 3  | 22-Sep         | Complete / Report Error |
| PVWA5     | 12.2.4  | 12.2.12     | US     |           | Wave 3  | 22-Sep         | Complete / Report Error |
| PVWA6     | 12.2.4  | 12.2.12     | US     |           | Wave 1  | 20-Sep         | Complete / Report Error |

## V9 and V10 Interface for PVWA

- v9 is the older interface, its for the OG users  
- v10 is the newer interface

***Steps to activate v9 interface***
1. Go to Administration in PVWA
2. Go to options
3. Go to general
4. Use v10logonPage : set it to No

This will revert back to the old v9 interface

### Load Balancer Overview

End users access the system through the load balancer, identified as the VIP (Virtual IP) or load balancer farm ID. The load balancer then routes the users to a PVWA, using a round robin method to evenly distribute the user load.

### Key Points

- Distinguishing which PVWA is being used during a connection is challenging, unlike PSM load balancing where it's clearer.
- For PSM, the specific PSM in use must be defined at the platform level. This step isn't necessary for PVWA.

## PVWA Internal User Suspension and Unsuspension

### How to Unsuspend PVWA Internal Users

1. **Understanding the Issue**:
   - During the PVWA installation, safes and PVWA internal users are created and added to the vault.
   - The vault's IP and port number are available in the `vault.ini` file.
   - Credentials for internal users are stored in the vault, while the respective PVWA server holds credential files for `PVWAAppUser` and `PVWAGWUser`.

2. **Role of Credential Files**:
   - All transactions involve the credential file. A matching cred file indicates a valid transaction, while a mismatch results in transaction denial.
   - `PVWAGWUser` manages external logins (e.g., Administrator, LDAP users).
   - `PVWAAppUser` handles internal communications with the vault and other components.

3. **Suspension**:
   - After 5 incorrect login attempts, the user gets suspended. This suspension is evident in the server central administration console and the specific component's logs.
   - On the PVWA page, the connectivity status will display as "disconnected". (Note: If there's only one PVWA in the infrastructure and it's down, this status won't be visible on the PVWA).

4. **Unsuspending the User**:
   - Access the CyberArk Vault Admin Console.
   - Navigate to the user directory and find the suspended user (e.g., `PVWAAppUser` or `PVWAGWUser`).
   - Right-click on the user and select "Unsuspend".
   - Verify that the user status changes to active and ensure the PVWA's connectivity status returns to "connected" (if possible).
5. **Additional Steps**:
   - Consider reviewing security protocols to prevent frequent suspensions.
   - Monitor logs to understand the cause of repeated incorrect login attempts.

By following these steps, you can unsuspend and restore PVWA internal users to their normal operational state.

### Steps to Create the CRED File

We have to first check which user is suspended, and then to note the server and its detail login and start the process 

We have to go the component that is not working and its server and stop its services  
	- the IIS services are stopped ( if its a different component, stop its respective services )
- Go to the vault and update the password
- Go to the component server and update the cred file with the password that was updated in the vault, ensure that there is no mistake.
- Its advised to update the password for both the users (PVWAGWUser and PVWAGWUser) and create the cred file.

## Entropy Files

for security entropy files are created, before 12.0 this didn't exist, it was introduced in the version 12.1  
1. appuser.ini.entropy  
2. gatewayuser.ini.entropy