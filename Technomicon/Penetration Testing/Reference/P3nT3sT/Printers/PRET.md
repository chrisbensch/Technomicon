---
category: Uncategorized
tags: [pentest]
created: 2024-12-21

---
# Installation
```bash
pip install colorama pysnmp  
git clone https://github.com/RUB-NDS/PRET
```

# Usage
The tool allows for communicating in three languages i.e. Adobe PostScript and HP Printer Job Language (PCL & PJL). More information on these can be found on the Hacking Printers Wiki. We have no idea what language is used by the service on the target. Let's try using all three options provided by the script, starting with PostScript (ps)

```bash
./pret.py 10.10.10.201 ps/pjl/pcl
```


Last updated: `$= dv.current().file.mtime.toFormat("MMMM dd, yyyy 'at' HH:mm")`
