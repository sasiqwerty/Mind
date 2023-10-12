---
aliases: 
tags: 
date created: Wednesday, August 9th 2023, 3:23:47 pm
date modified: Wednesday, August 9th 2023, 3:34:46 pm
---
The refresh period in PVWA is the amount of time between automatic updates of the accounts and files lists in the PVWA. The default refresh period is 20 minutes. This means that every 20 minutes, the PVWA will check with the Privileged Session Manager (PSM) to see if there are any new or updated accounts or files. If there are, the PVWA will update its lists accordingly.

The refresh period is important for ensuring that the PVWA always has the most up-to-date information about the accounts and files that users can access. This helps to prevent users from trying to access accounts or files that they no longer have permission to access, and it also helps to ensure that users are aware of any new accounts or files that have been created.

The refresh period can be configured in the PVWA's administration console. To do this, open the administration console and navigate to the **Configuration Options** page. In the **PIM Suite Configuration** section, you will see the **Refresh Period** setting. 

Its the frequency in minutes at which the PVConfiguration.xml, Policies.xml,SafeTemplate.xml, CPM.ini and Policy.ini configuration files in the server are read.  
![[Pasted image 20230809153425.png]]
- It is important to note that the refresh period is only for automatic updates. 
- This is useful if you need to make sure that the PVWA has the most up-to-date information immediately.