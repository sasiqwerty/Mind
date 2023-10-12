---
aliases:
tags: docs
date created: Saturday, July 29th 2023, 4:50:57 pm
date modified: Saturday, July 29th 2023, 5:01:33 pm
---

## Overview

#docs 

All passwords must be handled through the PVWA interface to ensure that the passwords on remote devices must be synchronized with the corresponding passwords in the Password Vault. However, if a password on the remote device is changed manually and not through the PVWA, it is no longer synchronized with its corresponding password in the Vault, and it becomes unavailable.

Whenever this happens, it is essential for the relevant personnel to be alerted as soon as possible so that they can identify the unsynchronized password and regain control over the remote device.

The CPM can verify password content on remote devices to ensure that they are synchronized with corresponding passwords in the Password Vault, and are valid and up-to-date. This process can either be managed automatically by the CPM or manually by an authorized user. If the password on the remote machine is not synchronized with the password in the Vault, the CPM alerts the user and can start a reconciliation process to synchronize the passwords. For more information about reconciling passwords, refer to Reconcile Password .

The CPM verifies all types of passwords, including group passwords and linked passwords. Passwords that are created automatically in the Vault as a result of auto-detection are verified immediately. The CPM does not lock passwords when it verifies them, whether in regular or exclusive mode.

Automatic password verification is determined by the following:

- The Master Policy defines how frequently passwords will be verified.  
- Platform settings applied to the account determine how verification is initiated and the hours during which the verification process will take place.  
Password verification is entirely independent of the password change process, which is configured separately.

For more information about password verification on other platforms, contact CyberArk support.

### Verify a Password Automatically

Users who belong to the Vault Admins group can configure password verification processes in the platform in the platform settings page. The Vault Admins group must be an owner of the CPM Safe with the following authorizations:

- Retrieve passwords  
- Update password value  
Enable automatic password verification

### Verify a Password Manually

Although password verification processes can be scheduled to take place automatically at regular intervals, a verification process can also be initiated manually in the PVWA. Users who have the following Safe member authorizations can initiate a password verification process by the CPM:

- Initiate CPM password management operations  
Verify a password manually 

#website  
[Verify Passwords | CyberArk Docs](https://docs.cyberark.com/PAS/Latest/en/Content/PASIMP/Verifying-Passwords.htm)