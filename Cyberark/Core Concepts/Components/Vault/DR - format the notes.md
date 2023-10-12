---
aliases: 
tags: 
date created: Saturday, August 12th 2023, 8:27:04 pm
date modified: Sunday, August 13th 2023, 3:58:34 pm
---

## Manual Fail Back Steps:

Before attempting the Failback steps, make sure the DR_Failback user is enabled.

1. Update the Padr.ini file in Primary Vault with `ActivateManualFailOver=No` and `FailoverMode=No`  
   And Delete the last two lines (log number and timestamp of the last successful replication) in the file.

2. Start the `CyberArkVaultDisasterRecovery` Service at primary node(You have already the PrivateArk Server service in stop status, since it is in failover state)

In Prod Padr.log we will see the `MetaDataReplication` is running successfully message.  
And the Replication will Ended after some time.

To bring back the Primary Vault Up and running to the Production State.  
update the `ActivateManualFailover=Yes` in padr.ini of Prod node and restart the CyberArk DR service.

This will automatically starts this PrivateArk Server Service, and the DisasterRecovery Service will stop automatically.

Remove the two time stamp lines at DR vault-Padr.ini and set Failover Mode=No  
Stop the PrivateArk Server service in DR Vault.  
Start the DR service at DR Vault.

## Plan of Action

1. Check the health page in PVWA.
2. Enable DR User
3. Trigger Full Replication
4. Check the Metadata replication.
5. Initiate the Automatic Failover
6. Check the Health page in PVWA
7. Check the all the components are connected to DR or not.
8. Connect the CPM To the DR.
9. Create a Safe called Test_Safe1
10. Enable DR_Failback User
11. Do the Manual Failback
	1. Reverse Replication
	1. Manual Failback
12. Check if any issues identified.
13. Connect to CPM
14. Check the health page in PVWA.

## Fail Over

### Services Before Fail Over In the DR Vault

what are all the services would be in running state.  

#### On

- CyberArk Vault Disaster Recovery  
- PrivateArk DataBase  
- CyberArk Logic Container  
- CyberArk Windows hardened firewall

#### Off

- PrivateArk Server Service  
- CyberArk Event Notification Engine

### Services After Fail over In the DR Vault

#### On

All Services except CyberArk Vault Disaster Recovery Service.


the credential file is created in the disaster recovery vault and the user will be in the primary vault.

## What Are the Right Questions in This Topics?

```mermaid
graph LR
A[Disaster Recovery Module]
A --> B[Real-Time Replication]
A --> C[Automated Failover]
A --> D[Manual Failover]
A --> E[Failback]
A --> F[Monitoring and Health Checks]
A --> G[Activity Logging]
A --> H[Data Encryption]
A --> I[Testing and Validation]
A --> J[Notification and Alerts]

B --> B1[Synchronize Data]
B --> B2[Configuration Updates]

C --> C1[Automatic Detection of Disaster]
C --> C2[Initiate Failover]

D --> D1[Admin-Initiated Failover]

E --> E1[Restore Primary Vault]
E --> E2[Sync Changes]

F --> F1[Monitor DR Vault Health]
F --> F2[Initiate Actions]

G --> G1[Log Activities]

H --> H1[Encrypt Data Replication]

I --> I1[Test Disaster Recovery Process]

J --> J1[Generate Notifications]

```
DR Drill flowchart
```mermaid
graph TD
    A[Start: Initiate DR Drill] --> B[Simulate Outage at Primary Site]
    B --> C[Activate DR Vault]
    C --> D{Validate & Test}
    D --> E1[Check Connectivity]
    D --> E2[Test Data Integrity]
    D --> E3[Functional Tests]
    D --> F[All tests successful?]
    F --> |Yes| G[Begin Failback Process]
    F --> |No| H[Log Issues & Investigate]
    G --> I[Re-establish Replication to Primary]
    I --> J[Switch Operations Back to Primary]
    J --> K[Reset DR Vault to Standby]
    K --> L[End: Document Observations & Refine Process]
    H --> L

```

