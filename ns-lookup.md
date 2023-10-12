---
aliases: 
tags: 
date created: Wednesday, September 13th 2023, 9:22:55 pm
date modified: Wednesday, September 13th 2023, 9:23:01 pm
---
`nslookup` is a network administration command-line tool available in many computer operating systems for querying the Domain Name System (DNS) to obtain domain name or IP address mapping or for any other specific DNS record.

Here's a basic overview of how to use `nslookup`:

1. **Check a domain's IP address**
   
   Syntax: `nslookup domain.com`
   
   This command queries DNS to retrieve the IP address associated with `domain.com`.
   
2. **Find out the mail servers for a domain**
   
   Syntax: `nslookup -type=mx domain.com`
   
   This will return Mail Exchange (MX) records for `domain.com`, which tells you the mail servers associated with that domain.

3. **Specifying a DNS server to query**

   If you don't want to use the default DNS server that your system is configured to use, you can specify a particular server. 

   Syntax: `nslookup domain.com dns_server`
   
   For example: `nslookup domain.com 8.8.8.8` (This will use Google's public DNS)

4. **Interactive mode**

   You can also use `nslookup` in interactive mode. Simply type `nslookup` and hit enter. From there, you can make multiple queries without exiting the tool. For example:

   ```
   > set type=mx
   > domain.com
   ```

5. **Reverse DNS Lookup**

   If you want to find out the domain associated with a specific IP address, you can perform a reverse DNS lookup.

   Syntax: `nslookup IP_address`
   
   Example: `nslookup 8.8.8.8`

6. **Exit the tool**

   If you are in interactive mode, you can type `exit` and press Enter to exit `nslookup`.

Remember: `nslookup` may be deprecated in certain systems, with tools like `dig` and `host` being recommended. However, `nslookup` is still widely used and available on many platforms. If you're getting started with DNS queries, it's good to familiarize yourself with all these tools.