#learn 
Zero trust is a philosophy and practice of network data security that assumes every user, device and service that attempts to connect to an organization’s network is hostile until proven otherwise. The fundamental principle of zero trust is to secure an organization’s data wherever it might live, allowing only legitimate users and entities access to relevant resources and assets.

The modern data landscape includes cloud or SaaS deployments, data centers, remote workforces, mobile devices and a myriad of apps, which can no longer be protected by traditional security strategies. Allowing data and workloads to live, operate and be accessed in this expanded attack surface leaves many organizations increasingly susceptible to a host of security vulnerabilities and access issues. This problem was only compounded by industry-wide responses to COVID-19, in which companies moved quickly to support an all-remote work environment.  

In 2020, attackers exploited software created by the company SolarWinds as a conduit to gain access to hundreds of the company’s customers. Consequently, zero trust network access (ZTNA) emerged as part of a rejuvenated effort to mitigate malware, ransomware and other types of global [cybersecurity threats](https://www.splunk.com/en_us/data-insider/what-are-modern-cybersecurity-threats.html).

Zero trust is not a specific security architecture, a product or software solution but rather a methodology for secure access that requires an organization to rethink their security strategy and network architecture. The key to understanding a zero trust network is understanding who is making access requests and from which device the request originates — then mapping that request to access policies per application or asset.

## What are the core principles of the zero trust model? 

To be successful, a zero trust framework entails several core underlying principles, including:

- **Assume the network is always hostile**: Basic practice before zero trust had been to assume that if you were accessing a known network, you could be relatively certain it was secure. With zero trust, you assume it is not secure.
- **Accept that external and internal threats are always on the network**: Traditional security methods assumed networks were secure until a threat was detected. Zero trust turns this model on its head.
- **Know that the location of a corporate network or cloud provider locality is not enough to decide to trust in a network**: Traditional security rules based on IP address are no longer reliable.
- **Authenticate and authorize every device, user and network flow**: A zero trust model authorizes and authenticates user access by least-privilege access on a per-session basis.
- **Implement policies that are dynamic and calculated from as many data sources as possible**: End-to-end data analytics should be established, providing monitoring and [threat detection](https://www.splunk.com/en_us/data-insider/threat-intelligence.html) across the entire architecture, including cloud environments, which support both IT and security operations requirements.

## What is a zero trust architecture? 

A zero trust architecture, or ZTA, is a cybersecurity architecture based on the principles of zero trust, designed to prevent data breaches, cyber attacks and unauthorized access of sensitive data while limiting internal lateral movement of attackers or malicious insiders.

The [American Council for Technology and Industry Advisory Council (ACT-IAC)](https://www.actiac.org/) lays out the six pillars of a zero trust security model, each of which are built upon a foundation of data.

![[Pasted image 20230727162652.png]]

- **Users**: The ongoing authentication of trusted users and user identity, the continuous monitoring and validation of user trustworthiness to govern their access and privileges.
- **Devices**: Measuring the real-time cybersecurity posture and trustworthiness of devices to apply strategic access management policies.
- **Network**: The ability to conduct network segmentation, as well as isolate and control the network, including software-defined networks, software-defined wide area networks and internet-based technologies.
- **Applications**: Securing and properly managing the application layer, as well as cloud services, containers and virtual machines.
- **Automation**: [Security automation, orchestration and response (SOAR)](https://www.splunk.com/en_us/data-insider/what-is-soar.html) allow organizations to automate tasks across products through workflows and for interactive end-user oversight.
- **Analytics**: Visibility and analytics tools like [security information and event management (SIEM)](https://www.splunk.com/en_us/data-insider/what-is-siem.html), advanced [security analytics](https://www.splunk.com/en_us/data-insider/what-is-cybersecurity-analytics.html), and [user and entity behavior analytics (UEBA)](https://www.splunk.com/en_us/data-insider/user-behavior-analytics-ueba.html) allow security experts to observe what’s happening and orient their defenses accordingly.

## Why is a zero trust framework important? 

Historically, [cybersecurity](https://www.splunk.com/en_us/data-insider/what-is-cybersecurity.html) used to revolve around building a hardened perimeter, and then layer security tools like moats and walls around a castle. This concept made sense when cyberthreats only emerged from outside, and assets lived on premises.

Today’s new ecosystem — cloud, remote workforces and mobile devices — fails to conform to traditional security strategies. Instead, it greatly expands the attack surface by allowing data and workloads to live, operate and be accessed from almost anywhere. Zero trust addresses these challenges by starting with the assumption that all networks are compromised until proven otherwise.

## What issues does zero trust address? 

Zero trust addresses the security challenges an organization faces when it stores data in multiple locations — both on-premises and in private and public cloud environments — and allows wide access to these resources by employees, providers, contractors, suppliers, partners and other authorized users and their personal devices.

For example, imagine an employee who is authorized to use their organization’s case management system from a newly assigned device. The employee makes a request from that device and is granted access. Eventually, they download software from an unauthorized source — possibly something as simple as a printer driver. Because the device is continuously monitored in a zero trust strategy, the update is flagged. This newly added component has altered the configuration — and therefore the trust score — of the device in question. When the employee attempts to connect to the system, their access might be denied, or downgraded, depending on their new trust score and associated policy. In this way, applying multiple factors (in this case, the combined scores of the user, device and resource) helps security teams dynamically reduce risk to enterprise resources. A zero trust system has the ability to factor in changing conditions for continuous evaluation, and continuous protection.

## What is a zero trust implementation? 

As organizations look to adopt a zero trust strategy, it’s essential that they monitor, detect and investigate security incidents relating to zero trust controls and policies — specifically the protections in place for users, systems, applications and data.

The following maturity model breaks down an organization’s security journey into distinct stages. With the goal that each stage covers specific objectives, and allows for incremental, iterative improvements before moving on to the next phase of growth. Although this journey is focused on security outcomes, it also aligns with the development of IT monitoring capabilities through the reuse and rehashing of data.

A zero trust implementation includes:

**Advanced detection**: Apply sophisticated detection mechanisms at a granular level including machine learning.

**Automation and orchestration**: Establish a consistent and repeatable security operation capability.

**Enrichment**: Augmenting security data with intelligence sources to better understand the context and impact of an event.

**Expansion**: Collecting additional data sources like endpoint activity and network metadata to drive advanced attack detection.

**Normalization**: Applying a standard security taxonomy and add asset and identity data.

**Collection**: Collecting basic security logs and other machine data from your environment.

## What are the benefits of zero trust? 

A zero trust model can significantly improve an organization’s security posture and minimize operational overhead by eliminating the sole reliance on perimeter-based protection. Instead of following traditional methods, zero trust establishes a certain level of trust at each access point — effectively securing user identity, assets and resources. This doesn’t mean getting rid of perimeter security and traditional security policies, however. Rather, it’s an organizational shift in approach when it comes to protecting core assets.

## What are the challenges of zero trust? 

Until recently, individually authenticating every object requesting access to a network posed a significant challenge to user experience for most organizations. Certain technologies lacked the necessary integration capabilities, limiting an organization’s ability to centrally and holistically monitor the overall security of their organization’s resources, creating further fragmentation and requiring a detailed implementation by security engineers.

Now there are multiple technologies available that revolve around access control — that is, a set of rules to determine who should be granted access to a restricted location and/or critical information. A zero trust architecture can stitch these systems together, reducing the complexity of managing multiple controls independently.

In addition to the technological challenges, establishing a zero trust methodology or implementing zero trust solutions can seem daunting, but while the approach may sound like a total change, it does not require a “rip and replace” upgrade of any systems. In fact, the change to zero trust can be accomplished incrementally with changes to policies and access controls.

## How do you get started with zero trust? 

Implementing a zero trust architecture depends on many variables based on your current network setup. A comprehensive guide to getting started is beyond the scope of this document. But here are some key steps you can take to help you prepare.

**Stage 1: Collect Relevant Data:** First, identify your organization’s most critical assets — specifically what you need to protect and monitor in order of priority. Once you’ve triaged your assets, you’ll have a much better idea of where to allocate resources, and where to start ingesting data from. Because zero trust consists of many different types of technologies, there’s a good chance your organization already relies on some of these systems. This will be an important source of data for IT and security monitoring, and the very foundation of a comprehensive end-to-end zero trust program.

**Stage 2: Understand and Contextualize Your Data:** Contextualizing your data is key to any zero trust strategy. To understand your data, you have to implement a standard taxonomy across all data sources — otherwise you’re left with a whole lot of noise. Creating a taxonomy for your data will eliminate a lot of confusion, especially as you continue to level up on your security journey.

One example is how firewall vendors use different log formats and data structures across systems. In order to support centralized monitoring, firewall log data needs to be structured in a way that normalizes field names and values, putting them into a consistent format.

**Stage 3: Expand On Your Data:** More often than not, the continuous monitoring of security controls will fail to detect advanced security threats. This is why security monitoring should look at how target systems function, as well as what authorized use looks like. A holistic view of systems, data and users also needs to be established — and that includes behavioral and infrastructure monitoring. Why? Because zero trust can’t always stop fraud, insider threats or advanced attacks that occur via authorized means (e.g., a compromised user account).

But a zero trust strategy can contain an incident, and restrict the scope of any potential damage. If we’re looking in the wrong place, however, there’s a good chance this type of threat won’t be detected in time. By considering zero trust policies and how an authorized user should behave, we can gain insight into anomalies we should be monitoring, so we can better detect malicious access.

**Stage 4: Enrich and Augment Your Data:** Threat intelligence (TI) helps us identify indicators of compromise (IoCs) across zero trust controls and protected systems. This helps us understand the threat landscape as it relates to the systems and users we’re protecting, and to also identify known IoCs that would otherwise go undetected by zero trust security controls. Examples of this include IP addresses, URLs or file hashes associated with phishing activity, or identifying information relating to an SSL certificate known to be used for malicious purposes.

Secondly, understanding the posture of protected assets — as well as the systems used to access these resources — helps with risk scoring and security incident prioritization, as well as access authorization. For example, user systems with missing or insufficient system patches can have their access to critical systems limited, and security incidents connected to known vulnerabilities can be prioritized.

On top of all this, attack surface management solutions can help with overall security posture — specifically focusing efforts on optimizing security controls and ensuring end-to-end visibility. If we know we have gaps in our controls, we can look to mitigate or implement enhanced monitoring.

## The Bottom Line: Zero Trust is an essential culture shift 

IT organizations have for the most part been lucky as they’ve moved sensitive and valuable data to the cloud, with only a small percentage experiencing damaging attacks. The uptick of remote work environments due to COVID-19 and the SolarWinds attack showed how vulnerable open networks can be. Regardless of the challenges around introducing a new mindset, culture and set of related practices, organizations need to understand the concept of zero trust so they can see how, where and why they remain vulnerable.

#website
[What is Zero Trust? Zero Trust Security Model Explained | Splunk](https://www.splunk.com/en_us/data-insider/what-is-zero-trust.html)