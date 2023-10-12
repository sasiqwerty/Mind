---
aliases: 
tags: 
date created: Thursday, August 3rd 2023, 12:43:13 pm
date modified: Thursday, August 3rd 2023, 12:43:29 pm
---
The **PasswordLevelRequestTimeframe** feature in the Automatic Password Management tab in CyberArk is used to specify the minimum amount of time that must pass between password requests for the same account. This can help to prevent brute force attacks against accounts.

The **PasswordLevelRequestTimeframe** setting can be configured in the CyberArk Password Vault Admin Console. To do this, navigate to **Administration** > **System Configuration** > **Automatic Password Management**. In the **Automatic Password Management** dialog box, set the **PasswordLevelRequestTimeframe** parameter to the desired value.

The default value for the **PasswordLevelRequestTimeframe** setting is 30 minutes. This means that a user must wait at least 30 minutes before they can request a new password for the same account. If you need to increase the amount of time between password requests, you can do so by increasing the value of the **PasswordLevelRequestTimeframe** setting.

However, it is important to note that increasing the amount of time between password requests can also make it more difficult for users to access accounts if they forget their passwords. Therefore, it is important to configure the **PasswordLevelRequestTimeframe** setting based on the needs of your environment.

Here are some additional things to keep in mind about the **PasswordLevelRequestTimeframe** setting:

- The **PasswordLevelRequestTimeframe** setting applies to all users who are authorized to request passwords for the same account.
- The **PasswordLevelRequestTimeframe** setting is not cumulative. This means that if a user requests a new password for an account, and then requests a new password for the same account again 15 minutes later, they will have to wait another 15 minutes before they can request a third password.
- The **PasswordLevelRequestTimeframe** setting is a soft limit. This means that if a user requests a new password for an account before the **PasswordLevelRequestTimeframe** has expired, the vault will not reject the request. However, the user may have to wait longer for the password to be granted.

I hope this helps! Let me know if you have any other questions.