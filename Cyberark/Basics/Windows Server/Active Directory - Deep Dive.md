---
aliases: 
tags: 
date created: Monday, August 21st 2023, 1:59:51 pm
date modified: Monday, August 21st 2023, 2:01:01 pm
---

## Introduction

A network directory service has entries for users and groups, workstations and servers, policies and scripts, printers and queues, switches and routers, and just about anything else that relates to computing. The attributes for these entries have something to do with their relationship to network services. For example, authentication credentials can be stored in a directory service so users can log on from anywhere the directory service is available.

A directory service is not a general-purpose database.

Finally, a directory service needs management tools. Administrators need some way to add information to the directory, remove outdated information, and make use of the information that remains. These tools need to be global in scope, straightforward to operate, and aid in diagnosing any problems that might arise.

### Questions to Ponder

1. How does a directory service work? 
2. Why does it work that way? 
3. How does it break? 
4. How is it fixed? 
5. And most important, how does it make my job easier so I don't spend all my spare time managing the service that's supposed to be helping me manage the network?



The `dc` style generally indicates a dns-based LDAP tree of some kind. This is the style Active Directory (AD) uses. If you don't care about dns-based LDAP trees, then other types can be used just fine. Novell's eDirectory is an `O` based tree. Some caveats:

- DC-style is what AD uses. A lot of 3rd party products that support AD LDAP sources like this style of tree a lot better than `O` based trees. I've had trouble getting these clients to talk to O-style LDAP trees.
- AD doesn't use `O` at all, so some LDAP clients/parsers may not support it as a result. The same goes for `L` (location).
- If you're not DNS-rooting your tree, DC-style is much less important
- Hybrid styles are just fine. Your LDAP root is `dc=example,dc=com`, and you use an O-style tree under that. DN's could very well be, `cn=bobs,ou=users,o=company,dc=example,dc=com`

In general, your need to be compatible with 3rd party LDAP client is what should drive your structure. If it needs a dialect, it'll probably need to look as active-directory like as possible. If they're pure LDAP clients, in that they really do support the entire spec, then structure shouldn't matter.
 
[LDAP Namespace Structure | Understanding Active Directory Services | InformIT](https://www.informit.com/articles/article.aspx?p=101405&seqNum=7)
