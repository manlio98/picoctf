Istruzioni per completare la sfida ctf "Matryoshka doll":

Soluzione
    1) Analizzando l'immagine dolls.jpg con il comando "strings" utilizzando la web shell.
    2) Notiamo che al suo interno c'è un'altra immagine. Quindi bisogna estrarre questa immagine
    3) Lo facciamo attraverso lo strumento binwalk
    4) Con il comando "binwalk -e dolls.jpg" possiamo estrarre l'immagine
    5) Questo processo bisogna iterarlo per 4 volte finche non troviamo il file binario flag.txt che contiene appunto la flag.