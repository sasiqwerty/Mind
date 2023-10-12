---
aliases: 
tags: 
date created: Friday, August 11th 2023, 12:33:47 pm
date modified: Monday, October 9th 2023, 9:41:37 pm
---
[[Password Vault Web Access]]  
logging in as [[Administrator]]  
monitor group


what are the groups in [[Vault]] 

- To get reports tab in [[Password Vault Web Access]] we should be a part of PVWAMonitor group in [[CyberArk]]
- The master user cannot login in other servers that don't have the vault installed.
- as the dbparm.ini file has the recovery private key location in the vault so that's why its not allowing the user to login elsewhere #doubt 

## Do This Exercise

### Create a New account in Components Server

assign the newly created account to different [[Groups and Users in PrivateArk]] and see how [[Password Vault Web Access]] interface reacts to these changes and document them

### Open Any Recording and See the Tabs Displayed in the [[PrivateArk Client]].

![[add-safe-member-authorizations.png]]

<iframe style="border:none" width="800" height="450" src="https://whimsical.com/embed/CqEyvhUwTj9iX4om7MyiBk"></iframe>
