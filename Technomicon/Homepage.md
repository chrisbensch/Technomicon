---
category: 
tags:
  - homepage
  - index
created: 2024-12-21
---

# 📜 The Technomicon

## 🚀 Where to Start
This vault is your knowledge base and second brain. Here's how to navigate:

1. **Courses, Exams, CTFs**: This is where I keep notes for any courses or exams I'm studying for or use for reference.
2. **Digital Forensics**: This is to store any DFIR reference material and methodologies.
3. **Penetration Testing**: This is to store any Penetration Testing reference material and methodologies.
4. **System Administration**: This is to store any System Administration reference material and methodologies.

### 📅 Recent Notes
```dataview
TABLE file.mtime as "Last Modified"
FROM "/"
SORT file.mtime desc
LIMIT 5
```


Last updated: `$= dv.current().file.mtime.toFormat("MMMM dd, yyyy 'at' HH:mm")`