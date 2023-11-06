---
aliases: 
tags: 
date created: Sunday, November 5th 2023, 4:47:44 pm
date modified: Sunday, November 5th 2023, 7:05:43 pm
---
Enable the DR user from the [[PrivateArk Client]]  
Install the [[disaster recovery module]] and ensure that the vault has replicated successfully  
Open the `C:\Program Files (x86)\PrivateArk\PADR\Logs\PADR.log` file, you should see entries with informational codes `PAREP013I` Replicating Safe and at the end, `PADR0010I Replicate ended`.  
Open `\Conf\padr.ini` file and note that `FailoverMode` is equal to No.  
Stop the PrivateArk Server Service  
Open the PADR log file and you will be able to see that the DR vault is unable to reach the production vault.  
The log can be monitored with this command in the PowerShell : `Get-Content .\logs\padr.log –wait`  
After 5 failures by default, the DR Vault will go into failover mode. Total duration = 5 minutes. Check the PADR.log and review the sequence of events.  
Note : The built-in Administrator user is now being managed by the CPM and the password has been changed and replicated to the DR Vault. In the event of an actual disaster, the built-in Administrators password may not be accessible and so it is important to configure the DR Vault to support LDAP Authentication for administrative and normal user access.

## Manual Fail Back Steps:

Before attempting the Failback steps, make sure the DR_Failback user is enabled.

1. Update the Padr.ini file in Primary Vault with `ActivateManualFailOver=No` and `FailoverMode=No`  
   And Delete the last two lines (log number and timestamp of the last successful replication) in the file.

2. Start the `CyberArkVaultDisasterRecovery` Service at primary node(You have already the PrivateArk Server service in stop status, since it is in failover state)

In Prod Padr.log we will see the `MetaDataReplication` is running successfully message.  
And the Replication will Ended after some time.

To bring back the Primary Vault Up and running to the Production State.  
update the `ActivateManualFailover=Yes` in padr.ini of Prod node and restart the CyberArk DR service.

This will automatically starts this PrivateArk Server Service, and the DisasterRecovery Service will stop automatically.

Remove the two time stamp lines at DR vault-Padr.ini and set Failover Mode=No  
Stop the PrivateArk Server service in DR Vault.  
Start the DR service at DR Vault.

CyberArk is a leading security solution that focuses on privileged access management. In the context of CyberArk and many other IT systems, the terms "FailOverMode", "FailBack", and "FailOver" relate to high availability and disaster recovery mechanisms. Here's a brief overview of these terms:

1. **FailOver**:
   - **Definition**: Failover is the process of switching to a redundant or standby system, server, hardware component, or network upon the failure or abnormal termination of the previously active system.
   - **In CyberArk**: If the primary CyberArk server (or any other component) becomes unavailable, the system will automatically switch to a secondary or backup server to ensure continuous service availability. This process is transparent to the end-users, ensuring that there's no disruption in service.

2. **FailOverMode**:
   - **Definition**: This typically refers to the mode or state the system is in when it has switched to the backup or secondary system due to a failure in the primary system.
   - **In CyberArk**: When the primary server is down, and the system has switched to the backup server, it's said to be in "FailOverMode". In this mode, certain functionalities might be limited or operate differently compared to when the primary server is active.

3. **FailBack**:
   - **Definition**: Failback is the process of restoring a system, component, or service back to its primary state or location after it has been shifted to a backup or secondary location during a failover.
   - **In CyberArk**: Once the issues with the primary server are resolved and it's back online, the system can be switched back from the secondary server to the primary server. This process of returning to the primary server is known as "FailBack". It ensures that the primary system is once again the active system, and the secondary system returns to its standby state.
- **LastDataReplicationTimestamp**: