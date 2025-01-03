---
category: Uncategorized
tags: [pentest]
created: 2024-12-21

---
- A property of an object that specifies *who* can do *what* with an object.
- When an entity tries to perform an action on the object, the security reference monitor compares if the entity has proper privileges to perform the action based on the security descriptor of the object.
- A security descriptor contains:
	- Owner SID.
	- *DACL* (Discretionary Access Control List) which specifies *who* has *what* level of access to an object.
	- *SACL* (System Access Control List) which specifies which operation by which user should be logged in the security audit log. Not meant to provide access.
	- These lists contains ACE (Access Control Entities)
		- A header
		- Access control entry: SID + Access Mask (Allow/Deny)
- When an entity opens a handle to an object, the following steps are checked.
	- If the object has no DACL entry, then, the entity has full access to the object.
	- If the entity has take-ownership privilege, then write access is allowed on the object.
	- If the caller is the owner of the object, read-controll and write DACL access is granted on the object.
	- Then is ACE list is check from first to last.


Last updated: `$= dv.current().file.mtime.toFormat("MMMM dd, yyyy 'at' HH:mm")`
