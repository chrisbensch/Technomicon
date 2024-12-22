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

## 📊 Vault Stats
```dataview
table
    length(rows) as "Total Notes",
    sum(length(file.tags)) as "Total Tags"
from ""
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

## 🔍 Quick Access
### Courses and Exams
```dataview
table file.name as "Course/Exam", created as "Created Date"
from "Courses and Exams"
sort created desc
limit 5
```

### Forensics
```dataview
table file.name as "Forensics Note", created as "Created Date"
from "Forensics"
sort created desc
limit 5
```

### Penetration Testing
```dataview
table file.name as "Penetration Testing Note", created as "Created Date"
from "Penetration Testing"
sort created desc
limit 5
```

### System Administration
```dataview
table file.name as "System Administration Note", created as "Created Date"
from "System Administration"
sort created desc
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
