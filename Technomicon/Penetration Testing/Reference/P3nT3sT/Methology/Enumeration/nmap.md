---
category: Uncategorized
tags: [pentest]
created: 2024-12-21

---
# Scanning all IP quick.


```bash  
ports=$(nmap -p- --min-rate=1000 -T4 <IP> | grep '^[0-9]' | cut -d '/' -f 1 | tr '\n' ',' | sed s/,$//) 
```

```bash
nmap -p$ports -sC -sV <IP>
```


Last updated: `$= dv.current().file.mtime.toFormat("MMMM dd, yyyy 'at' HH:mm")`
