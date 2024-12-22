---
category: Uncategorized
tags: [pentest]
created: 2024-12-21

---
Base64 encode each line of file:
```bash - kali
while read line; do echo -n -i $line | base64 >> outputfile.txt; done < /usr/share/seclists/Passwords/Common-Credentials/best15.txt
```


Last updated: `$= dv.current().file.mtime.toFormat("MMMM dd, yyyy 'at' HH:mm")`
