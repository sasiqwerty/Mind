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
