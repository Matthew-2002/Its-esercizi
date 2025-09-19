create domain stringa as varchar;

create domain IntGEZ as integer
	check (value >= 0);


create domain RealGEZ as real
	check (value >= 0);


create type ruolo as enum
	('Direttore', 'Segretario', 'Progettista');

create domain codicefiscale as char(16)
	check (value ~ '^[A-Z]{6}\d{2}[A-Z]\d{2}[A-Z]\d{3}[A-Z]$');