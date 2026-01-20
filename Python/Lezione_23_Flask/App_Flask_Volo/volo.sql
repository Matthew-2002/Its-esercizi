CREATE domain Stringa as varchar; 
CREATE domain IntGZ as integer 
    check (value > 0);
CREATE domain IntG1900 as integer 
    check (value > 1900); 
CREATE domain IntGEZ as integer 
    check (value >= 0); 

CREATE Table Nazione (
    nome Stringa primary key
);

CREATE Table Città (
    id integer primary key,
    nome Stringa,
    n_abitanti IntGEZ not null,
    nazione Stringa not null,

    unique (nome,nazione),

    foreign key(nazione)
        references nazione(nome)
);

CREATE Table Aeroporto (
    codice Stringa primary key,
    nome Stringa not null,
    città integer not null,
    foreign key(città)
        references città(id)
);

CREATE Table CompagniaAerea(
    nome Stringa primary key,
    fondazione IntG1900 not null,
    città integer not null,
    foreign key(città)
        references città(id)
);

CREATE Table Volo (
    codice Stringa primary key,
    durata_in_minuti IntGZ not null,
    partenza Stringa not null,
    arrivo Stringa not null,
    CompagniaAerea Stringa not null,
    foreign key(partenza)
        references Aeroporto(codice),
    foreign key(arrivo)
        references Aeroporto(codice),
    foreign key(CompagniaAerea)
        references CompagniaAerea(nome)
);