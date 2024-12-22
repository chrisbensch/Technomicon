---
category: 
tags:
  - homepage
  - index
  - navigation
created: 2024-12-21
---
# 🏠 Welcome to My Vault

## 🚀 Where to Start
This vault is your knowledge base and second brain. Here's how to navigate:

1. **Daily Notes**: Start your day by creating a daily note to capture thoughts, tasks, and ideas
2. **Quick Capture**: Use the Quick Capture note for fleeting thoughts you'll process later
3. **MOCs (Maps of Content)**: Browse through topic-specific indexes that organize related notes

## 📊 Vault Statistics


### 📝 Notes by Category
```dataview
TABLE length(rows) as "Notes"
FROM "/"
GROUP BY category as "Categories"
SORT length(rows) DESC
```
### 📅 Recent Notes
```dataview
TABLE file.mtime as "Last Modified"
FROM "/"
SORT file.mtime desc
LIMIT 5
```

### 🏷️ Most Used Tags
```dataview
TABLE WITHOUT ID
	length(rows) as "Count",
	tag as "Tag"
FROM "/"
FLATTEN file.tags as tag
GROUP BY tag
SORT count DESC
LIMIT 10
```

### 📈 Notes Created by Month
```dataview
TABLE WITHOUT ID
	dateformat(file.ctime, "yyyy-MM") as "Month",
	length(rows) as "Notes Created"
FROM "/"
GROUP BY dateformat(file.ctime, "yyyy-MM")
SORT date desc
LIMIT 6
```

Last updated: `= date(today)`


Last updated: `$= dv.current().file.mtime.toFormat("MMMM dd, yyyy 'at' HH:mm")`
