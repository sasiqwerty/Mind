---
aliases: 
tags: 
date created: Tuesday, September 26th 2023, 2:11:53 pm
date modified: Monday, January 8th 2024, 12:56:47 pm
---

## LDAPS Integration in CyberArk

The LDAP integration parameters specify information required by the CyberArk Vault to recognize external directories and create User accounts and Groups. A different set of directory configurations define each external directory that the Vault will work with.

After each LDAP directory has been configured in the PVWA, these parameters are stored in the LDAPConf.xml in the VaultInternal Safe. Do not modify the parameters directly in these files.

### Steps on How to Perform LDAP Integration

1. Go to User Provisioning  
2. Click on New domain  
3. Enter the domain name  
4. Do not choose Secure Connection (SSL)  
5. Enter the Bind user name and password  
6. Enter the domain base context

- LDAP : Unsecure Connection (Port 389)  
- LDAPS : SSL-based encryption is a secure connection (Port 636)

### General Integration Parameters - LDAP

These Parameters 

### Directories - LDAP

These parameters define the External Directories that the Vault will recognize and integrate with.

### Hosts - LDAP

These parameters define host servers for External Directories

### Profiles - LDAP

These parameters define profile files for different types of External Directories 

## Dump

### How to Import Domain Certificate

- Get the public domain certificate and the relevant domain controller certificates of the requested domain. 
- On the Vault machine and the IIS machine, select Add/Remove Snap-in from the file menu. 
- Add ‘Certificates’ from the left menu and click Add. 
- Select the ‘Computer Account’ and then ‘Local Computer’. 
- Expand Certificates (Local Computer), then expand Trusted Root Certification Authorities. The Certificates folder appears. 
- Import and Place all domain certificates in the following store for all of the enterprise Vaults. 
- Add the domain name (as appears in the certificate) to the Vault local HOSTS file with every IP Address that is relevant for connection from the Vault. 
- Continue and Connect your domain.
