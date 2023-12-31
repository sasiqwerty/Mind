---
aliases: 
tags: 
date created: Sunday, August 13th 2023, 4:10:51 pm
date modified: Sunday, November 5th 2023, 7:03:18 pm
---

## Disaster Recovery

In this section we will test the Disaster Recovery (DR) procedures for automatic failover and manual failback. The exercise will include the following steps:

1. First, we will configure the Disaster Recovery module on the DR server to perform an automatic failover in case the Primary Vault is no longer reachable.
2. We will execute a full replication from the Primary Vault to the DR Vault.
3. We will test an automatic failover from the Primary Vault to the DR Vault. As part of the test, we will also confirm that our end users can still access critical systems via CyberArk, without any human intervention.
4. We will set the Primary Vault to act as DR and replicate all data back from the DR Vault to the Primary Vault.
5. We will then perform a manual failback from the DR Vault to the Primary Vault
6. Lastly, we will set the DR Vault back to DR mode and confirm our end users are still able to connect to critical systems via CyberArk.

Note : The below steps have already been performed by the implementation team:

The PrivateArk Server, PrivateArk Client, and Disaster Recovery module have all been installed on both your vault01a and DR servers by the implementation team.

A second DR user called “DR_Failback” was manually created by the implementation team during the deployment of the Primary Vault for the purpose of supporting the failback procedure from the DR site back to the primary site.

However, both the DR and DR_Failback users are currently disabled. You will need to enable these users to complete the Disaster Recovery exercises.

### Step 1: Enable Automatic Failover on the DR Vault

As noted above, the implementation team has already installed the PrivateArk Server, PrivateArk Client and Disaster Recovery service on the DR server. However, to avoid an unwanted automatic failover during the first days of the course, automatic failover was disabled, and the DR user deactivated. We are now going to enable the DR user and Automatic Failover to the DR Vault.

1. Note : Do NOT change the password as the DR user has already authenticated to the Vault during initial implementation and the password for the user has already been rotated. If you change the password to Cyberark1, you will need to create a new cred file as well. The DR user is located under the System branch.
2. On the Components server, connect as the Administrator user with the PrivateArk Client to the Primary Vault and enable the DR user.
3. Next, power on the 08-DR server. Remember, it will take a moment for the machine to start.
4. Sign into Windows on the DR server as Administrator.
5. Open the file explorer and navigate to C:\Program Files (x86)\PrivateArk\PADR\Conf. Double click on the padr.ini file to edit it with Notepad
6. Change the `EnableFailover` setting to `Yes` and delete the last two lines of the file (if present). This will trigger a full replication when we restart the Disaster Recovery service, ensuring we have the most up-to-date data.
7. Save the file and exit Notepad.

Notice `FailoverMode` is currently set to No. Do NOT change this setting. It will automatically change later when we test the failover process.

  

### Step 3: Execute Automatic Failover Test

  

Now, we will execute an automatic failover test by stopping the Primary Vault server. If everything works as expected the Disaster Recovery module on the DR server will recognize that the Primary Vault is offline and trigger an automatic failover.

  

Sign into Windows on the Primary Vault server (Vault01A) as Administrator.

Open the Server Central Administration app and stop click on the red traffic light to stop PrivateArk Server service.

Once the Primary Vault has stopped, return to the console of the DR Server.

Monitor the the tail on the padr.log file. You should see messages stating that the Disaster Recovery service is unable to reach the Primary Vault

After 5 failures, the DR Vault will go into failover mode (this is the default setting). Check the padr.log and review the sequence of events.

  

#### Confirm Automatic Failover on the DR Vault

  

On the DR server (10.0.14.1), open the Windows Services applet and confirm the CyberArk Vault Disaster Recovery service has terminated.

Confirm the PrivateArk Server service is now running on the DR server (10.0.14.1).

  

#### Confirm Automatic Failover of PVWA and PSM

  

In this section we will confirm our end users (like John) can still access critical systems via CyberArk, even though the Primary Vault is offline, without human intervention.

  

Note the implementation team has already configured the PVWA and PSM to automatically failover to the DR Vault when the Primary Vault is no longer available. To support automatic failover, the Vault.ini file for both services has been configured with the IP addresses of both the Primary Vault and the DR Vault separated by a comma.

  

Here you can see the configuration of the PVWA Vault.ini file.

  

- To confirm that both the PVWA and PSM automatic failover was successful, return to the console of the Components server.

- Open Chrome and verify that you can still login to the PVWA as John, even though the Primary Vault is offline.

- Now, verify you can launch a secure session to the target Windows machine using the localadmin01 account via PSM. If everything worked as expected, John should still be able to access the target server via CyberArk, without any human intervention.

  

Note: You may need to try to launch the connection via PSM a couple of time before it works, as it may take a few minutes before the PSM fails over to the DR Vault.

  

### Step 4: Execute a Full Replication back to the Primary Vault

  

Before we failback to the Primary Vault we must first make sure we replicate all the latest data from the DR Vault (which served as the active Vault for the duration of resolving the incident). In this section we will use the Disaster Recovery module on vault01a toreplicate data back from the DR Vault to the Primary Vault.

  

