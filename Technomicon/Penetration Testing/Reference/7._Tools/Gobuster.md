---
category: Uncategorized
tags: [pentest]
created: 2024-12-21

---
#### VHOST discovery
```bash - kali
gobuster vhost -u http://example.domain -w /usr/share/seclists/Discovery/DNS/subdomainstop1million-5000.txt | grep -v 302
```

#### https with php extension
```bash - kali
gobuster -w directory-list-2.3-medium.txt -t 50 -k -u https://administrator1.friendzone.red/ -x php
```


Last updated: `$= dv.current().file.mtime.toFormat("MMMM dd, yyyy 'at' HH:mm")`
