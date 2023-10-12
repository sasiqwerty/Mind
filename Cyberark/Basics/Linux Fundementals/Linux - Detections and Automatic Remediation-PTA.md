---
aliases: 
tags: 
date created: Wednesday, August 16th 2023, 7:29:04 pm
date modified: Monday, August 21st 2023, 11:06:15 am
---

## Detections and Automatic Remediation for UNIX/Linux

### Unmanaged Privileged Access

In this section you will observe how the PTA detects when privileged accounts are being used and then check if they are being managed by CyberArk. If the account is not managed, the PTA will generate a security event and add the account to the list of Pending Accounts. The Vault Administrator can then onboard the account to the relevant safe. Automatic Onboarding Rules can also be applied.  
First, we need to establish an SSH session to the target Linux server to create an event on the PTA, which we will review using the Security pane in the PVWA. 
1. Open PuTTy from the Components server and open an SSH session to Target Linux as root02 (password: Cyberark1).
2. Login to the PVWA as mike and go to Security -> Security Events and verify that you can see the “Unmanaged privileged account” alert related to root02
3. Go to Accounts Feed -> Pending & Discovery. Select root02 from the list (use “Refine By” to search for the account if needed) and click on Onboard Accounts.
4. Onboard the account to the Lin-Fin-US safe and associate the account with the LIN SSH 30 platform.
5. Enter “Cyberark1” as the default password.
6. You should also return to Security -> Security Events and close the Security event now that it has been dealt with.

### Suspected Credential Theft and Automatic Password Rotation

In this section, you will configure the PTA to detect when privileged accounts are being used without first retrieving the password from CyberArk PAM and trigger the CPM to initiate a password change. 

1. Login to the PVWA as Paul and go to POLICIES -> Safes. Select the Lin-Fin-US safe and click on Members. 
2. Click on Add Member and search for the PTAUser in the Vault. Select the PTAUser. Keep the default permissions and expand Account Management. Select “Initiate CPM account management operations” and click on Add.
3. Repeat the above step to add the PTAAppUser to the Lin-Fin-US safe as well (including the “Initiate CPM account management operations” permission).
4. Close and exit from your putty session to 10.0.0.20 if it is still open. 
5. Once again, open PuTTy from the Components server and open an SSH session to Target Linux as root02 (password: Cyberark1).
6. Login to the PVWA as mike and go to Security -> Security Events and verify that you can see the “Suspected Credentials Theft” alert related to root02.
7. Open the Activities tab for the root02 account to verify that the CPM changed the password after the PTA detected the suspected credential theft alert and under Activities added the relevant file category for Immediate Change.

To detect Suspected Credential Theft, the PTA compares the login time on the target machine with the last time the password was retrieved from the Vault. By default, the PTA creates a Suspected Credential Theft event if the password was not retrieved within the last 8 hours. For this lab, we have configured the PTA to raise an alert if the password was not retrieved within the last 2 minutes.

### Suspicious Password Change and Automatic Reconciliation

In this section you will configure the PTA to detect when a password is being changed manually, bypassing the CPM, and have the PTA trigger the CPM to reconcile the password. For this exercise to work, you must associate a reconcile account with root02.

1. Login to the PVWA as Paul and go to Accounts -> Accounts View and select the root02 account. Click on Details then in reconcile account, click the […] then Link.
2. Select root01 as the reconcile account and click OK to link the account
3. Go to Accounts -> Accounts View and select root02 again and launch an SSH connection via the PSM. 
4. Type the following command to change the password of root02 back to Cyberak1 
5. Go back to the PVWA as mike and go to Security -> Security Events. You should be able to see two new alerts. One for a “Suspicious activities detected in a privileged session”, and one for “Suspicious password change”. Verify that you can see the “Suspicious password change” alert and that an automatic password reconciliation was initiated.
6. Go to Accounts -> Accounts View and select root02. Verify that root02 has been reconciled by the CPM.

### Suspicious Activities in a Session and Automatic Suspension

In this section you will configure the PTA to detect when a risky command is used in a privileged session and to suspend the session automatically. 
1. Login to the PVWA as mike and go to Security -> Security Configurations -> Privileged Session Analysis and Response. Find the SSH passwd command (the command is used to change the password manually) and click on Edit.
2. Configure the risk to a Score of 90 and the Session response to Suspend. Click on Save.
3. Log in to the PVWA as Paul and go to Accounts -> Accounts View and select the root02 account. Launch a privileged session by clicking on the connect button. 
4. After the session opens, try to run the passwd root02 command again. The session should be suspended immediately, and a message should appear letting the user know the session is suspended.
5. Login to the PVWA as Mike. Go to Security -> Security Events and verify you can see the “Suspicious activities detected in a privileged session” alert. Verify that the session got a score of 90. 
6. Login to the PVWA as Cindy (our auditor) and go to the Monitoring pane. You will see Paul’s connection in Active Sessions with the options to Terminate, Suspend, Resume, or Monitor the session. If you had already closed the session, you would be able to play the recording.

### Security Rules Exceptions

In this section, we will tweak the rule we created in the last section so that if a designated user needs to execute passwd during a session, their session will not be suspended out. 
1. Log into the PVWA as mike and go back to Security -> Security Configurations, select the passwd rule and click the Edit button. 
2. To create an exception to the rule, click on Change scope.
3. Enter the username Paul in the field, hit Enter, and then click the Change Scope button. You will then be returned to Edit Rule dialogue. Click Save to close the dialogue.
4. To test the rule, you can log in to the PVWA as the user Paul, connect using any of the accounts in the Lin-Fin-US safe, and run the passwd command. Your session should not be suspended. Try the same with Carlos. This time your session should be suspended as before.

![[linux-pta.svg]]