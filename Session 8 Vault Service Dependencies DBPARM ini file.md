---
aliases: 
tags: 
date created: Wednesday, October 4th 2023, 5:05:48 pm
date modified: Wednesday, October 4th 2023, 9:23:11 pm
---

## Dependencies

| Service                                     | Depends on (This service depends on the following system component)                                                      |
|----------------------------------------------|-----------------------------------------------------------------|
| CyberArk Logic Container                     | HTTP Service, PrivateArk Database                               |
| PrivateArk Remote Control Agent              | NA                                                              |
| PrivateArk DataBase                          | NA                                                              |
| CyberArk Hardened Windows Firewall           | Base Filtering Engine, Windows Firewall Authorization Driver   |
| CyberArk Event Notification Engine           | PrivateArk Server                                          |
| PrivateArk Server                            | CyberArk Logic Container                                        |

1. **CyberArk Logic Container**
    - This service forms the core logic for certain CyberArk operations.
    - It **depends on**:
        - HTTP Service: Likely to facilitate web-based requests and operations.
        - PrivateArk Database: Probably where essential data is stored and from where the logic container fetches necessary information.
2. **PrivateArk Remote Control Agent** and **PrivateArk DataBase**
    - These do not depend on any other mentioned services and operate independently, hence marked as "NA".
3. **CyberArk Hardened Windows Firewall**
    - As a protective measure, it **depends on**:
        - Base Filtering Engine: The service that implements the user-mode filtering platform in Windows.
        - Windows Firewall Authorization Driver: This is a kernel-mode driver that processes all incoming and most outgoing traffic for the system.
4. **CyberArk Event Notification Engine**
    - This service likely informs or updates users or other components about specific events or changes.
    - It **depends on** the PrivateArk Server, suggesting that the event notification directly interacts or pulls data from this server.
5. **PrivateArk Server**
    - Serves as a central hub for certain CyberArk functions.
    - It **depends on** the CyberArk Logic Container, implying that the server utilizes the logic container for various operations or decision-making processes.

These relationships suggest a hierarchical system where some services serve as foundational elements (like the PrivateArk Database or CyberArk Logic Container), while others operate at higher levels, relying on the foundational elements for their operations (like the CyberArk Event Notification Engine relying on PrivateArk Server).

## dbparm.ini Configuration Guide

The `dbparm.ini` configuration file plays a crucial role in the initialization of the vault. This guide provides a concise understanding of its significance and relevant parameters.

### Initialization

1. **File Reading**: The vault reads the `dbparm.ini` configuration file upon start-up; any misconfiguration prevents the vault from starting.
2. **Operator CD**: Contains the essential server key for vault operation.
3. **Server Key Integration**: The server key from the Operator CD is loaded into the vault server's memory for successful initialization.
4. **Key Validity & Path Specification**: The server key must be valid, and its path explicitly mentioned in the configuration.

### Task Count Configuration

1. **Definition**: Task Count denotes the vault's capacity to handle simultaneous transactions.
2. **Default Setting**: The pre-set value for task count is 20.
3. **Performance Analysis**: Using the `PASreporter TOOL`, CyberArk reviews and recommends a specific task count value.
4. **Modification Implication**: Altering the task count necessitates adjusting the `maxtaskallocation` parameter based on needs.

## Other Parameters

1. **Entropy File**: Sourced from the operator CD and utilized in the construction of the vault database.
2. **DatabaseConnectionPasswordFile**: An internal password file that grants access to the vault.
3. **ServerCertificateFile**: Initially employs a self-signed certificate, which is eventually replaced with a CA certificate.
4. **AutoClearSafeHistory & AutoClearUserHistory**: Managed by a batch user, this function clears history logs for safes and user sessions.
5. **VaultID**: A unique hexadecimal ID located within the `dbparm.ini` file.
6. **AutosyncExternalObjects**: Enables synchronization with LDAP and other external directories.
7. **VaultDebugLevel**: A flexible setting that adjusts the debug level, permitting increases or decreases as necessary.
8. **DefaultTimeOut**: Establishes the default idle duration after which a user session concludes.
9. **AutomaticallyAddBuiltInGroups**: When safes are generated, certain users are inherently added based on this setting.
10. **LicenseUsageAlert**: Displays remaining license time, with alerts shown in server central administration.
11. **ComponentNotificationThreshold**: Monitors component usage and activates an alert when surpassing a predetermined threshold.
12. **BackupKey**: A link in the `dbparm.ini` that points to the backup location.
13. **StagingAreaDirectory**: Indicates the directory where safes are temporarily staged.  
![[Pasted image 20231004193744.png]]