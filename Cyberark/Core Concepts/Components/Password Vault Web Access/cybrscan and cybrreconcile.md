---
aliases: 
tags: 
date created: Wednesday, August 2nd 2023, 10:32:47 am
date modified: Wednesday, August 2nd 2023, 10:33:09 am
---
The **cybrscan** and **cybrreconcile** accounts are special accounts in CyberArk that are used for auditing and reconciliation purposes. The cybrscan account is used to scan the CyberArk environment for potential security vulnerabilities, while the cybrreconcile account is used to reconcile the permissions of accounts in the CyberArk vault with the permissions that are actually granted on the target systems.

**cybrscan** account

The cybrscan account is a privileged account that has access to all of the accounts in the CyberArk vault. This allows it to scan the vault for potential security vulnerabilities, such as accounts that have weak passwords or that are not being rotated regularly. The cybrscan account is also used to run reports on the CyberArk environment.

**cybrreconcile** account

The cybrreconcile account is a privileged account that is used to reconcile the permissions of accounts in the CyberArk vault with the permissions that are actually granted on the target systems. This is done by comparing the permissions that are stored in the vault with the permissions that are actually granted on the target systems. If there are any discrepancies, the cybrreconcile account will update the vault with the correct permissions.

**Both accounts are highly privileged and should only be used by authorized personnel.**

Here are some of the use cases for the cybrscan and cybrreconcile accounts:

- **Scanning the CyberArk environment for potential security vulnerabilities:** The cybrscan account can be used to scan the CyberArk environment for potential security vulnerabilities, such as accounts that have weak passwords or that are not being rotated regularly. This can help to identify and remediate security risks before they can be exploited by attackers.
- **Running reports on the CyberArk environment:** The cybrscan account can also be used to run reports on the CyberArk environment. This can be used to track the usage of privileged accounts, identify potential security risks, and ensure that the CyberArk environment is being managed effectively.
- **Reconciling the permissions of accounts in the CyberArk vault with the permissions that are actually granted on the target systems:** The cybrreconcile account can be used to reconcile the permissions of accounts in the CyberArk vault with the permissions that are actually granted on the target systems. This can help to ensure that the permissions of accounts in the CyberArk vault are always accurate and up-to-date.