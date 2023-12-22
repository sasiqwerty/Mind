---
aliases: 
tags: 
date created: Tuesday, December 19th 2023, 1:32:24 pm
date modified: Wednesday, December 20th 2023, 8:25:56 am
---
1. The vault administrator account and the password manager user can be selected for Windows Discovery Process.
2. To rotate all password every 90 days one has to make a change in the master policy.
3. SSH text recorder and Universal Keystrokes Text recorder are the default options a new Linux platform has.
4. EPM is used for managing loosely connected devices.
5. Logon and Reconcile accounts can be linked both at the account level and at the platform level.
6. CPM supports Windows services, Windows Scheduled Tasks and Windows Registry out of box. These are some dependent accounts. 
7. Question : In addition to add accounts and update account contents, which additional permission on the safe is required to add a Single account?  
	1. The correct Option is Update account properties
	2. Keep in mind that account contents and properties are not the same.
8. Question : Which parameters can be used to harden the Credential Files (CredFiles) while using CreateCredFile Utility? (Choose 3 )
	1. The correct options are : OS Username, the Current machine IP address and the current machine hostname (In total this question contains three options )
9. Question : When should vault keys be rotated?
	1. The correct option is when the vault keys are copied to file systems outside the vault.
10. Question : Which statement is true about setting the reconcile account at the platform level?
	1. The correct option is "a rule can be used to specify the reconcile account dynamically or a specific reconcile account can be selected."
11. Question : You have been asked to turn off the time access restrictions for a safe. Where is this setting found?
	1. The correct option is : The setting is found in the PrivateArk Client
12. Question : What are the valid ways to invite vendors using the remote access portal?
	1. The correct options are : By using the vendor invitation form and the self service invitation URL.
13. Match the following Question
	1. The correct options are : PSM SSH is used for UNIX systems, PSM-RDP is used for Windows, PSM-WinSCP is used for NIX file transfer, PSM SQL Plus is used for Databases and finally PSM-OS390 is used for Mainframe.
14. Question : The privileged access management solution provides an out of the box target platform to manage SSH keys and its called UNIX via SSH keys. How are these keys stored?
	1. The correct option is "Cyberark stores private keys in the vault and updates public keys on the target systems."
15. Your Organization has a requirement to allow only one user to "check out passwords" and through PSM securely. What needs to be configured in the master policy to ensure that this will happen?
	1. The correct option is : Enforce Check in/check out exclusive access should be active and the require privileged session monitoring and isolation should be enabled.
16. What can you do to ensure each component server is operational?
	1. We have to use the v10 interface and in the health check page and validate that each server is operational.
17. To use PSM connections while in PVWA, what are the minimum safe permissions a user or a group will need?
	1. List accounts and use accounts permissions.
18. What must you specify when configuring the discovery scan for UNIX?
	1. CPM scanner and list of machines to scan.
19. What are the common causes of installed components to display as disconnected?
	1. Network instability issues and Credential De-sync
20. What does the `minvalidity` parameter on a platform determine?
	1. A time between a password retrieval and the account becoming eligible for password change.
21. What are the tools to identify machines and accounts that create the highest risk and are exposed to lateral movement?
	1. Cyberark DNA report and MAP.
22. Click to connect is not enabled by default. How to active this feature?
	1. Navigate to policies and select master policy. There you will find an option to enable Allow EPV transparent connections.
23. When adding new applications to remote access portal the authentication methods used for PVWA are password and OTP.
24. How to disable session monitoring and recording for a group of accounts?
	1. Navigate to master policy and select session management, add an exception to the platform to disable session monitoring and recording policies.
