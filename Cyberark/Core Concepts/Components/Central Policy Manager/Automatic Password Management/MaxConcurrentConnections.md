---
aliases: 
tags: 
date created: Thursday, August 3rd 2023, 12:37:57 pm
date modified: Thursday, August 3rd 2023, 12:38:12 pm
---
The **MaxConcurrentConnections** feature in the Automatic Password Management tab in CyberArk is used to limit the number of concurrent connections that can be made to the vault when retrieving passwords. This can help to prevent the vault from being overloaded and can also help to improve performance.

The **MaxConcurrentConnections** setting can be configured in the CyberArk Password Vault Admin Console. To do this, navigate to **Administration** > **System Configuration** > **Automatic Password Management**. In the **Automatic Password Management** dialog box, set the **MaxConcurrentConnections** parameter to the desired value.

The default value for the **MaxConcurrentConnections** setting is 10. This means that up to 10 concurrent connections can be made to the vault when retrieving passwords. If you need to increase the number of concurrent connections, you can do so by increasing the value of the **MaxConcurrentConnections** setting.

However, it is important to note that increasing the number of concurrent connections can also increase the load on the vault. Therefore, it is important to configure the **MaxConcurrentConnections** setting based on the needs of your environment.

Here are some additional things to keep in mind about the **MaxConcurrentConnections** setting:

- The **MaxConcurrentConnections** setting applies to all users who are authorized to retrieve passwords from the vault.
- The **MaxConcurrentConnections** setting is not cumulative. This means that if two users are both trying to retrieve passwords at the same time, the vault will only allow one of those users to connect at a time.
- The **MaxConcurrentConnections** setting is a soft limit. This means that if more than the specified number of concurrent connections are made to the vault, the vault will not reject the additional connections. However, the additional connections may be delayed or may not be able to complete successfully.

I hope this helps! Let me know if you have any other questions.