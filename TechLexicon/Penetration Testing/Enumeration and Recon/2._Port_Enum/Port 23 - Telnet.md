```bash - kali
telnet $TARGET
```

```bash  - kali
nmap -p 23 --script=telnet-ntlm-info.nse $TARGET
```

![[TechLexicon/Penetration Testing/Reference/7._Tools/Hydra#Hydra against telnet]]