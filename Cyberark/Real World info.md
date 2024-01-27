---
aliases: 
tags: 
date created: Thursday, November 2nd 2023, 1:06:53 pm
date modified: Sunday, November 5th 2023, 4:13:45 pm
---

## Questions

### Personal and Professional Information

- **Can you tell me about yourself?**
- **What is your job role?**

  As a CyberArk administrator, my responsibilities include monitoring accounts, overseeing the health page, addressing tickets, and resolving occasional system bugs and glitches.

### Daily Routine and Activities

My day-to-day tasks involve:

- Checking all logs for errors and noting common issues that occur monthly.
- Monitoring the health page.
- Unsuspending users.
- Overseeing PVWA and PSM servers and their connections.
- Managing Vault CPU and disk usage.
- Assisting with troubleshooting.

### CyberArk Infrastructure

- **How many Vaults, PVWA, CPM, PSM, and DR Vaults do you have?**

  We manage:

  - 2 Vaults (1 primary, 1 DR).
  - 9 PVWAs within a VIP (F5) setup.
  - 11 PSMs, also within VIP (F5).
  - 3 CPMs, one for each geographical zone (China, India, and US).
  
  Our Vaults and DR are hosted on Azure cloud due to major outages previously experienced with local infrastructure. Half of our infrastructure is cloud-based, with a specialized team managing it.

- **What are the counts for Safes, Accounts, and Platforms?**

  We have approximately:

  - 100 Safes.
  - An equal number of Platforms.
  - 8,000 active accounts, alongside numerous inactive ones.

- **Where are your servers situated?**

  The majority of our servers are located in Hyderabad (HYD), while some are cloud-based with variable locations.

- **Which version of CyberArk are you using?**

  We are currently on version 12.6, having recently upgraded from 11.7.

### Operational Procedures

- **In the Asset list (Excel sheet) - are details automatically removed when a server is deleted?**

  No, the details are not automatically removed. When a server is decommissioned, a ticket is raised to the relevant team, who then manage the changes. The Asset list is updated post-approval.

- **How do you log into PVWA and then to another PVWA, CPM, PSM, or Vault?**

  Access is typically granted via shared accounts or direct RDP, depending on the severity of the issue at hand.

### Upgrades and Challenges

- **Have there been any recent upgrades to CyberArk?**

  Yes, as mentioned earlier, an upgrade to version 12.6 was recently performed.

- **What are the prevalent challenges or issues your company faces with CyberArk?**

  Our company encounters several recurring issues:

  - Group Policy changes leading to server misconfigurations.
  - Firewall or port connectivity issues with PSM and CPM.
  - Rare PSM certificate misconfigurations.
  - Load balancer issues.
  
  Most issues are typically resolved with a system restart, but persistent or critical errors are escalated to our L3 team or directly to CyberArk support.


