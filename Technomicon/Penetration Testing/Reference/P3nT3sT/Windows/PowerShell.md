---
category: Uncategorized
tags: [pentest]
created: 2024-12-21

---
# PowerShell
## Base64 encoder

[Raiku base64 encoding](https://raikia.com/tool-powershell-encoder/)

This will encode the command you input into valid PowerShell Base64 for use with “EncodedCommand”.

Note: This is not a normal base64 encoder!  It converts the string to UTF-16LE first before encoding, as that is what PowerShell expects!


Last updated: `$= dv.current().file.mtime.toFormat("MMMM dd, yyyy 'at' HH:mm")`
