---
aliases: OU
tags: 
date created: Thursday, July 27th 2023, 5:35:43 pm
date modified: Wednesday, August 2nd 2023, 10:47:44 am
---
In Active Directory, an OU (Organizational Unit) is a container that can be used to logically group objects, such as users, groups, computers, and other OUs. OUs are a way to organize your Active Directory environment and to make it easier to manage.

## What is an Organizational Unit in Active Directory?

An OU is a container within a [Microsoft](https://www.techtarget.com/searchwindowsserver/definition/Microsoft) [Windows](https://www.techtarget.com/searchwindowsserver/definition/Windows) Active Directory ([AD](https://www.techtarget.com/searchwindowsserver/definition/Active-Directory)) domain that can hold users, groups and computers. It is the smallest unit to which an administrator can assign [Group Policy](https://www.techtarget.com/searchwindowsserver/definition/Group-Policy) settings or account permissions.

An AD organizational unit can have multiple OUs within it, but all attributes within the containing OU must be unique. Active Directory OUs cannot contain objects from other [domains](https://www.techtarget.com/searchwindowsserver/definition/Active-Directory-domain-AD-domain).

## What is an Organizational Unit Name?

Organizational unit names are administrative names assigned to OUs for easy reference.

## Some Points to Consider

- **Performance:** OUs can have a negative impact on performance if they are not used correctly. For example, if you have a large number of OUs, it can take longer for Active Directory to search for objects.
- **Complexity:** OUs can add complexity to your Active Directory environment. If you are not careful, you can create a complex and confusing Active Directory environment.
