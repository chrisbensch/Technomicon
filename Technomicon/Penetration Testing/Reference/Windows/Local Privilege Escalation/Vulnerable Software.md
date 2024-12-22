---
category: Uncategorized
tags: [pentest]
created: 2024-12-21

---
- WMIC query to list installed software with version
	```bash
	wmic product get name,version,vendor
	```


Last updated: `$= dv.current().file.mtime.toFormat("MMMM dd, yyyy 'at' HH:mm")`
