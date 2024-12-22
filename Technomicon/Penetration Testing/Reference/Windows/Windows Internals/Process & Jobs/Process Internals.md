---
category: Uncategorized
tags: [pentest]
created: 2024-12-21

---
- Every window process is represented by the process executive structure called `EPROCESS`.
- `EPROCESS` contains reference to one more internal structures such as `ETHREAD` which represents the threads inside the process.
- All process structures resides in the system address space except the `Process Environment Block (PEB)` which resides in the user process address space.
- 