---
aliases: 
tags: 
date created: Tuesday, September 19th 2023, 3:32:36 pm
date modified: Tuesday, September 19th 2023, 3:35:14 pm
---

## **For Version 12.1.0 or below**

  
**1.** On the PVWA Server, stop IIS  
![pvwacredfiles1.png](https://cyberark.my.site.com/servlet/rtaImage?eid=ka32J000000LVVv&feoid=00N2J000009R3kg&refid=0EM2J000002iLFZ)  
  
**2.** Logon to PrivateArk Client as “Administrator” or any other user with “Manage Users” privileges in the root location.  
![pvwacredfiles2.png](https://cyberark.my.site.com/servlet/rtaImage?eid=ka32J000000LVVv&feoid=00N2J000009R3kg&refid=0EM2J000002iLFe)  
**3.** Go to Menu “Tools-Administrative Tools-Users and Groups”  
![pvwacredfiles3.png](https://cyberark.my.site.com/servlet/rtaImage?eid=ka32J000000LVVv&feoid=00N2J000009R3kg&refid=0EM2J000002iLFj)  
  
**4.** Select “PVWAAppUser” and click “Update”. (Note: Make sure you select the right PVWAAppUser. Be careful if you have more than one PVWAAppUser, e.g. PVWAAppUser1 and select the correct one by checking C:\CyberArk\Password Vault Web Access\credfiles > appuser.ini and gwuser.ini!)  
![pvwaobfuscated1.png](https://cyberark.my.site.com/servlet/rtaImage?eid=ka32J000000LVVv&feoid=00N2J000009R3kg&refid=0EM2J000002iMg7)  
  
**5.** In the “Authentication Tab” specify a new, random password in the “Password” field, repeat it and click “OK”.  
![pvwacredfiles5.png](https://cyberark.my.site.com/servlet/rtaImage?eid=ka32J000000LVVv&feoid=00N2J000009R3kg&refid=0EM2J000002iLEc)  
  
**6.** Click "Trusted Net Areas" button and make sure "State" is set to "Active". If it is set to "Inactive" click "Activate" to change the state to active. Remember / write down the password set as it will be needed in a later step.  
![pvwacredfiles6.png](https://cyberark.my.site.com/servlet/rtaImage?eid=ka32J000000LVVv&feoid=00N2J000009R3kg&refid=0EM2J000002iLGD)  
  
**7.** Select “PVWAGWUser” and click “Update”.  
(Note: Make sure you select the right PVWAGWUser. Be careful if you have more than one PVWAGWUser, e.g. PVWAGWUser1 and select the correct one!)  
![pvwaobfuscated2.png](https://cyberark.my.site.com/servlet/rtaImage?eid=ka32J000000LVVv&feoid=00N2J000009R3kg&refid=0EM2J000002iMgC)  
**8.** In the “Authentication Tab” specify a new, random password in the “Password” field, repeat it and click “OK”.  
![pvwacredfiles8.png](https://cyberark.my.site.com/servlet/rtaImage?eid=ka32J000000LVVv&feoid=00N2J000009R3kg&refid=0EM2J000002iLGN)

## **9.** Click "Trusted Net Areas" Button and Make Sure "State" is Set to "Active". If it is Set to "Inactive" Click "Activate" to Change the State to Active. Remember / Write down the Password Set as it Will Be Needed in a Later Step.

![pvwacredfiles9.png](https://cyberark.my.site.com/servlet/rtaImage?eid=ka32J000000LVVv&feoid=00N2J000009R3kg&refid=0EM2J000002iLGc)  
  
**10.** On the PVWA Server, open an administrative command line and go to “C:\CyberArk\Password Vault Web Access\Env”.  
![pvwacredfiles10.png](https://cyberark.my.site.com/servlet/rtaImage?eid=ka32J000000LVVv&feoid=00N2J000009R3kg&refid=0EM2J000002iLGh)  
  
**11.** Run “CreateCredFile.exe **appuser.ini**”  
  
**12.** When prompted enter the following information:  
![pvwacredfiles12.png](https://cyberark.my.site.com/servlet/rtaImage?eid=ka32J000000LVVv&feoid=00N2J000009R3kg&refid=0EM2J000002iLGr)  
  
**13.** Run “CreateCredFile.exe **gwuser.ini**”  
  
**14.** When prompted enter the following information:  
![pvwacredfiles14.png](https://cyberark.my.site.com/servlet/rtaImage?eid=ka32J000000LVVv&feoid=00N2J000009R3kg&refid=0EM2J000002iLGw)  
  
**15.** Move the newly created “appuser.ini” and “gwuser.ini” to “C:\CyberArk\Password Vault Web Access\CredFiles”  
![pvwacredfiles151.png](https://cyberark.my.site.com/servlet/rtaImage?eid=ka32J000000LVVv&feoid=00N2J000009R3kg&refid=0EM2J000002iLH1)  
![pvwacredfiles152.png](https://cyberark.my.site.com/servlet/rtaImage?eid=ka32J000000LVVv&feoid=00N2J000009R3kg&refid=0EM2J000002iLHa)  
**16.** Make sure to grant "Modify" permissions to user "Network Service" on “appuser.ini” and “gwuser.ini” using Windows Explorer.  
  
**17.** Start IIS (and its dependent services) on the PVWA machine.  
![pvwacredfiles17.png](https://cyberark.my.site.com/servlet/rtaImage?eid=ka32J000000LVVv&feoid=00N2J000009R3kg&refid=0EM2J000002iLHf)  
  
**18.** Make sure you can access the PVWA using your web browser.  
![pvwacredfiles18.png](https://cyberark.my.site.com/servlet/rtaImage?eid=ka32J000000LVVv&feoid=00N2J000009R3kg&refid=0EM2J000002iLHk)  
  
_Note_: The passwords for these users are automatically changed by the application in the Vault and the credential files are automatically updated with the new passwords each time they change.

## PSM - How Can I Create or Update the Credential Files (credfile) for the PSM Manually? (12.1 AND HIGHER)

**IMPORTANT NOTE: The credfile process has changed in version 12.1. If you are on version 12.0 or below, please use directions from** [**this article**](https://cyberark-customers.force.com/s/article/PSM-update-credential-files)  **instead. DO NOT use this article.**  
 

To determine your version, run the following command. The following output indicates version 12.1 or higher:

![image.png](https://cyberark.my.site.com/servlet/rtaImage?eid=ka32J000000538F&feoid=00N2J000009R3kv&refid=0EM2J000002jtrY)

Versions under 12.1 print the following with a version below 12.1:  
![image.png](https://cyberark.my.site.com/servlet/rtaImage?eid=ka32J000000538F&feoid=00N2J000009R3kv&refid=0EM2J000002jttA)

In order to do this, run the createcredfile utility on the PSM machine as follows:

**1.** Stop the PSM service via the Windows services console  
![psmcredfile1.png](https://cyberark.my.site.com/servlet/rtaImage?eid=ka32J000000538F&feoid=00N2J000009R3kv&refid=0EM2J000002iOZ3)

**2.** Logon to PrivateArk Client as “Administrator” or any other user with “Manage Users” privileges in the root location.  
![psmcredfile2.jpg](https://cyberark.my.site.com/servlet/rtaImage?eid=ka32J000000538F&feoid=00N2J000009R3kv&refid=0EM2J000002iOZD)  
**3.** Go to Menu “Tools-Administrative Tools-Users and Groups”  
![psmcredfile3.jpg](https://cyberark.my.site.com/servlet/rtaImage?eid=ka32J000000538F&feoid=00N2J000009R3kv&refid=0EM2J000002iOZI)  
**4.** Select “PSMApp_xxx” and click “Update”. (Note: Make sure you select the right PSMAppUser. Be careful if you have more than one PSM! If there is more than one, you can check the credfile locations from the file location in step 10)  
![psmcredfile4.jpg](https://cyberark.my.site.com/servlet/rtaImage?eid=ka32J000000538F&feoid=00N2J000009R3kv&refid=0EM2J000002iOZS)  
**5.** In the “Authentication" tab, specify a new, random password in the “Password” field, repeat it and click “OK”. Remember / write down the password set as it will be needed in a later step.  
![psmcredfile5.jpg](https://cyberark.my.site.com/servlet/rtaImage?eid=ka32J000000538F&feoid=00N2J000009R3kv&refid=0EM2J000002iOZX)  
**NOTE**: Ensure that "Password Never Expires" is checked.

**6.** Click "Trusted Net Areas" button and make sure "State" is set to "Active". If it is set to "Inactive" click "Activate" to change the state to active.  
![psmcredfile6.jpg](https://cyberark.my.site.com/servlet/rtaImage?eid=ka32J000000538F&feoid=00N2J000009R3kv&refid=0EM2J000002iOZc)  
**7.** Select “PSMGW_xxx” and click “Update”. (Note: Make sure you select the right PSMgwuser. Be careful if you have more than one PSM! If there is more than one, you can check the user.ini from the file location in step 10)  
![psmcredfile7.jpg](https://cyberark.my.site.com/servlet/rtaImage?eid=ka32J000000538F&feoid=00N2J000009R3kv&refid=0EM2J000002iOZh)  
**8.** In the “Authentication" tab, specify a new, random password in the “Password” field, repeat it and click “OK”. Remember / write down the password set as it will be needed in a later step.  
![psmcredfile5.jpg](https://cyberark.my.site.com/servlet/rtaImage?eid=ka32J000000538F&feoid=00N2J000009R3kv&refid=0EM2J000002iOa1)  
**NOTE**: Ensure that "Password Never Expires" is checked.  
  
**9.** Click "Trusted Net Areas" button and make sure "State" is set to "Active". If it is set to "Inactive" click "Activate" to change the state to active.  
![psmcredfile6.jpg](https://cyberark.my.site.com/servlet/rtaImage?eid=ka32J000000538F&feoid=00N2J000009R3kv&refid=0EM2J000002iOa6)  
  
**10.** On the PSM Server, open an administrative command line and go to “<Drive>:\Program Files (x86)\CyberArk\PSM\Vault”  
![psmcredfile10.jpg](https://cyberark.my.site.com/servlet/rtaImage?eid=ka32J000000538F&feoid=00N2J000009R3kv&refid=0EM2J000002iOaQ)  
  
**11.** Run the following command:

CreateCredFile.exe psmapp.cred Password /Username {username} /Password {password} /AppType PSMApp /DPAPIMachineProtection /EntropyFile /ExePath "{capsm.exe file path}"

  
The output will look like this:  
  
![](https://cyberark.my.site.com/servlet/rtaImage?eid=ka32J000000538F&feoid=00N2J000009R3kv&refid=0EM2J000002jvh0)  
  
  
**12.** Run the following command:

CreateCredFile.exe psmgw.cred Password /Username {username} /Password {password} /AppType PSMApp /DPAPIMachineProtection /EntropyFile /ExePath "{capsm.exe file path}"

The output will look like this:  
  
![](https://cyberark.my.site.com/servlet/rtaImage?eid=ka32J000000538F&feoid=00N2J000009R3kv&refid=0EM2J000002jvhz)  
  
**13.** Start the PSM service. If the service starts, we can assume the process completed successfully as the PSM will not start with a bad credfile.  
![psmcredfile14.jpg](https://cyberark.my.site.com/servlet/rtaImage?eid=ka32J000000538F&feoid=00N2J000009R3kv&refid=0EM2J000002iOb4)