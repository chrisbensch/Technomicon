---
category: Uncategorized
tags: [pentest]
created: 2024-12-21

---
### Syntax
```bash
# List
msfvenom -l [types]

# Generate
msfvenon -p [payload] LHOST=<ip> LPORT=<port> [options]
```
### Types
- payloads
- encoders
- nops
- platforms
- archs
- encrypt
- format
- all
### Options
- `-f [format]` : specifiy the format of the payload. Can be listed with `msfvenom -l format`
- `-o [filename]` : specify the output filename


Last updated: `$= dv.current().file.mtime.toFormat("MMMM dd, yyyy 'at' HH:mm")`
