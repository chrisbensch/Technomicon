---
category: Uncategorized
tags: [pentest]
created: 2024-12-21

---
```bash - kali
echo "$TARGET example.domain" | sudo tee -a /etc/hosts
```

```bash - kali
echo '$TARGET friendzone.red administrator1.friendzone.red hr.friendzone.red uploads.friendzone.red' >> /etc/hosts
```

```bash - kali
sudo -- sh -c "echo '$TARGET example.domain' >> /etc/hosts"
```


Last updated: `$= dv.current().file.mtime.toFormat("MMMM dd, yyyy 'at' HH:mm")`
