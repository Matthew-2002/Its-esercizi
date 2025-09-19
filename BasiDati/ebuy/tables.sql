create table Utente (
    username stringa primary key,
    registrazione timestamp not null
);

create table PostOggetto (
    descrizione stringa not null,
    pubblicazione timestamp not null,
    ha_feedback boolean not null,
    voto Voto,
    commento Stringa,
    utente Stringa not null,
    istante_feedback timestamp,
    id serial primary key,
    foreign key (utente) references
        Utente(username),
    check(
        (ha_feedback = true) 
                =
        (commento is not null) and
        (ha_feedback = true) 
                =
        (istante_feedback is not null) and
        (ha_feedback = true) 
                =
        (voto is not null) and
        (commento is null)
                or
        (ha_feedback = true)                 
    )
);

create table PostOggettoUsato (
    condizione Condizione not null,
    anni_garanzia IntGEZ not null,
    post_oggetto primary key,
    foreign key (post_oggetto) 
        references PostOggetto(id)
);
create table VenditoreProf (
    vetrina Url unique not null,
    utente Stringa primary key,
    foreign key (utente) references 
        Utente(username)
);

create table PostOggettoNuovo (
    anni_garanzia IntGE2 not null,
    post_oggetto integer primay key,
    foreign key (Post_Oggetto) 
        references PostOggetto(id)
);

create table Privato (
    utente Stringa primary key,
    foreign key (utente) references
        Utente(username)
);

create table Asta (
    prezzo_base RealGEZ not null,
    prezzo_bid RealGZ not null,
    scadenza timestamp not null,
    post_oggetto int primary key,
    foreign key (post_oggetto) references
        PostOggetto(id)
);

create table Bid (
    codice serial primary key,
    istante timestamp unique not null,
    asta int unique not null,
    privato Stringa not null,
    foreign key (asta) references
        Asta(post_oggetto),
    foreign key (privato) references
        Privato(utente)
);


create table CompraloSubito (
    prezzo RealGZ not null,
    post_oggetto integer primary key,
    foreign key (post_oggetto) references
        PostOggetto(id)
);

create table Acquirente (
    istante timestamp not null,
    privato Stringa not null,
    compralo_subito integer primary key,
    foreign key (compralo_subito) references
        CompraloSubito(post_oggetto),
    foreign key (privato) references
        Privato(utente)
);

create table MetodoDiPagamento (
    nome Stringa primary key  
);

create table Met_Post (
    id serial primary key,
    metodo_di_pagamento stringa not null,
    post_oggetto integer not null,
    foreign key (post_oggetto) 
        references PostOggetto(id),
    foreign key (metodo_di_pagamento) 
        references MetodoDiPagamento(nome)
);

create table Categoria (
    nome Stringa primary key,
    super Stringa,
    check (nome <> super)
);
alter table Categoria add 
foreign key (super) references
    Categoria(nome);