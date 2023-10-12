---
aliases: 
tags: 
date created: Wednesday, August 16th 2023, 7:29:04 pm
date modified: Wednesday, August 16th 2023, 7:33:21 pm
---

## Unmanaged Privileged Access

In this section you will observe how the PTA detects when a Windows account is being added to a privileged group and then checks if the account is being managed by CyberArk. If the account is not managed, the PTA will generate a security event and add the account to the list of Pending Accounts. 

Unlike the previous example, in this case the account is detected by the PTA as soon as the account is granted privileged permissions, allowing PTA to respond and take control over this unmanaged privileged account. This solution shortens the time it takes to detect an attacker or a malicious insider who attempts to create a backdoor account, bypassing the organizational policy.

1. First, login to the PVWA using LDAP authentication with John.
2. Locate the localadmin01 account on target server target-win.acme.corp and click on Connect. 
3. As localadmin01 on the target server, open Computer Management and navigate to Local Users and Groups -> Users. Right-click on Users and select "New User…".
4. Add a new user called backdoor. Set the password to Cyberark1 and select Password never expires. Then click on Create.
5. Right-click on the newly added user and select properties. Go to the Member Of tab and click on Add…
6. Type "Administrators" and then Check names…. Click on OK to add the backdoor user to the local Administrators group.
7. Log into the PVWA as mike and go back to Security -> Security Events. After about 20 seconds or so, you should be able to see a new Security Event for Unmanaged Privileged Account, notifying the CyberArk Security administrator that an account called backdoor, which is not managed by CyberArk, was added to the local privileged Administrators group.
8. On the left navigation select Accounts, then go to Accounts Feed -> Pending & Discovery. Select backdoor from the list (use “Refine By” to search for the account if needed) and click on Onboard Accounts.
9. Onboard the account to the Win-Srv-Fin-US safe and associate the account with the WIN SRV LCL ADM 45 platform. Choose to Automatically reconcile the password to take full control of the backdoor account. Click on Onboard.
10. Verify that the backdoor account has been reconciled by the CPM.

## Suspicious Activities in a Windows Session and Automatic Suspension

 In this section you will configure the PTA to detect when a risky command is used in a Windows privileged session and to suspend the session automatically. We will use this ability to prevent malicious users from adding another backdoor account. 
 
 1. Login to the PVWA as mike and go to Security -> Security Configurations -> Privileged Session Analysis and Response. Click on "Add rule".
 2. Under Category select Windows titles. Under Pattern enter:
 3. Under description enter: "Prevent malicious insiders from adding a backdoor user". Set the risk score to 80 and set the session response to Suspend. Then click on Add.
 4. Login to the PVWA as John. Launch another privileged session as localadmin01 on target server target-win.acme.corp. Try to add a second backdoor user. If the above steps were configured successfully, the system should suspend your session, preventing you from adding another backdoor user.
 5. Login to the PVWA using LDAP authentication as mike. Go to Security -> Security Events and verify you can see the “Suspicious activities detected in a privileged session” event. Verify that the session got a score of 80.
 6. Click on Resume to re-activate the suspended session.