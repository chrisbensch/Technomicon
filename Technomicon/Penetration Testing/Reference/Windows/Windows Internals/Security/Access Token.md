---
category: Uncategorized
tags: [pentest]
created: 2024-12-21

---
- Access token is a kernel object that identifies the security context of a process or a thread.
- A token attached to a *Process* is called a *Primary Token*.
- A token attached to *Thread* is called a *Impersonation Token*.
- Access token describes Privileges, Accounts, Groups associated with the process/thread.
- Lsass.exe creates the initial token when the user logs in and hands the token to winlogon process.
- `LogonUser` function is used to create a new security token. This token can be used with `CreateProcessAsUserW` function, or directly with `CreateProcessWithLogonW`.


Last updated: `$= dv.current().file.mtime.toFormat("MMMM dd, yyyy 'at' HH:mm")`
