---
aliases: 
tags: 
date created: Monday, October 9th 2023, 6:52:15 pm
date modified: Monday, October 9th 2023, 6:56:02 pm
---

## **Snapshot Summary**:

A snapshot is a preserved point in time for a virtual machine. Key components of a snapshot include:
- **VM Settings**: A snapshot captures the entire VM settings. Restoring a snapshot will also restore these settings. These settings are stored in a machine configuration (an XML text file) and use minimal space.
- **Virtual Disks' State**: Snapshots save the full state of all virtual disks. Reverting to a snapshot undoes all changes to the machine's disks. However, this is true primarily for virtual hard disks in "normal" mode. Technically, Oracle VM VirtualBox uses differencing images to track changes since the snapshot, and restoring a snapshot discards these changes. Details on this mechanism can be found in [Section 5.5, “Differencing Images”](https://www.virtualbox.org/manual/UserManual.html#diffimages).
    - The differencing image starts small but grows with each write operation post-snapshot.
- **Memory State (If Applicable)**: If taken while the machine is active, the snapshot includes the machine's memory state. Resuming from this snapshot picks up from where it was taken. Note that this memory state file can be as large as the VM's memory, consuming significant disk space.

**Options in Oracle VM VirtualBox**:

1. **Save the Machine State**: 
    - Freezes the VM and saves its entire state to the local disk.
    - On restart, the VM continues from where it was paused, similar to suspending a laptop by closing its lid.
2. **Send the Shutdown Signal**:
    - Sends an ACPI shutdown signal to the VM.
    - Mimics pressing the power button on a physical computer, triggering a proper shutdown within the VM.
3. **Power Off the Machine**:
    - Stops the VM without preserving its state.

**Oracle VM VirtualBox Command-Line Options**:

1. **Pause the VM**:
    ```bash
    VBoxManage controlvm <vm> pause
    ```
    - Temporarily halts the VM without permanently altering its state.
    - The VM window turns gray, indicating it's paused.
    - GUI Equivalent: "Pause" item in the "Machine" menu.

2. **Save the VM State**:
    ```bash
    VBoxManage controlvm <vm> savestate
    ```
    - Saves the VM's current state to the disk and stops the VM.
    - GUI Equivalent: "Close" item in the "Machine" menu followed by "Save the machine state" option.