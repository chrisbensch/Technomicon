---
category: Uncategorized
tags: [pentest]
created: 2024-12-21

---
- *S*ecurity *Id*entifier
- Identifier for identities executing actions (Officially called *Principal*), can be:
	- Users
	- Groups
	- Computers 
	- Domains
	- and more.
- SID is made up of
	- Starts with *S* to denote the string is a SID.
	- Revision number - Identifies the SID structure version - Always 1
	- 48-bit authority identifier that issues the SID - Identifies the highest level of authority that can issue SIDs for a particular type of security principal.
		- 1 for Everyone Group (World Authority)
		- 5 for Specific Windows server account or group (NT Authority)
	- Subauthorities - Contains one or more subauthority value in the format of Y1-Y2-Y2...Yn
		- Y1 - Yn-1 : Identifies the domain in an active directory.
		- Yn : Is called the Relative ID (RID), identifies the particular
- SID is statistically unique
- Windows defines well knows SIDs, through `IsWellKnownSid` function. Some well known SIDs are:
	- *S-1-1-0*: Everyone - All Users
	- *S-1-2-0*: Local - Users to who log on physically
	- *S-1-5-18*: Local System - Local System Account
	- *S-1-5-20*: Network Service - Network Service Account
	- *S-1-5-19*: Local Service - Local Service Account
	- *S-1-5-32-544*: Administrators - Administrators group
- `KKEY_Users` contains the list of SIDS that logged into the the machine.
- `HKEY_Current_Users` is just a symbolic link to the current user SID in `HKEY\Users`


Last updated: `$= dv.current().file.mtime.toFormat("MMMM dd, yyyy 'at' HH:mm")`
