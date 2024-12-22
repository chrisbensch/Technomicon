---
category: Uncategorized
tags: [pentest]
created: 2024-12-21

---
https://www.mankier.com/1/nikto

#### Commands

```bash - kali
sudo nikto -h http://$TARGET:80
```

```bash - kali
sudo uniscan -qwedsu http://$TARGET:80
```

#### Proxy usage
```bash - kali
sudo proxychains nikto -h http://$TARGET:80
```

```bash - kali
sudo proxychains uniscan -qwedsu http://$TARGET:80
```


Last updated: `$= dv.current().file.mtime.toFormat("MMMM dd, yyyy 'at' HH:mm")`