25. A password compliance audit has found out that for a few domain admin accounts one time password access is not enabled, and the sessions are not recorded. To solve this problem we have to create two exceptions at the master policy to that platform, for exclusive access and recording and monitoring policies.
26. To enable full control over the invitation process, one has to be a vendor manager after being invited to the Remote Access Portal.
27. When running a "Privileged Account Inventory" Report through the reports page in PVWA on a specific safe to show the complete inventory information one has to have list accounts and view safe members permissions.
28. To ensure non-repudiation has to enable exclusive access and one time password in master policy.
29. To identify the most powerful accounts in the organization one has to use Discovery and Audit also called DNA and Privileged Account Matrix (PAM) which is based on XML
30. Accounts that discovered but that are not added to the vault by an automated onboarding rule are added to pending accounts list for review and manual upload.
31. When onboarding an account that is not supported out of the box one has to create a service ticket in the customer portal explaining the requirements.
32. Universal Keystrokes text recorder with windows events text recorder disabled is an option for PSM recording customization.
33. Safe and Platform are the mandatory fields when onboarding pending accounts.
34. To generate an entitlement report one needs to have "manage users" and "Audit Users" permission.
35. The minimum permissions to add multiple accounts from file when using PVWA bulk upload are add accounts, update account content and update account properties.
36. A user needs to view recorded sessions through the PVWA, without giving auditor access one has to have access to the recording safe and the safe the account is in.
37. To view the list of approvers one has to navigate to the PVWA and open the policies page. Access control contains the same and the right safe has to be selected. Later in the safe members option there is an option for workflow here we see who can authorize the password requests.
38. When one does not see the Fast Forward option one has deduce that its a recording for an SSH Session.
39. The HTML5 gateway can be configured in Privileged Session Management found in options.
40. The recovery private key is stored in a physical safe, while the recovery public key is stored in a hardware security module. The server key is stored in the vault disk drive and the SSH keys are stored in the vault.
41. To reduce the possibility of credential theft one has to enable dual control password access approval and one time password option found in the master policy.
42. To achieve identity security success using the CyberArk blueprint, we need to first understand the identity attack chain, then assess the organization's security posture and secure the human identities. 
43. The safe naming convention should combine environments, owners and platforms to minimize the total number of safes created, it has to kept in mind that the safe name cannot exceed more than 28 characters.
44. To configure a logon account for multiple platforms, one has to change this setting at the platform level.
45. To learn more about the CyberArk blueprint we can visit the Blueprint webpage and attend product webinars.
46. To ensure proper connectivity we need to provide the IP or the FQDN of each server and verify that the correct PSM connection component appears within the platform settings.
47. winRC5 error reports a lack of permission to change its own password.
48. The configuration file used by the CPM scanner while scanning Linux devices is UnixPrompts.ini 
49. The privileged accounts compliance status displays the number of days left until a password is due to expire.
50. To duplicate a cyberark platform the easy way is to duplicate it in the PVWA.
51. Export Vault data allows one to create list of master policy settings, owners and safes for output to text file or databases.
52. To enable PSM for all platforms navigate to master policy and enable session management.
53. OBDC is the common interface used for CPM when it connects to a database.
54. The correct way to install a platform is to download it from the cyberark marketplace.
55. To enable cold storage backup solution, we need to install the vault backup utility on a different machine and trigger full backup.
56. To manage automated onboarding rules one has to be a vault admin.
57. New onboarding rules are created in the PVWA, the option is found in accounts > onboarding rules.
58. When onboarding multiple accounts from the pending account list, the platform setting has to be same across all the selected accounts.
59. Exclusive access and one time password setting is good to keep track of who is accessing shared accounts.
60. The PSM setting in master policy related to session monitoring and isolation, Record and save session activity both the settings are to be active.
61. To change the safe where recordings are kept for a specific platform, the SessionRecorderSafe has to be updated.
62. ISS Application Pools can be added as a service account.
63. When an account is unable to change its own password, to ensure password reset Set the parameter ChangePasswordlnResetMode to Yes.
64. to enable password change outside working hours we have to update the password change parameters of the platform to match the permitted time frame.
65. Exclusive access allows only one person to check-out an account at a time. One-time password schedules an account for a password change after the MinValidityPeriod period expires.
66. The account has to be a member of Domain Admin group if configured for windows account discovery. 
67. To view the safe recordings one requires to retrieve and list accounts and view audit, where as the access the without confirmation and create folders are not needed.
68. A new html gateway is deployed in the organization arrange the steps in the right order:
69. In the Administration navigate to Options under options select Privileged Session Management and click on Configured PSM Servers and select existing PSM host you will find Connection Details and the option to add PSM gateway.
70. A reconcile account can be added at the platform and the account level.
71. To view reports page in PVWA one has to be a member of PVWAMonitor group.
72. In the platform policy > Automatic Password Management > Password Change > ToHour & FromHour : this has to be enabled to prevent password change during business hours.