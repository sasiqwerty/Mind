---
aliases: 
tags: 
date created: Monday, August 28th 2023, 8:54:34 am
date modified: Monday, December 4th 2023, 11:53:22 pm
---

## Load Balancer

A load balancer is a device or software application that distributes incoming network traffic across multiple servers to ensure that no single server is overwhelmed with too much traffic. This helps to optimize resource use, maximize throughput, reduce latency, and ensure fault-tolerant configurations. Load balancers play a crucial role in maintaining the performance and availability of applications and services in a computing environment.

### Key Features

![[load-balancer-key-features.svg]]

### Types

![[load-balancer-types.svg]]  

### gpt4-notes

1. **Distribution of Traffic**: The primary function of a load balancer is to distribute incoming traffic to multiple servers based on various algorithms like round-robin, least connections, least response time, etc.

2. **Fault Tolerance and High Availability**: If one of the servers fails, the load balancer redirects traffic to the remaining operational servers. This ensures that the application remains available even if some of its servers are down.

3. **Health Checks**: Load balancers continuously monitor the health of servers. If a server is not responding or is down, the load balancer stops sending traffic to that server until it is healthy again.

4. **SSL Termination**: Load balancers can handle the SSL handshake process, offloading the SSL processing from the backend servers. This is known as SSL termination.

5. **Session Persistence**: Some applications require that a user's session remains on the same server. Load balancers can use various methods, like cookies or source IP, to ensure that all requests from a user during a session are sent to the same server.

6. **Scalability**: As traffic to an application increases, more servers can be added to the pool, and the load balancer will start sending traffic to the new servers.

7. **Protection Against DDoS Attacks**: Some advanced load balancers offer features to mitigate Distributed Denial of Service (DDoS) attacks.

8. **Caching**: Some load balancers provide caching functionality, storing content in memory, which reduces the need to fetch fresh content from the server for every request.

9. **Compression**: To speed up web applications, load balancers can compress outbound data.

10. **Content Switching**: Based on request attributes like headers, cookies, or IP address, the load balancer can decide which server to send the request to.

There are different types of load balancers, including:

- **Hardware Load Balancers**: Physical devices optimized to distribute traffic. They are typically faster but can be more expensive.
  
- **Software Load Balancers**: These are applications that run on standard hardware or cloud instances. Examples include Nginx, HAProxy, and cloud-based solutions like AWS Elastic Load Balancing.

- **Application Load Balancers (Layer 7)**: Operate at the application layer and can make routing decisions based on content type, URL, etc.

- **Network Load Balancers (Layer 4)**: Operate at the transport layer and make decisions based on IP address, ports, and protocol.
