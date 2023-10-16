---
aliases: 
tags: 
date created: Monday, October 16th 2023, 11:50:21 am
date modified: Monday, October 16th 2023, 3:05:07 pm
---
IMG-20231015-WA0001.jpg  


Which accounts can be selected for use in the Windows discovery process? (Choose 2)

an account stored in the Vault  
an account specified by the user  
the Vault Administrator  
any user with Auditor membership  
the PasswordManager user



IMG-20231015-WA0002.jpg

Your organization requires all passwords be rotated every 90 days. Where can you set this requirement?

Master Policy  
Safe Templates  
PVWAConfigxml  
Platform Configuration




IMG-20231015-WA0003.jpg  
You created a new platform by duplicating the out-of-box Linux through the SSH platform. Without any change, which Text Recorder Type(s) will the new platform support? (Choose 2.)

SSH Text Recorder  
Universal Keystrokes Text Recorder  
Events Text Recorder  
SQL Text Recorder  
Telnet Commands Text Recorder



IMG-20231015-WA0004.jpg  

What is required to Manage loosely connected devices?

PSM for SSH  
EPM  
PSM  
PTA

IMG-20231015-WA0005.jpg  
Where can reconcile and/or logon accounts be linked to an account? (Choose 2)

account settings  
platform settings  
master policy  
safe settings  
service account settings



IMG-20231015-WA0006.jpg  

