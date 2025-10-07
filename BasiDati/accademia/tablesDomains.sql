CREATE type Strutturato as enum(
    'Ricercatore',
    'Professore Associato',
    'Professore Ordinario'
);
CREATE type LavoroProgetto as enum(
    'Ricerca e sviluppo',
    'Dimostrazione',
    'Management',
    'Altro'
);
CREATE type LavoroNonProgettuale as enum(
    'Didattica',
    'Ricerca',
    'Missione',
    'Incontro Dipartimentale',
    'Incontro Accademico',
    'Altro'    
);
CREATE type CausaAssenza as enum(
    'Chiusura Universitaria', 
    'Maternita', 
    'Malattia'
);
CREATE domain PosInteger as integer
    check(
        value >= 0
    );
CREATE domain StringaM as varchar(100);
CREATE domain NumeroOre as integer
    check(
        value >= 0 and 
        value <= 8
    );
CREATE domain Denaro as real
    check(
        value >= 0
    );

CREATE table Persona(
    id PosInteger primary key,
    nome StringaM not null,
    cognome StringaM not null,
    posizione Strutturato not null,
    stipendio Denaro not null
);
CREATE table Progetto(
    id PosInteger not null,
    nome StringaM not null,
    inizio date not null,
    fine date not null,
    budget Denaro not null,
    primary key (id),
    unique (nome),
    check(inizio < fine)
);
CREATE table WP(
    progetto PosInteger not null,
    id PosInteger not null,
    nome StringaM not null,
    inizio date not null,
    fine date not null,
    primary key (progetto, id),
    unique (progetto, nome),
    foreign key (progetto) references Progetto(id),
    check(inizio < fine)
);
CREATE table AttivitaProgetto(
    id PosInteger not null,
    persona PosInteger not null,
    progetto PosInteger not null,
    wp PosInteger not null,
    giorno date not null,
    tipo LavoroProgetto not null,
    oreDurata NumeroOre not null,
    primary key (id),
    foreign key (persona) references Persona(id),
    foreign key (progetto, wp) references WP(progetto, id)
);
CREATE table AttivitaNonProgettuale(
    id PosInteger not null,
    persona PosInteger not null,
    tipo LavoroNonProgettuale not null,
    giorno date not null,
    oreDurata NumeroOre not null,
    primary key (id),
    foreign key (persona) references Persona(id)
);
CREATE table Assenza(
    id PosInteger not null,
    persona PosInteger not null,
    tipo CausaAssenza not null,
    giorno date not null,
    primary key (id),
    foreign key (persona) references Persona(id)
);
