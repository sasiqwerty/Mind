---
aliases: 
tags: 
date created: Thursday, August 31st 2023, 1:36:15 pm
date modified: Wednesday, November 1st 2023, 2:54:08 pm
---

## Easy-to-Read Instructions for Configuring PSM Server and Related Settings

### Summary

The following steps guide you through signing in to your PSM Server, adjusting certificates, editing group policy, and updating configurations on your PVWA.

### Detailed Steps

1. **Log in to PSM Server**
   - Use your Domain Administrator credentials.

2. **Access Server Manager**
   - Look for `Remote Desktop Services` in the left menu.

3. **Edit Deployment Properties**
   - Navigate to `Tasks > Edit Deployment Properties`.
   - In the new window, go to `Certificates`.
   - Select `Choose a different certificate` and locate your `.pfx` file.
     - Note: The real environment uses `.cer`, so you'll need to convert it to `.pfx`.

4. **Upload Certificate**
   - Open the `.pfx` file.
   - Enter your password.
   - Tick the box saying "Allow the certificate to be added to the Trusted Root..."
   - Confirm with `OK`.

5. **Local Group Policy**
   - Open the Group Policy editor.
   - Navigate through the following path:
     ```
     Computer Configuration > Administrative Templates > Windows Components > Remote Desktop Services > Remote Desktop Session Host > Security
     ```
  
6. **Set Encryption Level**
   - Open `Set client connection encryption level`.
   - Enable it and set it to `High Level`.
   - Confirm with `OK`.
   - **Note**: This applies to native RDP encryption, which is not recommended over SSL.

7. **Set Security Layer**
   - Open `Require use of specific security layer for remote (RDP) connections`.
   - Enable it and set the layer to `SSL`.
   - Confirm with `OK`.

8. **Login to PVWA**
   - Use `vaultadmin01` credentials.
   - Go to:
     ```
     ADMINISTRATION > Configuration Options > Options > Privileged Session Management > Configured PSM Servers > PSMServer > Connection Details > Server
     ```
   - Change the `Address` attribute to the FQDN matching the COMPOIC server certificate.

9. **Update Component Parameters in PVWA**
   - Navigate to:
     ```
     ADMINISTRATION > Configuration Options > Options > Connection Components > PSM-SSH > Component Parameters
     ```
   - The property name should be `authentication level: i` and its value should be `1`.

For the configuration to work as expected, ensure you follow these steps in the given order.