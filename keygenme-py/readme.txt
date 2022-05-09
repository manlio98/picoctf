Istruzioni per completare la sfida ctf "Keygenme":

Soluzione
    1)Analizzando il file "keygenme-trial".py. Precisamente nella funzione check_key
    2)Effettua il confronto proprio con la flag.
    3)Notiamo che la parte dinamica della flag viene calcolato effettuando l'hashing dell'username, cioè FREEMAN.
    4)Preleviamo la parte di codice (dalla riga 157 a 192) dove calcola l'hashing.
    5)Inserisco questa parte di codice nel file "getflag.py"
    6)In modo tale da calcolare la parte rimanente della flag.
    7)ottenendo cosi la parte dinamica della flag.
    8)Aggiugendo la parte statica prelevabile nella riga 19 più la parte dinamica appena calcolata otteniamo la flag.