Which dependent accounts does the CPM support out-of-the-box? (Chaos

Solaris Configuration file  
Windows Services  
Windows Scheduled Tasks  
Windows DCOM Applications  
Windows Registry  
Key Tab file


IMG-20231015-WA0007.jpg  
CyberArk Defender - PAM - Dattatraya B Ingale

In addition to add accounts and update account contents, which additional permission on the safe is required to add a Single account?

Upload Accounts Properties  
Rename Accounts  
Update Account Properties  
Manage Safe



IMG-20231015-WA0008.jpg  


Which parameters can be used to harden the Credential Files (CredFiles) while using CreateCredFile Utility? (Choose 3 )

OS Username  
Current machine IP  
Current machine hostname  
Operating System Type (Linux/Windows/HP-UX)  
Vault IP Address  
Time Frame



IMG-20231015-WA0009.jpg  
Yvoe

Where can a user with the appropriate permissions generate a report? (Choose 2)

PWVA > Reports  
PrivateArk Client  
Cluster Vault Manager  
PrivateArk Server Monitor  
PARClient

IMG-20231015-WA0010.jpg  

When should vault keys be rotated?

when it is copied to file systems outside the vault  
annually  
whenever a CyberArk user leaves the organization  
when migrating to a new data center



IMG-20231015-WA0011.jpg  


Which statement is true about setting the reconcile account at the platform level?

This is the only way to enable automatic reconciliation of account passwords.  
CPM performance will be improved when the reconcile account is set at the platform level.  
A rule can be used to specify the reconcile account dynamically or a specific reconcile account can be selected.  
This configuration prevents the association from becoming broken if the reconcile account is moved to a different safe.

IMG-20231015-WA0012.jpg

You have been asked to turn off the time access restrictions for a safe.Where is this setting found?

PrivateArkClient  
RestAPl  
PVWA  
Vault  


IMG-20231015-WA0013.jpg  

What are valid ways to invite vendors using the Remote Access portal? (Choose 2.)


Use the vendor invitation form.  
Call the vendor users and have them scan a QR code  
Use the self-service invitation URL.  
Add the vendors in PVWA and send them their password.  
Contact CyberArk support to help invite the vendors,


IMG-20231015-WA0014.jpg  
PSM-SSH

Match the connection component to the corresponding OS/Function.

| **OS**          | **Function**          |
|-------------|-------------------|
| PSM-SSH     | UNIX              |
| PSM-RDP     | Windows           |
| PSM-WinSCP  | NIX File Transfer |
| PSM-SQLPlus | Database          |
| PSM-OS390   | Mainframe         |



IMG-20231015-WA0015.jpg  

The Privileged Access Management solution provides an out-of-the-box target platform to manage SSH keys, called UNIX Via SSH Keys. How are these keys managed? 

CyberArk stores Private keys in the Vault and updates Public keys on target systems  
CyberArk stores Public keys in the Vault and updates Private keys on target systems  
CyberArk does not store Public or Private keys and instead uses a reconcile account to create keys on demand  
CyberArk stores both Private and Public keys and can update target systems with either key



IMG-20231015-WA0017.jpg  

Your organization has a requirement to allow only one user to "check out passwords" and connect through the PSM securely. What needs to be configured in the Master policy to ensure this will happen?

Enforce check-in/check-out exclusive access = active; Require privileged session monitoring and isolation = active  
Enforce check-in/check-out exclusive access = inactive- Require privileged session monitoring and isolation = inactive  
Enforce check-in/check-out exclusive access = inactive; Record and save session activity = active  
Enforce check-in/check-out exclusive access = active; Record and save session activity = inactive



IMG-20231015-WA0018.jpg  

What can you do to ensure each component server is operational?


Logon to PVWA with v10 UI, navigate to Healthcheck and validate each component server is connected to the Vault.  
Ping each component server to ensure connectivity  
Use the PrivateArk client to connect to the Vault server and validate all the services are running  
Install the Vault Server Interface on a remote machine to avoid Interactive logon to the Vault OS and review the ITALog.log through the Vault Server interface.



IMG-20231015-WA0019.jpg  

To use PSM connections while in the PVVVA, what are the minimum safe permissions a user or group will need?

List Accounts, Use Accounts  
List Accounts, Use Accounts, Retrieve Accounts  
Use Accounts  
List Accounts, Use Accounts, Retrieve Accounts, Access Safe without confirmation



IMG-20231015-WA0020.jpg  

What must you specify when configuring a discovery scan for UNIX? (Choose 2)  

Vault Administrator  
CPM Scanner  
root password for each machine  
list of machines to scan  
safe for discovered accounts



IMG-20231015-WA0021.jpg  

According to CyberArk, which Issues most commonly cause installed components to display as disconnected in the System Health Dashboard? (Choose 2)

network instabilities!outages  
vault license expiry  
credential de-sync  
browser compatibility issues  
installed location file corruption


IMG-20231015-WA0022.jpg  

What does the minvalidity parameter on a platform policy determine?

time between a password retrieval and the account becoming eligible for a password change  
timeout for users signed into the PVWA as configured in the global settings  
minimum amount of time that Just In Time access is valid  
time in minutes before an empty safe ill be automatically deleted



IMG-20231015-WA0023.jpg  

Which tools can you use to identify the machines and accounts that create the highest risk and are exposed to lateral movement? (Choose 2)


Accounts Discovery Feed  
CyberArk DNA Report  
REST API scripts  
CyberArk DNA Map  
Get-LocalUser Powershell cmdlet



IMG-20231015-WA0024.jpg  

In your organization the "click to connect" button is not active by default. How can this feature be activated?

Policies > Master Policy > Allow EPV transparent connections > Inactive  
Policies > Master Policy— Session Management > Require privileged session monitoring and isolation > Add Exception  
Policies > Master Policy > Allow EPV transparent connections > Active  
Policies > Master Policy > Password Management



IMG-20231015-WA0025.jpg

You are adding a new application in the Remote Access portal. Which authentication methods can you use to authenticate users to the PW/AQ (Choose 2)

Password `  
OpenID  
Certificate  
SAML  
OTP

IMG-20231015-WA0026.jpg  


Due to corporate storage constraints, you have been asked to disable session monitoring and recording for 500 testing accounts used for your lab environment. How do you accomplish this?  

Master Policy>select Session Management>add Exceptions to the platform(s)>disable Session Monitoring and Recording policies  
Administration>Platform Management>select the platform(s)>disable Session Monitoring and Recording  
Polices>Access Control (Safes)>select the safe(s)>disable Session Monitoring and Recording policies  
Administration>Configuration Options>Optjon9select Privilege Session Management>disable Session Monitoring and Recording policies


IMG-20231015-WA0027.jpg  

A password compliance audit found
1. One-time password access of 20 domain accounts that are members of Domain Admins group In Active Directory are not being enforced
2. All the sessions of connecting to domain controllers are not being recorded by CyberArk PSM  
What should you do to address these findings?


Edit the Master Policy and add two policy exceptions. enable "Enforce one-time password access', enable "Record and save session activity"  
Edit safe properties and add two policy exceptions. enable •Enforce one-time password access", enable "Record and save session activity'  
Edit CPM Settings and add two policy exceptions enable "Enforce one-time password access", enable "Record and save session activity"  
Contact the Windows Administrators and request them to add two policy exceptions at Active Directory Level. enable "Enforce one-time password access", enable "Record and save session activity"  


IMG-20231015-WA0028.jpg

A company has multiple business units that have their own set of vendors. Each business unit has a distinct role to manage vendor access. The business units want to have full control over the Invitation process for their set of vendors. After inviting the user to the Remote Access portal, which permissions should be delegated?  

Administrator  
Vendor Manager  
Viewer  
User

IMG-20231015-WA0029.jpg  

You are running a "Privileged Accounts Inventory" Report through the Reports page in PVWA on a specific safe, To show complete account inventory information, which permission/s are needed on that safe?

List Accounts, View Safe Members  
Manage Safe Owners  
List Accounts, Access Safe without confirmation  
Manage Safe, View Audit



IMG-20231015-WA0030.jpg  

Which master policy settings ensure non-repudiation?

Require password verification every X days and enforce one-time password access.  
Enforce check-in/check-out exclusive access and enforce one-time password access.  
Allow EPV transparent connections ('Click to connect') and enforce check-in/check-out exclusive access.  
Allow EPV transparent connections ('Click to connect') and enforce one-time password access.`


IMG-20231015-WA0031.jpg  
You need to identity the most powerful accounts in your organization to prepare for the initial PAM onboarding process. Which tools or features can be used to locate and onboard these accounts? (Choose 2.)

Discovery and Audit (DNA)  
CyberArk's Command Line Interface (PACLI)  
Onboarding and Secure Account Feed  
Accounts Discovery  
Privilege Account Matrix (PAM) XML-based

IMG-20231015-WA0032.jpg  
CyberArk Defender - PAM -

Which statement is correct concerning accounts that are discovered, but cannot be added to the Vault by an automated onboarding rule?

They are added to the Pending Accounts list.  
They cannot be onboarded to the Password Vault.  
They must be uploaded using third party tools.  
They are not part of the Discovery Process.


IMG-20231015-WA0033.jpg  
You are onboarding an account that is not supported out of the box. What should you do first to obtain a platform to import?

Create a service ticket in the customer portal explaining the requirements of the custom platform.  
Search common community portals like stackoverflow, reddit, github for an existing platform.  
From the platforms page, uncheck the "Hide non-supported platforms" checkbox and see if a platform meeting your needs appears.  
Visit the CyberArk marketplace and search for a platform that meets your needs.

IMG-20231015-WA0034.jpg  
Which item is an option for PSM recording customization?

Windows events text recorder with automatic play-back  
Windows events text recorder and universal keystrokes recording simultaneously  
Universal keystrokes text recorder with windows events text recorder disabled  
Custom audio recording for windows events


IMG-20231015-WA0035.jpg  

What are the mandatory fields when onboarding from Pending Accounts? (Choose 2.)

Address  
Safe  
Account Description  
Platform  
CPM



IMG-20231015-WA0036.jpg  

Which Vault authorization does a user need to have assigned to able to generate the "Entitlement Report" from the reports page in PVWA? (Choose 2)

Manage Users  
Audit Users  
Read Activity  
View Entitlements  
List Accounts

IMG-20231015-WA0037.jpg  

What are the minimum permissions to add multiple accounts from a file when using PWIA bulk-uploadQ (Choose 3.)

add accounts  
rename accounts  
update account content  
update account properties  
view safe members  
add safes

IMG-20231015-WA0038.jpg  

A user needs to view recorded sessions through the PVWA. Without giving auditor access, which safes does a user need access to view PSM recordings? (Choose 2)


Recordings safe  
Safe the account is in  
System safe  
PYWAConfiguratjon safe  
Vaultlnternal safe



IMG-20231015-WA0039.jpg  
A user requested access to view a password secured by dual control and IS unsure who to contact to expedite the approval process The Vault Admin has been asked to look at the account and identify who can approve their request. What is the correct location to Identify users or groups who can approve?  

PWVA > Administration > Platform Configuration Edit Platform > Ul & Workflow > Dual Control > Approvers  
PVWA Policies > Access Control (Safes) Select the safe > Safe Members > Workflow > Authonze Password Requests  
PVWA> Account List > Edit > Show Advanced Settings Dual Control > Direct Managers  
PrivateArk > Adrntn Tools > Users and Groups Auditors (Group Membership)

IMG-20231015-WA0040.jpg  

In PVWA you are attempting to play a recording made of a session by user jsmith. but there is no option to "Fast Forward" within the video, It plays and only allows you to skip between commands instead. You are also unable to download the Video What could be the cause?

Recording is of a PSM for SSH sesston.  
The browser you are using ts out of date and needs an update to be supported  
You do not have the iView Audit" permtsslon on the sate where the account stored.  
You need to update the recorder settings in the platform to enable screen capture every ms or lessons



IMG-20231015-WA0041.jpg  
CyberArk Defender - PAM - Dattatraya B Ingale

You are configuring CyberArk to use TML5 gateways exclusively for PSM connections. In the PVWA, where do you set DefaultConnectionMethod to HTML5?

Options > Privileged Session Management Ul  
Options > Privileged Session Management  
Options > Privileged Session Management Defaults  
Options > Privileged Session Management Interface



IMG-20231015-WA0042.jpg  

Match each key to its recommended storage location.

| Key                  | Storage Location                       |
|----------------------|----------------------------------------|
| Recovery Private Key | Store in a Physical Safe               |
| Recovery Public Key  | Store in a Hardware Security Module    |
| Server Key           | Store on the Vault Server Disk Drive   |
| SSH Keys             | Store in the Vault                     |

IMG-20231015-WA0043.jpg  

Which processes reduce the risk of credential theft? (Choose 2.)

require dual control password access approval  
require password change every X days  
enforce check-in/check-out exclusive access  
enforce one-time password access

IMG-20231015-WA0045.jpg  

What are common ways that organizations leverage the CyberArk Blueprint for Identity Security Success? (Choose 3.)

to understand the identity attack chain  
to discover all digital Identities  
to describe the explicit order of operations for Identity Security  
to assess an organization's security posture  
to build an Identity Security roadmap  
to secure their human identities

IMG-20231015-WA0046.jpg  

You are creating a shared safe for the help desk. What must be considered regarding the naming convention?

Ensure the naming convention does not exceed 28 characters.  
Combine environments, owners and platforms to minimize the total number of safes created.  
Safe owners should determine the safe name to enable them to easily remember it.  
The word "Safe" cannot be used

IMG-20231015-WA0048.jpg  
You are onboarding 5000 UNIX root accounts for rotation by the CPM. You discover that the CPM is unable to login directly with the root account and will need to use a secondary account. How can this be configured to allow for password management using least privilege?  

Configure each CPM to the correct logon account  
Configure each CPM to use the correct reconcile account  
Configure the UNIX platform to use the correct logon account  
Configure the UNIX platform to use the correct reconcile account

IMG-20231015-WA0049.jpg  
Where can you find resources to learn more about the CyberArk Blueprint? (Choose 2)  
CyberArk Blueprint Webpage  
References within the Identity Security Platform  
Product Webinars  
CyberArk University Course


IMG-20231015-WA0050.jpg  
A recently-hired colleague onboarded five new Local Accounts that are used for standalone Windows Servers. After attempting to connect to the servers from PVWA, the colleague noticed that the "Connect" button was greyed out for all five new accounts. What can you do to help your colleague resolve this issue? (Choose 2.)
- Verify that the address field is populated with an IP or FQDN of each server.
- Verify that the correct PSM connection component appears within account platform settings.
- Verify that the address field is blank and that the correct PSM connection component appears within account platform settings.
- Notify the Windows Team that created the new accounts that the CyberArk PAM solution is not designed to manage local accounts on Windows Servers.
- Verify that the "Disable automatic management for this account" setting for each account is not enabled.

#todo #later #dump 

IMG-20231015-WA0051.jpg  
You receive this error:  
"Error in changepass to user domain\user on domain (winRc=5) Access is denied"  
Which could be the cause?  
“Error in changepass to user domaimuser on domain server(- domain fwinkc=5) Acc  
Record



IMG-20231015-WA0052.jpg  
A  
B  
7 Cc  
D

Which configuration file is used by the CPM scanner when scanning UNIX:Linux devices?

UnixPrompts.ini  
plink exe  
dbparm. ini

UnixScanner int



IMG-20231015-WA0053.jpg  
iad

Which built-in report from the reparts page in PVWA displays the number of days until a

A Priieged Accounts Inventory

"= B Privileged Accounts Compliance Status  
Cc Activity Log

> D

Privileged Accounts CPM Status



IMG-20231015-WA0054.jpg  
What is the easiest way to dupti ate an

| RAR Bivatetih Copp gente Ha canter he oer wy  
Rom te PVA rival ray ten ory : : ' Vite gs on  
Co Veo Deseteree copy tart tin aieiy are a : im vi :  
Dumb UME IMS asin gmc Stes

te andl reneme the platform



IMG-20231015-WA0055.jpg  
What are valid ways to invite vendors using the Remote Access portal? (Choose 2.)

Use the vendor invitation form

Call the vendor users and have them scan a QR cade

Use the self-service invitation URL

Add the vendors in PVWA and send them their password.

Contact CyberArk support to help invite the vendors.



IMG-20231015-WA0056.jpg  
What are common ways that organizations leverage the CyberAtk Blueprint tor identity Securt y Su

A

to understand the identity attack chain

to discover all digital identities

to describe the explicit order of aperations for Identity Security  
io assess an organization's security posture  
to build an identity Security roadmap

to secure their human identities

CCESS



IMG-20231015-WA0057.jpg  
Export Vault Data

Export Vault Information  
PrivateArk Chent

Privileged Threat Analytics



IMG-20231015-WA0058.jpg  
CyberArk Defender - PAM - HEMA SURYA PRAKASH YARRAMSETTI  
% Comment:  
tn BYWNA, you ate attempting tu pi

AY A Teron Miike  
What could be the cause?

Recording is uta TSM tnt SSL geo

The browser you ian using os

A

iss

~ CG You da not nave tas Ves  
D

You nessa tr updates the

fobead You ate

also Unabie to download the video



IMG-20231015-WA0059.jpg  
You need to enable the PSM for all platforms  
Where do you perform this task?

Platform Management > (Platform) = U! & Workflows

A.  
— B. Master Policy > Session Management

C.

D.

Master Policy = Privileged Access Workflows

Administration > Options > Connection Components



IMG-20231015-WA0060.jpg  
en the CPM connects to a database, which interface is most commonly used?



IMG-20231015-WA0061.jpg  
A  
~ B  
Cc

D

What is the correct process to install a custom platform from the CyberArk Marketplace?

Locate the custom platform in the Marketplace and click Import

Download the platform from the Marketplace and import it using fhe PVWA

Contact CyberArk Suppart for guidance on how to import the platform

Duplicate an existing platform and align the setting to match the platform from the Marketplace



IMG-20231015-WA0062.jpg  
Access Code

326-212.482

How do you create a cold storage backup?

"OA On the DR Vault, install PARe plate accordina to the Installation quick

eo codfgure Hie logon ini file and detine the Schedule tasks for full and incremental backups.

install the Vault Backup utiity on a different machine from the Enterprise Password Vauit server and trigger the full backup

B  
CG Configure the backup options 1 the PVWA  
D

On the DR Vault, configure the cold storage backup path in TSParn ini file

“Hee  
Wie ae Bg


IMG-20231015-WA0063.jpg  
To manage automated onboarding rules 4 CyherArk user must be ar

UDA Vault Admins  
2B PasswordManagers  
~~ C Auditors

“ D Administrators

ember ofwrech group?



IMG-20231015-WA0064.jpg  
Fann  
if i

Recortiag  
, What can you do to ensure each component server is operational?

POA Logon to PVWA with v10 UI Navigate to Healthcheck. and validate each component server is connected to the Vauit -  
oO 8B. Ping each component server to ensure connectivity  
° Cc. Use the PrivateArk client to connect to the Vault server and validate ail the services are running  
fp OD.

\nstall the Vault Server interface on a remote machine to avoid interactive logon to the Vault OS and review the [TALog log through the Vault Server niedtace::



IMG-20231015-WA0065.jpg  
You want to create a new onboarding rule  
Where do you accomplish this?

A In PVWA. click Reports = Unmanaged Accounts = Rules  
8B In PYWA, click Options = Platform Management = Onboarding Rules  
ae in PrivateArk. click Tools » Onboarding Rules

D.

In PVWA. click Accounts = Onboarding Rules

EP



IMG-20231015-WA0066.jpg  
Platform  
© B. Connection Component  
oc CPM

Vault



IMG-20231015-WA0068.jpg  
-yberArk Defender - PAM - HEMA SURYA PRAKASH YARRAMSETTI

Configure one hme passwords tor the aper

Configure shared account mode nn ihe appro}

Configure bath one line pas

5 anor  
Conhgure abject level access contre ari fm a

he

You have been asked to secure a set of shared ai count. my Cyber  
Which secunty configuration should you te: ommend?

sale

ve

wifes

Peake sate

AL tinge ¢

the apprpe

vater 4

ale: Glatte

eer ay OVP eT

UM eg

in Master Ba icy

Tir arr iat oe



IMG-20231015-WA0069.jpg  
require dual control password access approval

require password change every X days

enforce check-in/check-out excllisive Aleess

enforce one-time password access



IMG-20231015-WA0070.jpg  
4

Recording

Which setting in the Master Policy controls whether PSM is enabled and sessions will be recorded?

“OA Require privileged session monitoring and isolation = Inactive Record and save session activity = active  
OB Require privileged session monitoring and isolation = inactive Record and save session activity = inactive  
OC. Require privileged session monitoring and isolation = active: Record and save session activity = active

oD. Require privileged session monitoring and isolation = active: Record and save session activity = inactive



IMG-20231015-WA0071.jpg  
What does the Minvalidity parameter on a platform polley determine”?

time in minutes befare an empty safe will be automatically deer

~~ A time between a Password retrieval and the account becorning  
B timeout for users signed into the PVWA as configured in the pos  
C minimum amount of tme that Just in Time ACCESS |S valid

- D

ed



IMG-20231015-WA0072.jpg  
“O A SessionRecorderSafe  
© B. SessionSafe  
oc. RecordingsPath

OD. RecordingLocation



IMG-20231015-WA0073.jpg  
Accompany fas nity Basins ate mente : ; ry, an 7 B athe OTT ayer Fhe nyitatin peneess for thext set of vendors  
AteC ining the seri Mie Hamat Pees a garta a oa

Aatwrs

User

Venter Manian

1 Viewer



IMG-20231015-WA0074.jpg  
Which usage can be added as a service account platform?

A Kerberos Tokens  
~ B uS Apphcation Pools
- Cc PowerShell Libraries  
~ Oo

Loosely Connected Devices

Ls



IMG-20231015-WA0075.jpg  
yberArk Defender - PAM - HEMA SURYA PRAKASH YARRAMSETTI

OA Set the parameter RCAllowManualReconciation ti Yes  
B Set the parameter ChangePasswordinResethode to Yes  
Set the parameter lanoreReconcweAnMssingArc aunt io No

Set the UntockUserOnRecancile io Yes



IMG-20231015-WA0076.jpg  
Which authentication methods can you use to aut

UIA Password  
1B OpeniD  
oC. Centificate  
HD. SAML  
E.

OTP

You are adding a new application in the Remote A

cCcess portal

henticate users to the PVWA? (Choose 2)



IMG-20231015-WA0077.jpg  
OA

8B  
c  
D  
is

You need to identity the most powerful accounts i your ordanication th prenare for tie -pitiat £  
Which tools or features can be used te locate and onboard these accounts? i hence 7

Oiscovery and Audd RNA

CyberArk’s Comm

Onboarding and Secure

Accounts Discovery

Privilege Account Matrix (PAM) XLS



IMG-20231015-WA0078.jpg  
CyberArk Defender - PAM - HEMA PRAKASH YARRAMSETTI

Access Code

326-212-48:

A Manage Users

B Audit Users

c Read Activity

Dd View Entitlemenis  
E

List Accounts



IMG-20231015-WA0079.jpg  
You have been given the requirement that certain accounts cannot have their passwords updated dunng business ours  
How can you set up a configuration to meet this requirement?

oO Change settings on the CPM configuration safe so that access 1s permitted after business hours only.

Update the password change parameters of the platform to match the permitted tme frame

ie)

