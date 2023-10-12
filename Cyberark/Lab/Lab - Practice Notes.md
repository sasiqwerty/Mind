---
aliases: 
tags: 
date created: Monday, August 7th 2023, 2:23:14 pm
date modified: Monday, August 7th 2023, 5:42:51 pm
---

## Lab Learning

### User Management

#### Know the Players

| Username           | Auth Method | CyberArk Role         | LDAP Group             |
|--------------------|-------------|-----------------------|------------------------|
| Administrator      | CYBERARK    | Vault Admin           |                        |
| Master             | CYBERARK    | Master User           |                        |
| CyberArk Team (AD) |             |                       |                        |
| Mike               | LDAP        | Vault Admin           | CyberArk Vault Admins  |
| Cindy              | LDAP        | Auditor               | CyberArk Auditors      |
| Dexter             | LDAP        | User Manager (custom) | CyberArk Help Desk     |
| Linux Team         |             |                       |                        |
| Paul               | LDAP        | Safe Manager          | CyberArk Safe Managers |
| Carlos             | LDAP        | User                  | LinuxAdmins            |
| Windows Team       |             |                       |                        |
| Tom                | LDAP        | Safe Manager          | CyberArk Safe Managers |
| John               | LDAP        | User                  | WindowsAdmins          |
| Oracle Team        |             |                       |                        |
| Robert             | LDAP        | Safe Manager          | CyberArk Safe Managers |

#### [[LDAP Integration]]

#### Unsuspend a User

- Open the [[PrivateArk Client]]
- Tools > Administrative Tools > Users and Groups  
![[Pasted image 20230807144439.png]]
- Locate the User
- Trusted Net Areas > Activate (to unsuspend the user)  
![[Pasted image 20230807144539.png]]

#### Login with Master

- On the vault server open the ```C:\Program Files (x86)\PrivateArk\Server\Conf\dbparm.ini
- The RecoveryPrvKey ```RecoveryPrvKey=”C:\CYBR_Files\Keys\Master CD\recprv.key”
- 