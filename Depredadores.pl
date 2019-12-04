animal(tigre).
clase(tigre, mamifero).
alimentacion(tigre, carnivoro).
piel(tigre, pelaje).
horario(tigre, diurno).
rol_cadena(tigre, consumidor_tercer_orden).

animal(conejo).
clase(conejo, mamifero).
alimentacion(conejo, herbivoro).
piel(conejo, pelaje).
horario(conejo, diurno).
rol_cadena(conejo, consumidor_primer_orden).

animal(zorro).
clase(zorro, mamifero).
alimentacion(zorro, carnivoro).
piel(zorro, pelaje).
horario(zorro, diurno).
rol_cadena(zorro, consumidor_segundo_orden).
seCome(X, Y) :- esPresa(X, Y).
seCome(X, Y) :- esPresa(X, Z), seCome(Z, Y).
presa(X) :-  alimentacion(X, herbivoro), rol_cadena(X, consumidor_primer_orden).