Note:

The implementation team has already installed the Disaster Recovery module on vault01a, and manually created a separate DR user for the purpose of performing replication from the DR Vault back to the Primary Vault.

  

The new user is called DR_Failback, and has been made a member of the built-in group DR_Users. The user was assigned the following Vault authorizations: Backup All Safes and Restore All Safes.

  

From Components, use PrivateArk Client to connect to the DR Vault and enable the user DR_Failback.

  

Note:

Do NOT change the password as the DR_Failback user has already authenticated to the Vault during initial implementation, and the password for the user has already been rotated. If you change the password to Cyberarkl, you will need to create a

new cred file as well.

  

The DR_Failback user is located under the System branch.

  

- Open the console on vault01a (10.0.10.1).

- Open the file explorer and navigate to C:\Program Files (x86)\PrivateArk\PADR\Conf.Double click on the padr.ini file to edit it with Notepad.

- Make the following changes to the padr.ini file on vault01a:

  - Set FailoverMode to No.

  - Delete the last two lines (log number and timestamp of the last successful replication) in the file.

- Save the file and close it.

- Start the ‘CyberArk Disaster Recovery’ Service on the Primary Vault

- Right click on the Get-DR-log.ps1 file located on the desktop of the vault01a and select Run with PowerShell.

- Monitor the tail of the padr.log to verify that the Primary Vault has replicated all the changes from the DR Vault.

  On the Components server, login to the PVWA as Mike. Navigate to SYSTEM HEALTH to review the current system health. Note that now Vault 10.0.10.1 is considered DR while Vault 10.0.14.1 is considered PRIMARY.

  

Note

Contrary to the PVWA and PSM, the CPM is not configured to perform an automatic failover, which is why it is showing as disconnected in the image above. This is to avoid the situation of split brain between the two Vaults. To support password rotation in the DR site, we will need to manually failover the CPM to the DR Vault (by setting the DR Vault IP address in the vault.ini file of the CPM). We will not perform manual failover for the CPM in this exercise.

  

### Step 5: Execute Failback Procedure by Using Manual Failover

  

Now that all the data has been replicated back from the DR Vault to the Primary Vault, we can proceed with performing a manual failback from the DR Vault to the Primary Vault. The failback procedure will be performed using a Manual Failover.

  

- Make sure you are working on vault01a (10.0.10.1).

- Open the file explorer and navigate to C:\Program Files (x86)\PrivateArk\PADR\Conf. Double click on the padr.ini file to edit it with Notepad.

- Set ActivateManualFailover to Yes

- Save the file and close it.

- Restart the CyberArk Disaster Recovery service on vault01a (10.0.10.1). The service should start and stop immediately (because of the ActivateManualFailoversetting). Then the PrivateArk Server service should start.

  

Important: The above steps are critical for a successful failback from the DR Vault to the Primary Vault. Reverting to the Primary Vault without first performing a proper failover can result in data inconsistencies.

  

#### Confirm Manual Failover on the Primary Vault

  

Monitor the tail running on the padr.log file on vault01a (10.0.10.1). Confirm you can see the messages stating that the Failover process ended successfully, that the Vault service is starting, and that the Disaster Recovery service has terminated.

Verify that the the CyberArk Vault Disaster Recovery service has terminated on vault01a (10.0.10.1)

Verify that the PrivateArk Server service has started successfully on vault01a (10.0.10.1).

  

### Step 6: Set the DR Server back to DR Mode

  

In the last section of this exercise, we will set the DR server back to DR mode.

  

- Return to the console of DR (10.0.14.1).

- On the DR server, edit the padr.ini file and make the following changes:

    - Set FailoverMode to No.

    - Delete the last two lines (log number and timestamp of the last successful replication) in the file.

    - Save and exit the file.

- Using the Windows Services applet, stop the PrivateArk Server service on DR (10.0.14.1).

- Then, start the CyberArk Vault Disaster Recovery service on DR (10.0.14.1).

- Check the tail running on the padr.log file on the DR server (10.0.14.1) and confirm that a full replication process started and that the replication (from the Primary Vault to the DR Vault) has ended successfully.

  

#### Confirm Automatic Failover for PVWA and PSM

  

In this step we will confirm that our end users can still access critical systems via CyberArk.

  

- Login to the PVWA as John and launch a secure connection to the target Windowsmachine using the account localadmin01. If everything works as expected, John should be able to launch the secure connection without any human intervention.

- Lastly, login to the PVWA as Mike and navigate to SYSTEM HEALTH. Confirm server 10.0.10.1 once again acts as PRIMARY and server 10.0.14.1 acts as DR. Confirm all other components are connected.

  

Note: It may take a little longer for the PSM for SSH service to failover, but eventually it should failover to the functioning Vault.

Important: Due to some limitations in our lab, it is important to disable both the DR and the DR_Failback users (using the PrivateArk Client) until the time you want to work again on the disaster recovery exercise