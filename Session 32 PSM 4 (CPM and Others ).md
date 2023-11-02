---
aliases: 
tags: 
date created: Wednesday, November 1st 2023, 3:14:25 pm
date modified: Wednesday, November 1st 2023, 5:35:49 pm
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