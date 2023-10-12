---
aliases: 
tags: 
date created: Thursday, August 31st 2023, 8:57:24 pm
date modified: Thursday, August 31st 2023, 8:58:44 pm
---

## Installation and Configuration Course

admin course completed

how to install and configure

## Sequence to Follow when Installing

before 10.7

vault > cpm > pvwa > psm

after 10.7

vault > pvwa > cpm > psm

the order was changed as the CPM needs APIs of PVWA, so if we install the PVWA account discovery process will run smoothly

## Installation

pvwa and cpm can be installed together?

psm servers not installed together in a single server

psmp is installed in a linux server

vault is installed in a non-domain joined server

### Vault Software Can Be Downloaded from

in the lab guide its in the shared z drive

## NIC Hardening

network interface card hardening

  

- remove all the unnecessary network settings

- only keep the ipv4 and ipv6

- how to get subnet mask, Ip, and default gateway

- type ipconfig and ensure that the values are accurate

- vault server is not joined to the domain, its never done

- adding vault server under domain, if policies are changed in domain the vault policies will change if added to domain

- vault should be under workgroup? this is doubt that needs to be fixed

- vault is a hardened server

- remove all DNS server details

- in the dns tab deselect the register this connections address in DNS

- in the WINS tab deselect the LMHOSTS lookup setting

- select disable NETBIOS over TCP/IP

  

other servers wont be able to find this server when the above settings are followed

  

- check the server operating system

- windows 2012 server is not recommended

- windows 2012 and 2019 server operating system are advised

- in 2019 server operating system, we can not unistall the options in NIC they can only be unchecked

- in 2016 they can be uninstalled

- diff between ipv4 and ipv6

  

    this only applies in the lab, copy the files from the z drive and then perform the nic hardening

### Vault Install Starts

- setup.exe - run as admin, the vault setup

- on a fresh install there wont be any services running as nothing is installed

- accept the EULA

- name and company name will be asked fill the details accordingly ( not important ) wont affect the install

- standalone and cluster node vault installation options are shown and we select standalone

- the location of install is asked, the drive location, just keep in mind that it shouldn't be a deep directory

- choose a folder for safes and their storage location, the physical location of the safes when they are created

  

- license is required for install
- license path is also asked the format is in XML language
- the key will be in the license file
- one PSM can support 100 concurrent connections but the license will limit the number of connections
- pwva users are also controlled here
- components how many is mentioned here
- according to the needs the license is generated
- sales exec will do the license stuff
- operator cd is required for install
- server key is used when the vault starts and stop, the key will get loaded into the memory
- notes stopped at 50 min in the first video continue later 