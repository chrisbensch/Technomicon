---
category: Uncategorized
tags: [pentest]
created: 2024-12-21

---
## Query Installed Antivirus
```powershell
# Using wmic 
wmic /namespace:\\root\securitycenter2 path antivirusproduct

# Using powershell WMI
Get-CimInstance -Namespace root/securitycenter2 -Class antivirusproduct
```
# Windows Defender
- Windows Defender is windows's preinstalled AntiVirus solution.
- Works in 3 modes:
	- Active: When Defender is the primary AV.
	- Passive: When 3rd party AV is installed. Works partially.
	- Disabled: When Defender is fully disabled or uninstalled.
```powershell
# Check if Microsoft defender is running
Get-Service windefend

# Check what elements of defender is running 
Get-MpComputerStatus | select realtimeprotectionenabled

# Disable Realtime Monitoring
Set-MpPreference -disableRealtimeMonitoring $true

```


Last updated: `$= dv.current().file.mtime.toFormat("MMMM dd, yyyy 'at' HH:mm")`
