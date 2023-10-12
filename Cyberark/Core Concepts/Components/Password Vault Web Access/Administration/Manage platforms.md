fA [[Platform]] defines shared characteristics for multiple accounts.

## Target platforms
Target platforms are associated with target accounts. Target accounts allow users to connect to various machines and devices. 

**Examples of target accounts are**
- Operating systems
- Databases
- Security appliances
- Network devices
- Directories
- Applications

## Dependent Platforms
Dependent platforms are associated with dependent accounts.

Dependent accounts are accounts that represent resources, such as Windows Services or Windows Scheduled Tasks, that are accessed from a target machine, not necessarily the same target machine, and require the same credentials as the target machine. When changing a password, the CPM synchronizes the target account password with all other occurrences of that password in the related dependent accounts.

## Group Platforms

A group platform is associated with a group. A group includes multiple accounts. Account groups are a group of accounts that share a password and for which passwords are managed together, whether the password change is scheduled or initiated by a user.

Account that belong to a group have two platforms assigned to them:

- Target platform. This is the typical platform associated with an account, which includes the CPM plugin that performs the password change on the target machine.
- Group platform. This platform determines when the password is changed and the password policy.

## Rotational group Platforms

Rotational group platforms are associated with a group of accounts for which the credentials are changed asynchronously.

This is beneficial in a dual account deployment.
