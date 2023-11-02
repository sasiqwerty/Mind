---
aliases: 
tags: 
date created: Monday, October 30th 2023, 9:24:59 am
date modified: Wednesday, November 1st 2023, 3:14:14 pm
---
s

## Introduction

- The PSM is installed on a Windows system as an automatic system service called CyberArk Privileged Session Manager.  
- It can be stopped and started through the standard Windows service management tools.  
- **PSM activity logs are stored in the Log subfolder of the PSM installation folder**. These log files can be uploaded to the Vault for long term storage. 
- The PSM install log is located at `C:\Temp\PSM\PSMInstall.log`. This log file monitors the installation process and ensures that PSM was installed successfully. 
- You can check the `PSMConsole` and `PSMTrace` logs to find out why the PSM Service is stopping. 
- The maximum size of the log file is specified in the PSM configuration.

## PSM Logging Overview

- **Location**: Log files are stored in the `Log` subfolder of the PSM installation.
- **Upload**: Logs can be transferred to the Vault for extended storage.
- **Max Size**: Determined by the PSM configuration.

### Log Handling

| Aspect                 | Details                                                                                             |
|------------------------|-----------------------------------------------------------------------------------------------------|
| Event Viewer Errors    | Some PSM-specific errors appear only in the event viewer.                                           |
| Log Rotation           | When logs attain the size defined in `LogRotationSize`, they move to the `\old` subfolder. A new log is then initiated. |

### Recording in Event Viewer

- **Standard Monitoring**: PSM errors are recorded in the machine's Event Log and specific log files.
- **Identification**: Messages in the Event Log carry the prefix **CyberArk PSM** to denote PSM-related activities.

| Log                                       | Description                                                                                                                                                                           |
|-------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `PSMConsole.log`                          | Contains informational messages and errors related to PSM function. Intended for system administrators monitoring PSM status.                                                           |
| `<SessionID>.Recorder.log`                | Contains errors and trace messages for the PSM Recorder. Useful for troubleshooting. Messages depend on the Recorder's debug settings in the PSM configuration.                          |
| `<SessionID>.connection component>.log`   | Contains errors and trace messages related to the connection component. Useful for troubleshooting. Messages depend on the Connection Client's debug settings in the PSM configuration. |
| `PSMConnectorsDeployment.log`             | Contains errors and trace messages about the shared universal connector deployment on multiple PSM servers. Useful for troubleshooting.                                                |
| `PSM Server log files`                    | These logs are in the `PSM\Logs` directory and are subsequently moved to the `PSM\Logs\old` subdirectory.                                                                              |
| `PSM Recorder and Connection client`      | These logs are in the `PSM\Logs\Components` directory and later shifted to the `PSM\Logs\Components\old` subdirectory.                                                                |

## Enable Debugging

- We have to set the debug level from the [[Password Vault Web Access|PVWA]], this setting applies to all the [[Privileged Session Manager|PSM]]s in the load balancer. 
	- Server Settings > TraceLevels = 1,2,3,4,5,6,7  
	- Recorder Settings > TraceLevels= 1,2  
	- Connection Client Settings > TraceLevels = 1,2
- Enabling debug mode will apply the change to all the PSMs in the VIP/Load balancer, its advisable to complete the debug task as quickly as possible and disable debug as the messages generated would increase the load on the servers and in some cases also the vault.  

### Levels

TraceLevels indicate:  
0 - None.  
1 - Exceptions only. Each error in the system will be sent to the trace file, whether  
it is recoverable or not.  
2 - Controller trace. Includes the initialization of the PSMServer, recovery  
procedure and configuration.  
3 - Listener trace. Each session identified by the listener is reported, whether it is  
handled or not.  
4 - Session trace. Includes all the work done for a session (authentication and  
impersonation, password retrieval, activation of components, etc.).  
5 - Uploader trace.  
6 - CASOS errors trace (Vault errors trace).  
7 - CASOS debug and activity trace.

## PSM Folder Structure

#todo  
`PSMInitSession.exe` : The main application the initializes the sessions via [[CyberArk]].

Users can connect through the PVWA portal, or alternatively through PSM for Windows, that is, directly from their desktops using any standard RDP client application, such as MSTSC, different Connection Managers or an RDP file.

By default, the user connects to the PSM machine through port 3389, using the RDP protocol. This is required to facilitate remote access, although this port is not usually opened in the corporate firewall, and in some cases it is not permitted.

You can configure PSM to provide secure remote access to a target machine through an HTML5 gateway when connecting with the PVWA portal. The HTML5 gateway tunnels the session between the end user and the PSM machine using a secure WebSocket protocol (port 443). This eliminates the requirements to open an RDP connection from the end-user's machine. Instead, the end user only requires a web browser to establish a connection to a remote machine through PSM.

Alternatively, PSM can be configured to work with the Microsoft Remote Desktop Gateway (RDGateway) which tunnels the RDP session between the user and the PSM machine using the HTTPS protocol (port 443). This provides a secure connection without needing to open the firewall. All information that is transferred between the user and the PSM machine is encrypted and protected by the HTTPS protocol, which enables secure cross-network and remote access.

## Connection Components

## RDP via SSL

### Steps

