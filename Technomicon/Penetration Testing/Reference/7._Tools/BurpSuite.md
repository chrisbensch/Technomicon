---
category: Uncategorized
tags: [pentest]
created: 2024-12-21

---
#### Intercept traffic on different port

Proxy > Options > Proxy listeners > Add

Binding > Bind to port: (Whatever port target is using, example: 8888)

Request handling > Redirect to host: $TARGET > Redirect to port: 8888


#### BurpSuite proxy setup

Project options > Socks Proxy:

![[Pasted image 20220711114726.png]]

Foxy Proxy > Burp


Last updated: `$= dv.current().file.mtime.toFormat("MMMM dd, yyyy 'at' HH:mm")`