A  
OB.  
c Disable automatic CPM management for all accounts that are assigned to this platform  
D.

oa Add an exception to the Master Policy to allow the action for this platform during the permitted time



IMG-20231015-WA0080.jpg  
Cyberfrk Defender - PAM - HEMA SURYA PRAKASH YARRAMSETTI

UME e =

Werebosrd

\n addition to add accounts and update account contents which additional permission on the safe 1§ required

Oa Upload Accounts Properties  
Os Rename Accounts

one Update Account Properties

fF OD Manage Safe



IMG-20231015-WA0081.jpg  
When should vault keys be rotated?

A when it !s copied to file systems outside the vault  
~ &B annually  
~ Cc whenever a CyberArk user leaves the organization  
2D

when migrating to a new data center



IMG-20231015-WA0082.jpg  
CyberArk Defender - PAM - HEMA SURYA PRAKASH YARRAMSETTI  
~ Ea

Toe tin Pay

between one tite

Winch statement about the Master Pobpy best ost mbes fie dlrs fies

Utero d thea Couns daveicd font fite wate automatically

"GOA Laclusive access moans That onty speech aeungp obras tery re tia ae ner el yor been  
OB Exctusive access Jocks the ancunat -adediiutess bat bi gers de Der t red pag phaueee f  
oc Lirdusive access is enablod by defanibis the Master bhegg fer tere jae et Puen gt uy i} He ens  
Exclusive access allows ony ann petsot lo dies ko ibati ae Gen) at kine nega " or es) pee Debates after the Ria vaielityPengud pened OxpNes

