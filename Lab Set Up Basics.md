---
aliases: 
tags: 
date created: Monday, January 1st 2024, 4:31:22 pm
date modified: Monday, January 1st 2024, 6:53:33 pm
---

## Basics

### 1. How to Set up the Lab?

 Having a lab in your PC is creating the virtual version of the Cyberark infra in one place. It enables the user to learn the concepts and apply them rapidly.

Note : **We Wont Be Covering how to Set up a Remote Lab in a server**

### 1. Physical Requirements for Setting Up a Lab in Your Own System

This table categorizes the physical requirements for setting up a lab in your own system into minimum and optimal (best results) specifications.

| Requirement Level | Processor            | RAM         | Storage           |
|-------------------|----------------------|-------------|-------------------|
| Minimum           | i5 or Ryzen 5        | 16 GB   DDR4    | 500 GB SSD        |
| For Best Results  | i7 or Ryzen 7        | 32 GB DDR5  | 1 TB NVME SSD     |

### 2. Enabling Virtualization

- Virtualization is a technology that allows you to create multiple simulated environments or dedicated resources from a single, physical hardware system.  
- It's a powerful tool in computing that enables better efficiency and flexibility in using computer hardware.

#### Enabling Virtualization at the BIOS Level and Its Necessity

To enable virtualization at the BIOS level:

1. **Restart your computer** and enter the BIOS setup. This is typically done by pressing a key during the boot process, like F2, F12, Del, or Esc.
2. **Navigate to the CPU or Advanced settings** section. The exact location and name vary by manufacturer.
3. **Find the Virtualization setting**. It might be labeled as 'VT-x', 'AMD-V', 'SVM', 'Virtualization Technology', or similar.
4. **Enable the setting** and save your changes.

**Why at the BIOS Level?**
- Virtualization technology is integrated into the CPU. Enabling it at the BIOS level allows the operating system and applications to access this hardware feature directly.
- This low-level enablement ensures that the virtualization capabilities are available and operational as soon as the operating system loads, providing better performance and stability for virtual machines.

### 3. Applications Needed to Set Up a Lab

Virtual Box or VMware

#### VirtualBox: A Simple Overview

- VirtualBox is a virtualization software that works on Windows, macOS, Linux, and Solaris. 
- It's free and open source, available under the GNU GPL v3. It allows you to run multiple operating systems on one computer, making it useful for both personal and business use. 
- It's known for being feature-rich and high-performing.  

