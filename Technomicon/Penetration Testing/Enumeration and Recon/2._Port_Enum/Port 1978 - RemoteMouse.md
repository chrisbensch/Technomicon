---
category: Uncategorized
tags: [pentest]
created: 2024-12-21

---
```bash - kali
wget https://raw.githubusercontent.com/p0dalirius/RemoteMouse-3.008-Exploit/master/RemoteMouse-3.008-Exploit.py
```

Ping test first with [[tcpdump]], modify cmd command on line 280.

After success, just generate malicious exe, transfer and execute:

Generate malicious exe:
[[1._Reverse Shells (WIN)#Stageless Payloads]]

Set up python server:
[[TechLexicon/Penetration Testing/Reference/7._Tools/Python#Server]]

[[rlwrap]]

[[4._File Transfers]]

![[Pasted image 20220705124109.png]]

