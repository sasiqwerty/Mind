---
aliases: 
tags: 
date created: Friday, August 18th 2023, 3:54:36 pm
date modified: Friday, August 18th 2023, 4:01:42 pm
---

## CPM Service Operational but Not Reflecting Policy Updates in PM Console

#real-world-CybArk-Problem

### CPM Service Operational but Not Reflecting Policy Updates in PM Console

Has Anyone Encountered a Scenario where the CPM (Central Policy Manager) Services Are Operational, but there Are no Policy Updates Reflected in the PM (Policy Manager) Console Logs, Resulting in Halted Password Management Processes?

Asked on 18-08-23 Friday by +65 9112 2134 (Onkar in #CyberArkLearning)  

**Suggested Solution:**
1. **Service Verification**: Firstly, ensure that all related services, not just the CPM, are running correctly. Sometimes, services appear to be running, but they might not be functional.
  
2. **Logs Examination**: Examine logs other than just the PM console logs. There might be related logs that can give more insight into any underlying issues.

3. **Connectivity Issues**: Ensure that there are no network or connectivity issues between the CPM and any dependent systems or databases.

4. **Policy Version Check**: Make sure that you're working with the latest and compatible policy version. Sometimes, older or mismatched policy versions can cause update issues.

5. **Manual Update Trigger**: Try to manually trigger a policy update from the PM console. This can help in identifying if the issue is with automatic updates or if the system itself is unable to fetch updates.

6. **Check Disk Space**: Ensure there's sufficient disk space on the server where the CPM and PM are hosted. Lack of space can often lead to unexpected behavior.

7. **User Privileges**: Ensure that the CPM service account has the necessary privileges to make updates to the policy manager. Sometimes, permissions can get inadvertently modified, leading to such issues.

8. **Software Patches and Updates**: Make sure that your software is updated to the latest version. Manufacturers often release patches to resolve known bugs.

9. **Contact Support**: If you're still facing the issue after trying the above solutions, it might be a good idea to contact the software vendor's support team, as they might be aware of specific issues or bugs that can cause such behavior.

10. **Backup and Restart**: As a last resort, take a backup of all configurations and consider restarting the CPM services or the entire server. Sometimes, this can resolve issues that arise due to prolonged service runtimes or minor glitches.

### PTA V13.2 Installation: Missing License Prompt and Dashboard Access Issue

After a successful installation of PTA v13.2, there was no prompt for license input upon attempting to log in, and the dashboard was inaccessible. Is this an inherent behavior of version 13.2, or have the license upload and dashboard functionalities been deprecated in this version? Has anyone else faced a similar issue?

Asked on 18-08-23 Friday by +91 80999 92020 (Abhishek D in #CyberArkLearning)  

**Suggested Solution:** 

1. **Documentation Check**: Refer to the official documentation for PTA v13.2. The manufacturer's release notes or user guide might provide information on changes in the version, including removal or modification of the license upload and dashboard features.

2. **License Configuration**: Navigate to the settings or configuration section. Some versions might have moved the license input section from the login to another location within the tool.

3. **Installation Verification**: Ensure that the installation process was completed without any interruptions or errors. It might be worth considering a re-installation after verifying system requirements and compatibility.

4. **Check User Privileges**: Ensure you're logging in with an account that has sufficient privileges. Some functionalities, including the dashboard and licensing, might be restricted to administrative accounts.

5. **Software Patches and Updates**: Look for any patches or updates available for PTA v13.2. Sometimes, initial releases can have minor issues that are resolved in subsequent patches.

6. **User Feedback**: Engage with online forums or communities specific to PTA. Other users might have encountered and resolved similar issues.

7. **Contact Support**: If the issue persists and there's no clear documentation on the changes, contact the software vendor's support team for assistance.

8. **Alternative Versions**: If the functionality has indeed been removed in v13.2 and is crucial for your operations, consider rolling back to a previous version of PTA where these features were available. Always ensure to back up your data and configurations before downgrading.

Remember always to have a backup of your configurations and data before making major changes or updates.