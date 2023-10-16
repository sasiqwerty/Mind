---
aliases: 
tags: 
date created: Monday, July 31st 2023, 9:13:43 am
date modified: Monday, October 16th 2023, 3:31:05 pm
---

## Plan for the Day

learn the folder structure of the vault and PrivateArk server

## Study Topics

## Topics Discussed

An XLT file is a template created by Microsoft Excel, a spreadsheet application included with the Microsoft Office suite. It contains default formatting and data for a spreadsheet and is used as a basis for creating new .XLS files. XLT files are saved in the Excel Binary File Format, which was the primary format until the Office Open XML format (.XLTX file extension) replaced it in Excel 2007 for Windows and 2008 for Mac.

## Topics Practiced

## Doubts

## Ideas

## Thoughts

in the program files x86 folder we have the PrivateArk folder that contains 3 more folders 
1. Client
2. PADR
3. Server

### The Client Folder Contains the following Files

1. Graphics - The folder related to graphics
2. Reports - The folder that stores .xlt file to create reports in excel format
3. Arkui.exe is the executable file that opens the [[PrivateArk Client]]
4. PAconfig.exe
5. PAinfo.exe
6. PALink.exe

### The Server Folder Contains the

conf folder  
database folder  
event notification engine folder  
graphics folder  
hardening folder - for manual hardening after vault install  
keys folder  
LDAP folder  
Logic Container folder  
Logs folder  
Syslog folder  
other dll files  
CACert.exe file  
CAVaultManager.exe  
ChangeServerKeys.exe  
dbmain.exe  
PARagent.exe  
Recover.exe  
SafeRecover.exe  
srvGui.exe - the exe file that opens the server central administration console

### Conf

dbparm.ini file  
dbparm.ini.good ( the file that was in working condition when the vault started)  
dbparm.sample.ini ( this file contains all the possible parameters for the dpparm.ini)  
license.xml  
PARagent.ini  
ParAgent.pass  
PARAGENT.pass  
PARAGENT.sample.ini  
passparm.ini  
passparm.ini.good  
passparm.sample.ini  
tsparm.ini  
tsparm.ini.good  
vault.ini

this folder contains all the configuration files and backed up working versions of the config files as .good files  
it also contains the .sample files that store all the possible parameters allowed in the respective files





















