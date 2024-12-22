---
category: Uncategorized
tags: []
---

---
aliases: [Home, Dashboard]
tags: [dashboard]

# 📚 Vault Overview

> [!multi-column]

> [!column|flex 3]
## 📊 Key Statistics

Total Notes: `$= dv.pages().length`
Total Tags: `$= dv.pages().file.tags.distinct().length`
Modified Last Week: `$= dv.pages().where(p => p.file.mtime >= date(today) - dur('1 week')).length`

## 📝 Recently Modified
```dataview
TABLE WITHOUT ID
  file.link as "Note",
  dateformat(file.mtime, "dd-MM-yyyy") as "Modified"
FROM ""
SORT file.mtime DESC
LIMIT 5
```

## 📈 Notes By Folder
```dataview
TABLE WITHOUT ID
  length(rows) as "Count",
  round(length(rows) * 100 / length(dv.pages())) + "%" as "Percentage"
GROUP BY file.folder
WHERE file.folder != null
SORT length(rows) DESC
```

> [!column|flex 2]
## ⭐ Starred Pages
```dataview
LIST
FROM ""
WHERE contains(file.tags, "#star")
LIMIT 10
```

## 🏷️ Most Used Tags
```dataview
TABLE WITHOUT ID
  length(rows) as "Count",
  round(length(rows) * 100 / length(dv.pages())) + "%" as "Percentage"
GROUP BY file.tags as Tag
WHERE file.tags
SORT length(rows) DESC
LIMIT 10
```

> [!column-end]

## 📊 Word Count Statistics
```dataview
TABLE WITHOUT ID
  round(average(rows.file.size)) as "Average Size (bytes)",
  sum(rows.file.size) as "Total Size (bytes)"
FROM ""
```

## 🔗 Most Linked Notes
```dataview
TABLE WITHOUT ID
  length(file.inlinks) as "Inbound Links",
  file.link as "Note"
FROM ""
WHERE length(file.inlinks) > 0
SORT length(file.inlinks) DESC
LIMIT 5
```
```