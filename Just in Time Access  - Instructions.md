---
aliases: 
tags: 
date created: Sunday, August 20th 2023, 2:41:36 pm
date modified: Friday, September 29th 2023, 12:16:32 am
---
n---
aliases: 
tags: 
date created: Sunday, August 20th 2023, 2:41:36 pm
date modified: Sunday, August 20th 2023, 4:49:45 pm
---
[[Password Upload Utility]] + [[Just in Time Access  - Instructions]] video

<iframe width="560" height="315" src="https://www.youtube.com/embed/JlkMzlwvO4c" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


A major step in the Privilege Access Management program is to secure the Windows local administrators. This is essential to reduce the risk of lateral movement. CyberArk enables securing local administrator credentials, as well as using PSM to access those accounts. 

There are cases, however, where managing the local administrator passwords is not possible at the initial stage of deployment, whether because of objection from the IT users,or other reasons. Just-inTime (JIT) access allows you to gain control over local administrator security without inconveniencing administrative users. It can be used as an intermediate step towards full implementation of Vaulting the local administrator accounts. You can grant Windows admins on-demand, ad-hoc privileged access to Windows targets,for a predefined number of hours (4 hours by default). 

During this time, domain users can request to access a system as a local administrator. If authorized, the system temporarily adds the logged-on Windows users into the target system's local administrator group, without the need to manage the credentials of the localadministrator on that target. This allows for a frictionless and lightweight solution that enables your organization to introduce privileged controls and help establish habitual security, before moving into a robust PAM program. 

The workflow, as exhibited in the following diagram, starts when an end user requests access to a designated target machine and then is added to the local admin groups. The end user is notified that they have been granted access (or not), and once granted, is able to access the target machine using their own login for 4 hours (by default). After this period, the user is automatically removed from the local admin group.

## Set up the JIT Access Platform

In this exercise, you will set up Just-in-Time access for the Windows admin user (John), allowing John to be added to the local admin group on the target system for 4 hours. 
1. Log into the PVWA as mike. 
2. Go to ADMINISTRATION -> Platform Management and duplicate the WIN SRVLCL ADM 45 Platform to a new platform called WIN SRV JIT. You may add a description stating accounts associated with this platform are not managed by the CPM
3. Click on Edit to edit the new platform. In the new platform set the following parameters to NO. 
	1. UI & Workflows 
		1. AutoChangeOnAdd 
	2. Automatic Password Management --> Password Change 
		1. AllowManualChange  
		2. PerformPeriodicChange
	3. Automatic Password Management --> Password Verification
		1. VFAllowManualVerification
		2. VFPerformPeriodicVerification
	4. Automatic Password Management -> Password Reconciliation
		1. RCAllowManualReconciliation
		2. RCAutomaticReconcileWhenUnsynched
4. In the new platform, go to UI & Workflows -> Properties. Remove the Username property from Required, and add a new property called Username under Optional.
5. In the new Platform, right-click on Automatic Password Management, and select Additional Policy Settings.
6. Under Additional Policy Settings, set AllowDomainUserAdHocAccess to Yes.
7. You will see a pop-up dialog warning you to use the AllowedSafes parameter to limit the use of this policy to only those Safes where it is appropriate. Click Yes.

> Note: For JIT access, a domain account that has been configured as a reconcile account should be associated with the platform. In our case, this has already been defined in the base platform we duplicated: WIN SRV LCL ADM 45 

> Note: For security best practice, you need to limit the Safes that are required for ad hoc access, by setting the AllowedSafes parameter with a regular expression that lists the Safes that this platform can be applied to. This too has already been defined in the base platform we duplicated: WIN SRV LCL ADM 45 

> Note: You can also set the time, in minutes, after which a user is automatically removed from the Administrators group on the target machine. By default, the parameter is set to 240 minutes (4 hours).

![[Pasted image 20230820145031.png]]

### Add the Local Administrator Account

Go to Accounts View and click on Add Account. Add the local administrator account of the Target Windows server

![[Pasted image 20230820145423.png]]

### Test Just-in-Time Access

1. First, open MSTSC (you can use the search functionality to find the application).
2. Attempt to connect to target-win.acme.corp as acme\\John
3. You should receive an error stating that John is not authorized for remote login:
4. Now, login to the PVWA as John. Search for the Target Windows local Administrator account and click on Get Access.
5. If you configured everything successfully, you should receive a notification saying you’ve been granted admin access for 4 hours.
6. Now try to launch another RDP connection to the Target Windows server as acme\\John. You should be able to login this time.
7. After successfully connecting to the Target Windows server, go to Computer Management -> Local Users and Groups -> Groups and open the local Administrators group. Verify that acme\John was added to the group.
8. Disconnect from the Target Windows server.