---
category: Uncategorized
tags: [pentest]
created: 2024-12-21

---
```bash - kali
telnet $TARGET
```

```bash  - kali
nmap -p 23 --script=telnet-ntlm-info.nse $TARGET
```

![[TechLexicon/Penetration Testing/Reference/7._Tools/Hydra#Hydra against telnet]]


Last updated: `$= dv.current().file.mtime.toFormat("MMMM dd, yyyy 'at' HH:mm")`
