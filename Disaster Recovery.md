---
aliases: 
tags: 
date created: Sunday, November 5th 2023, 4:47:44 pm
date modified: Sunday, November 5th 2023, 5:50:18 pm
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


