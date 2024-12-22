---
category: Uncategorized
tags: [pentest]
created: 2024-12-21

---
- WMIC query to list installed software with version
	```bash
	wmic product get name,version,vendor
	```