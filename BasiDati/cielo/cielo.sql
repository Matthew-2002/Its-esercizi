CREATE domain PosInteger as integer 
    check (value >= 0);

CREATE domain StringaM as varchar(100);

CREATE domain CodIATA as char(3);

CREATE table Compagnia (
    nome StringaM primary key,
    annoFondaz PosInteger
);

CREATE table LuogoAeroporto (
    aeroporto CodIATA primary key,
    citta StringaM,
    nazione StringaM
);

CREATE table Aeroporto (
    codice CodIATA primary key,
    nome StringaM not null,
    foreign key (codice) references LuogoAeroporto(aeroporto) deferrable
);

alter table LuogoAeroporto add
foreign key (aeroporto) references Aeroporto(codice) deferrable;

CREATE table Volo (
    codice PosInteger not null,
    comp StringaM not null,
    durataMinuti PosInteger not null,
    primary key (codice, comp),
    foreign key (comp) references Compagnia(nome)
);

CREATE table ArrPart (
    codice PosInteger not null,
    comp StringaM not null,
    arrivo CodIATA not null,
    partenza CodIATA not null,
    primary key (codice, comp),
    foreign key (arrivo) references Aeroporto(codice),
    foreign key (partenza) references Aeroporto(codice),
    foreign key (codice, comp) references Volo(codice, comp) deferrable
);

alter table Volo add 
foreign key (codice, comp) references ArrPart (codice, comp) deferrable;
