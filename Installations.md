---
aliases: 
tags: 
date created: Wednesday, October 4th 2023, 11:16:27 pm
date modified: Friday, October 6th 2023, 2:55:34 am
---

## Vault Installation

the installation of the vault is done in steps
1. Preparation
2. Vault Server Installation
3. [[PrivateArk Client]] Installation

### Prerequisites

- License.xml files  
- Operator CD  
- Master CD  
- Server

The standalone vault only requires TCP IPv4 for communication.  

### Step 1

**Preparation Steps for CyberArk Vault Installation:**
1. Ensure **TCP/IPv6** is selected.
2. Access **TCP/IPv4** properties:
   - Set IP: `10.0.10.1`, Subnet: `255.255.0.0`, Gateway: `10.0.255.254`.
   - Clear all DNS servers and choose *Advanced*.
   - Uncheck "Register this connections addresses in DNS" in DNS tab.
   - In WINS tab, turn off “Enable LMHOSTS lookup”.
   - Disable *NetBIOS over TCP/IP*.
   - Confirm changes to return to properties dialog.
3. Only retain **TCP/IPv4** and **TCP/IPv6**; deselect others. 
4. Deselect other Protocols

### Step 2

1. **Install Visual C++ Redistributable:**
   1. Execute `VC redist.x64.exe`.
   2. Note: This installs MSVC runtime libraries, essential for apps built with Microsoft C and C++ tools.
2. **Initiate Server Installation:**
   1. Right-click on `setup.exe` (server) and choose *Run as Administrator*.
3. **Choose Installation Type:**
   1. Opt for *Standalone Vault Installation*.
4. **Specify Installation Folder:**
   1. By default: `C:Program Files (x86)\PrivateArk`.
   2. Recommendation: Retain this location.
5. **Determine Safes Location:**
   1. Designate a location for your safes, where encrypted data is stored.
6. **License Configuration:**
   1. When prompted, provide the path to the *license folder*.
7. **Operator CD Configuration:**
   1. When prompted, provide the path to the *Operator CD folder*.
8. **Remote Control Agent Setup:**
   1. Configure the agent or opt to skip.
   2. Note: This facilitates administrative vault operations from remote terminals.
9. **System Hardening:**
   1. Proceed with the hardening process.
10. **Configure Built-in Users:**
   1. Set password for *master user*.
   2. Set password for *administrator user*.
11. **Concluding Step:**
   1. After PrivateArk client installation, restart the server.

**Notes** : The Visual C++ Redistributable installs Microsoft C and C++ (MSVC) runtime libraries. These libraries are required by many applications built by using Microsoft C and C++ tools. If your app uses those libraries, a Microsoft Visual C++ Redistributable package must be installed on the target system before you install your app.

### PrivateArk Client Installation

**Process Overview:** The installation process is straightforward.

1. **Initiate Client Installation:**
   - Right-click on the client.
   - Select *Run as Administrator*.
2. **Installation Settings:**
   - Opt for the default settings.
   - Continue with the installation.
3. **Server Configuration:**
   - When prompted, input:
     - A meaningful server name.
     - Its IP address.
     - The default username you'd like to use for login.
4. **Concluding Step:**
   - After the installation, restart the server.

### Post Vault Installation

Ensure that the below mentioned services are up and running.

| Service Name                               | Primary Function                                                                                                          |
|--------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| **PrivateArk Server Service**              | Main service for the vault; dependent services like ENE halt if it's restarted. Handles the start/stop of the vault.       |
| **PrivateArk Database Service**            | Core service for data access. Interruption can halt PrivateArk Server and risk database corruption.                        |
| **PrivateArk Remote Control Agent Service**| Provides remote access and monitoring but is non-essential.                                                                 |
| **CyberArk Logic Container Service**       | Manages master policy execution and application logic for database read/write.                                             |
| **CyberArk Event Notification Engine Service** | Manages email-based notifications for password expiry, user login requests, etc.                                           |
| **CyberArk Windows Hardened Firewall Service** | Converts Windows firewall into CyberArk service during hardening, securing inbound/outbound traffic (only port 1858).    |

## PVWA Installation

### Automating PVWA Prerequisites Using CyberArk Script

CyberArk provides a script to streamline the setup of PVWA prerequisites, performing the following:

1. Installing web server roles and features.
2. Generating a self-signed web certificate.
3. Setting up HTTPS bindings.

**Note**: If the Web Server is already set up, omit this section.

**Configuration and Script Details:**

- **Config File**: `PVWA_Prerequisites_Config.xml`  
  This file incorporates 5 scripts:
   1. `PVWA_VerifyDotNetFrameworkVersion.psm1`
   2. `PVWA_InstallWebServerRoles.psm1`
   3. `PVWA_DisableIPV6.psm1`
   4. `PVWA_ConfigSelfCertificat.psm1`
   5. `PVWA_IIS_SSL_TLS_Settings.psm1`

