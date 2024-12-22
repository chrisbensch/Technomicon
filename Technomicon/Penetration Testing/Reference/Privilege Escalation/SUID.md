---
category: Uncategorized
tags: [pentest]
created: 2024-12-21

---
- Binaries with SUID bit set runs with it's owners's privilege.
```bash
# find all files with SUID bit set
find / -type f -perm -04000 -ls 2>/dev/null
```