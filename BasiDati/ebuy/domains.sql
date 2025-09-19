CREATE domain IntGE2 as integer check (value > 1);
CREATE type Condizione as enum ('Ottimo', 'Buono', 'Discreto', 'Da Sistemare');
CREATE domain Url as varchar(255);
CREATE domain Stringa as varchar(100);
CREATE domain RealGEZ as real check (value >= 0);
CREATE domain RealGZ as real check (value > 0);
CREATE domain IntGEZ as integer check (value >= 0);
CREATE domain Voto as integer check (value > 0 and value < 6);
