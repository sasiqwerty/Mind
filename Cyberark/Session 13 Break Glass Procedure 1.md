---
aliases: 
tags: 
date created: Wednesday, October 4th 2023, 4:12:04 pm
date modified: Tuesday, October 17th 2023, 9:51:49 pm
---

## Break-Glass Process Design and Procedures for CyberArk

### Summary:

A break-glass process ensures that emergency access to critical systems, such as the CyberArk ecosystem, is available. While CyberArk requires a specific break-glass account, other assets might too. The focus here is on securing and retrieving the CyberArk Master private encryption key and associated Master password. These are typically stored physically and should be set/retrieved by multiple trusted individuals.

### Detailed Procedures:

1. **Storage of the Master Private Key**:
   - The Master private key is usually delivered and stored on a physical CD.
2. **Access Control**:
   - Ensure more than one person has access to each physical safe.
     - This prevents single points of failure.
     - Plan for situations where an individual might be unavailable (e.g., vacations, illnesses).
3. **Emergency Retrieval Process**:
     - Verify the emergency and document the reasons for initiating the break-glass process.
     - Retrieve the Master private key CD and the password.
     - Access the CyberArk system using the Master private encryption key and the Master password.
     - Once the emergency is resolved, reset the Master password.

## Recover Passwords and Safes outside the Vault

### SafeRecover

This utility is used to recover the contents of a Safe.

SafeRecover has the following usage:  
`Saferecover[safe] [output directory] [keys directory]`

|Parameter|Description|
|---|---|
|Safe|Name of the Safe to recover. Use wildcards for multiple Safes.|
|Output directory|Name of the folder in which the utility will store the recovered Safe contents.|
|Keys directory|The path of the Recovery key.  <br>Note:  This key is on the Master CD only.|

**For example:**

> `saferecover Research C:\Research F:`

The above example will cause the SafeRecover utility to recover the Safe called Research, and store the recovered files in the C:\Research folder. The utility will use the Recovery key on the Master CD, which is on the F: drive.

### Password Recovery Using `recover.exe` Outside of the Vault

When you need to recover passwords from the Vault using `recover.exe`, it's vital to follow the steps carefully. This guide provides you with step-by-step instructions to accomplish this. 


1. **Perform a Full Backup**: 
   - Always begin by taking a full backup of your current system. This ensures you can restore the system to its previous state in case of any issues.
2. **Setup the Recovery Folder**:
   - Create a folder on the server where you intend to do the recovery.
   - From the Vault's installation folder, copy the following files into your newly created folder:
     ```plaintext
     calibeay64102o.dll  
     cassleay64102o.dll 
     Recover.exe
     ```
3. **Install Visual C++ Dependencies**:
   - Install `Visual C++ 2013 redist x64`.
4. **Insert the Master CD**:
   - This contains essential recovery keys.
5. **Recover the Encrypted Object**:
   - Navigate to the folder where `Recover.exe` is located.
     ```plaintext
     C:\Recover>recover.exe
     ```
   - Provide the necessary information prompted:
     - **File to recover**: Path and object name of the file you intend to decrypt.
       ```plaintext
       Example: C:\PrivateArk\Safes\Data\RH_Local_Admin\root\operating system-rh_local_accounts-10.0.123.#000000000000027#-localadmin02
       ```
     - **Output directory**: Where the decrypted file will be saved.
       ```plaintext
       Example: c:\Recover
       ```
     - **Private recovery key directory**: Location of `recprv.key` on the server.
       ```plaintext
       Example: D:\
       ```
6. **Retrieve Password**:
   - Navigate to the output directory.
   - Open the decrypted file using a text editor (e.g., Notepad) to obtain the password.

#### Important Notes

- `Recover.exe v12.0` requires `calibeay64102u.dll` and `cassleay64102u.dll`. Prior versions used `calibeay64102o.dll` and `cassleay64102o.dll`. Note the distinction between files ending in "u.dll" and "o.dll".
  
- For `Recover.exe v13`, you'll need `libeay64.dll` and `ssleay64.dll`. As with previous Vault versions, these DLLs, alongside `Recover.exe`, can be found under the Vault Installation Folder, typically located at:
  ```plaintext
  X:\Program Files (x86)\PrivateArk\Server
  ```
