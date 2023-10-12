---
aliases: 
tags: 
date created: Thursday, August 3rd 2023, 12:40:10 pm
date modified: Thursday, August 3rd 2023, 12:40:21 pm
---
The **LooselyConnectedDevices** feature in the Automatic Password Management tab in CyberArk is used to manage passwords for devices that are not always connected to the network. This can be useful for managing passwords for devices such as laptops, tablets, and smartphones.

The **LooselyConnectedDevices** feature works by storing passwords for these devices in the CyberArk vault. When a user needs to access a device that is not connected to the network, they can use the CyberArk Password Manager (CPM) to retrieve the password from the vault.

The **LooselyConnectedDevices** feature is enabled by default. However, you need to have the CyberArk EPM (Endpoint Privilege Manager) agent installed on the devices that you want to manage.

Here are some additional things to keep in mind about the **LooselyConnectedDevices** feature:

- The **LooselyConnectedDevices** feature only works for devices that have the CyberArk EPM agent installed.
- The **LooselyConnectedDevices** feature can be slow if the devices are not connected to the network.
- The **LooselyConnectedDevices** feature can be disabled if you do not want to manage passwords for devices that are not always connected to the network.
