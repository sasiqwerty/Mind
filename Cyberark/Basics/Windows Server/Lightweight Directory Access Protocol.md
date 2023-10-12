---
aliases: LDAP, Lightweight Directory Access Protocol
tags: concept
---
#learn
### What is LDAP (Lightweight Directory Access Protocol)?

LDAP (Lightweight Directory Access Protocol) is a software [protocol](https://www.techtarget.com/searchnetworking/definition/protocol) for enabling anyone to locate data about organizations, individuals and other resources such as files and devices in a network -- whether on the public internet or a corporate [intranet](https://www.techtarget.com/whatis/definition/intranet). LDAP is a "lightweight" version of Directory Access Protocol (DAP), which is part of X.500, a standard for directory services in a network. LDAP is considered lightweight because it uses a smaller amount of code than other protocols.

A directory tells the user where in the network something is located. On [TCP/IP](https://www.techtarget.com/searchnetworking/definition/TCP-IP) networks -- including the internet -- the domain name system ([DNS](https://www.techtarget.com/searchnetworking/definition/domain-name-system)) is the directory system used to relate the domain name to a specific network address, which is a unique location on the network. However, the user may not know the domain name. LDAP allows a user to search for an individual without knowing where they're located, although additional information will help with the search.

### Uses of LDAP

The most common use of LDAP is to provide a central place for authentication, meaning it stores usernames and passwords. LDAP can then be used in different applications or services to validate users with a plugin. For example, LDAP can be used to validate usernames and passwords with [Docker](https://www.techtarget.com/searchitoperations/definition/Docker-image), [Jenkins](https://www.techtarget.com/searchsoftwarequality/definition/Jenkins), [Kubernetes](https://www.techtarget.com/searchitoperations/definition/Google-Kubernetes), OpenVPN and Linux Samba servers. System administrators can also use LDAP single sign-on to control access to an LDAP database.

LDAP can also be used to add operations into a directory server database, authenticate -- or "bind" -- sessions, delete LDAP entries, search and compare entries using different commands, modify existing entries, extend entries, abandon requests or unbind operations.

LDAP is used in Microsoft's [Active Directory](https://www.techtarget.com/searchwindowsserver/definition/Active-Directory) but can also be used in other tools such as OpenLDAP, Red Hat Directory Server and IBM Security Directory Server for example. OpenLDAP is an open source LDAP application. It is a Windows LDAP client and admin tool developed for LDAP database control. This tool should enable users to browse, look up, remove, create and change data that appears on an LDAP server. OpenLDAP also lets users manage passwords and browse by schema.

Red Hat Directory Server is a tool used to manage multiple systems with an LDAP server in a UNIX environment. Red Hat Directory Server enables users to store user details in the server. The tool also provides users with secure and restricted access to directory data, group membership and remote access, as well as access via validation procedures.

IBM Security Directory Server is an IBM-based implementation of LDAP. This tool focuses on faster development and distribution of identity control, security and web applications. Security Directory Server includes different validation methods such as validation via digital certificate, Simple Authentication and Security Layer (SASL) and CRAM-MD5.

If an organization is having trouble deciding when to use LDAP, they should consider it in use cases such as the following:

- a single piece of data needs to be found and accessed regularly;
- the organization has a lot of smaller data entries; or
- the organization wants all smaller pieces of data in one centralized location, and there doesn't need to be an extreme amount of organization between the data.

### Levels of LDAP Directory

An LDAP configuration is organized in a simple "tree" hierarchy consisting of the following levels:

- The root directory, which branches out to:
- Countries, each of which branches out to:
- Organizations, which branch out to:
- Organizational units -- divisions, departments and so forth -- which branches out to:
- Individuals, which includes people, files and shared resources such as printers.

An LDAP directory can be distributed among many servers. Each server can have a replicated version of the total directory that is synchronized periodically. An LDAP server is called a Directory System Agent (DSA). An LDAP server that receives a request from a user takes responsibility for the request, passing it to other DSAs as necessary while ensuring a single coordinated response for the user.

### LDAP and Active Directory

Lightweight Directory Access Protocol is the protocol that [Exchange Server](https://www.techtarget.com/searchwindowsserver/definition/Microsoft-Exchange-Server) uses to communicate with Active Directory. To really understand what LDAP is and what it does, it is important to understand the basic concept behind Active Directory as it relates to Exchange.

Active Directory is a directory service for managing domains, users and distributed resources such as objects for Windows operating systems. A directory service manages domains and objects while controlling which users have access to each resource. Active Directory is available on Windows Server 2022 and is comprised of multiple services. Services included in Active Directory are Domain, Lightweight Directory, Certificate, Federation and Rights Management services. Each service is included under the Active Directory name to expand directory management capabilities. Active Directory was first previewed in 1999 and has continued to receive updates since then -- including an update with Windows Server 2016 that improved secure Active Directory environments and the ability to migrate Active Directory environments to cloud or hybrid cloud environments.

Active Directory contains information regarding every user account on an entire network. It treats each user account as an object. Each user object also has multiple attributes. An example of an attribute is the user's first name, last name or e-mail address. All this information exists within a huge, cryptic database on a domain controller -- Active Directory. The challenge is to extract information in a usable format. This is LDAP's main job.

LDAP uses a relatively simple, string-based query to extract information from Active Directory. LDAP can store and extract objects such as usernames and passwords in Active Directory and share that object data throughout a network. The nice part is that this all happens behind the scenes. A regular end user will never have to manually perform an LDAP query because Outlook is LDAP-enabled and knows how to perform all the necessary queries on its own.


- [Difference between LDAP and OAuth 2 - GeeksforGeeks](https://www.geeksforgeeks.org/difference-between-ldap-and-oauth-2/)
 
## Process

#application 
- LDAP Port Number for the connection is 389
- LDAPS (LDAP over TLS/SSL) Port Number for the connection is 636
- 