Istruzioni per completare la sfida ctf "information":

1. Digitiamo il comando "exiftool cat.jpg" tramite web shell di picoCTF.
2. Otteniamo le informazioni sul file precisamente i metadati.
3. Notiamo il campo "License" in formato base 64.
4. Preleviamo ciò e decodifichiamo tramite il comando "echo cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9 | base64 -d" .
5. Otteniamo cosi il flag. 