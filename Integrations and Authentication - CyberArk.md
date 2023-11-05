---
aliases: 
tags: 
date created: Sunday, November 5th 2023, 1:11:28 pm
date modified: Sunday, November 5th 2023, 4:38:56 pm
---

## Authentications

### [[LDAP Integration|LDAP authentication]]

To configure the vault to use LDAP over SSL connections, you must import the Certificate Authority’s root Certificate into the Windows Trusted Root Certificate Store on the Vault Server and make the necessary changes on the PVWA.

1. **Download the Certificate**:
   - Obtain the certificate from the Domain Controller.
   - Store the certificate in the VaultInternal Safe.

2. **Open Certificate Manager**:
   - On the Vault Server, run `certlm.msc` to access the Certificate Manager.

3. **Modify Hosts File**:
   - Add the IP address of the Domain Controller to the hosts file, ensuring you have administrative privileges to do this.

4. **Create LDAP Bind Account**:
   - At the Domain Controller, set up an LDAP bind account with administrative rights.

5. **Configure LDAP in PVWA**:
   - Log into Password Vault Web Access (PVWA) as an Administrator.
   - Navigate to `User Provisioning > LDAP Integration Page`.
   - Enter details such as the new domain name, address, LDAP bind account username and password, and the domain base context.
   - Enable SSL settings as this setup is for SSL connections.

6. **Map Groups**:
   - At this stage, the required groups should already exist on the Active Directory (AD) side.
   - Simply map these groups in the PVWA; the bind account information should autofill.

### RADIUS Authentication

Enable RADIUS authentication, and test 2 Factor Authentication. You will have the option to download the application “Google Authenticator” on your smartphone to generate a RADIUS token. If you do not wish to install the app on your phone you have the option to use the emergency scratch code tokens, provided to you when you register a user in Google Authenticator.

![[Pasted image 20231105162549.png]]

The image illustrates a user access flow involving CyberArk's Privileged Account Security solution, with multi-factor authentication via a RADIUS server using FreeRADIUS on CentOS, and OTP generation through Google Authenticator. Communication is secured with HTTPS, and the OTP relies on time synchronization.

### PKI Authentication

### 2FA - Two Factor Authentication

## Integrations

### SIEM Integration

To integrate CyberArk with a SIEM solution and send audit logs via the syslog protocol, you can follow these streamlined steps:

1. **Choose XSL Translator**:
   - Navigate to the directory `C:\Program Files(x86)\PrivateArk\Server\Syslog`.
   - Select the sample translator file for your SIEM, e.g., `ArcSightACME.sample.xsl`.
   - Rename the file to `ArcSightACME.xsl`.
2. **Copy Configuration Section**:
   - Open `dpparm.sample.ini` located at `C:\Program Files(x86)\PrivateArk\Server\Conf`.
   - Copy the entire `[SYSLOG]` section from this file.
3. **Edit Configuration File**:
   - Using administrative privileges, edit the `dbparm.ini` file to include the copied `[SYSLOG]` section.
   - Update the configuration with the appropriate settings, such as the IP address of your syslog server.
4. **Restart CyberArk Service**:
   - After making changes, restart the PrivateArk Server Service to apply them.
5. **Validate Configuration**:
   - Check the `ITALOG.log` file for any syntax errors and to confirm successful integration.

Below is the edited section of the `dbparm.ini` file, tailored for your SIEM integration:

```ini
[SYSLOG]
SyslogTranslatorFile=Syslog\ArcSightACME.xsl
SyslogServerPort=514
SyslogServerIP={Enter the IP Address of the SYSLOG server}
SyslogServerProtocol=UDP
SyslogMessageCodeFilter=0-999
SyslogSendBOMPrefix=NO
UseLegacySyslogFormat=yes
SendMonitoringMessage=No
```

Remember to replace `{Enter the IP Address of the SYSLOG server}` with the actual IP address of your syslog server.

After these steps, CyberArk should start sending audit logs to your SIEM system, enhancing your monitoring and incident response capabilities.

### NTP Integration

To configure the Vault Server's system clock for synchronization with an internal time source, follow these steps:

1. **Edit Configuration File**:
   - Open Windows File Explorer and navigate to `C:\Program Files(x86)\PrivateArk\Server\Conf`.
   - Locate and edit the `dbparm.ini` file with administrative privileges.

2. **Add NTP Firewall Rule**:
   - In the `dbparm.ini` file, add or edit the `[NTP Firewall Rule]` section as follows (replace `{enter the IP address of the vault}` with the actual IP address of your vault):

```ini
[NTP Firewall Rule]
AllowNonStandardFWAddresses = [{enter the IP address of the vault}],Yes:outbound/udp
```



1. **Confirm Windows Time Service**:
   - Ensure the Windows Time service is running on the Vault Server. This can typically be checked in the Services management console (`services.msc`).

2. **Configure Time Sync Command**:
   - Open a command prompt with Administrator privileges.
   - Enter the command to configure the external time source:

```powershell
  W32tm /config /manualpeerlist:10.0.0.2 /syncfromflags:manual /reliable:YES /update
```

   Replace `10.0.0.2` with the actual IP address of your internal time source.

1. **System Clock Adjustment**:
   - After running the command, the system clock should synchronize with the specified time source and display the correct time.

By completing these steps, you will ensure that the Vault Server's system clock is in sync with an internal time source, which is vital for the proper functioning of CyberArk's PAM solution.

### SMTP Integration

- SMTP (Simple Mail Transfer Protocol) is **a TCP/IP protocol used in sending and receiving email**.  
- Port 25 is traditionally used for email submission by many mailbox providers.
- In distributed environments, SMTP is used to transfer messages between MTAs on different machines.

To set up email notifications in CyberArk using SMTP, follow these steps:

1. **Ensure Service is Running**:
   - Confirm that the CyberArk Event Notification Engine Service is active.
2. **Log in as Administrator**:
   - Access the CyberArk interface and log in with Administrator credentials.
3. **Access Setup Wizard**:
   - Navigate to `Administration > Configuration Options`.
   - Click on `Setup Wizard`.
4. **Select Email Notifications**:
   - Within the wizard, choose the option for email notifications.
5. **Configure SMTP Settings**:
   - Enter the IP address of the Vault.
   - Provide the sender email address.
   - Use the default SMTP port (25) and accept the default PVWA URL.
6. **Send Test Email**:
   - Send a test email to verify the setup is working correctly.
7. **Check Email Reception**:
   - Log into the email account you sent the test email to.
   - Confirm receipt of the test email.

Troubleshooting Steps

If there's a need to rerun the setup wizard:

1. **Change SMTP Server IP**:
   - Adjust the SMTP server IP to `1.1.1.1` as a placeholder if necessary.
2. **Confirm Service Status**:
   - Ensure the Event Notification Engine service is running on the Vault Server.

### SNMP Integration

[Configure Remote Monitoring | CyberArk Docs](https://docs.cyberark.com/PAS/13.0/en/Content/PASIMP/Configuring-Remote-Monitoring.htm)

The Remote Monitoring uses SNMP to send Vault traps to a remote terminal. This enables users to receive both Operating System and Vault information, as follows:

Operating System information:

- CPU, memory, and disk usage
- Event log notifications
- Service status

Component-specific information:

- Password Vault and DR Vault status
- Password Vault and DR Vault logs

CyberArk provides two MIB files (for SNMP v1 and SNMPv2) that describe the SNMP notifications that are sent by the Vault. These files can be uploaded and integrated into the enterprise monitoring software.