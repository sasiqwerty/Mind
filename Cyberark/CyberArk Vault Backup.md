---
aliases: 
tags: 
date created: Sunday, November 5th 2023, 4:49:04 pm
date modified: Sunday, November 5th 2023, 5:01:22 pm
---
Configure component CyberArk Replicate to backup the vault to a remote server.

1. **Enable Backup User**:
   - Use the PrivateArk Client to locate and enable the backup user.
2. **Set Up PrivateArk Replicator**:
   - Install PrivateArk Replicator.
   - Edit the `vault.ini` file within the Replicator component to specify the vault name and address, using port 1858.
```ini
vault = "{enter the name here}"
Address = "{enter the vault IP address}"
PORT = 1858
```
3. **Create Credential File**:
   - Run `CreateCredFile.exe` to generate a credential file for the backup user.
4. **Schedule Backup Task**:
   - Set up a Windows Scheduled Task to run the backup daily at a specified time.
   - Use the command `vault.ini /logonfromfile user.ini /FullBackup` as the task argument.
5. **Initiate Replication**:
   - To manually start a full replication, use the same command in the PrivateArk Replicate directory.
	   - `vault.ini /logonfromfile user.ini /FullBackup`
6. **Log Review**:
   - Check the `PAReplicate.log` file for operation results and any errors.
7. **Test Restore Process**:
   - Open PowerShell in the Replicate directory.
   - Use the `PARestore.exe` command with appropriate arguments to test safe restoration.
```powershell
PARestore.exe vault.ini dr /RestoreSafe “{safe name here}” /TargetSafe {new safe name here}
```
**Important Note**: When restoring, always use a different safe name to avoid conflicts with deleted folders and ensure historical data integrity.