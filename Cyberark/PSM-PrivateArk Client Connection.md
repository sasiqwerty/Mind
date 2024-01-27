---
aliases: 
tags: 
date created: Thursday, October 12th 2023, 8:40:31 pm
date modified: Thursday, October 12th 2023, 9:10:42 pm
---
#clean

## **Introduction To PSM-PrivateArk Client Connection Configuration**

CyberArk's PSM-PrivateArk Client Connection ensures rigorous oversight of PrivateArk Client operations, especially those initiated by the Vault Admin. This concise guide delineates the steps for configuring this vital security feature, prioritizing transparency and traceability within the PrivateArk ecosystem.

## **PSM-PrivateArk Client Connection Configuration**

| Step | Description                                                                                                                 | Action/Location                                                                                             |
|------|-----------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| 1    | **Prerequisite**: Install PrivateArkClient on the PSM server                                                                | -                                                                                                           |
| 2    | Onboard Vault Admin user (`Administrator`) in PVWA manually                                                                 | System type: `Application`<br>Platform: `CyberArk Vault`<br>Safe: Select any<br>Server IP: Provide Vault IP |
| 3    | Create a vault server in the PrivateArk Client                                                                              | Name: Vault server IP address<br>Server address: Provide<br>Auth method: `PrivateArk Authentication`        |
| 4    | Export Configuration Data                                                                                                  | Tools→Administrator Tools→Export Configuration Data→Save to desktop & rename to `GlobalSettings.ini`       |
| 5    | Set permissions for `GlobalSettings.ini`                                                                                   | Right-click → Properties → Security → Edit → Add `PSMShadowUsers` group → Provide Read & Execute Permission |
| 6    | Execute Vault Configuration data                                                                                           | Navigate to `PAConfig.exe` → cmd/powershell (admin) → Run `PAConfig.exe /inifile <path to GlobalSetting.ini>` |
| 7    | Edit `PSMConfigAppLocker.xml` and add PrivateArk Client application path                                                     | Path: `C:/Program Files(X86)/PrivateArk/Client/Arkuit.exe` (Open in notepad/notepad++ in admin mode)       |
| 8    | Execute `PSMConfigAppLocker.ps1` script                                                                                     | Open powershell (Ensure `Set-Execution Policy` is set) → Run script                                        |
| 9    | Test the setup                                                                                                             | PVWA→Accounts → Select `administrator` account → Click on 'Connect'(PSM-PrivateArk Client)                 |    

### Flowchart

![[mermaid-diagram-2023-10-12-203954.svg]]

### **Summary**:

The PSM-PrivateArk Client Connection is a configuration setup that facilitates the isolation, monitoring, and recording of activities performed on the PrivateArk Client, especially by the Vault Admin user. This configuration ensures the Vault activities are logged and transparent. The process involves several stages, from onboarding the Vault Admin user to executing specific scripts and ensuring the proper permissions and paths are set. The configuration can be applied to other CyberArk components in a similar manner.