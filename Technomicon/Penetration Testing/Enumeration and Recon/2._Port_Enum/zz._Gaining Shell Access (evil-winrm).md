---
category: Uncategorized
tags: [pentest]
created: 2024-12-21

---
```bash - kali
sudo gem install winrm winrm-fs colorize stringio
```   

```bash - kali
cd /opt && sudo git clone https://github.com/Hackplayers/evil-winrm.git && cd -
```

```bash - kali
ruby /opt/evil-winrm/evil-winrm.rb -i $TARGET -u $USER -p '$PASSWORD'
```

```bash - kali
ruby /opt/evil-winrm/evil-winrm.rb -i $TARGET -u $PASSWORD -H '$HASH'
```


Last updated: `$= dv.current().file.mtime.toFormat("MMMM dd, yyyy 'at' HH:mm")`
