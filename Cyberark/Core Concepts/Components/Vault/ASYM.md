---
aliases: ASYM test tool
tags: 
date created: Sunday, July 30th 2023, 4:40:02 pm
date modified: Monday, July 31st 2023, 8:40:48 am
---
The ASYM Test tool is a command-line utility that can be used to test the functionality of the asymmetric encryption keys used by CyberArk Privileged Access Manager (PAM). The tool can be used to generate, encrypt, and decrypt data using the keys, and to verify the integrity of the data.

The ASYM Test tool is available as part of the CyberArk PAM installation package. To use the tool, you must first generate a set of asymmetric encryption keys using the CyberArk Key Generator utility. Once you have generated the keys, you can use the ASYM Test tool to test their functionality.

To run the ASYM Test tool, you must open a command prompt and navigate to the directory where the tool is located. Then, you can run the tool by typing the following command:

```
asymtest <key_file> <data_file>
```

The `<key_file>` parameter specifies the path to the file containing the asymmetric encryption keys. The `<data_file>` parameter specifies the path to the file containing the data that you want to encrypt or decrypt.

For example, to encrypt the file `data.txt` using the keys in the file `keys.txt`, you would run the following command:

```
asymtest keys.txt data.txt
```

The ASYM Test tool will encrypt the data in the `data.txt` file and write the encrypted data to a new file called `data.txt.enc`.

To decrypt the data in the `data.txt.enc` file, you would run the following command:

```
asymtest keys.txt data.txt.enc
```

The ASYM Test tool will decrypt the data in the `data.txt.enc` file and write the decrypted data to a new file called `data.txt`.

The ASYM Test tool can also be used to verify the integrity of data that has been encrypted using the asymmetric encryption keys. To do this, you would run the following command:

```
asymtest -v <key_file> <data_file>
```

The ASYM Test tool will verify the integrity of the data in the `data_file` file and report whether the data has been tampered with.

For more information on the ASYM Test tool, please refer to the CyberArk PAM documentation.