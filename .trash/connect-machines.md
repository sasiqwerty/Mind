---
aliases: 
tags: 
date created: Tuesday, September 12th 2023, 8:26:54 pm
date modified: Tuesday, September 12th 2023, 8:29:07 pm
---
virtual box

This is possible with VirtualBox .

You need to create a `natnetwork` , you can do it by command line .

```
VBoxManage natnetwork add --netname natnet1 --network "192.168.15.0/24" --enable
```

And for each VM , change the _Adapter 1_ to be attach to a **NAT Network**

After rebooting , each VM must be able to ping other VM and ping outside .

`ping 8.8.8.8` must work

PS: tested on VirtualBox 6.1.8 on macos Catalina

PS1: the network "192.168.15.0/24" from the example must not conflict with your local network or others network to access internet , you may need to change .

## 7.35. VBoxManage Natnetwork

NAT networks use the Network Address Translation (NAT) service, which works in a similar way to a home router. It groups systems using it into a network and prevents outside systems from directly accessing those inside, while letting systems inside communicate with each other and outside systems using TCP and UDP over IPv4 and IPv6.

A NAT service is attached to an internal network. Virtual machines to make use of one should be attached to it. The name of an internal network is chosen when the NAT service is created, and the internal network will be created if it does not already exist. The following is an example command to create a NAT network:

VBoxManage natnetwork add --netname natnet1 --network "192.168.15.0/24" --enable

Here, `natnet1` is the name of the internal network to be used and `192.168.15.0/24` is the network address and mask of the NAT service interface. By default, in this static configuration the gateway will be assigned the address 192.168.15.1, the address after the interface address, though this is subject to change.

To add a DHCP server to the NAT network after creation, run the following command:

VBoxManage natnetwork modify --netname natnet1 --dhcp on

The subcommands for **VBoxManage natnetwork** are as follows:

VBoxManage natnetwork add --netname <name>  
                         [--network <network>]  
                         [--enable|--disable]  
                         [--dhcp on|off]  
                         [--port-forward-4 <rule>]  
                         [--loopback-4 <rule>]  
                         [--ipv6 on|off]  
                         [--port-forward-6 <rule>]  
                         [--loopback-6 <rule>]
    

**VBoxManage natnetwork add**: Creates a new internal network interface, and adds a NAT network service. This command is a prerequisite for enabling attachment of VMs to the NAT network. Parameters are as follows:

`--netname <name>`

Where <name> is the name of the new internal network interface on the host OS.

`--network <network>`

Where <network> specifies the static or DHCP network address and mask of the NAT service interface. The default is a static network address.

`--enable|--disable`

Enables and disables the NAT network service.

`--dhcp on|off`

Enables and disables a DHCP server specified by `--netname`. Use of this option also indicates that it is a DHCP server.

`--port-forward-4 <rule>`

Enables IPv4 port forwarding, with a rule specified by <rule>.

`--loopback-4 <rule>`

Enables the IPv4 loopback interface, with a rule specified by <rule>.

`--ipv6 on|off`

Enables and disables IPv6. The default setting is IPv4, disabling IPv6 enables IPv4.

`--port-forward-6 <rule>`

Enables IPv6 port forwarding, with a rule specified by <rule>.

`--loopback-6 <rule>`

Enables the IPv6 loopback interface, with a rule specified by <rule>.

VBoxManage natnetwork remove --netname <name> 

**VBoxManage natnetwork remove**: Removes a NAT network service. Parameters are as follows:

`--netname <name>`

Where <name> specifies an existing NAT network service. Does not remove any DHCP server enabled on the network.

VBoxManage natnetwork modify --netname <name>  
                            [--network <network>]  
                            [--enable|--disable]  
                            [--dhcp on|off]  
                            [--port-forward-4 <rule>]  
                            [--loopback-4 <rule>]  
                            [--ipv6 on|off]  
                            [--port-forward-6 <rule>]  
                            [--loopback-6 <rule>]
    

**VBoxManage natnetwork modify**: Modifies an existing NAT network service. Parameters are as follows:

`--netname <name>`

Where <name> specifies an existing NAT network service.

`--network <network>`

Where <network> specifies the new static or DHCP network address and mask of the NAT service interface. The default is a static network address.

`--enable|--disable`

Enables and disables the NAT network service.

`--dhcp on|off`

Enables and disables a DHCP server. If a DHCP server is not present, using enable adds a new DHCP server.

`--port-forward-4 <rule>`

Enables IPv4 port forwarding, with a rule specified by <rule>.

`--loopback-4 <rule>`

Enables the IPv4 loopback interface, with a rule specified by <rule>.

`--ipv6 on|off`

Enables and disables IPv6. The default setting is IPv4, disabling IPv6 enables IPv4.

`--port-forward-6 <rule>`

Enables IPv6 port forwarding, with a rule specified by <rule>.

`--loopback-6 <rule>`

Enables IPv6 loopback interface, with a rule specified by <rule>.

VBoxManage natnetwork start --netname <name>
    

**VBoxManage natnetwork start**: Starts the specified NAT network service and any associated DHCP server. Parameters are as follows:

`--netname <name>`

Where <name> specifies an existing NAT network service.

VBoxManage natnetwork stop --netname <name>
    

**VBoxManage natnetwork stop**: Stops the specified NAT network service and any DHCP server. Parameters are as follows:

`--netname <name>`

Where <name> specifies an existing NAT network service.

VBoxManage natnetwork list [<pattern>] 

**VBoxManage natnetwork list**: Lists all NAT network services, with optional filtering. Parameters are as follows:

`[<pattern>]`

Where <pattern> is an optional filtering pattern.