**Steps for Script Execution and Validation:**

1. **Check Execution Policy:**
   - Execute: `Get-ExecutionPolicy`
     - **Expected Outcome**: `Restricted`
2. **Bypass Execution Policy for Present Process:**
   - Execute: `Set-ExecutionPolicy Bypass -Scope Process`
3. **Execute PVWA Prerequisites Script:**
   - Run: `.\PVWA_Prerequisites.ps1`
   - **Important**: The script's execution might take a few minutes.
4. **Post-Execution Verifications:**  
   a. **Script Confirmation:**
      - Check for messages: `Operation Succeeded` and `IsSucceeded: 0` to confirm the script ran successfully.  
   b. **Inspect Log:**
      - Refer to `Script.log` at:
        - `C:\CYB_Files\Password Vault Web Access-RIs-v12.6\Installation Automation\[date_time]`  
   c. **IIS Manager Validation:**
      - Launch the IIS Manager console.
      - Ensure IIS is up and running with a self-signed certificate.
      - Validate incoming HTTPS requests are channeled through the certificate:
        1. Proceed to “Default Web Site”.
        2. Opt for *Edit Site* > *Bindings*.
        3. Scrutinize the HTTPS Binding to ensure the self-signed SSL certificate is in place.

Note: The `PVWA_Prerequisites` script creates a self-signed certificate and uses this certificate for  
binding HTTPs incoming requests. In a production environment, we recommend updating the HTTPS binding  
with a certificate provided by a Trusted Certification Authority.

### Import Trusted Certificates for Web Hosting

**Objective**: Substitute the self-signed certificate, generated by the prerequisites script, with a Web Certificate issued by ACME Certificate Authority. 

**Procedure**

1. **Access the PVWA Server**:
   - Login to the PVWA Server using credentials of a Domain Admin User
2. **Launch IIS Manager**:
   - Navigate to: `Start Menu > Administrative Tools`.
   - Open the **Internet Information Services (IIS) Manager**.
   - Within **Connections**, highlight the host name and access `Server Certificates`.
3. **Import Certificate**:
   - From the **Actions** menu, select `Import...`.
   - Click on the ellipsis to locate the `.pfx` Certificate file.
4. **Choose the Certificate File**:
   - Go to: `C:\CYBR_Files` and open `comp01a_sslweb.pfx`.
   - Input the password: `Cyberark1`.
   - For **Certificate Store**, opt for `Web Hosting`.
   - Ensure `Allow this certificate to be exported` is checked.
5. **Configure HTTPS Binding**:
   - In **Connections**, expand `Sites` and choose `Default Web Site`.
   - In the **Actions** column, tap on `Bindings...`.
6. **Apply the New Certificate**:
   - Access the **https** binding by double-clicking.
   - Select the newly imported certificate titled: `COMP01AWebCert_2022`.
7. **Finalize**:
   - Confirm your selections by clicking `OK` and subsequently close the window.

### Require HTTP over SSL (PVWA)

**Objective**: Set up IIS to mandate SSL connections. This step is crucial as a groundwork for upcoming authentication sections.

**Steps**:

1. **Access IIS Manager**:
   - Navigate to: `Start Menu > Administrative Tools`.
   - Open **Internet Information Services (IIS) Manager (INETMGR)** on your component server.

2. **Configure SSL Settings**:
   - Proceed to `Default Web Site`.
   - Double-click on `SSL Settings` (represented by a golden padlock icon).
   - Ensure `Require SSL` is selected.
   - Confirm your choice in the `Actions` menu.

3. **Test the IIS Setup**:
   - It's vital to ensure the IIS server operates flawlessly before installing PVWA software.
   - Launch **Internet Explorer** and try connecting to the default web site on the component server using both HTTP and HTTPS URLs.  
     - For HTTP: `http://{servername}.acme.corp/`
     - For HTTPS: `https://{servername}.acme.corp/`

### PVWA Application Installation

**Recommendation**: It's advisable to perform a graceful server restart after the installation of each component.

**Steps**:

1. **Initiate Installation**:
   - Log into the server with local admin privileges.
   - Right-click the setup and choose `Run as Administrator`.
2. **Install Necessary Packages**:
   - If prompted, install the `Microsoft Visual C++ 2013 Redistributable` packages.
3. **Agree to Terms**:
   - Read and accept the End-User License Agreement (EULA).
4. **Input Company Details**:
   - Enter your company's relevant information.