ubiali Hh ids ea

L Fy ull  
“ dekacithit alee



IMG-20231015-WA0084.jpg  
CyberArk Defender -

A Member of Domain Admin Group  
B Member of LDAP Admin Group  
Cc Read and Write Permissions  
D

Read Only Permissions



IMG-20231015-WA0085.jpg  
Which authorizations are required in a recording safe to allow a group to view recordings’?

| [

|  
\ +  
Retrieve accounts/files | ' | Required

List accounts/files Not Required:

View audit

Access Safe without  
a" ‘ Ohans aesveer lets  
Confirmation

Create Folders

| Drag answer bare



IMG-20231015-WA0086.jpg  
Comment

Anew HTML5 Gateway has been deployed in your organization

Unordered Options

| Administration Options

Privileged Session Management

ponnaured PSM Servers and select existing PSM  
0s

Connection Details

Add PSM gateway

from the PVWA, arrange the steps to configure a PSM host to use the HTML5 Gateway in

Ordered Response

the correct sequence

2



IMG-20231015-WA0087.jpg  
Windows events text recorder with automatic play-back

A.

1. Windows events text recorder and universal keystrokes recording simultaneously  
C. Universal keystrokes text recorder with windows events text recorder disabled  
D.

Custom audio recording for windows events


IMG-20231015-WA0088.jpg  
F

Shdepoa  
Which statement ts true about Setting the reconcile account at the platform level?

This is the only way to enable automatic reconciliation of account passwords

CPM performance will be IMproved when the reconcile account ts set at the platform level

B  
c Asule can be used to specify the reconcile accuunt dynaineally of a specific reconcile account can be selected  
D

This configuration prevents the association from becoming broken if the re

concile account 1s moved to a different safe



IMG-20231015-WA0089.jpg  
CyberArk Defender - PAM - HEMA SURYA PI

Where can you assign a Reconcile account? (Choose 2 }

“OA in PVWAat the account level

OB. in PVWA in the platform configuration  
: oO Cc. in the Master policy of the PYWA

OC D. at the Safe level

Oe

in the CPM settings



IMG-20231015-WA0090.jpg  
add accounts

rename accounts  
update account content  
update account properties

view safe members

add safes



IMG-20231015-WA0092.jpg  
PVWAMonitor

ReportUsers  
PVWaAReports

Operators



IMG-20231015-WA0093.jpg  
Which parameters can be used to harden the Credential Files (CredFiles

OS Username  
Current machine IP  
Current machine hostname

Operating System Type (Linux:Windows. HP-UX)  
Vault IP Address

Time Frame

) while using CreateCredPile UMmny



IMG-20231015-WA0094.jpg  
CyberArk Defender - PAM - HEMA SURYA PRAKASH YARRAMSETTI

You are concerned about the Windows Domain password changes occur Q during business hours  
Which settings must be updated to ensure passwords are only rotated outside of business hours?

In the platform policy

Automatic Password Management = Password Change » ToHour & FromHour

B in the Master Policy  
Account Change Window = ToHour & From Hour

~ € Admunistration Settings  
CPM Settings > ToHour & FromHour

- DB On each individual account  
Edit > Advanced > ToHour & FromHour



WhatsApp Image 2023-10-15 at 11.01.27_14ffa2af.jpg  
Your organization has a requirement to allow only one user to “check out passwords” and connect through the PSM securely.  
What needs to be configured in the Master policy to ensure this will happen?

OA Enforce check-in'check-out exclusive access = active, Require privileged session monitor ng and isolation = active

0B. Enforce check-in‘check-out exclusive access =

mactive: Require privileged session monitoring and isolation = inactive

OC. Enforce check-inicheck-out exclusive access = inactive, Record and save session activity = active

oD. Enforce check-in/check-out exclusive access = active, Record and save session activity = active



WhatsApp Image 2023-10-15 at 11.01.27_5bf82ef3.jpg  
The Privileged Access Management solution provides an out-of-the-box target platform to manage SSH keys. called UNIX Via SSH Keys.  
” How are these keys managed?

OA CyberArk stores Private keys in the Vault and updates Public keys on target systems

QB CyberArk stores Public keys in the Vault and updates Private keys on target systems

EOC, CyberArk does not store Public or Private keys and instead uses a reconcile account to create keys on demand

OD. CyberArk stores both Private and Public keys and can update target systems with either key



WhatsApp Image 2023-10-15 at 11.01.27_ea51b6cf.jpg  
What can you do to ensure each com

xe) A.  
© B.  
“OC

