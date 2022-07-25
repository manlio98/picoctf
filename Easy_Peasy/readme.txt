Istruzioni per completare la sfida ctf "Easy Peasy":

1) Analizzando il codice, si nota che c'è un'operazione di modulo.
2) Passando come input, 50000 (keylen) - 32, si ritorna "l'inizio del file" al ciclo successivo.
3) Passando come input, 32 , si può prendere la flag cifrata
4) Istruzioni da seguire per eseguire il passo 2 e passo 3: "python -c "print('a'*49968); print('a'*32)" | nc mercury.picoctf.net 58913"
5) Preleva la chiave cifrata (appena esegue il programma easy peasy) e l'output del passo 4.
6) Per ottenere la flag eseguire il programma "getflag".