```mermaid
graph TD
    A[Check the health page in PVWA] --> B[Enable DR User]
    B --> C[Trigger Full Replication]
    C --> D[Check the Metadata replication]
    D --> E[Initiate the Automatic Failover]
    E --> F[Check the Health page in PVWA]
    F --> G[Check if all the components are connected to DR or not]
    G --> H[Connect the CPM To the DR]
    H --> I[Create a Safe called Test_Safe1]
    I --> J[Enable DR_Failback User]
    J --> K[Do the Manual Failback]
    K --> L1[Reverse Replication]
    L1 --> L2[Manual Failback]
    L2 --> M[Check if any issues identified]
    M --> N[Connect to CPM]
    N --> O[Check the health page in PVWA]

```

![[Pasted image 20230813155012.png]]

## Disaster Recovery Flowcharts

```mermaid
graph TD
A[Start: Disaster Recovery Process]
A --> B1[1. Enable Automatic Failover on DR Vault]
B1 --> B2[2. Execute Full Replication to DR Vault]
B2 --> B3[3. Execute Automatic Failover Test]
B3 --> B4[4. Execute Full Replication Back to Primary Vault]
B4 --> B5[5. Execute Failback Using Manual Failover]
B5 --> B6[6. Set DR Server Back to DR Mode]
B6 --> End[End of Process]
```

### Step 1

```mermaid
graph TD
A[Start: Enable Automatic Failover on DR Vault]
A --> B1[Configure Disaster Recovery module on DR server]
B1 --> B2[Enable the DR user]
B2 --> B3[Set up Automatic Failover to the DR Vault]
B3 --> End[End of Step 1]
```

### Step 2

```mermaid
graph TD
A[Start: Execute Full Replication to DR Vault]
A --> B1[Restart CyberArk Disaster Recovery service]
B1 --> B2[Confirm completion of replication from Primary Vault]
B2 --> B3[Review current system health in PVWA]
B3 --> End[End of Step 2]
```

### Step 3

```mermaid
graph TD
A[Start: Execute Automatic Failover Test]
A --> B1[Stop the Primary Vault server]
B1 --> B2[Monitor DR server for failover triggers]
B2 --> B3[Confirm Automatic Failover on the DR Vault]
B3 --> B4[Confirm Automatic Failover of PVWA and PSM]
B4 --> End[End of Step 3]
```

### Step 4

```mermaid
graph TD
A[Start: Execute Full Replication Back to Primary Vault]
A --> B1[Ensure all recent data is replicated from DR Vault]
B1 --> B2[Use Disaster Recovery module on vault01a]
B2 --> B3[Enable user DR_Failback]
B3 --> B4[Edit padr.ini file on vault01a]
B4 --> B5[Start CyberArk Disaster Recovery Service on Primary Vault]
B5 --> B6[Monitor and verify replication from DR Vault]
B6 --> B7[Review system health in PVWA]
B7 --> End[End of Step 4]
```

### Step 5

```mermaid
graph TD
A[Start: Execute Failback Using Manual Failover]
A --> B1[Ensure working on vault01a 10.0.10.1]
B1 --> B2[Edit padr.ini file on vault01a]
B2 --> B3[Set ActivateManualFailover to Yes]
B3 --> B4[Restart CyberArk Disaster Recovery service on vault01a]
B4 --> B5[Monitor padr.log file on vault01a]
B5 --> B6[Confirm messages of successful Failover process]
B6 --> B7[Verify CyberArk Vault Disaster Recovery service termination on vault01a]
B7 --> B8[Verify PrivateArk Server service start on vault01a]
B8 --> End[End of Step 5]
```

### Step 6

```mermaid
graph TD
A[Start: Set the DR Server Back to DR Mode]
A --> B1[Ensure working on the DR server]
B1 --> B2[Edit padr.ini file on DR server]
B2 --> B3[Set ActivateManualFailover to No]
B3 --> B4[Restart CyberArk Disaster Recovery service on DR server]
B4 --> B5[Monitor and verify replication from Primary Vault]
B5 --> B6[Confirm start of full replication process]
B6 --> B7[Review system health in PVWA]
B7 --> End[End of Step 6]
```
