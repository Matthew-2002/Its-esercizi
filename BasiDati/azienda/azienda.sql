CREATE domain Stringa as varchar(100);

CREATE domain Valore as Real 
    check (value >= 0);

CREATE domain Valuta as varchar(3);

CREATE type Denaro as (
    valore Valore,
    valuta Valuta
);

CREATE domain IntGZ as integer
    check (value > 0);

CREATE type Indirizzo as (
    via Stringa,
    civico Stringa,
    cap varchar(5)
);

CREATE domain CF as varchar(16);

CREATE table Impiegato (
    nome Stringa not null,
    cognome Stringa not null,
    data_nascita date not null,
    stipendio Denaro not null,
    matricola IntGZ primary key
);

CREATE table Dipartimento (
    nome Stringa not null,
    telefono Stringa not null,
    codice IntGZ primary key
);

CREATE table Afferisce (
    data_afferenza date not null,
    dipartimento IntGZ not null,
    impiegato IntGZ primary key,
    foreign key (impiegato) references impiegato(matricola),
    foreign key (dipartimento) references dipartimento(codice)
);

CREATE table Dirige (
    impiegato IntGZ not null,
    dipartimento IntGZ primary key,
    foreign key (impiegato) references impiegato(matricola),
    foreign key (dipartimento) references impiegato(matricola)
);

CREATE table Progetto (
    nome Stringa primary key,
    budget Denaro not null
);

CREATE table Partecipa (
    impiegato IntGZ,
    progetto Stringa,
    primary key (impiegato, progetto),
    foreign key (impiegato) references impiegato(matricola),
    foreign key (progetto) references progetto(nome)
);

