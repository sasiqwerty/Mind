---
aliases: new user linux
tags: 
date created: Monday, July 31st 2023, 3:21:02 pm
date modified: Thursday, December 14th 2023, 10:10:47 pm
---
To create a new privileged user in a Linux server, you can follow these steps. I'll assume you have administrative or root access to the server:

1. **Connect to the Server**: Log in to the Linux server using SSH or directly through the console as the root user or any user with sudo privileges.

2. **Add a New User**: Use the `adduser` or `useradd` command to create a new user. The `adduser` command is a higher-level interface that automatically sets up the user's home directory and some other configurations, while `useradd` is more basic and requires additional options for setting up the user environment. I'll use `adduser` in this example:

```bash
sudo adduser newusername
```

Replace "newusername" with the desired username for the new privileged user.

1. **Set the Password**: Once the user is created, set a password for the new user:

```bash
sudo passwd newusername
```

You will be prompted to enter and confirm the new password.

1. **Grant Administrative Privileges**: By default, the new user will have standard user privileges. If you want to grant administrative privileges to this user, you can add the user to the `sudo` or `wheel` group. Members of the `sudo` group can run commands with `sudo` to perform administrative tasks.

On some Linux distributions, the `sudo` group is used, while on others (like CentOS and some Debian-based distributions), the `wheel` group is used. Check your distribution's documentation to confirm which group to use.

**Using `sudo` group**:

On distributions that use the `sudo` group, you can add the user to the `sudo` group using the `usermod` command:

```bash
sudo usermod -aG sudo newusername
```

**Using `wheel` group**:

On distributions that use the `wheel` group, you can add the user to the `wheel` group using the `usermod` command:

```bash
sudo usermod -aG wheel newusername
```

1. **Verify Administrative Privileges**: To verify that the new user has administrative privileges, you can try running a command with `sudo`:

```bash
sudo some_command
```

You will be prompted to enter the user's password, and if everything is set up correctly, the command should execute with administrative privileges.

That's it! You have successfully created a new privileged user in the Linux server. Remember to use administrative privileges responsibly and grant them only to trusted users who need them for specific tasks.