---
aliases: 
tags: 
date created: Wednesday, November 1st 2023, 3:14:25 pm
date modified: Thursday, November 2nd 2023, 1:00:27 pm
---

## Locking Down a User's Interface in PrivateArk

### Prerequisites:

- Ensure all Virtual Machines (VM's) are started in your Skytap lab before proceeding, excluding the DR VM.

### Steps:

1. **Login to PrivateArk Client**:
    - Use administrator credentials.
2. **Access Directory Mapping**:
    - Navigate: `Tools > Administrative Tools > Directory Mapping`.
3. **Update User Template's Authorized Interfaces**:
    - Go to: `Map Name Users_acme.corp > Update > User Template > General > Authorized Interfaces`.
4. **Modify Authorized Interfaces**:
    - Using the center arrows, move all entries from the **Authorized Interfaces** column to the **Available Interfaces** column. 
    - Exception: Retain entries `PSM`, `PSMP`, and `PVWA` in the Authorized Interfaces.
5. **Finalize Changes**:
    - Click `OK` three times.
    - Exit the Directory Mapping utility.
    - Log off from the PrivateArk Client.
6. **Modify Authentication Method for a Specific Vault**:
    - While logged off, choose the desired Vault in the PrivateArk Client.

![[Pasted image 20231101172333.png]]

## CPM Related Topics

### CPM Optimization

To optimize CPM (Centralized Password Management) performance in a busy environment, consider adjusting the following settings:

1. **AllowedSafes**: Limits which safes the CPM will search. Use Regex to narrow down your selection.
2. **Immediateinterval**: The time interval, post-manual change, when CPM will attempt the change. Recommended value is 5 minutes.
3. **Interval**: Determines how often CPM will check for password changes automatically. Standard value is 1440 minutes.
4. **FromHour/ToHour**: Restricts when CPM operations will occur. Suitable for staggering different platforms.

#### 1. AllowedSafes

- **Location**: Automatic Password Management -> General
- **Default Setting**: `.*` (matches all)
- **Recommended**: Use Regex to be as restrictive as possible.

`AllowedSafes=Win.*|Dom.*`

#### 2. Immediateinterval

- **Location**: Automatic Password Management -> General
- **Default Setting**: Not specified
- **Recommended**: 5 minutes

#### 3. Interval

- **Location**: Automatic Password Management -> General
- **Default Setting**: 1440 minutes
- **Recommended**: Keep as-is unless using `FromHour`/`ToHour`.

#### 4. Stagger Platforms Using FromHour/ToHour

- **Location**: Automatic Password Management for password changes, verifications, and reconciliations
- **Time Range**: 1 to 24 (in hours)

**Example Configuration**:

- Service Account password changes: `0000-0759`
- Firecall account password changes: `0800-1559`
- Local administrator account changes: `1600-2359`

**Historical Note**: Before CPM version 9.10, the `Interval` value was calculated based on `FromHour` and `ToHour`. Since 9.10, this is no longer necessary. Stick to the default 1440 minutes if not using `FromHour`/`ToHour` to avoid performance issues.

### Change Password in Reset Mode

ChangePasswordInResetMode : Defines whether or not password changes will be performed via reset mode using the reconciliation account. This is useful in cases here the password policy prevents the user from changing his own password when a password minimal age restriction is applied.  
Note : This setting has to be turned on when the automatic password management is activated in the particular [[Platform]].

### Managing [[Administrator]] (CyberArk) with CPM

To manage the password for the built-in CyberArk Administrator user, configure the Central Policy Manager (CPM). Post-configuration, Vault administrators will need to retrieve the password from the Vault itself or through a PSM Connection Component.


|**Parameter** | **Value**|  
|--------------|----------|  
|System(Device) Type|  Application|  
|Platform | CyberArk Vault|  
|Username | Administrator |  
|Address | 10.0.10.1 |  
|Password | Cyberark1|


Remember that the account type being onboarded is an 'Application' type, even though it’s for managing the CyberArk Administrator user.

After this, Vault administrators will need to access the Vault or a PSM Connection Component to retrieve the Administrator password whenever necessary.

## Connect with PSM-PrivateArk Client

- Configure the PSM to support the PSM-PrivateArk Client Connection Component. The PrivateArk Client must be installed on the PSM server, as instructed during the PSM Installation section of this guide. The PrivateArk Client must also be configured in Global Configuration mode, which enables you to define Vault definitions that will be available to users of the PSM-PrivateArk Client Connection Component.  
- Sign in to the PSM server Comp01C as Admin02 and run the PrivateArk Client from the desktop. Do not login to the Vault.  
- Ensure that at least one vault server is defined, as shown in the graphic. If not, select the File, New, Server menu option and define a new vault using 10.0.10.1 for the Name, and Address fields.  
- Ensure that Authentication method = PrivateArk authentication  
- Go to Tools > Administrative Tools > Export Configuration Data.  
- Browse to your Desktop folder and select “Export Global Configuration Data” and click OK. Close the PrivateArk Client.  
- Rename the file to GlobalSettings.ini.  
- Right click on GlobalSettings.ini file and choose Properties > Security tab. Select “Edit…, Add…” and assign default (RX) permissions for the local Comp01C\PSMShadowUsers group.  
- Use the PAConfig.exe utility to change the configuration to Global Configuration. Open Windows Powershell (Admin) in folder “C:\Program Files (x86)\PrivateArk\Client” and run the following command: `PAConfig.exe /inifile c:\Users\Admin02\Desktop\GlobalSettings.ini`  
- Restart the server.  
- Sign in to the PSM server Comp01C as Admin02 and add the Private Ark client executable as an authorized application in the Applocker configuration.  
- Using File Explorer navigate to c:\Program Files (x86)\CyberArk\PSM\Hardening. (PSM Hardening hides local drives to users. In the address bar, type “c:\” to display the local drive.)  
- Edit the file PSMConfigureApplocker.xml using Notepad++.  
- Find the “Generic Client support” section at the bottom. Copy the “Generic client sample” line. Paste this line anywhere without comments.  
- Update the new line as show below.  
- `<Application Name=”PrivateArk Client” Type=”Exe” Path="C:\Program Files (x86)\PrivateArk\Client\Arkui.exe” Method=”Hash” />`
- Save the file.
- Objective: Apply the Applocker rules by executing the PSMConfigureApplocker.ps1 script
- Execute the following 3 commands.
```powershell
Get-ExecutionPolicy
Set-ExecutionPolicy Bypass -Scope Process
.\psmconfigureapplocker.ps1
```
- Sign in to the PVWA from Comp01A or Comp01B.  
	- Enable RDP over SSL (see “Use RDP over SSL” on page 103) for the PSM-PrivateArkClient connection component.  
	- Test both members of the load balanced pool of PSM servers  
	- Update the CyberArk Vault platform to take advantage of the load balanced PSM configuration. 
- Attempt to connect to the Vault using Administrator and the PSM-PrivateArkClient connection component.