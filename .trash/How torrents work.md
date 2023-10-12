---
aliases: 
tags: 
date created: Saturday, August 12th 2023, 8:17:22 pm
date modified: Friday, September 29th 2023, 12:17:47 am
---
![[Pasted image 20230812201728.png]]  

1. **Tracker URLs**:
   - A tracker is a server that helps in coordinating the transfer of files between different peers in the BitTorrent network.
   - When you download a torrent file and open it in a torrent client, the client contacts the tracker specified in the torrent file to get a list of peers that are sharing the same file.
   - The tracker keeps track of which peers have which parts of the file, allowing for efficient data exchange.
   - Tracker URLs are the addresses of these servers.

2. **Web seed URLs**:
   - Web seeding is a method that allows a torrent client to download parts of a file from a regular HTTP server, in addition to downloading from peers in the BitTorrent network.
   - This can be useful for content distributors who want to provide an initial boost in download speed or ensure availability even if no other peers are sharing the file.
   - The Web seed URL is the address of the HTTP server hosting the file.

3. **DHT Network**:
   - DHT stands for Distributed Hash Table. It's a decentralized system that allows torrent clients to find peers directly, without the need for a central tracker.
   - When a torrent client supports DHT, it can find other peers that are sharing the same file by querying the DHT network.
   - This means that even if the original tracker goes offline, the torrent can still be downloaded using DHT.
   - DHT can be thought of as a "trackerless" system, making torrents more resilient and harder to shut down.