OD

PONEAL Sever Ss operat onal?

Logon to PVWA with v1 Ui navigat

eto Heath,

4 and validate earch ¢ omponent serv.

$ Conner  
Ping each component server to

StS

Use the PrivateArk cient to cor

‘ver_and vaildale all the services are fun

mwnAg  
Install the Vault Server interface one

femote maci

ne tC avond interactive logan to the Vauit OS and review the ITAL

rough the Vault Server interface



WhatsApp Image 2023-10-15 at 11.01.28_9d7b7b19.jpg  
CyberArk Defender - PAM - Dattatraya B Ingale

What must you specify when contouring a dist overy Seat for NIK?! (sanse 21

tA Vault Adminstuaty  
B CPM Scanbe:  
me foot password for ean h machine  
tL! D hst of machines to scan

CLE safe for discovered accounts



WhatsApp Image 2023-10-15 at 11.01.28_aeb1356e.jpg  
yberArk Defender - PAM - Dattatraya B Ingale

According to CyberArk, which issues most commonly cause Installed components to display 4 discorinected in the System Health Dashboard? (Choose 2

Qa network instabiities:outages

QB vault license expiry  
oc credential de-sync  
ao browser compatibility issues

| O E. installed location file corruption



WhatsApp Image 2023-10-15 at 11.01.28_d6d6e70f.jpg  
COR  
OB.  
boc  
=O D.

List Accounts. Use Accounts  
List Accounts. Use Accounts  
Use Accounts

List Accounts. Use Accounts

E. To use PSM connections while in the PVWA what are the minimum safe permissions a user or group will need?

Retrieve Accounts

Retrieve Accounts, Access Safe without confirmation



WhatsApp Image 2023-10-15 at 11.03.04_13280e20.jpg  
Dg

Drag

Drag answer fete

Recovery Private Key

Recovery Publi Key

SSH Kays

Wisnaaan nn



WhatsApp Image 2023-10-15 at 11.05.11_dba56cfd.jpg  
t Recorcnng  
Which authorizations are required in a recording safe to allow a group to view recordings? :



WhatsApp Image 2023-10-15 at 11.05.12_2d037e76.jpg  
Which authorizations are require

d in a tecording sate to allow a group to view recordings?

Recording

Retrieve accounts/files Required  
List accounts/files Required  
View audit Required

Access Safe without  
confirmation

Create Folders