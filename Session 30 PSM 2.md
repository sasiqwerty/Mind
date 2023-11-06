---
aliases: 
tags: 
date created: Saturday, October 28th 2023, 8:02:20 am
date modified: Sunday, November 5th 2023, 10:13:06 pm
---

## PSM Introduction

- **Cyber-Ark Privileged Session Manager** is the only service under PSM.  
- Restarting this service will cause the ongoing connections to close and stop working and it will cause an interruption, this kind of action should be informed prior. Its a very serious problem. This should be done during non business hours. 
- when server reboots are performed, this will cause the service to stop.
- To perform any activity it has to be taken out of VIP/Load balancer before performing a change.

### Active Connections

- The users connected to the target servers can be viewed directly in the target server in the task manager users tab  
- The live connections can also be seen in the monitoring tab in the [[Password Vault Web Access|PVWA]]
- Live sessions safe in the vault contains the details about the live sessions and files are created on the fly.
- **PSM Bypass Activity** : Bypassing the security is not encouraged under normal circumstances, as direct connections are possible.

## PSM Connectors

- PSM connectors enable users to connect to target machines. This is done on a platform-by-platform basis, and affects all the accounts that are associated with the platform.  
- During PSM installation, a series of supported PSM connectors are created. You can use these connectors with the default settings, or you can customize them by changing existing parameters or adding additional parameters manually.  
- In addition, you can develop Custom Universal Connectors or download connectors from the CyberArk Marketplace and then deploy them to your environment, as described in Deploy PSM Connectors.

## Configuration Files

### basic_psm.ini

basic_psm.ini is the main Config file

| Key                          | Value                                           |
|------------------------------|-------------------------------------------------|
| PSMVaultFile                 | "C:\Program Files (x86)\CyberArk\PSM\Vault\Vault.ini" |
| PSMAppCredFile               | "C:\Program Files (x86)\CyberArk\PSM\Vault\psmapp.cred" |
| PSMGWlCredFile               | "C:\Program Files (x86)\CyberArk\PSM\Vault\psmgw.cred" |
| LogsFolder                   | "C:\Program Files (x86)\CyberArk\PSM\Logs" |
| TempFolder                   | "C:\Program Files (x86)\CyberArk\PSM\Temp" |
| RecordingsDirectory          | "C:\Program Files (x86)\CyberArk\PSM\Recordings" |
| PSMServerId                  | "PSMServer" |
| PSMServerAdminId             | "PSMAdmin" |
| ConfigurationSafe            | "PWAConfig" |
| ConfigurationFolder          | Root |
| PVConfigurationFileName      | PVConfiguration.xml |
| PoliciesConfigurationFileName| Policies.xml |

When new PSMs are installed their names are generated and the `PSMServerId` is defined.  
	`PSM_{hostname}`

### vault.ini File for [[Privileged Session Manager|PSM]]

| Key                    | Value                                 | Description |
|------------------------|---------------------------------------|-------------|
| TIMEOUT                | 30                                    | Seconds to wait for a Vault to respond to a request |
| VAULTDN                |                                       | Vault's Distinguished Name (PKI Authentication) |
| PROXYTYPE              | HTTP                                  | Possible values - HTTP, HTTPS, SOCKS4, SOCKS5 |
| PROXYADDRESS           | 192.33.44.55                          | Proxy server IP address (mandatory when using proxy server) |
| PROXYPORT              | 8081                                  | Proxy server IP Port |
| PROXYUSER              | xxx                                   | User for Proxy server if NTLM authentication is required |
| PROXYPASSWORD          | yyy                                   | Password for Proxy server if NTLM authentication is required |
| PROXYAUTHDOMAIN        | NT_DOMAIN_NAME                        | Domain for Proxy server if NTLM authentication is required |
| BEHINDFIREWALL         | NO                                    | Accessing the CyberArk vault via a Firewall. |
| USEONLYHTTP1           | NO                                    | Use only HTTP 1.0 protocol. Valid either with proxy settings Or with BEHINDFIREWALL |
| NUMOFRECORDSPERSEND    | 15                                    | Number of file records that require an acknowledgement from the Vault server |
| NUMOFRECORDSPERCHUNK   | 15                                    | Number of file records to transfer together in a single TCP/IP send/receive operation |
| ENHANCEDSSL            | NO                                    | Enhanced SSL based connection (port 443) is required |
| PREAUTHSECUREDSESSION  | NO                                    | Enable pre authentication secured session |
| TRUSTSSC               | NO                                    | Trust self-sign certificates in pre authentication secured session |
| ALLOWSSCFOR3PARTYAUTH  | NO                                    | Are self-sign certificates allowed for 3rd party authentication (like RADIUS) |
| PROXYCREDENTIALS       |                                       | Instead of specifying proxy user and clear text proxy password, they can be given in the file pointed by this parameter |
| [API]                  |                                       | |
| Addresses              | "https://pvwa.acme.com/pspwdvault/api"| PVWAConfig safe is created during installation during the installation of PVWA |
| ApiKeyPath             | "C:\Program Files (x86)\CyberArk\PSM\Vault\apigw.cred" | |

## PSM Recordings

- Error location : `C:\Program Files(x86)\CyberArk\PSM\Recordings\Errors`  
- Recording Folder : `C:\Program Files (x86)\CyberArk\PSM\Recordings`