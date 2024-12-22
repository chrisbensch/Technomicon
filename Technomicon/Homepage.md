---
category: 
tags:
  - homepage
  - index
  - navigation
created: 2024-12-21
---

# 📜 The Technomicon

## 🚀 Where to Start
This vault is your knowledge base and second brain. Here's how to navigate:

1. **Daily Notes**: Start your day by creating a daily note to capture thoughts, tasks, and ideas
2. **Quick Capture**: Use the Quick Capture note for fleeting thoughts you'll process later
3. **MOCs (Maps of Content)**: Browse through topic-specific indexes that organize related notes

### 📅 Recent Notes
```dataview
TABLE file.mtime as "Last Modified"
FROM "/"
SORT file.mtime desc
LIMIT 5
```


Last updated: `$= dv.current().file.mtime.toFormat("MMMM dd, yyyy 'at' HH:mm")`