[Oracle VM VirtualBox](https://www.virtualbox.org/) - Main Site  
[Oracle® VM VirtualBox®](https://www.virtualbox.org/manual/UserManual.html) - User Manual

### 4. Basic Networking Concepts Needed

### IP Addresses

- **Static IP Address**: A permanent and fixed Internet Protocol address assigned to a device, typically for consistent network identification.
- **Dynamic IP Address**: A temporarily assigned IP address that changes each time a device connects to the network, usually managed by a DHCP server.  

Table comparing Static and Dynamic IP Addresses:

| Feature               | Static IP Address                                | Dynamic IP Address                              |
|-----------------------|--------------------------------------------------|-------------------------------------------------|
| **Definition**        | A permanent IP address assigned to a computer.   | An IP address that changes every time you connect. |
| **Assignment**        | Manually set by an administrator.               | Automatically assigned by a DHCP server.       |
| **Consistency**       | Remains the same over time.                      | Changes with each new connection or lease time.|
| **Best Used For**     | Servers, websites, remote access systems.        | Most home networks, consumer devices.          |
| **Cost**              | Often more expensive, less common for home use. | Typically included in standard internet service. |
| **Management**        | Requires more management and setup.             | Easier to manage, less technical knowledge needed. |
| **Risk of IP Conflicts** | Lower, as the address is unique and static.    | Higher, especially in networks with many devices. |
| **Flexibility**       | Less flexible, as changes require manual reconfiguration. | More flexible, easily accommodates network changes. |

This table highlights the key differences between static and dynamic IP addresses, offering insights into their application, management, and suitability for different network scenarios.

### Windows Firewall

A firewall is a security system that controls and monitors network traffic based on predetermined security rules. It acts as a barrier between a trusted internal network and untrusted external networks, such as the internet, to prevent unauthorized access and cyber threats.  
Firewalls can be implemented in both hardware and software, or a combination of both.

## VMs

### 1. How to Set up VMs?

Click **New** in the VirtualBox Manager window. The **Create Virtual Machine** wizard is shown, to guide you through the required steps for setting up a new virtual machine (VM).  
![[Pasted image 20240101184009.png]]  
The **Create Virtual Machine** wizard pages are described in the following sections.
- **ISO Image.** Select an ISO image file. The image file can be used to install an OS on the new virtual machine or it can be attached to a DVD drive on the new virtual machine.
- **Skip Unattended Installation.** Disables unattended guest OS installation, even if an ISO image is selected that supports unattended installation. In that case, the selected ISO image is mounted automatically on the DVD drive of the new virtual machine and user interaction is required to complete the OS installation
- Create Virtual Machine Wizard: Unattended Guest OS Install  
![[Pasted image 20240101184113.png]]
- **Base Memory.** Select the amount of RAM that Oracle VM VirtualBox should allocate every time the virtual machine is started. The amount of memory selected here will be taken away from your host machine and presented to the guest OS, which will report this size as the virtual machines installed RAM.
- **Processor(s).** Select the number of virtual processors to assign to the VM.  
    It is not advised to assign more than half of the total processor threads from the host machine.
- **Enable EFI.** Enables Extensible Firmware Interface (EFI) booting for the guest OS.
- Create Virtual Machine Wizard: Virtual Hard Disk  
![[Pasted image 20240101184311.png]]

### 2. Types of Snapshots and why We Need Them.

![[Pasted image 20240101184446.png]]

The Snapshots window includes a toolbar, enabling you to perform the following snapshot operations:

- **Take.** Takes a snapshot of the selected VM. See [Section 1.11.1, “Taking, Restoring, and Deleting Snapshots”](https://www.virtualbox.org/manual/UserManual.html#snapshots-take-restore-delete "1.11.1. Taking, Restoring, and Deleting Snapshots").
- **Delete.** Removes a snapshot from the list of snapshots. See [Section 1.11.1, “Taking, Restoring, and Deleting Snapshots”](https://www.virtualbox.org/manual/UserManual.html#snapshots-take-restore-delete "1.11.1. Taking, Restoring, and Deleting Snapshots").
- **Restore.** Restores the VM state to be the same as the selected snapshot. See [Section 1.11.1, “Taking, Restoring, and Deleting Snapshots”](https://www.virtualbox.org/manual/UserManual.html#snapshots-take-restore-delete "1.11.1. Taking, Restoring, and Deleting Snapshots").
- **Properties.** Displays the properties for the selected snapshot. The **Attributes** tab is used to specify a Name and Description for the snapshot. The **Information** tab shows VM settings for the snapshot.
- **Clone.** Displays the **Clone Virtual Machine** wizard. This enables you to create a clone of the VM, based on the selected snapshot.
- **Settings.** Available for the Current State snapshot only. Displays the **Settings** window for the VM, enabling you to make configuration changes.
- **Discard.** For a running VM, discards the saved state for the VM and closes it down.
- **Start.** Start the VM. This operation is available for the **Current State** item.

### 2. How to Enable File Sharing? ( Avoid Hardening the server) - VirtualBox Guest Additions

![[WhatsApp Image 2024-01-01 at 18.49.19_3e9a089b.jpg]]

With the _shared folders_ feature of Oracle VM VirtualBox, you can access files of your host system from within the guest system. This is similar to how you would use network shares in Windows networks, except that shared folders do not require networking, only the Guest Additions. Shared folders are supported with Windows 2000 or later, Linux, and Oracle Solaris guests. Oracle VM VirtualBox includes experimental support for Mac OS X and OS/2 guests.

Shared folders physically reside on the _host_ and are then shared with the guest, which uses a special file system driver in the Guest Additions to talk to the host. For Windows guests, shared folders are implemented as a pseudo-network redirector. For Linux and Oracle Solaris guests, the Guest Additions provide a virtual file system.

To share a host folder with a virtual machine in Oracle VM VirtualBox, you must specify the path of the folder and choose a _share name_ that the guest can use to access the shared folder. This happens on the host. In the guest you can then use the share name to connect to it and access files.

There are several ways in which shared folders can be set up for a virtual machine:

- In the window of a running VM, you select **Shared Folders** from the **Devices** menu, or click on the folder icon on the status bar in the bottom right corner.
- If a VM is not currently running, you can configure shared folders in the virtual machine's **Settings** window.

#### There Are Two Types of Shares

- Permanent shares, that are saved with the VM settings.
- Transient shares, that are added at runtime and disappear when the VM is powered off. These can be created using a check box in VirtualBox Manager, or by using the `--transient` option of the **VBoxManage sharedfolder add** command.

### NAT Network

The NAT Networks tab in Network Manager lists all NAT networks that are currently in use.

- Click **Create** to add a new NAT network to the list.
- Click **Remove** to remove a NAT network from the list.
- Click **Properties** to show or hide settings for the selected NAT network.

To configure a NAT network, select the network name in the **Name** field and do the following:

- Use the **General Options** tab to configure the network settings used by the NAT network. For example, the network address and mask of the NAT service interface.

![[WhatsApp Image 2024-01-01 at 18.49.46_c340da25.jpg]]

## To Be Continued

## Windows and Networking

1. What is an ISO file and why is it used for windows installation?
2. How is an OS installed generally?
3. What are ISO files and VDI files related to VMs
4. Creating VMs with windows and assigning storage, RAM and thread count.
5. Understanding the CyberArk requirements and creating VMs accordingly.
6. Creating a NAT Network and pinging all the servers in the NAT Network.
7. Assigning STATIC IP addresses for all the systems in domain and doing the ping test.
8. Installing the [[Active Directory]]
9. Promoting a server to domain controller.
10. Creating the Users and groups needed for [[CyberArk]] in the [[Domain]] controller.
11. Domain joining the component server.
12. Learning about Network Card Interface for Vault Installation.