5. **Web Application Location**:
   - The default path is: `C:\inetpub\wwwroot\PasswordVault\`.
6. **Configuration Files Location**:
   - The default directory is: `C:\CyberArk\Password Vault Web Access`.
7. **Choose Installation Type**:
   - You'll have options for either the Full Password Vault Web Access or its mobile variant. Make a selection based on your needs or opt for both.
8. **Authentication Method**:
   - It's recommended to select `LDAP` and `CyberArk` as your authentication methods.
9. **Vault Configuration**:
   - Input the vault address, vault port (typically `1858`), and the PVWA URL.
10. **User Credentials**:
   - Username: `administrator`
   - Password: `Cyberark1`
1. **Completion**:
   - Once all steps are executed, the installation process is concluded.  
Sure! I've structured the information for clarity:

### Post PVWA Installation Checks:

1. **Inspect Installation Log**:
   - Review the `PVWAInstall.log`.
   - To locate the file, open the Run dialog and input `%temp%`.
2. **Connect to PVWA via Browser**:
   - Launch Chrome.
   - Navigate to `https://comp01a.acme.corp/PasswordVault/v10/logon.`
   - Ensure the PVWA login page appears. This check confirms that the PasswordVault application communicates successfully with the PrivateArk Server.
3. **Login to PVWA**:
   - Use CyberArk Authentication to sign in as an Administrator.
   - Verify that the following sections display accurately:
     - Policies
     - Accounts
     - Applications
     - Reports
     - Administration
4. **Session Termination**:
   - Log out from PVWA.

### CyberArk PVWA Server Hardening

**Introduction**:  
Hardening the PVWA server is essential to ensure it adheres to CyberArk's security standards, whether in 'In Domain' or 'Out of Domain' deployments. This hardening process combines enforcing security policies (through GPO or INF), manual operations, and automated tasks using Installation Automation PowerShell scripts.

**Key Notes**:  
- A majority of the PVWA hardening steps can be executed using a PowerShell script, though they can also be carried out manually.
- Certain configurations can't be automated and necessitate manual execution.

**Objective**:  
For the PVWA or CPM server, only the 'Client for Microsoft Networks', 'File and Printer Sharing for Microsoft Networks', and the 'TCP/IPv4' network protocol are essential. Our goal is to disable all other Network Interface Card (NIC) protocols, services, and clients.

**Steps**:

1. **Access Network Connections**:
   - Right-click on the Start Menu.
   - Navigate to `Network Connections > Change adapter options`.
2. **Modify ACME Network Adapter Properties**:
   - Right-click on the `ACME Network Adapter`.
   - Opt for `Properties`.
3. **Configure Network Protocols, Services, or Clients**:
   - Retain only the following components:
     1. `Client for Microsoft Network` #todo
     2. `File and Printer Sharing for Microsoft Network`
     3. `Internet Protocol Version 4 (TCP/IPv4)`
   - Deactivate all other default protocols, services, and clients.
4. **Restart the Server**:
   - Reboot the server to apply the changes.

#### **Installation Automation Hardening**

**Initial Setup**

1. **Server Sign-In**:
   - Access the `Comp01A` server with local Administrator rights or as an ACME Domain user possessing Local Admin privileges.
   - Proceed to: `C:\CYBR_Files\Password Vault Web Access-RIs-v12.6\InstallationAutomation\`.
2. **Execute PowerShell Commands**:
   - Launch **Windows PowerShell as an Administrator** from the directory mentioned above.
   - When prompted, click 'Yes' and execute the following commands:
     ```powershell
     Set-ExecutionPolicy Bypass -Scope Process
     .\PVWA_Hardening.ps1
     ```

##### Notes

- Running `Get-ExecutionPolicy` shows the current Execution Policy. ACME.Corp's default is set to `ExecutionPolicy Restricted`.
- The command `Set-ExecutionPolicy Bypass -Scope Process` only modifies the Execution Policy for the ongoing session without altering PowerShell's default Execution Policy.
- The `.\PVWA_Hardening.ps1` script triggers the PowerShell hardening process.

#### **Post-Script Verifications**

1. Ensure the script has run successfully by looking for messages like `Operation Succeeded` and `IsSucceeded: 0`.
2. Inspect the `Script.log` for details, located at: `C:\CYBR_Files\Password Vault Web Access-RIs-v12.6\InstallationAutomation\timestamp`.

### **Final Manual Hardening for PVWA Deployments**

**Objective**:

Eliminate superfluous Application Pools from IIS.

 **Steps For IIS Hardening**:

1. **IIS Configuration Manager**:
   - Open the IIS Configuration Manager.
2. **Manage Application Pools**:
   - In the 'Connections' pane, navigate to `Application Pools`.
   - Retain only:
     - `DefaultAppPool` (Managed Pipeline Mode = Integrated)
     - `PasswordVaultWebAccess` (Managed Pipeline Mode = Integrated)
   - Erase all other pre-existing Application Pools.
