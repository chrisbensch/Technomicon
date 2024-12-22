---
category: Uncategorized
tags: [pentest]
created: 2024-12-21

---
- PsExec is a lightweight telent replacemnt developed by Microsoft that executes process on remove windows systems using any user's credentials
- PsExec authentication is performed via SMB.
- Similar to RDP but without the GUI.
### Impacket's psexec.py
```bash
psexec.py Administrator@<ip> cmd.exe
```
https://www.rapid7.com/blog/post/2013/03/09/psexec-demystified/


Last updated: `$= dv.current().file.mtime.toFormat("MMMM dd, yyyy 'at' HH:mm")`
