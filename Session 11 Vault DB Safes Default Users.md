---
aliases: 
tags: 
date created: Wednesday, October 4th 2023, 5:05:38 pm
date modified: Wednesday, October 4th 2023, 11:20:10 pm
---

## my.ini File

### Overview

- `my.ini` configures the vault database.
- Always consult CyberArk support before making modifications.
- The vault's database is MySQL-based and isn't alterable.

### Key Configuration Parameters

- Specifies the metadata location.
- Dictates RAM allocation for the database in kb, particularly for the InnoDB storage engine.
- InnoDB is MySQL's default storage engine from version 8.0, striking a balance between reliability and performance. [More on InnoDB](https://dev.mysql.com/doc/refman/8.0/en/innodb-introduction.html).
- InnoDB buffer pool size generally takes up 80% of available RAM.

### Auxiliary Data

- The `bin` folder (server > database) contains MySQL's auxiliary files.
- Issues within the vault database and InnoDB interactions can be found in `vaultDB.log`.

### MySQL Upgrades

- Prior to CyberArk 11.7, MySQL's version was 5.7. From CyberArk 12 onwards, it's 8.0.
- Upgrade cautiously, transitioning from 5.7 -> 5.8 -> 8 to avoid complications.
- CyberArk recommends specific intermediate versions for smooth upgrades.
- For data recovery (due to corruption), CyberArk offers a clean metadata folder (located in `PrivateArk > safes > metadata`).

## Vault Hardening Overview

The Vault hardening process is an essential component of the Vault installation. For all production environments, CyberArk strongly advises undergoing comprehensive Vault hardening. For detailed Vault Security Standards, refer to the [CyberArk documentation portal](https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/Latest/en/Content/Security/Standards-CyberArks%20Digital%20Vault%20Server%20Security%20Standard.htm).

### Hardening Process Details

The hardening protocol involves alterations to the vault OS registry, security policy, and network properties. Additionally, it assumes control over the Windows firewall. After installation, the hardening log can be located at `%windir%\Temp\Hardening.log`. Since this is a temporary location, it's recommended to transfer the log to a secure location.

### Third-party Software Installation

CyberArk generally advises against installing third-party software on the Vault because they could increase vulnerability. However, some clients may opt to install such software to satisfy specific business needs, acknowledging the heightened risk.

Commonly installed third-party software by CyberArk clients includes:
- VMWare tools or other hypervisor support tools.
- Tools or drivers for hardware management or SAN.

If such software installations are imperative, it's preferable to do so before starting the Vault hardening process. Post-hardening, the installation or updating of applications and drivers can become challenging due to disabled services and altered system permissions.

### Hardening Settings Configuration

The primary settings for hardening are present in the "Hardening.ini" file located at `<vault installation path>\server\hardening\hardening.ini`. The settings are:

```
hardening.ini
HardenNetworkDevice=Yes
HardenWindowsSecurity=Yes
HardenWindowsLocalSecurity=Yes
HardenWindowsFireWall=Yes
```

For specific requirements, these settings can be adjusted.

### Specific Hardening Processes

### Network Cards/Adapters Hardening

For IPv4:
- Disable 'NetBIOS'.
- Disable 'LMHOSTS lookup'.
- Disable 'Register this connection's addresses in DNS'.

For IPv6:
- Disable 'Register this connection's addresses in DNS'.

### Windows Settings

#### Windows Security Hardening

Files specific to this process are determined by the operating system: server 2008, server 2012, or server 2016. These files are available on the installation CD/media or within the 'Hardening' folder at `C:\Program Files (x86)\PrivateArk\Server\Hardening\StandaloneVault`. For detailed configurations, open the respective .inf file in a text editor.

#### Windows Audit Policy Hardening

Depending on the OS, use files named 'Windows2008Audit.csv', 'Windows2012Audit.csv', or 'Windows2016Audit.csv'. These files are located in the same directory as the security hardening files.

#### Windows Local Security Hardening

The modifications under this category include:
- Disabling all local users except for the user logged in during the install.
- Retaining only local admin users and the currently logged-in user in local groups.
- Deleting the registry value: `LMachine/Software/Microsoft/Windows/CurrentVersion/Run/VMware User Process`.
- Enabling daylight saving.

#### Windows Firewall Hardening

All firewall rules are eliminated during the installation. Subsequently, rules are dynamically managed based on requirements. A related log is available at: 
- Event Viewer (Local) > Applications and Services Logs > Microsoft > Windows > Windows Firewall With Advanced Security > Firewall.

Static rules are also introduced, but they remain under the vault's control and are based on rules specified in the DBParm.ini file.

## Users, Groups and Safes of Vault

 #todo