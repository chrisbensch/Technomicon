---
category: Uncategorized
tags: [pentest]
created: 2024-12-21

---
#### Portscan
```bash - kali
#!/bin/bash
if ["$1" == "" ]
then
  echo "Usage: ./port.sh [IP]"
  echo "Example ./port.sh $TARGET"
else
  echo "Please wait while it is scanning all the open ports..."
  nc -nvz $1 1-65535 > $1.txt 2>&1
fi
tac $1.txt
rm -rf $1.txt
```


Last updated: `$= dv.current().file.mtime.toFormat("MMMM dd, yyyy 'at' HH:mm")`
