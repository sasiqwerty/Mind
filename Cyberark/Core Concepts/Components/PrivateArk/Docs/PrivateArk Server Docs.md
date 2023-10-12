### PrivateArk Server Windows Service

The Server interface can only be installed on the Server host.

[![Server startup](https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/12.2/en/Content/Images/PASIMP/Working%20with%20the%20Server%20Interface_thumb_0_48.png)](https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/12.2/en/Content/Images/PASIMP/Working%20with%20the%20Server%20Interface.png)

It is possible to operate the Server from a remote terminal. For more information, refer to [Remote Administration for the Vault/DR Vault](https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/12.2/en/Content/PASIMP/Remote-Administration-for-the-Vault-DR-Vault.htm#_Ref364686153).

The Server interface enables the following operations:

- Starting the Server, which then begins operating as a Windows service.
- Stopping the Server.
- Displaying the Server log.
- Administrating the Server settings, which include the Server IP address and the location of Safes stored in the Vault.

As a service, the Server can be configured to start automatically or manually.
The Server Key is required to start the Server. There are two ways of providing the Server Key upon startup, as follows:

- The Server Key can be permanently installed on the Server host.  This enables you to configure the Server to start automatically.
- The Server Key can be stored on a removable media, such as a disk or CD.  This means that the disk or CD must be in place in order to start the Server and can be removed after the Server has started.

### Specify Administration Settings

The Settings window enables you to view and modify the network adapter configurations and the Safe directories used by the CyberArk Vault.

[View the administration settings](https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/12.2/en/Content/PASIMP/Specifying-Administration-Settings.htm?tocpath=Administrator%7CComponents%7CDigital%20Vault%7COperate%20the%20CyberArk%20Vault%7C_____3#)

1. From the Administration menu, select PrivateArk Settings; the PrivateArk Settings window appears.
2. In the Network Adapters tab, you can view a list of your Network Adapters.
   [![PrivateArk settings](https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/12.2/en/Content/Images/PASIMP/Operating%20the%20CyberArk%20Vault_thumb_0_48.jpg)](https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/12.2/en/Content/Images/PASIMP/Operating%20the%20CyberArk%20Vault.jpg)
3. To configure an adapter, select it, then click Edit; the Set Network Adapter configuration window appears.
   [![Setnetworkadapterconfig](https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/12.2/en/Content/Images/PASIMP/Operating%20the%20CyberArk%20Vault_1_thumb_0_48.jpg)](https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/12.2/en/Content/Images/PASIMP/Operating%20the%20CyberArk%20Vault_1.jpg)
4. Specify the Adapter type, then click OK.
5. Click the Managed safes tab to display the directories in which Safes are stored. Safe directories that have been erased appear in red.
   [![managed safes](https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/12.2/en/Content/Images/PASIMP/Operating%20the%20CyberArk%20Vault_2_thumb_0_48.jpg)](https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/12.2/en/Content/Images/PASIMP/Operating%20the%20CyberArk%20Vault_2.jpg)
6. To add a Safe directory, click Add; the Browse window appears enabling you to select a directory in which to store more Safes.
7. To remove a Safe directory, select the directory to remove, then click Remove.
8. Click OK to close the PrivateArk Settings window.
9. Restart the Server for the changes to take effect.
