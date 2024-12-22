---
category: Uncategorized
tags: [pentest]
created: 2024-12-21

---
#### Heartbleeed
```bash - kali
nmap -p 443 --script ssl-heartbleed $TARGET
```

```bash - kali
curl https://$TARGET:443/ -k
```

