---
aliases: 
tags: 
date created: Tuesday, September 19th 2023, 3:36:48 pm
date modified: Tuesday, September 19th 2023, 3:39:20 pm
---

## CPM – How Can I Create or Update the Credential Files (credfile) for the CPM Manually? (12.0 AND BELOW)

**IMPORTANT NOTE: The credfile process has changed in version 12.1. If you are on version 12.1 or higher, please use directions from** [**this article**](https://cyberark-customers.force.com/s/article/CPM-How-can-I-create-or-update-the-credential-files-credfile-for-the-CPM-manually-12-1-AND-HIGHER) **instead. DO NOT use this article.**

To determine your version, run the following command. The following output indicates version 12.1 or higher:

![image.png](https://cyberark.my.site.com/servlet/rtaImage?eid=ka32J000000YUuQ&feoid=00N2J000009R3kg&refid=0EM2J000002jtrY)

Versions under 12.1 print the following with a version below 12.1:  
![image.png](https://cyberark.my.site.com/servlet/rtaImage?eid=ka32J000000YUuQ&feoid=00N2J000009R3kg&refid=0EM2J000002jttA)

  
In order to do this, run the createcredfile utility on the CPM machine as follows:

**1.** Stop the CPM service via the Windows services console  
![cpmcredfile1.png](https://cyberark.my.site.com/servlet/rtaImage?eid=ka32J000000YUuQ&feoid=00N2J000009R3kg&refid=0EM2J000002iMiI)  
  
**2.** Logon to PrivateArk Client as “Administrator” or any other user with “Manage Users” privileges in the root location.  
![cpmcredfile2.jpg](https://cyberark.my.site.com/servlet/rtaImage?eid=ka32J000000YUuQ&feoid=00N2J000009R3kg&refid=0EM2J000002iMiX)  
  
**3.** Go to Menu “Tools-Administrative Tools-Users and Groups”  
![cpmcredfile3.jpg](https://cyberark.my.site.com/servlet/rtaImage?eid=ka32J000000YUuQ&feoid=00N2J000009R3kg&refid=0EM2J000002iMih)  
  
**4.** Select “PasswordManager” and click “Update”. (Note: Make sure you select the right PasswordManager. Be careful if you have more than one CPM! If there is more than one, you can check the user.ini from the file location in step 7)  
![cpmcredfile5.png](https://cyberark.my.site.com/servlet/rtaImage?eid=ka32J000000YUuQ&feoid=00N2J000009R3kg&refid=0EM2J000002iMim)  
  
**5.** In the “Authentication" tab, specify a new, random password in the “Password” field, repeat it and click “OK”.  
![cpmcredfile6.png](https://cyberark.my.site.com/servlet/rtaImage?eid=ka32J000000YUuQ&feoid=00N2J000009R3kg&refid=0EM2J000002iMir)  
  
**6.** Click "Trusted Net Areas" button and make sure "State" is set to "Active". If it is set to "Inactive" click "Activate" to change the state to active. Remember / write down the password set as it will be needed in a later step.  
![cpmcredfile7.png](https://cyberark.my.site.com/servlet/rtaImage?eid=ka32J000000YUuQ&feoid=00N2J000009R3kg&refid=0EM2J000002iMiw)  
  
**7.** On the CPM Server, open an administrative command line and go to “<drive>:\Program Files (x86)\CyberArk\Password Manager\Vault”  
![cpmcredfile8.png](https://cyberark.my.site.com/servlet/rtaImage?eid=ka32J000000YUuQ&feoid=00N2J000009R3kg&refid=0EM2J000002iMj1)  
  
**8.** Run createcredfile.exe user.ini  
  
**9.** When prompted fill out the following information:  
![cpmcredfile9.png](https://cyberark.my.site.com/servlet/rtaImage?eid=ka32J000000YUuQ&feoid=00N2J000009R3kg&refid=0EM2J000002iMj6)  
  
**10.** Start the CPM service through the services console  
![cpmcredfile10.png](https://cyberark.my.site.com/servlet/rtaImage?eid=ka32J000000YUuQ&feoid=00N2J000009R3kg&refid=0EM2J000002iMjG)  
  
**11.** If starting the service succeeds, the credfile was reset correctly as the service will not start without a valid credfile

## CPM – How Can I Create or Update the Credential Files (credfile) for the CPM Manually? (12.1 AND HIGHER)

**IMPORTANT NOTE: The credfile process has changed in version 12.1. If you are on version 12.0 or below, please use directions from** [**this article**](https://cyberark-customers.force.com/s/article/CPM-How-can-I-create-or-update-the-credential-files-credfile-for-the-CPM-manually) **instead. DO NOT use this article.**  
 

To determine your version, run the following command. The following output indicates version 12.1 or higher:

![image.png](https://cyberark.my.site.com/servlet/rtaImage?eid=ka32J000000YUuV&feoid=00N2J000009R3kv&refid=0EM2J000002jtrY)

Versions under 12.1 print the following with a version below 12.1:  
![image.png](https://cyberark.my.site.com/servlet/rtaImage?eid=ka32J000000YUuV&feoid=00N2J000009R3kv&refid=0EM2J000002jttA)

 

In order to do this, run the createcredfile utility on the CPM machine as follows:

**1.** Stop the CPM service via the Windows services console  
![cpmcredfile1.png](https://cyberark.my.site.com/servlet/rtaImage?eid=ka32J000000YUuV&feoid=00N2J000009R3kv&refid=0EM2J000002iMiI)  
  
**2.** Logon to PrivateArk Client as “Administrator” or any other user with “Manage Users” privileges in the root location.  
![cpmcredfile2.jpg](https://cyberark.my.site.com/servlet/rtaImage?eid=ka32J000000YUuV&feoid=00N2J000009R3kv&refid=0EM2J000002iMiX)  
  
**3.** Go to Menu “Tools-Administrative Tools-Users and Groups”  
![cpmcredfile3.jpg](https://cyberark.my.site.com/servlet/rtaImage?eid=ka32J000000YUuV&feoid=00N2J000009R3kv&refid=0EM2J000002iMih)  
  
**4.** Select “PasswordManager” and click “Update”. (Note: Make sure you select the right PasswordManager. Be careful if you have more than one CPM! If there is more than one, you can check the user.ini from the file location in step 7)  
![cpmcredfile5.png](https://cyberark.my.site.com/servlet/rtaImage?eid=ka32J000000YUuV&feoid=00N2J000009R3kv&refid=0EM2J000002iMim)  
  
**5.** In the “Authentication" tab, specify a new, random password in the “Password” field, repeat it and click “OK”.  
![cpmcredfile6.png](https://cyberark.my.site.com/servlet/rtaImage?eid=ka32J000000YUuV&feoid=00N2J000009R3kv&refid=0EM2J000002iMir)  
  
**6.** Click "Trusted Net Areas" button and make sure "State" is set to "Active". If it is set to "Inactive" click "Activate" to change the state to active. Remember / write down the password set as it will be needed in a later step.  
![cpmcredfile7.png](https://cyberark.my.site.com/servlet/rtaImage?eid=ka32J000000YUuV&feoid=00N2J000009R3kv&refid=0EM2J000002iMiw)  
  
**7.** On the CPM Server, open an administrative command line and go to “<drive>:\Program Files (x86)\CyberArk\Password Manager\Vault”  
![cpmcredfile8.png](https://cyberark.my.site.com/servlet/rtaImage?eid=ka32J000000YUuV&feoid=00N2J000009R3kv&refid=0EM2J000002iMj1)  
  
**8.** Run the following command:

CreateCredFile.exe user.ini Password /Username {username} /Password {password} /AppType CPM /EntropyFile /DPAPIMachineProtection

  
  
**9.** The output will look like this:  
![](https://cyberark.my.site.com/servlet/rtaImage?eid=ka32J000000YUuV&feoid=00N2J000009R3kv&refid=0EM2J000002jvhG)  
  
  
**10.** Start the CPM service through the services console  
![cpmcredfile10.png](https://cyberark.my.site.com/servlet/rtaImage?eid=ka32J000000YUuV&feoid=00N2J000009R3kv&refid=0EM2J000002iMjG)  
  
**11.** If starting the service succeeds, the credfile was reset correctly as the service will not start without a valid credfile