---
aliases: 
tags: 
date created: Tuesday, August 8th 2023, 10:15:04 am
date modified: Tuesday, August 8th 2023, 10:18:06 am
---

## Info from Bard

The "Save account versions from the last X days" option in the Edit Safe feature of CyberArk PVWA determines how many password versions are stored for each account in the safe. By default, the last 7 days of password versions are stored. This means that if you change the password for an account today, you will be able to view the previous 6 password versions in the Safe.

You can change the number of password versions to be stored by entering a different value in the "Save account versions from the last X days" field. For example, if you enter "10", then the last 10 password versions will be stored for each account in the safe.

This feature is useful for auditing purposes. If you need to track changes to passwords, you can view the previous password versions in the Safe. This can be helpful for troubleshooting security incidents or for investigating suspicious activity.

Here are some additional details about the "Save account versions from the last X days" option:

- The number of password versions that are stored is determined by the "PasswordLastVersions" property of the safe. This property can be set when the safe is created or it can be modified later using the Edit Safe feature.
- The password versions are stored in the Vault. This means that they are protected by the same security features as the rest of the data in the Vault.
- The password versions are not deleted automatically. You can manually delete them if you no longer need them.

## Edit Safe - save account Versions from the Last X Days

I think this feature is just for [[Password]]s and has nothing to do with deletions.

### How to Test This Feature?

- Create a windows account and change its password 10 times  
- Change the parameter to 1 day and see how many versions its storing