---
category: Uncategorized
tags: [pentest]
created: 2024-12-21

---
# Check applocker rules/policy
```powershell
Get-AppLockerPolicy -Effective | select -expandproperty rulecollections
```


Last updated: `$= dv.current().file.mtime.toFormat("MMMM dd, yyyy 'at' HH:mm")`
