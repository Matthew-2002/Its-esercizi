begin transaction;

CREATE domain Stringa  as varchar(100);

CREATE domain RealGEZ as Real check
    (value >= 0);

CREATE domain IntGEZ as integer check
    (value >= 0);

CREATE domain Real0_1 as Real check
    (value >= 0 and value <= 1);

CREATE domain CAP as varchar(5) check (value ~ '^[0-9]{5}$');

CREATE type Indirizzo as(
        via Stringa,
        civico Stringa,
        CAP CAP
);
CREATE domain CodiceFiscale as varchar(16) check
        (value ~ '^[A-Z]{6}[0-9]{2}[A-Z][0-9]{2}[A-Z][0-9]{3}[A-Z]$');

CREATE domain partitaiva as varchar(11) check (value ~ '^[0-9]{11}$');

CREATE domain Telefono as varchar(17) check (value ~ '^\+([0-9]{1,3})([ ]?[0-9]){6,14}$');

CREATE domain Email as varchar(100) check
        (value ~ '^[A-Za-z0-9._-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$');

CREATE type stato as enum (
    'in preparazione', 
    'inviato', 'da saldare', 
    'saldato'
);

CREATE table nazione (
    nome Stringa primary key
);
CREATE table regione (
    nome Stringa not null,
    nazione Stringa not null,
    primary key (nome, nazione),
    foreign key (nazione) references nazione(nome)
);
CREATE table citta (
    nome Stringa not null,
    regione Stringa not null,
    nazione Stringa not null,
    id integer primary key,
    unique (nome, regione, nazione) 
);
create table Direttore (
    nome Stringa not null,
    cognome Stringa not null,
    data_nascita date not null,
    anni_servizio IntGEZ not null,
    citta integer not null,
    cf CodiceFiscale primary key,
    foreign key (citta) references citta(id)
);
CREATE table Dipartimento (
    nome Stringa primary key,
    indirizzo Indirizzo not null,
    direttore CodiceFiscale not null,
    unique (direttore),
    foreign key (direttore) references direttore(cf)
);

CREATE table fornitore (
    ragione_sociale Stringa not null,
    partitaiva partitaiva primary key,
    indirizzo indirizzo not null,
    telefono Telefono not null,
    email Email not null
);
CREATE table ordine (
    data_stipula date not null,
    imponibile RealGEZ  not null,
    aliquotaIVA Real0_1 not null,
    descrizione Stringa not null,
    stato stato not null,
    dipartimento Stringa not null,
    fornitore partitaiva not null,
    id IntGEZ primary key,
    unique (dipartimento),
    unique (fornitore)
);

commit;