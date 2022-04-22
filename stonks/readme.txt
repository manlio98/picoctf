Istruzioni per completare la sfida ctf "Stonks":

Soluzione
    1) il file vuln.c alla riga 72 effettua la fgets che contiene la flag.
    2) Dopodichè, alla riga 91 effettua una scanf,
    3) Dato che la scanf legge tutto ciò che sta in cima allo stack, possiamo leggere il contenuto.
    4) Utilizzando lo specificatore %s leggiamo il contenuto in formato esadecimale.
    5) Eseguiamo il file vuln.c e Scriviamo sullo STDOUT più volte lo specificatore %s.
    6) Prelevo la stringa/contenuto esadecimale.
    7) Converto la stringa in codice ASCII.
    8) Ottenendo la stringa che si trova nel programma python getflag.py (riga 1).
    9) il programma getflag.py converte la stringa/flag in formato big_indian.
    10) Ottenendo cosi la flag.
