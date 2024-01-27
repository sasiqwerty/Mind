---
aliases: 
tags: 
date created: Sunday, November 5th 2023, 7:54:22 pm
date modified: Sunday, November 5th 2023, 7:54:38 pm
---

## What Are the Vault Security Layers? #defcon1

CyberArk's Vault employs a multi-layered security approach to ensure the utmost protection for stored credentials and other sensitive data. Here's a breakdown of these layers:

1. **Session Encryption**:
    - **Proprietary Protocol**: The Vault requires a dedicated server to operate, a mandate enforced by the CyberArk firewall. This firewall restricts communication to and from the server, only allowing its proprietary authenticated protocol, known as the Vault protocol.
    - **OpenSSL Encryption**: All passwords and files within the Vault are encrypted, utilizing an encryption framework that remains transparent to the end-user. Consequently, neither users nor administrators have to manage or address key-related issues.

2. **Firewall**:
    - **Hardened built-in Windows Firewall**: CyberArk's firewall ensures that the Vault's code is the sole executable on its dedicated server, guaranteeing a pristine environment and enabling the security system's total control over the server.

3. **Authentication**:
    - **Single or Two Factor Authentication**: Access to the Vault mandates authentication via a robust bi-directional authentication protocol. Methods include Passwords, PKI digital certificates, RSA SecurID tokens, RADIUS protocol, USB Tokens, or Windows authentication. The Privileged Account Security solution can also integrate third-party authentication tools.

4. **Discretionary Access Control**:
    - **Granular Permissions**: The Privileged Account Security solution has an intrinsic access control system. Users are shielded from passwords or details not meant for them. Permissions include reading, writing, deleting, or administrating based on access control rules.
    - **Role-Based Access Control**: The Vault's Visual Security offers a unique way for users to monitor the activities performed in their Safes by peers. They can observe real-time interactions, including logins and data retrievals.

5. **Mandatory Access Control**:
    - **Subnet-Based Access Control**: Restrictions based on specific subnets.
    - **Time Limits and Delays**: Access can be restricted or delayed based on specific timings.

6. **Auditing**:
    - **Tamperproof Audit Trail**: Visual Security functionalities notify users of any Vault activities and instantly highlight accessed passwords and files.
    - **Event-Based Alerts**: Automatic notifications for specific events.

7. **File Encryption**:
    - **Hierarchical Encryption Model**: An organized encryption structure.
    - **Every Object Has a Unique Key**: Each password and file within the Vault gets encrypted with its unique key, leveraging an encryption infrastructure invisible to the end user, freeing them from key management issues.

This multi-layered approach ensures the Vault provides the highest level of security for privileged credentials and other sensitive information.****