---
aliases: 
tags: 
date created: Tuesday, July 25th 2023, 7:31:32 am
date modified: Sunday, July 30th 2023, 4:29:48 pm
---

## Type 1: Active Directory Objects

Active directory objects represent more prominent actors and resources in the system. These include users, computers, folders, groups, printers, etc.

- **Users**: Users are the individuals or actors who need access to the system resources. The particular details for users are the username and a password for login.
- **Computers**: Computers represent workstations, laptops, desktops or servers, etc.
- **Contacts**: Contacts are the objects that contain information about the third-party actors who do not belong to the system but have a relation with it.
- **Groups**: Groups represent a collection of several objects, including user accounts, computers, or contacts. Groups can be Security groups or Distribution groups, and it allows the configuration of many objects like one single unit.
- **Shared folder**: Shared folders are the objects mapped to a server share, and system users use them to share files throughout the network.
- **Printer**: Printers are also shared over the network for different users.
- **Organizational Unit (OU)**: Organizational units are the objects that act as a container to include objects in the network, including users, computers, or groups. It stores similar objects to represent them as one unit to make applying policies and permissions easily in one go.
- **Domain**: It is like a mini network within a network that shares a common suffix and is under the control of a domain administrator. People can share hardware and software resources over a domain for other users.
- **Print queue**: It represents a series of documents that are in the waiting line for a printer in the domain.
- **Site link**: It represents a hyperlink to subpages in a website. It refers to pages when working on Google listings and site navigation.
- **IP subnet**: It is a subdivision of an IP network that is logically visible. IP subnetting allows the division of networks in more than one network.
- **Server**: The server is the big boss in the network that manages the entire network and decides access to resources and rights of the user.
- **Directory connector**: The directory connector supports integrating functionality with the Active Directory.

## Type 2: Active Directory Sites and Services

Active Directory Sites and services represent different aspects of activity directory resources. These resources include domain controllers, clients, databases and WAN, etc.

- **Domain controller**: It is a logical server responsible for permissions and management of access to domain resources. It is a Microsoft Windows or Windows NT network term.
- **Client**: The client is a device that obtains information and applications from a server.
- **Contacts**: Contacts are the objects that contain information about the third-party actors who do not belong to the system but have a relation with it.
- **Database**: A database is a record-saving resource or a structured set of data stored in a computer device.
- **WAN**: Wide area network, i.e., WAN is a geographically dispersed telecommunications network.

### Type 3: Exchange Objects

Exchange objects include all the messages and relevant virtual resources that pass between users, servers, and clients. Let us list and explain these active directory icons and symbols.

- **Exchange Organization**: The Exchange organization object determines how servers communicate with one another.
- **Message Format**: It contains predetermined fields in the message.
- **Exchange Server**: Exchange Server is a significant resource of the messaging service in most networks, working in synchronization with Active Directory.
- **Public Folder**: Public folders have shared resources over a domain for users to access information. Public folders can be structured hierarchically and are connected with a shared folder database.
- **Storage Group**: Storage groups represent different storage classes available in your network.
- **Recipient Policy**: Recipient Policies are the objects in which Windows Active Directory and Exchange 2003 employ LDAP to control the output.
- **POP Virtual Server**: A POP Server is a server that implements Post Office Protocol (POP) to retrieve messages.
- **IMAP Virtual**: Internet Message Access Protocol

## Links

[What is Active Directory (AD)? (techtarget.com)](https://www.techtarget.com/searchwindowsserver/definition/Active-Directory#:~:text=Active%20Directory%20stores%20data%20as,such%20as%20users%20or%20groups.)  
[Active Directory Icons & Symbols | EdrawMax (edrawsoft.com)](https://www.edrawsoft.com/active-directory-symbols.html)

## CyberArk Process Related Stuff

#important #application  

### Password Change

Accounts have been onboarded through LDAP Integration cannot have their passwords changed by the [[Vault|vault]] user or the [[Password Vault Web Access|PVWA]] user because they are not part of the [[CyberArk]] infrastructure. The password is only changed at the [[Active Directory|AD]] side of things.