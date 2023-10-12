---
aliases: 
tags: 
date created: Monday, July 31st 2023, 3:33:10 pm
date modified: Monday, August 21st 2023, 10:11:23 am
---
The service is generally used because it is not safe for people to directly log into the [[Vault]] server as their actions are not recorded.  
Remote connection is used to log in and complete tasks, this way we can ensure that everything is properly monitored and accounted for.

## PARAgent.exe And PARAgent.ini

- whenever changes are made to these files the PrivateArk Remote control agent service has to be restarted.![[Pasted image 20230731174907.png]]
- The password.cred in the [[Remote Control Client]] and PARagent.pass details should match or there will be an error.  
![[Pasted image 20230731191848.png]]  

### Paraclient - ENE Command

![[Pasted image 20230731193353.png]]  
  ![[Pasted image 20230731193229.png]]  

### Another way of Connecting to the Vault Server without the password.cred File

![[Pasted image 20230731193740.png]]

### PARagent.pass

The PARagent.pass file is a password file used by the CyberArk Remote Control Agent. The file contains the encrypted password for the remote user account that is used to control the CyberArk Enterprise Vault (EPV) server and the Disaster Recovery Vault (DR Vault).

The PARagent.pass file is located in the following directory:

```
%ProgramFiles%\CyberArk\Enterprise Vault\Remote Control Agent\
```

The file is a text file, but the password is encrypted. You cannot view the password unless you have the CyberArk Password Safe application.

If you lose the PARagent.pass file, you will not be able to remotely control the EPV server or DR Vault. You will need to generate a new PARagent.pass file and configure the Remote Control Agent to use the new file.

To generate a new PARagent.pass file, you can use the CyberArk Password Safe application. In the Password Safe application, click on the **New** button and select the **Remote Control Agent** template. Enter a name for the new file and click on the **Create** button.

Once you have created the new PARagent.pass file, you need to configure the Remote Control Agent to use the new file. In the PARAgent.ini file, modify the **RemoteUserCredentials** parameter to point to the new PARagent.pass file.

After you have configured the Remote Control Agent, you need to restart the service. The Remote Control Agent will then use the new PARagent.pass file to authenticate to the EPV server or DR Vault.  
![[Pasted image 20230731192046.png]]  
![[Pasted image 20230731161012.png]]  
![[Pasted image 20230731161040.png]]  

### PARAgent.ini Parameter Explanation

- This is used for both remote control and monitoring 

Settings related to [[Remote Control Client]]  
![[Pasted image 20230731173158.png]]  
Remote Monitoring Settings  
![[Pasted image 20230731173256.png]]

### PARAgent.exe

![[Pasted image 20230731174532.png]]  

## Ports

Port 9022 is used by the CyberArk Remote Control Agent, the VMware Server Console, and the QuickTime Streaming Server.

- **CyberArk Remote Control Agent:** The CyberArk Remote Control Agent is a Windows service that allows you to remotely control the CyberArk Enterprise Vault (EPV) server and the Disaster Recovery Vault (DR Vault). The Remote Control Agent uses port 9022 to communicate with the remote computer.
- **VMware Server Console:** The VMware Server Console is a graphical user interface (GUI) that allows you to manage a VMware Server virtual machine. The VMware Server Console uses port 9022 to communicate with the virtual machine.
- **QuickTime Streaming Server:** The QuickTime Streaming Server is a software application that allows you to stream multimedia content over a network. The QuickTime Streaming Server uses port 9022 to receive connections from clients.

## Information about PARAgent.exe and PARAgent.ini

PARAgent.exe and PARAgent.ini are files used by the CyberArk Remote Control Agent. The PARAgent.exe file is the executable file that starts the Remote Control Agent service. The PARAgent.ini file is a configuration file that specifies the settings for the Remote Control Agent.

The Remote Control Agent is a Windows service that allows you to remotely control the CyberArk Enterprise Vault (EPV) server and the Disaster Recovery Vault (DR Vault). The Remote Control Agent can be used to perform various tasks, such as restarting the EPV server, mounting and unmounting vaults, and managing users.

