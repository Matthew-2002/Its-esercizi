create table Docente (
	mat integer not null,
	cognome varchar(100) not null,
	nome varchar(100) not null,
	email varchar(100) not null,
    primary key (mat)
);

create table Corso (
	codice integer not null,
	nome varchar(100),
	aula varchar(10),
    primary key (codice)
);

create table Incarico (
	docente integer not null,
	corso integer not null,
    primary key (docente, corso),
    foreign key (docente) references Docente(mat),
    foreign key (corso) references Corso(codice)
);





	
	
	
	

