---
aliases: 
tags: 
date created: Thursday, August 3rd 2023, 12:39:16 pm
date modified: Thursday, August 3rd 2023, 12:39:26 pm
---
The **SearchForUsages** feature in the Automatic Password Management tab in CyberArk is used to automatically search for and update passwords that are used in multiple places. This can help to ensure that all copies of a password are synchronized and up-to-date.

The **SearchForUsages** feature is enabled by default. When it is enabled, the CyberArk Password Manager (CPM) will automatically search for all usages of a password when it is changed. If the CPM finds any other usages of the password, it will update them to the new value.

The **SearchForUsages** feature can be disabled in the CyberArk Password Vault Admin Console. To do this, navigate to **Administration** > **System Configuration** > **Automatic Password Management**. In the **Automatic Password Management** dialog box, clear the **SearchForUsages** checkbox.

Here are some additional things to keep in mind about the **SearchForUsages** feature:

- The **SearchForUsages** feature only searches for usages of passwords that are changed by the CPM. It does not search for usages of passwords that are changed manually.
- The **SearchForUsages** feature can be slow if there are a lot of usages of a password.
- The **SearchForUsages** feature can be disabled if you do not want the CPM to automatically update passwords that are used in multiple places.
