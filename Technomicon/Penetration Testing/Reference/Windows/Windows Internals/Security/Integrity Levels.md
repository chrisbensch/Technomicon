---
category: Uncategorized
tags: [pentest]
created: 2024-12-21

---
- Integrity levels were introduced, to differentiate between a process running under the same user but one with elevated privilege and one with standard privilege.
- Integrity levels:
	- System (highest)
	- High
	- Medium
	- Low
- They are represented as internally [SID](TechLexicon/Penetration%20Testing/Reference/Windows/Windows%20Internals/Security/SID.md)s
- This is called *Mandatory Access Control* (MIC) in the [Access Token](Access%20Token.md)
- Process running as:
	- Standard User -> Medium
	- Administrator -> High
	- Service running as Local System, Network Service, Local Service -> System
- Process with low integrity level cannot access objects with high integrity level.
- Objects with no integrity value is perceived as objects with medium integrity. Hence, most of the files and folders are medium integrity object and requires an process with medium or above integrity level to interact with the object.
- Integrity levels take precedence over [Security Descriptor](Security%20Descriptor.md). Even if a process has full control over the access, it cannot access the object if the integrity level of process is lower than that of the object.


Last updated: `$= dv.current().file.mtime.toFormat("MMMM dd, yyyy 'at' HH:mm")`
