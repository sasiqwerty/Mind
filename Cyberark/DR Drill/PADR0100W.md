---
aliases: 
tags: 
date created: Saturday, August 12th 2023, 8:44:59 am
date modified: Saturday, August 12th 2023, 8:45:06 am
---
The error "PADR0100W" in CyberArk pertains to Metadata Replication warnings. Here's a summary of the information related to this error:

1. **Cause of the Error**:
   - The error is triggered when the `ReplicationUser.pass` file on the Primary Vault is missing, corrupted, or out of sync with the DR server's `MasterReplicationUser.pass` file. This password file is essential for connecting to the local MySQL to run the replication.  
     [Source](https://cyberark-customers.force.com/s/article/PADR0100W-Metadata-Replication-warning-Communication-error-Last-SQL-Error-0)

2. **Solution**:
   - On ALL Primary and DR Vault servers, you should modify the `slave_net_timeout` parameter to `30000` in the `my.ini` configuration file. This file is typically located in `<drive>:\Program Files (x86)\PrivateArk\Database`. This adjustment is necessary for all nodes in a High Availability (HA) environment. After making these changes, restart the PrivateArk Database service in ALL the sites.  
     [Source](https://cyberark-customers.force.com/s/article/00004539)

3. **Additional Information**:
   - There's another variant of the PADR0100W Metadata Replication warning which cites "Last IO Error Code: 1045". This issue arises when incremental replications fail, as indicated in the `padr.log`.  
     [Source](https://cyberark-customers.force.com/s/article/PADR0100W-Metadata-Replication-warning-Last-IO-Error-Code-1045)

If you're facing this issue, it's recommended to follow the provided solution and, if necessary, reach out to CyberArk's support for further assistance.