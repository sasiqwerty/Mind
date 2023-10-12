---
aliases: 
tags: 
date created: Sunday, August 13th 2023, 3:18:19 pm
date modified: Sunday, August 13th 2023, 3:18:27 pm
---

## Disaster Recovery

In this section we will test the Disaster Recovery (DR) procedures for automatic failover

and manual failback. The exercise will include the following steps:

1) First, we will configure the Disaster Recovery module on the DR server to perform

an automatic failover in case the Primary Vault is no longer reachable.

2) We will execute a full replication from the Primary Vault to the DR Vault.

3) We will test an automatic failover from the Primary Vault to the DR Vault. As part

of the test, we will also confirm that our end users can still access critical systems

via CyberArk, without any human intervention.

4) We will set the Primary Vault to act as DR and replicate all data back from the DR

Vault to the Primary Vault.

5) We will then perform a manual failback from the DR Vault to the Primary Vault

6) Lastly, we will set the DR Vault back to DR mode and confirm our end users are

still able to connect to critical systems via CyberArk.

  

The below steps have already been performed by the implementation team:

The PrivateArk Server, PrivateArk Client, and Disaster Recovery module have all

been installed on both your vault01a and DR servers by the implementation team.

A second DR user called “DR_Failback” was manually created by the

implementation team during the deployment of the Primary Vault for the purpose of

supporting the failback procedure from the DR site back to the primary site.

However, both the DR and DR_Failback users are currently disabled. You will need

to enable these users to complete the Disaster Recovery exercises.

  

Step 1: Enable Automatic Failover on the DR Vault

As noted above, the implementation team has already installed the PrivateArk Server,

PrivateArk Client and Disaster Recovery service on the DR server. However, to avoid

an unwanted automatic failover during the first days of the course, automatic failover was

disabled, and the DR user deactivated. We are now going to enable the DR user and

Automatic Failover to the DR Vault.

On the Components server, connect as the Administrator user with the PrivateArk

Client to the Primary Vault and enable the DR user.