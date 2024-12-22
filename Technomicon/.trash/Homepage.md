---
category: 
tags: 
created: 2024-12-21
---


```dataview
table category, length(rows) as "Number of Notes" from "" group by category
```


Last updated: `$= dv.current().file.mtime.toFormat("MMMM dd, yyyy 'at' HH:mm")`