[Secure RDP Connections with SSL | CyberArk Docs](https://docs.cyberark.com/PAS/12.6/en/Content/PASIMP/Securing-RDP-Connections-with-SSL.htm)  

The following procedure will guide you through the steps to assign a certificate to the Remote Desktop Services deployment in support of the PSM Farm virtual hostname.


1. Sign in to PSM Server as a Domain [[Administrator]]
2. Open Server Manager and select Remote Desktop Services in the left navigation pane.  
3. In Deployment Overview select **Tasks > Edit Deployment Properties**. In the Configure the deployment window, select **Certificates > Select existing certificate... > Choose a different certificate** and browse to the location of the .pfx file ( in the real environment it will be .cer format and it has to be converted to .pfx format)
4. Select the file with the .pfx extension and click Open. In the Password: field enter {password}, select the box to **"Allow the certificate to be added to the Trusted Root Certification Authorities..."** and select OK to close the Deployment Properties window. 
5. Open the local [[Group Policy]] editor in the server PSM is installed and Navigate to Computer Configuration > Administrative Templates > Windows Components > Remote Desktop Services > Remote Desktop Session Host > Security.
6. Open the Security settings for: Set client connection encryption level. Click on Enabled and set the encryption level to High Level then click 0K.
	1. Specifies whether to require the use of a specific encryption level to secure communications between client computers and RDP Session Host servers during Remote Desktop Protocol (RDP) connections. This policy only applies when you are using native RDP encryption, However. native RDP encryption (as opposed to SSL encryption) is not recommended. This policy does not apply to SSI encryption.
7. Open the setting for: Require use of specific security layer for remote (RDP) connections: Click on Enabled and set the Security Layer to SSL and click 0K.
8. Login to the PVWA from Comp01B/A as vaultadmin01. Navigate to ADMINISTRATION > Configuration Options > Options > Privileged Session Management > Configured PSM Servers > PSMServer > Connection Details > Server and change the Address attribute to the FQDN of the PSM server so that it matches the name defined in the COMPOIC server certificate. (the value before the change would be its IP address)
9. In the PVWA, navigate to ADMINISTRATION > Configuration Options > Options > Connection Components > PSM-SSH > Component Parameters.
	1. Under this setting the name of the property will be authentication level: i and its value is 1.


**Note**: You must be signed in to one of the component servers with a domain account for PSM Connection Components to be successful. If signed into the server as the local Administrator, the current user will not have access to the Certificate Revocation List Distribution Point.

### Steps Explained

#### Certificate Configuration

In this part, we focus on adding the necessary certificate to the Server where PSM is installed. For this, we need to sign in using Domain Administrator credentials. The certificate gets added under the role of 'Remote Desktop Services' via the Server Manager.

#### Group Policy Configuration

Given that the deployment usually takes place within a domain, the next step is to configure the settings in the Group Policy editor. Here, we set the encryption level for client connections and also specify the security layer for secure communications.

#### PVWA Configuration

Finally, we update the settings in PVWA (Privileged Web Access) to ensure they align with the changes made for the PSM server. Specifically, we make sure that the Fully Qualified Domain Name (FQDN) listed in the server certificate matches the name set in the PVWA settings. Additionally, we update the component parameters to a value of '1'. This ensures that the server will authenticate with the target machine before establishing a connection.  

### .cer Vs .pfx

The primary difference between `.cer` and `.pfx` files is that a `.cer` file usually contains only a public key, while a `.pfx` file contains both a private key and the corresponding public key. Additionally, `.pfx` files are password-protected to secure the private key.

---

#### Detailed Comparison

| **Attribute** | **.cer File** | **.pfx File** |
|---------------|---------------|---------------|
| **Contents** | Contains the public key. It can represent a certificate without the associated private key. | Contains both the public key and the associated private key. |
| **Protection** | Not password-protected since it only holds the public key, which is meant to be shared. | Password-protected to secure the private key, ensuring it remains confidential. |
| **Use Cases** | Often used to distribute the public certificate to parties that need to verify the authenticity of signed data or encrypt data to be decrypted by the certificate owner. | Used for backup and transfer of the private key and certificate pair, especially for tasks like secure server communications, code signing, or personal client authentication. |
| **Format** | Commonly in X format. | Often in PKCS#12 format (Public Key Cryptography Standards). |

---

Both `.cer` and `.pfx` files play a crucial role in the realm of public key infrastructure (PKI) and secure communications. It's essential to handle `.pfx` files with care due to the presence of the private key. If someone obtains the `.pfx` file and its password, they could impersonate the certificate holder or decrypt sensitive data meant only for the certificate holder.

## Flow

Users can connect to the PSM machine via the PVWA portal or directly through any standard RDP client. By default, connection occurs over port 3389 using the RDP protocol. PSM can also be configured for more secure access options:

1. **HTML5 Gateway**: Allows connection through the PVWA portal using a secure WebSocket protocol (port 443).
2. **Microsoft RDGateway**: Uses HTTPS protocol (port 443) to securely tunnel the RDP session.

Both options negate the need to open the firewall and ensure encrypted, secure access.

### Connection Methods

- **PVWA Portal**: Web-based interface for users to connect to PSM.
- **Direct RDP Client**: Applications like MSTSC or RDP files allow direct desktop connections.

### Default Settings

- **Port**: 3389
- **Protocol**: RDP
- **Firewall**: This port is typically not open in corporate settings.

### Secure Access Configurations

| Configuration        | Protocol      | Port | Firewall |
|----------------------|---------------|------|-----------|
| HTML5 Gateway        | WebSocket     | 443  | Not Required |
| Microsoft RDGateway  | HTTPS         | 443  | Not Required |

- **HTML5 Gateway**: Eliminates the need for an RDP client, requiring only a web browser.
- **Microsoft RDGateway**: Encrypts all information between the user and PSM, facilitating secure remote and cross-network access.

![[Pasted image 20231101114224.png]]  
![[Pasted image 20231101114214.png]]