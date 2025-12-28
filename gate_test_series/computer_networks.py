# computer_networks.py

questions = {
    "easy": [
        {"q": "How many layers are in the OSI model?", "options": ["4", "5", "7", "8"], "correct": "7"},
        {"q": "Which layer is responsible for routing packets across the network?", "options": ["Physical", "Data Link", "Network", "Transport"], "correct": "Network"},
        {"q": "What does HTTP stand for?", "options": ["High Text Transfer Protocol", "Hyper Transfer Text Protocol", "Hypertext Transfer Protocol", "Hyperlink Text Transfer Protocol"], "correct": "Hypertext Transfer Protocol"},
        {"q": "Which device operates at the Physical layer of the OSI model?", "options": ["Router", "Switch", "Hub", "Bridge"], "correct": "Hub"},
        {"q": "What is the standard port number for HTTPS?", "options": ["80", "443", "21", "25"], "correct": "443"},
        {"q": "Which protocol is used to map an IP address to a MAC address?", "options": ["DNS", "DHCP", "ARP", "ICMP"], "correct": "ARP"},
        {"q": "An IPv4 address consists of how many bits?", "options": ["16", "32", "64", "128"], "correct": "32"},
        {"q": "Which of the following is a 'connectionless' protocol?", "options": ["TCP", "UDP", "FTP", "HTTP"], "correct": "UDP"},
        {"q": "The 'Ping' command uses which protocol?", "options": ["TCP", "ARP", "ICMP", "SMTP"], "correct": "ICMP"},
        {"q": "Which topology requires a central controller or hub?", "options": ["Mesh", "Star", "Bus", "Ring"], "correct": "Star"}
    ],
    "medium": [
        {"q": "Which layer of the OSI model handles error detection and flow control at the hop-to-hop level?", "options": ["Network", "Transport", "Data Link", "Session"], "correct": "Data Link"},
        {"q": "What is the size of an IPv6 address?", "options": ["32 bits", "64 bits", "128 bits", "256 bits"], "correct": "128 bits"},
        {"q": "Which field in the IP header is used to prevent packets from looping infinitely?", "options": ["Checksum", "TTL (Time to Live)", "Fragment Offset", "Source IP"], "correct": "TTL (Time to Live)"},
        {"q": "In TCP, what is the purpose of the 'Three-Way Handshake'?", "options": ["To encrypt data", "To establish a reliable connection", "To terminate a session", "To compress the header"], "correct": "To establish a reliable connection"},
        {"q": "Which protocol is used to automatically assign IP addresses to devices on a network?", "options": ["DNS", "DHCP", "NAT", "RIP"], "correct": "DHCP"},
        {"q": "What is the default subnet mask for a Class C network?", "options": ["255.0.0.0", "255.255.0.0", "255.255.255.0", "255.255.255.255"], "correct": "255.255.255.0"},
        {"q": "Which layer is responsible for end-to-end communication and port addressing?", "options": ["Network", "Transport", "Application", "Presentation"], "correct": "Transport"},
        {"q": "What is 'Piggybacking' in computer networks?", "options": ["Adding extra bits for security", "Attaching an acknowledgement to an outgoing data frame", "Sending data across multiple paths", "Using a proxy server"], "correct": "Attaching an acknowledgement to an outgoing data frame"},
        {"q": "Which algorithm is used by the RIP (Routing Information Protocol)?", "options": ["Link State", "Distance Vector", "Dijkstra's", "Path Vector"], "correct": "Distance Vector"},
        {"q": "The process of hiding internal IP addresses behind a single public IP is called:", "options": ["Subnetting", "NAT (Network Address Translation)", "DNS", "Switching"], "correct": "NAT (Network Address Translation)"}
    ],
    "hard": [
        {"q": "In the TCP congestion control algorithm, what happens after a timeout?", "options": ["Threshold is doubled", "Congestion window is set to 1 MSS", "Congestion window is halved", "Slow start is disabled"], "correct": "Congestion window is set to 1 MSS"},
        {"q": "What is the maximum data rate of a standard Ethernet (10Base-T) cable?", "options": ["1 Mbps", "10 Mbps", "100 Mbps", "1000 Mbps"], "correct": "10 Mbps"},
        {"q": "Which protocol uses the Dijkstra algorithm to build a shortest-path tree?", "options": ["RIP", "BGP", "OSPF", "ARP"], "correct": "OSPF"},
        {"q": "In a Go-Back-N ARQ, if the window size is 7, what is the range of sequence numbers needed?", "options": ["7", "8", "14", "15"], "correct": "8"},
        {"q": "What is the 'Silber Bullet' problem (Silly Window Syndrome) associated with?", "options": ["IP Fragmentation", "TCP Flow Control", "DNS Caching", "Ethernet Collisions"], "correct": "TCP Flow Control"},
        {"q": "Which of these is a 'Classless Inter-Domain Routing' (CIDR) notation for a subnet with 64 addresses?", "options": ["/24", "/25", "/26", "/27"], "correct": "/26"},
        {"q": "In the context of network security, what does a 'Nonce' prevent?", "options": ["SQL Injection", "Replay Attacks", "DDoS", "Phishing"], "correct": "Replay Attacks"},
        {"q": "What is the bandwidth of a signal that ranges from 40 kHz to 100 kHz?", "options": ["140 kHz", "40 kHz", "60 kHz", "70 kHz"], "correct": "60 kHz"},
        {"q": "Which layer is responsible for translation, compression, and encryption?", "options": ["Session", "Presentation", "Application", "Transport"], "correct": "Presentation"},
        {"q": "A pure ALOHA network has a maximum throughput of approximately:", "options": ["18.4%", "36.8%", "50%", "100%"], "correct": "18.4%"}
    ]
}