---
category: Uncategorized
tags: [pentest]
created: 2024-12-21

---
![[Pasted image 20220908124907.png]]

Creating a wordlist with 5 lowercase characters, 4 numeric values, and 2 special characters.
```bash - kali
crunch 11 11 -t @@@@@%%%%^^ -o crunch.txt
```

Appending 4 numbers and 2 special characters to known beginning of password.
```bash - kali
crunch 11 11 -t bella%%%%^^ -o crunch.txt
```


Last updated: `$= dv.current().file.mtime.toFormat("MMMM dd, yyyy 'at' HH:mm")`
