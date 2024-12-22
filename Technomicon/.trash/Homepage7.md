---
category: Meta
tags: [homepage, index, navigation]
created: 2024-12-21
---

# 🏠 Welcome to My Vault

## 🚀 Where to Start
This vault is your knowledge base and second brain. Here's how to navigate:

1. **Daily Notes**: Start your day by creating a daily note to capture thoughts, tasks, and ideas
2. **Quick Capture**: Use the Quick Capture note for fleeting thoughts you'll process later
3. **MOCs (Maps of Content)**: Browse through topic-specific indexes that organize related notes

## 📊 Vault Statistics

### 📝 Note Counts
```dataview
TABLE WITHOUT ID
	length(rows) as "Total Notes",
	length(rows.file.tags) as "Total Tags",
	length(unique(rows.file.tags)) as "Unique Tags"
FROM "/"
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

## 🗺️ Main Areas

### 💭 Personal Knowledge
```dataview
LIST
FROM #pkm OR #learning
SORT file.mtime DESC
LIMIT 5
```

### 📝 Work
```dataview
LIST
FROM "Work"
WHERE contains(tags, "#active")
SORT file.mtime DESC
```

### 🎯 Personal Development
```dataview
LIST
FROM #goals OR #habits
WHERE !contains(file.path, "templates")
SORT file.mtime DESC
LIMIT 5
```

## 🔍 Quick Access

### ⏳ Ongoing Tasks
```dataview
TASK
FROM "/"
WHERE !completed
LIMIT 10
```

### 📚 Reading List
```dataview
TABLE WITHOUT ID
	file.link as "Book",
	status as "Status",
	rating as "Rating"
FROM #reading
WHERE contains(tags, "#book")
SORT rating DESC
LIMIT 5
```

## 🔄 Current Projects
```dataview
TABLE 
	status as "Status",
	deadline as "Deadline",
	priority as "Priority"
FROM #project
WHERE status != "Completed"
SORT priority ASC
```

---

> [!tip] Remember
> Regular maintenance and review keep your vault useful and organized. Schedule weekly reviews to process notes and maintain connections.

Last updated: `= date(today)`


Last updated: `$= dv.current().file.mtime.toFormat("MMMM dd, yyyy 'at' HH:mm")`