The PARAgent.ini file contains the following parameters:

- **RemoteHost** - The IP address or hostname of the remote computer that will be used to control the EPV server or DR Vault.
- **RemotePort** - The port number that will be used to communicate with the remote computer.
- **RemoteUserCredentials** - The path to the file that contains the encrypted password for the remote user account.
- **LogLevel** - The logging level for the Remote Control Agent.

You can edit the PARAgent.ini file to change the settings for the Remote Control Agent. However, you must restart the Remote Control Agent service after making any changes to the file.

For more information about the PARAgent.exe and PARAgent.ini files, please refer to the CyberArk documentation:

- [Remote Control Agent Parameter File](https://docs.cyberark.com/PAS/Latest/en/Content/PASREF/Remote%20Control%20Agent%20Parameter%20File.htm)
- [Remote Administration for the Vault/DR Vault](https://docs.cyberark.com/PAS/Latest/en/Content/PASIMP/Remote-Administration-for-the-Vault-DR-Vault.htm)

ask for this file  

![[Pasted image 20230731191634.png]]  
#doubt ![[Pasted image 20230731191528.png]]

### PARAgent.ini Table

<table style="width: 100%;mc-table-style: url('../Resources/TableStyles/RowsX.css');" class="TableStyle-RowsX" cellspacing="0">
                                                                    <colgroup><col style="width: 140px;" class="TableStyle-RowsX-Column-Column1">
                                                                    <col class="TableStyle-RowsX-Column-Column1">
                                                                    </colgroup><tbody>
                                                                        <tr class="TableStyle-RowsX-Body-Alternate">
                                                                            <td colspan="2" class="TableStyle-RowsX-BodyD-Column1-Alternate"><span class="Emphasis">Remote Control</span>
                                                                            </td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Alternate" data-mc-pattern="1">
                                                                            <td colspan="2" class="TableStyle-RowsX-BodyG-Column1-Alternate">
						RemoteStationIPAddress
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyH-Column1-Regular">
						Description
					</td>
                                                                            <td class="TableStyle-RowsX-BodyG-Column1-Regular">
						The IP address of the remote computer from where instructions will be received to carry out Server operations. Up to 3 IP addresses can be specified. 
						Separate the IP addresses with commas.
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyH-Column1-Regular">
						Acceptable Values
					</td>
                                                                            <td class="TableStyle-RowsX-BodyG-Column1-Regular">
						IP address
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyH-Column1-Regular">
						Default Value
					</td>
                                                                            <td class="TableStyle-RowsX-BodyG-Column1-Regular">
						-
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Alternate" data-mc-pattern="1">
                                                                            <td colspan="2" class="TableStyle-RowsX-BodyG-Column1-Alternate">
						RemoteAdminPort
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyH-Column1-Regular">
						Description
					</td>
                                                                            <td class="TableStyle-RowsX-BodyG-Column1-Regular">
						The port through which the above instructions will be received. This port number must be different from the Vault’s defined open ports.
						The CyberArk port for Remote Control is 9022.
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyH-Column1-Regular">
						Acceptable Values
					</td>
                                                                            <td class="TableStyle-RowsX-BodyG-Column1-Regular">
						Number
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyH-Column1-Regular">
						Default Value
					</td>
                                                                            <td class="TableStyle-RowsX-BodyG-Column1-Regular">
						-
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Alternate" data-mc-pattern="1">
                                                                            <td colspan="2" class="TableStyle-RowsX-BodyG-Column1-Alternate">
						UserCredentialsPath
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyH-Column1-Regular">
						Description
					</td>
                                                                            <td class="TableStyle-RowsX-BodyG-Column1-Regular">
						The full pathname to the credentials of the Remote Agent.
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyH-Column1-Regular">
						Acceptable Values
					</td>
                                                                            <td class="TableStyle-RowsX-BodyG-Column1-Regular">
						Path
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyH-Column1-Regular">
						Default Value
					</td>
                                                                            <td class="TableStyle-RowsX-BodyG-Column1-Regular">
						-
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Alternate" data-mc-pattern="1">
                                                                            <td colspan="2" class="TableStyle-RowsX-BodyG-Column1-Alternate">
						ExtensionComponentList
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyH-Column1-Regular">
						Description
					</td>
                                                                            <td class="TableStyle-RowsX-BodyG-Column1-Regular">
						The full pathnames of the component DLL files that the remote agent will load. These files are in the various installation folders.
						Separate the various pathnames with commas.
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyH-Column1-Regular">
						Acceptable Values
					</td>
                                                                            <td class="TableStyle-RowsX-BodyG-Column1-Regular">
						“path,path,…”
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyH-Column1-Regular">
						Default Value
					</td>
                                                                            <td class="TableStyle-RowsX-BodyG-Column1-Regular">
						-
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Alternate" data-mc-pattern="1">
                                                                            <td colspan="2" class="TableStyle-RowsX-BodyG-Column1-Alternate">
						AllowedMonitoredServices
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyH-Column1-Regular">
						Description
					</td>
                                                                            <td class="TableStyle-RowsX-BodyG-Column1-Regular">
						The name of the system services that can be monitored from a remote location. The name of the service must be specified as it appears in the Service Name field in the Service Properties window.
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyH-Column1-Regular">
						Acceptable Values
					</td>
                                                                            <td class="TableStyle-RowsX-BodyG-Column1-Regular">
						“&lt;service name&gt;,&lt;service name&gt;,…”
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyH-Column1-Regular">
						Default Value
					</td>
                                                                            <td class="TableStyle-RowsX-BodyG-Column1-Regular">
						-
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Alternate" data-mc-pattern="1">
                                                                            <td colspan="2" class="TableStyle-RowsX-BodyG-Column1-Alternate"><span class="Emphasis">Remote Monitoring</span>
                                                                            </td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Alternate" data-mc-pattern="1">
                                                                            <td colspan="2" class="TableStyle-RowsX-BodyG-Column1-Alternate">
						SNMPHostIP
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyH-Column1-Regular">
						Description
					</td>
                                                                            <td class="TableStyle-RowsX-BodyG-Column1-Regular">
						The IP address of the remote computer where SNMP traps will be sent.
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyH-Column1-Regular">
						Acceptable Values
					</td>
                                                                            <td class="TableStyle-RowsX-BodyG-Column1-Regular">
						IP address (supports multiple entries)
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyH-Column1-Regular">
						Default Value
					</td>
                                                                            <td class="TableStyle-RowsX-BodyG-Column1-Regular">
						-
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Alternate" data-mc-pattern="1">
                                                                            <td colspan="2" class="TableStyle-RowsX-BodyG-Column1-Alternate">
						SNMPTrapPort
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyH-Column1-Regular">
						Description
					</td>
                                                                            <td class="TableStyle-RowsX-BodyG-Column1-Regular">
						The port through which SNMP traps will be sent to the remote computer. Specify either port 161 or 162.
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyH-Column1-Regular">
						Acceptable Values
					</td>
                                                                            <td class="TableStyle-RowsX-BodyG-Column1-Regular">
						Port 
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyH-Column1-Regular">
						Default Value
					</td>
                                                                            <td class="TableStyle-RowsX-BodyG-Column1-Regular">
						162
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Alternate" data-mc-pattern="1">
                                                                            <td colspan="2" class="TableStyle-RowsX-BodyG-Column1-Alternate">
						SNMPTrapInterval
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyH-Column1-Regular">
						Description
					</td>
                                                                            <td class="TableStyle-RowsX-BodyG-Column1-Regular">
						The number of seconds that pass between notifications.
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyH-Column1-Regular">
						Acceptable Values
					</td>
                                                                            <td class="TableStyle-RowsX-BodyG-Column1-Regular">
						Number 
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyH-Column1-Regular">
						Default Value
					</td>
                                                                            <td class="TableStyle-RowsX-BodyG-Column1-Regular">
						30
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Alternate" data-mc-pattern="1">
                                                                            <td colspan="2" class="TableStyle-RowsX-BodyG-Column1-Alternate">
						SNMPCommunity
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyH-Column1-Regular">
						Description
					</td>
                                                                            <td class="TableStyle-RowsX-BodyG-Column1-Regular">
						The name of location where the SNMP traps originated.
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyH-Column1-Regular">
						Acceptable Values
					</td>
                                                                            <td class="TableStyle-RowsX-BodyG-Column1-Regular">
						String
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyH-Column1-Regular">
						Default Value
					</td>
                                                                            <td class="TableStyle-RowsX-BodyG-Column1-Regular">
						-
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Alternate" data-mc-pattern="1">
                                                                            <td colspan="2" class="TableStyle-RowsX-BodyG-Column1-Alternate">
						MonitoredEventLogNames
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyH-Column1-Regular">
						Description
					</td>
                                                                            <td class="TableStyle-RowsX-BodyG-Column1-Regular">
						The names of the event logs of activities that have taken place since the Server started, such as Application, Security, and System.<br><!--[CDATA[					]]--></td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyH-Column1-Regular">
						Acceptable Values
					</td>
                                                                            <td class="TableStyle-RowsX-BodyG-Column1-Regular">
						String
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyH-Column1-Regular">
						Default Value
					</td>
                                                                            <td class="TableStyle-RowsX-BodyG-Column1-Regular">
						-
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Alternate" data-mc-pattern="1">
                                                                            <td colspan="2" class="TableStyle-RowsX-BodyG-Column1-Alternate">
						SNMPTrapsThresholdCPU
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyH-Column1-Regular">
						Description
					</td>
                                                                            <td class="TableStyle-RowsX-BodyG-Column1-Regular">
						The interval in seconds between checks for CPU usage and the usage percentage threshold for SNMP traps, and the type of alerts that are written in the log. The threshold, retries, retriesinterval and state-full values are optional. 
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyH-Column1-Regular">
						Acceptable Values
					</td>
                                                                            <td class="TableStyle-RowsX-BodyG-Column1-Regular">
						Interval &gt; 0,Threshold &gt;= 0,[Retries &gt; 0,RetriesIntervals&gt;0,State-full – Yes/No]
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyH-Column1-Regular">
						Default Value
					</td>
                                                                            <td class="TableStyle-RowsX-BodyG-Column1-Regular">
						200,90,3,30,NO
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Alternate" data-mc-pattern="1">
                                                                            <td colspan="2" class="TableStyle-RowsX-BodyG-Column1-Alternate">
						SNMPTrapsThresholdPhysicalMemory
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyH-Column1-Regular">
						Description
					</td>
                                                                            <td class="TableStyle-RowsX-BodyG-Column1-Regular">
						The interval in seconds between checks for physical memory usage and the usage percentage threshold for SNMP traps, and the type of alerts that are written in the log. The threshold, retries, retriesinterval and state-full values are optional.
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyH-Column1-Regular">
						Acceptable Values
					</td>
                                                                            <td class="TableStyle-RowsX-BodyG-Column1-Regular">
						Interval &gt; 0,Threshold &gt;= 0,[Retries &gt; 0,RetriesIntervals&gt; 0,State-full – Yes/No]
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyH-Column1-Regular">
						Default Value
					</td>
                                                                            <td class="TableStyle-RowsX-BodyG-Column1-Regular">
						200,90,3,30,NO.
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Alternate" data-mc-pattern="1">
                                                                            <td colspan="2" class="TableStyle-RowsX-BodyG-Column1-Alternate">
						SNMPTrapsThresholdSwapMemory
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyH-Column1-Regular">
						Description
					</td>
                                                                            <td class="TableStyle-RowsX-BodyG-Column1-Regular">
						The interval in seconds between checks for swap memory usage and the usage percentage threshold for SNMP traps, and the type of alerts that are written in the log. The threshold, retries, retriesinterval and state-full values are optional.
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyH-Column1-Regular">
						Acceptable Values
					</td>
                                                                            <td class="TableStyle-RowsX-BodyG-Column1-Regular">
						Interval &gt; 0,Threshold &gt;= 0,[Retries &gt; 0,RetriesIntervals&gt; 0,State-full – Yes/No]
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyH-Column1-Regular">
						Default Value
					</td>
                                                                            <td class="TableStyle-RowsX-BodyG-Column1-Regular">
						200,90,3,30,NO
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Alternate" data-mc-pattern="1">
                                                                            <td colspan="2" class="TableStyle-RowsX-BodyG-Column1-Alternate">
						SNMPTrapsThresholdDiskUsage
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyH-Column1-Regular">
						Description
					</td>
                                                                            <td class="TableStyle-RowsX-BodyG-Column1-Regular">
						The interval in seconds between checks for disk usage and the usage percentage threshold for SNMP traps, and the type of alerts that are written in the log. The threshold, retries, retriesinterval and state-full values are optional. 
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyH-Column1-Regular">
						Acceptable Values
					</td>
                                                                            <td class="TableStyle-RowsX-BodyG-Column1-Regular">
						Interval &gt; 0,Threshold &gt;= 0,[Retries &gt; 0,RetriesIntervals&gt; 0,State-full – Yes/No]
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyH-Column1-Regular">
						Default Value
					</td>
                                                                            <td class="TableStyle-RowsX-BodyG-Column1-Regular">
						200,85,3,30,NO
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Alternate" data-mc-pattern="1">
                                                                            <td colspan="2" class="TableStyle-RowsX-BodyG-Column1-Alternate">
						SNMPTrapsThresholdServiceStatus
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyH-Column1-Regular">
						Description
					</td>
                                                                            <td class="TableStyle-RowsX-BodyG-Column1-Regular">
						The interval between checks for service status for SNMP traps, retries, retries interval and state-full values. The last 3 values are optional. 
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyH-Column1-Regular">
						Acceptable Values
					</td>
                                                                            <td class="TableStyle-RowsX-BodyG-Column1-Regular">
						Interval &gt; 0, [Retries &gt; 0,RetriesIntervals&gt; 0,State-full – Yes/No]
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyH-Column1-Regular">
						Default Value
					</td>
                                                                            <td class="TableStyle-RowsX-BodyG-Column1-Regular">
						200,3,30,NO
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Alternate" data-mc-pattern="1">
                                                                            <td colspan="2" class="TableStyle-RowsX-BodyG-Column1-Alternate">
						SNMPVersion
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyH-Column1-Regular">
						Description
					</td>
                                                                            <td class="TableStyle-RowsX-BodyG-Column1-Regular">
                        The SNMP version that will be used to send SNMP notifications. Any of the following values can be specified:
                        <table class="AutoNumber_p_TableTextBullet" style="width: 100%; margin-left: 0;" cellspacing="0" cellpadding="0"><colgroup><col style="width: 0px;"><col style="width: 24px;"><col style="width: auto;"></colgroup><tbody><tr><td valign="top"></td><td class="AutoNumber_p_Bullet" valign="top"><span class="bullet"><span style="color: #666666;" class="mcFormatColor"><span style="font-size: 0.4rem;" class="mcFormatSize">■</span></span></span></td><td class="AutoNumber_p_Bullet" valign="top" data-mc-autonum="<span style=&quot;color: #666666;&quot; class=&quot;mcFormatColor&quot;><span style=&quot;font-size: 0.4rem;&quot; class=&quot;mcFormatSize&quot;>■</span></span>">v1 – The Vault will support SNMPv1 with a unique OID for each trap.</td></tr></tbody></table><table class="AutoNumber_p_TableTextBullet" style="width: 100%; margin-left: 0;" cellspacing="0" cellpadding="0"><colgroup><col style="width: 0px;"><col style="width: 24px;"><col style="width: auto;"></colgroup><tbody><tr><td valign="top"></td><td class="AutoNumber_p_Bullet" valign="top"><span class="bullet"><span style="color: #666666;" class="mcFormatColor"><span style="font-size: 0.4rem;" class="mcFormatSize">■</span></span></span></td><td class="AutoNumber_p_Bullet" valign="top" data-mc-autonum="<span style=&quot;color: #666666;&quot; class=&quot;mcFormatColor&quot;><span style=&quot;font-size: 0.4rem;&quot; class=&quot;mcFormatSize&quot;>■</span></span>">v2 – The Vault will support SNMPv2. This is the default value.&nbsp; 
						</td></tr></tbody></table><table class="AutoNumber_p_TableTextBullet" style="width: 100%; margin-left: 0;" cellspacing="0" cellpadding="0"><colgroup><col style="width: 0px;"><col style="width: 24px;"><col style="width: auto;"></colgroup><tbody><tr><td valign="top"></td><td class="AutoNumber_p_Bullet" valign="top"><span class="bullet"><span style="color: #666666;" class="mcFormatColor"><span style="font-size: 0.4rem;" class="mcFormatSize">■</span></span></span></td><td class="AutoNumber_p_Bullet" valign="top" data-mc-autonum="<span style=&quot;color: #666666;&quot; class=&quot;mcFormatColor&quot;><span style=&quot;font-size: 0.4rem;&quot; class=&quot;mcFormatSize&quot;>■</span></span>">Compatibility – The Vault will send SNMP notifications using the format used in Vault versions prior to version 5.0.
					</td></tr></tbody></table></td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyH-Column1-Regular">
						Acceptable Values
					</td>
                                                                            <td class="TableStyle-RowsX-BodyG-Column1-Regular">
						String
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyH-Column1-Regular">
						Default Value
					</td>
                                                                            <td class="TableStyle-RowsX-BodyG-Column1-Regular">
						v2
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Alternate" data-mc-pattern="1">
                                                                            <td colspan="2" class="TableStyle-RowsX-BodyG-Column1-Alternate">
						LogMessagesFilterRegexp
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyH-Column1-Regular">
						Description
					</td>
                                                                            <td class="TableStyle-RowsX-BodyG-Column1-Regular">
						A list of filters that determines which messages will be sent through the SNMP server, as long as they are not listed in the ExcludedLogMessagesFilterRegexp parameter.
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyH-Column1-Regular">
						Acceptable Values
					</td>
                                                                            <td class="TableStyle-RowsX-BodyG-Column1-Regular">
						.*
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyH-Column1-Regular">
						Default Value
					</td>
                                                                            <td class="TableStyle-RowsX-BodyG-Column1-Regular">
						-
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Alternate" data-mc-pattern="1">
                                                                            <td colspan="2" class="TableStyle-RowsX-BodyG-Column1-Alternate">
						ExcludedLogMessagesFilterRegexp
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyH-Column1-Regular">
						Description
					</td>
                                                                            <td class="TableStyle-RowsX-BodyG-Column1-Regular">
						A list of filters that determines which messages will not be sent through the SNMP server. This list overrides the list in the <span class="Emphasis">LogMessagesFilter Regexp</span> parameter.
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyH-Column1-Regular">
						Acceptable Values
					</td>
                                                                            <td class="TableStyle-RowsX-BodyG-Column1-Regular">
						Regular expressions
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyH-Column1-Regular">
						Default Value
					</td>
                                                                            <td class="TableStyle-RowsX-BodyG-Column1-Regular">
						(ITA|PARE|PADR|CAS).*I
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Alternate" data-mc-pattern="1">
                                                                            <td colspan="2" class="TableStyle-RowsX-BodyG-Column1-Alternate">
						EnableTrace
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyH-Column1-Regular">
						Description
					</td>
                                                                            <td class="TableStyle-RowsX-BodyG-Column1-Regular">
						Determines whether or not trace data is written in the PARAgent.log file.
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyH-Column1-Regular">
						Acceptable Values
					</td>
                                                                            <td class="TableStyle-RowsX-BodyG-Column1-Regular">
						Yes/No
					</td>
                                                                        </tr>
                                                                        <tr class="TableStyle-RowsX-Body-Regular">
                                                                            <td class="TableStyle-RowsX-BodyB-Column1-Regular">
						Default Value
					</td>
                                                                            <td class="TableStyle-RowsX-BodyA-Column1-Regular">
						-
					</td>
                                                                        </tr>
                                                                    </tbody>
                                                                </table>