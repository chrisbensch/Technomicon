---
category: Uncategorized
tags: []
created: 2024-12-21

---
# 🏠 Welcome to My Obsidian Vault

## 📂 Categories Overview
Here are the top-level categories of content in this vault. Click on a category to explore its contents.

- [Courses and Exams](Courses%20and%20Exams)
- [Forensics](Forensics)
- [Penetration Testing](Penetration%20Testing)
- [System Administration](System%20Administration)

---

## 📊 Vault Summary

### Courses & Exams
```dataview
table length(rows) as "Total Notes"
from "Courses and Exams"
```

### Forensics
```dataview
table length(rows) as "Total Notes"
from "Forensics"
```

### Penetration Testing
```dataview
table length(rows) as "Total Notes"
from "Penetration Testing"
```

### System Administration
```dataview
table length(rows) as "Total Notes"
from "System Administration"
```

---

## 📚 Recent Notes
Here are the 5 most recently updated notes across your vault:

```dataview
table file.name as "Note", file.mtime as "Last Modified"
from ""
sort file.mtime desc
limit 5
```

---

## 🚀 Productivity Links
- [Daily Notes](obsidian://daily)
- [Templates](Templates)
- [All Tags](#tags)

---

## 🛠️ Maintenance Tasks
### Notes Missing Frontmatter
These notes do not have frontmatter metadata and might need to be updated:
```dataview
list from "" where !category
```

### Recently Created Notes
```dataview
table file.name as "Note", file.ctime as "Created Date"
from ""
sort file.ctime desc
limit 5
```


Last updated: `$= dv.current().file.mtime.toFormat("MMMM dd, yyyy 'at' HH:mm")`
