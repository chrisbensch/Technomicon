---
category: Uncategorized
tags: [pentest]
created: 2024-12-21

---
Found a file named: `backup.tar.gz.enc`. Use netpgp to decrypt it.

```bash - target
netpgp --decrypt --output=backup.tar.gz backup.tar.gz.enc
```


Last updated: `$= dv.current().file.mtime.toFormat("MMMM dd, yyyy 'at' HH:mm")`
