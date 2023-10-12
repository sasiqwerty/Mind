*This is an important interview question.*

The Master Policy allows you to easily define a corporate level policy that reflects the business goals and guidelines for managing privileged accounts and sessions across your entire organization. Using policy exceptions, you can define different policy behavior for specific platforms that require different workflows or policies to those defined in the Master Policy. The Master Policy also allows you to measure how well the corporate policy is adhered to and easily view the gaps. To view or define the Master Policy behavior, select a policy rule to view its current related settings.

## [Require dual control password access approval](Dual%20Access%20Control.md)

Use this rule to enforce an access control workflow in which end users will require authorization before accessing privileged accounts. Depending on advanced configuration, access authorization must be given by one or more managers.

## Enforce check-in/check-out exclusive access
 
Use this rule to ensure that only one user will be able to access and use an account at any given point of time. When a user checks out an account, it is locked and cannot be retrieved by other users. Other users can only check out the same account after the first user has checked the account back in. To achieve automatic release of locked passwords and full personal accountability, enable this and the “Enforce one-time password access” rule together. If a user doesn't check the account in manually within a predefined timeframe, the CPM will check it in automatically. This timeframe is determined by the 'Minimum timeframe that a password is available after retrieval' platform setting or by the timeframe defined in the dual control request.

## Enforce one-time password access
 
Use this rule to ensure that passwords are changed after each access. When a user retrieves an account, the CPM initiates a password change process that will occur automatically after a predefined timeframe. In contrast to the 'Enforce check-in/check-out exclusive access' rule, multiple users can access the same password simultaneously. To achieve personal accountability, enable this rule and the 'Enforce check-in/check-out exclusive access' rule together. The timeframe that an account will be available before it will be automatically changed is determined by the 'Minimum timeframe that a password is available after retrieval' platform setting or by the timeframe defined in the dual control request.

## Allow EPV transparent connections ('Click to connect')
 
Use this rule to allow end users to transparently connect to target devices, open applications , access web sites, etc. without exposing the password to the end user. Advanced settings determine whether or not end users can view or copy passwords.

## Require users to specify reason for access
 
Use this rule to force end users to specify an access reason. Depending on advanced configuration, users can either be restricted to selecting from a predefined reason list, or can specify a free text access reason.

## Require password change every X days
 
Use this rule to define how often passwords are changed to adhere to the enterprise policy. The PIM Suite either manages your passwords automatically or allows you to manage them manually, assisted by email notifications

## Require password verification every X days
 
Use this rule to define how often passwords are verified, ensuring that passwords stored in the Vault are always synchronized with passwords in the target systems. The PIM Suite either verifies your passwords automatically or allows you to verify them manually.

## Require privileged session monitoring and isolation
 
Use this rule to determine whether or not privileged sessions will be connected securely to target systems via the Privileged Session Manager (PSM), using stored privileged credentials without exposing passwords. To apply this rule, install and license the PSM. This rule will be ignored on platforms that do not support the PSM.

## Record and save session activity
 
Use this rule to determine whether or not privileged sessions initiated by the PSM will be recorded.

## Activities audit retention period
 
Use this rule to set the retention period of the audit events stored in the system. After the specified retention period, the audit events will automatically be deleted from the system.

