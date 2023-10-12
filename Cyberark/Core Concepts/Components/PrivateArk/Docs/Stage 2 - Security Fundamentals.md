## Stage 2 - Security Fundamentals

Compromising privileged accounts is a central objective for any attacker, and CyberArk Privileged Access Manager - Self-Hosted is designed to help improve your organization’s ability to control and monitor privileged activity. As with any security solution, it is essential to secure Privileged Access Manager - Self-Hosted to ensure the controls you have implemented are not circumvented by an attacker.

The controls described in this document are the minimal requirements for protecting your Privileged Access Manager - Self-Hosted deployment, and therefore your privileged accounts. Consolidated by our team, these controls reflect our experience in implementing industry best practices when supporting our customers in installing and operating our products. The requirements are also based upon analysis of various reports made by companies that experienced a security incident and other research data generally available in the industry. Details are included in [Digital Vault Security Standard](https://docs.cyberark.com/PAS/12.6/en/Content/Security/Standards-CyberArks%20Digital%20Vault%20Server%20Security%20Standard.htm).

**Kerberos Protocol Vulnerabilities:** 
- Recent cyberattacks have exploited weaknesses in the Kerberos protocol to infiltrate and move undetected within target environments.
- To counter this, the Digital Vault server should operate on a trusted, isolated platform.

**Minimal Requirements for Digital Vault Security:** 
1. **No Domain Membership**: The Digital Vault server should remain independent and not be a part of any Windows Domain.
2. **Software Exclusivity**: Avoid installing third-party software on the Digital Vault server to prevent potential vulnerabilities.
3. **Inbound Traffic Restriction**: Limit inbound network traffic to the Digital Vault server exclusively to CyberArk protocols.
4. **Outbound Traffic Restriction**: Outgoing network traffic from the Digital Vault should be limited to CyberArk protocols and sanctioned integrations, like LDAPs for user/group provisioning or SMTPs for email notifications.
5. **Unique OS Credentials**: Ensure the credentials for the Digital Vault server operating system are distinct and not replicated elsewhere.
6. **Consistent Infrastructure Controls**: Infrastructure that hosts the Digital Vault server should have identical security controls as those applied to the Digital Vault server itself.
7. **Regular Microsoft Security Updates**: Integrate the Digital Vault with a Windows Patch server (WSUS) and ensure regular updates. WSUS best practices include:
   - Adhering to Microsoft Security guidelines.
   - Dedicate a WSUS server solely for updating the Digital Vault or, at a minimum, set up a dedicated computer group for updates.
   - Enable WSUS to operate with HTTPS and a digital certificate.
   - Always use the actual WSUS IP address, avoiding DNS names.
   - Temporarily enable the connection between WSUS and the Vault only during update application times. Utilize WSUS scripts from the CyberArk Vault installation package for this purpose.
8. **Network Firewalls**: Leverage network-based firewalls to regulate, encrypt, and authenticate incoming administrative traffic.

**Infrastructure Recommendation:** 
- Due to the compounded risks and intricate nature of guaranteeing controls on underlying infrastructure like VMWare ESX and its supporting SAN, it's stressed that on-premise Digital Vault servers should be physical, not virtualized.

**Additional Resource:** 
- For an in-depth look into these guidelines and more, one should refer to the "Digital Vault Security Standard" document.

Overall, this guide emphasizes a multi-layered approach to security, ensuring that every aspect of the Digital Vault's environment is optimized for protection. Cybersecurity threats evolve, but with robust preventive measures, the risks can be substantially mitigated.


### [Use multi-factor authentication](https://docs.cyberark.com/PAS/12.6/en/Content/Security/Security%20Fundamentals-Introduction.htm#)

Using multi-factor authentication to Privileged Access Manager - Self-Hosted for all users and product administrators, enables you to mitigate common credential theft techniques, for example:

- Key loggers
- Tools capable of harvesting plaintext passwords

The list you provided offers a set of best practices for securing the deployment of CyberArk components and maintaining the integrity of privileged accounts. These practices emphasize security in an Active Directory (AD) environment, particularly in mitigating credential theft risks like Pass-the-Hash (PtH) attacks.

Here's a clear breakdown of the points:

1. **Mitigate Credential Theft**: CyberArk component servers should follow Microsoft's best practices to reduce credential theft risks, ensuring they are as secure as domain controllers (tier 0). Reference is provided to Microsoft's guide on "Mitigating Pass-the-Hash (PtH) Attacks and Other Credential Theft Techniques."

2. **Component Servers Domain Membership**: It might be safer to keep CyberArk component servers outside the domain. 

3. **Separate Installation for Components**: For best security, consider installing each CyberArk component on a separate server. If budget or infrastructure constraints make this infeasible, hardening measures are available for single-server installations of all components.

4. **DMZ Installation**: Avoid installing all components on a single server located in the Demilitarized Zone (DMZ). 

5. **Software Exclusivity**: To ensure effective hardening, do not install applications unrelated to CyberArk on the component servers.

6. **Access Restrictions**: Restrict the number of accounts with access to CyberArk component servers. If domain accounts are used for access, ensure these accounts don't have permissions for domain controllers, member servers, or workstations.

7. **Domain Credential Restrictions**: Minimize the number of domain credentials that can access the component servers.

8. **Network Protection**: Implement network-based firewalls and IPsec. These will restrict inbound administrative traffic, encrypt it, and authenticate its source. When accessing component servers, use the Privileged Session Manager (PSM) and the local administrator account.

9. **Application Allowlisting**: Employ application allowlisting to ensure only authorized applications can execute, reducing the risk from potentially malicious or unverified software.

10. **Update Regularly**: Consistently apply Microsoft's security patches and updates to keep the system protected against known vulnerabilities.

These recommendations are vital for organizations looking to safeguard their privileged account management systems. Given the sensitivity of data and operations managed by platforms like CyberArk, ensuring stringent security measures is paramount.