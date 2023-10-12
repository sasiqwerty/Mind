---
aliases: 
tags: 
date created: Wednesday, August 16th 2023, 1:18:53 pm
date modified: Thursday, August 17th 2023, 7:58:14 pm
---
What is the function of PTA in [[CyberArk]] ?
- [[Cyberark/PTA/Privileged Threat Analytics|PTA]] is a component of [[CyberArk]] 
- Within the CyberArk environment, if a hacker obtains access to administrative passwords, they also possess the capability to alter other passwords, amplifying the security vulnerability.
- When utilizing CyberArk's Privileged Threat Analytics, direct access to a computer is prohibited. If such access is detected, it is treated as a potential threat.

## Overview

- What are some suspicious activities that [[Cyberark/PTA/Privileged Threat Analytics|PTA]] will flag?  
![[pta.svg]]  
[[suspicious activities - PTA]] - file location

## Lab Notes Extract

### Privileged Threat Analytics

In this section, we will be looking at the CyberArk Privileged Threat Analytics (PTA) component. Both the target Linux and Windows servers have been configured to forward security information to the PTA. 

#### What Are These Topics with respect to [[Cyberark/PTA/Privileged Threat Analytics]] in [[CyberArk]] and how is it Done?

![[pta-exc-guide.mp3]]
1. **Unmanaged privileged access** : This refers to privileged accounts that are not managed or monitored by a Privileged Access Management (PAM) solution like CyberArk. These accounts can pose a significant security risk as they might be used without oversight.
	1. CyberArk's PTA can detect the use of privileged accounts that are not managed within the CyberArk solution. When such activity is detected, alerts are generated to notify security teams, allowing them to take appropriate action.
2. **Suspected credential theft and automatic password rotation** : Credential theft refers to unauthorized access or theft of privileged account credentials. 
	1. If PTA suspects that credentials have been compromised, it can trigger an automatic password rotation in the CyberArk Vault. This ensures that the potentially compromised credentials are no longer valid, thus preventing unauthorized access.
3. **Suspicious password change and automatic reconciliation** : Sometimes, privileged account passwords might be changed outside of the PAM system, either accidentally or maliciously.
	1. If PTA detects a password change that wasn't initiated through CyberArk, it can automatically reconcile the password. This means CyberArk will update its vault with the new password, ensuring that the PAM system always has the current, valid password for managed accounts.
4. **Suspicious activities in a session and automatic suspension** : This refers to monitoring active sessions for suspicious activities, such as unusual commands or actions that deviate from typical user behavior.
	1. PTA continuously monitors active sessions for anomalies. If suspicious activity is detected, PTA can automatically suspend or terminate the session, preventing potential malicious actions. Security teams are then alerted to review the session.
5. **Security rules exceptions** : In the context of PTA, this refers to exceptions or deviations from predefined security rules or policies.
	1. PTA allows administrators to define specific security rules and policies for privileged account usage. If any activity deviates from these rules, PTA will generate alerts. This helps in identifying potential policy violations or malicious activities.

![[mermaid-diagram-2023-08-16-175249.svg]]

![[pta-cyb-combo.svg]]  
Lab Work starts  

- Creating a root user in Linux
- how to trigger a pta event
- how to use [[PuTTY]] 
1. Accounts must pre-exist on the server for PTA to function.
2. If email integration is set up, PTA sends alerts to the configured email.
3. Continuous connection to the same account without CyberArk may trigger concerns.
4. By default, PTA doesn't monitor connection activities directly.
5. In testing environments, PTA configurations are adaptive to specific needs and use cases.
6. Accounts with passwords outside the vault are termed as "unmanaged Privileged Accounts."
7. PTA monitors for potential credential theft.
8. PTA users are added at the safe level, monitoring anomalies like unexpected activity. Suspicious behavior prompts password rotation.
9. Configurations are done at the safe level. Accessing a password from the safe is deemed "normal." Any other access method raises flags in PTA.

PTAUser - internal User  
CPM will perform the password change activities  
PTAAppUser - another [[Cyberark/PTA/Privileged Threat Analytics|PTA]] [[Users|user]]

create a few Linux accounts in the server and try to login directly without going through [[CyberArk]] , see if [[Cyberark/PTA/Privileged Threat Analytics|PTA]] is flagging it.  
![[Pasted image 20230817163315.png]]  
Remediation - what is it?  
what is a session in context of [[Privileged Session Manager|PSM]] ?  
what is a direct connection?  
In production PTAUser ?  
default user?  
default users of safe?  
adding users to safe - how many ways  
default users and groups in safe - it can be hidden  
![[Pasted image 20230817183038.png]]

automation - adding [[Users]]  
how many safes in a vault - in production ?  
limit for total no of safes - no we don't have a space just have to maintain the hardware for performance  
cloud structure - privileged cloud in AWS  
who maintains the server physically? hardware maintenance  
- teams in production 
	- wintel team
	- AD
	- Database
	- certifications team
	- auditing team
- [[Cyberark/PTA/Privileged Threat Analytics|PTA]] session 2 12 to 13 min mark - what are the functions of a CyberArk admin?
- page 198
- if the password is changed the [[Cyberark/PTA/Privileged Threat Analytics|PTA]] will recognize the event and trigger an immediate password [[Reconciliation]].
- what is the use of the health page in [[Password Vault Web Access|PVWA]] 
- risk score for commands (its written in regular expressions ) - security configurations 
- what is SSH ? 
- Change scope - exceptions for a single user
- Unmanaged [[Privileged Account]] - windows after account creation 
- What is the difference between session suspension and session termination?
- Port no 443 - [[Password Vault Web Access|PVWA]] between [[CPM]] 
- ![[Pasted image 20230817194936.png]]
- ![[Pasted image 20230817194951.png]]
- there wont be a direct connection between [[Password Vault Web Access|PVWA]] and target server as the [[Password Vault Web Access|PVWA]] is just the extended interface of the vault, CPM and PSM.
- The same logic applies to the [[PrivateArk Client]] and target servers there wont be a direct connection but the 
- all the components will communicate with the vault with 1858
	- the [[Password Vault Web Access|PVWA]] 
	- the [[CPM]] 
	- the [[Privileged Session Manager|PSM]] 
- while the [[CPM]] connects with 135 or 139 to the [[Target Server]] 
- the [[Privileged Session Manager|PSM]] connects to windows servers with the 3389 [[Ports]] 
- the [[Privileged Session Manager|PSM]] connects to Linux servers with the 22 [[Ports]] 
- the [[Privileged Session Manager|PSM]] connects to oracle servers with the 1521 [[Ports]] 
- [[Password Vault Web Access|PVWA]] communicates with the [[CPM]] with 443 port
- the [[Password Vault Web Access|PVWA]] communicates with the [[Privileged Session Manager|PSM]] 443 port
- [[Password Vault Web Access|PVWA]] communicates with the [[Cyberark/PTA/Privileged Threat Analytics|PTA]] with 443 [[Ports]] 
- ![[Pasted image 20230817195714.png]]
- what is EPM? End point privilege manger 
- ![[Pasted image 20230817195901.png]]
- ![[Pasted image 20230817200008.png]]