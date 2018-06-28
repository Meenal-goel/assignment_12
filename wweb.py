#1- What is an access token? Generate your access token for any API.(for example Twitter,Spotify etc). Q.2- Get the IP address of some common sites like Google, Facebook by using DNS lookup. Q.3- Using Tweepy library try to extract tweets from Twitter.

An access token is an object that describes the security context of a process or thread. The information in a token includes the identity and privileges of the user account associated with the process or thread. When a user logs on, the system verifies the user's password by comparing it with information stored in a security database. If the password is authenticated, the system produces an access token. Every process executed on behalf of this user has a copy of this access token.

The system uses an access token to identify the user when a thread interacts with a securable object or tries to perform a system task that requires privileges. Access tokens contain the following information:

The security identifier (SID) for the user's account
SIDs for the groups of which the user is a member
A logon SID that identifies the current logon session
A list of the privileges held by either the user or the user's groups
An owner SID
The SID for the primary group
The default DACL that the system uses when the user creates a securable object without specifying a security descriptor
The source of the access token
Whether the token is a primary or impersonation token
An optional list of restricting SIDs
Current impersonation levels
Other statistics
Every process has a primary token that describes the security context of the user account associated with the process. By default, the system uses the primary token when a thread of the process interacts with a securable object. Moreover, a thread can impersonate a client account. Impersonation allows the thread to interact with securable objects using the client's security context. A thread that is impersonating a client has both a primary token and an impersonation token.
Microsoft Windows [Version 6.3.9600]
(c) 2013 Microsoft Corporation. All rights reserved.


#2.Get the IP address of some common sites like Google, Facebook by using DNS lookup.

C:\Users\hp>nslookup google.com
Server:  UnKnown
Address:  fe80::bed1:1fff:fee6:c5d5

Non-authoritative answer:
Name:    google.com
Addresses:  2404:6800:4002:807::200e
          172.217.161.14


C:\Users\hp>nslookup facebook.com
Server:  UnKnown
Address:  fe80::bed1:1fff:fee6:c5d5

Non-authoritative answer:
Name:    facebook.com
Addresses:  2a03:2880:f10c:83:face:b00c:0:25de
          157.240.7.35



#4.What is a difference between library and API . Figure it out with examples.
A library is a chunk of code designed for reuse that is typically installed locally. A library is most often wrapped in an API that defines the functionality the library provides and how to use it.

Technically speaking, the term API refers to an interface that doesn't need to have an implementation. However, when people speak of an API they are usually referring to a reusable library or service. Where a library is used as a package of code, a service is a running system that provides functionality to other systems and applications.

