---
category: Uncategorized
tags: [pentest]
created: 2024-12-21

---
- The right of an account to perform some system level operation.
- These rights are stores in the access token.
- Some privileges:
	- Shutting down the computer
	- Debug process
	- Taking ownership of an object
- Privileges can be edited with Local Security Policy Editor
- Privileges cannot be added to the active security tokens. Users need to logon again to get the new privileges.


Last updated: `$= dv.current().file.mtime.toFormat("MMMM dd, yyyy 'at' HH:mm")`
