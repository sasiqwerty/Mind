### What is a domain controller?

#watch [Domain controller server - YouTube](https://www.youtube.com/watch?v=xBVauAnUT0s)


A domain controller is a type of server that processes requests for authentication from users within a computer [domain](https://www.techtarget.com/whatis/definition/domain). Domain [controllers](https://www.techtarget.com/whatis/definition/controller) are most commonly used in Windows Active Directory ([AD](https://www.techtarget.com/searchwindowsserver/definition/Active-Directory)) domains but are also used with other types of identity management systems.

Domain controllers duplicate directory service information for their domains, including users, [authentication](https://www.techtarget.com/searchsecurity/definition/authentication) credentials and enterprise [security policies](https://www.techtarget.com/searchsecurity/definition/security-policy).

### What are the main functions of a domain controller?

Domain controllers restrict access to domain resources by authenticating user identity through login credentials, and by preventing unauthorized access to those resources.

Domain controllers apply security policies to requests for access to domain resources. For example, in a [Windows AD domain](https://www.techtarget.com/searchwindowsserver/definition/Active-Directory-domain-AD-domain), the domain controller draws authentication information for user accounts from AD.

A domain controller can operate as a single system, but they are usually implemented in [clusters](https://www.techtarget.com/whatis/definition/cluster) for improved reliability and availability. For domain controllers running under Windows AD, each cluster comprises a primary domain controller (PDC) and one or more backup domain controllers (BDC). In [Unix](https://www.techtarget.com/searchdatacenter/definition/Unix) and [Linux](https://www.techtarget.com/searchdatacenter/definition/Linux-operating-system) environments replica domain controllers copy authentication databases from the primary domain controller.

![[Pasted image 20230727174102.png]]

### Why is a domain controller important?

Domain controllers control all domain access, blocking unauthorized access to domain networks while allowing users access to all authorized directory services.

The domain controller mediates all access to the network, so it is important to protect it with additional security mechanisms such as:

- [firewalls](https://www.techtarget.com/searchsecurity/definition/firewall)
- secured and isolated networks
- security protocols and encryption to protect stored data and data in flight
- restricted use of insecure protocols, such as [remote desktop protocol](https://www.techtarget.com/searchenterprisedesktop/definition/Remote-Desktop-Protocol-RDP), on controllers
- deployment in a physically restricted location for security
- expedited patch and configuration management
- blocking internet access for domain controllers

Domain controllers control all access to computing resources in an organization, so they must be designed to resist attacks and to continue to function under adverse conditions.

### How are domain controllers set up in Active Directory?

Domain control is a function of Microsoft's Active Directory, and domain controllers are servers that can use Active Directory to respond to authentication requests.

Experts advise against relying on a single domain controller, even for smaller organizations. Best practices call for one primary domain controller and at least one backup domain controller to avoid downtime from [system unavailability](https://www.computerweekly.com/feature/Uptime-and-availability-Making-sense-of-supplier-SLAs).

Another best practice is to deploy each domain controller on a standalone physical server. This includes virtual domain controllers, which should be run on virtual machines ([VMs](https://searchservervirtualization.techtarget.com/definition/virtual-machine)) running on different physical hosts.

Domain controllers can be deployed on physical servers, running as VMsor as part of a [cloud directory service](https://www.techtarget.com/searchcloudcomputing/feature/A-cloud-services-cheat-sheet-for-AWS-Azure-and-Google-Cloud).

Steps for setting up an AD domain controller include:

- **Domain assessment.** The first step in setting up a domain controller is to assess the domain in which the controller will be set up. This assessment includes determining what types of domain controllers are needed, where they will be located and how they interoperate with existing systems in the domain.
- **New deployment or addition.** Whether planning for a new deployment of AD domain controllers or adding a new controller for an existing domain, determine the domain controller location and the resources needed to run the centralized domain controller and any virtual domain controllers.
- **Security by design.** It's imperative to secure a domain controller from internal or external attacks. Also, design the domain controller architecture to be secure from service disruptions from loss of connectivity, loss of power or system failures.

Specifics [for setting up](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/install-active-directory-domain-services--level-100-) and configuring AD domain controllers vary depending on the version of [Windows Server](https://www.techtarget.com/searchwindowsserver/definition/Microsoft-Windows-Server-OS-operating-system) in use on the domain.

### Other domain controller implementation options

The following options are available when setting up a domain controller with AD:

- **Domain Name System (**[**DNS**](https://www.techtarget.com/searchnetworking/definition/domain-name-system)**) server:** The domain controller can be configured to function as a DNS server. Dell [recommends](https://www.dell.com/support/kbdoc/en-ca/000128457/best-practices-for-dns-configuration-in-an-active-directory-domain) configuring at least one domain controller as a DNS server.
- **Global Catalog capabilities:** The domain controller can be configured to use Global Catalog, which enables the controller to return AD information about any object in the organization, regardless of whether the object is in the same domain as the domain controller. This is useful for large enterprises with multiple AD domains.
- **Read only domain controller (**RODC**):** Domain controllers used in branch offices or in other circumstances where network connectivity is limited can be configured as read-only.
- **Directory Services Restore Mode (**[**DSRM**](https://searchwindowsserver.techtarget.com/definition/Directory-Services-Restore-Mode-DSRM)**):** DSRM provides the option to do emergency maintenance, including restoring backups, on the domain controller. A DSRM password must be configured in advance.

### What are the benefits of domain controller?

Domain controller benefits include:

- Centralized management of domain controllers enables organizations to authenticate all directory services requests using a centralized domain controller.
- Distributed and replicated domain controllers enforce security policies and prevent unauthorized access across enterprise networks and [WAN](https://www.techtarget.com/searchnetworking/definition/WAN-wide-area-network).
- Access to [file servers](https://www.techtarget.com/searchnetworking/definition/file-server) and other network resources through domain controllers provides seamless integration with directory services such as Microsoft AD.
- Support for secured authentication and transport protocols in domain controllers improves authentication process security.
![[Pasted image 20230727174046.png]]

### What are the limitations of domain controllers?

Some domain controller limitations include:

- Single point of failure for network domain control.
- Because they control access to the entire network, domain controllers are a target for [cyber attack](https://www.techtarget.com/searchsecurity/definition/cyber-attack). Successfully hacking a domain controller could give the attacker access to all domain network resources as well as authentication credentials for all users in the domain.
- Networks that use domain controllers for authentication and access security are dependent on them. To reduce risk of downtime, controllers can be deployed in clusters.
- Domain controllers require additional infrastructure and security mechanisms.

_Domain controllers are fundamental to securing unauthorized access to an organization's domains. Learn how to set up and_ [_deploy a Windows Server 2016 domain controller_](https://www.techtarget.com/searchwindowsserver/answer/How-to-deploy-a-Windows-Server-2016-domain-controller) _securely._