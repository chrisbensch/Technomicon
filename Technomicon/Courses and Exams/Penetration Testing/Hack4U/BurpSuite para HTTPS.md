---
created: 2024-12-21

---
--------------------
- tags: #burpsuite
-------------------------
- Ir a https://burp
- Arriba a la derecha clicamos en CA Certificate y descargamos el certificado de BurpSuite
- Luego vamos a Settings en el navegador Firefox
- Buscamos certificates
- Hacemos clic en View Certificates...
- Hacemos clic en Import...
- Selecccionamos el certificado descargado de BurpSuite
- Marcamos la opción "Trust this CA to identify websites"
- Hacemos clic en OK

Y listo!! :)


Last updated: `$= dv.current().file.mtime.toFormat("MMMM dd, yyyy 'at' HH:mm")`
