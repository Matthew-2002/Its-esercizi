--1 Quali sono i nomi degli impiegati nati a partire dall'anno 1988

select distinct
    p.nome, 
    p.cognome
from 
    impiegato i,
    persona p
where
    p.data_nascita >= '01/01/1900' and
    p.cf = i.persona
;
--2 Quali sono i nomi di tutti i progetti?

select distinct
    p.nome
from 
    progetto p
;
--3 Quali sono gli stipendi dei direttori?

select distinct
    i.stipendio
from 
    impiegato i
where 
    i.ruolo = 'Direttore'
;
--4 Quanti sono i progettisti?

select
    count(*) as numero_progettisti
from 
    impiegato 
where   
    impiegato.ruolo = 'Progettista'
;
--5 Quanti sono i responsabili?

select
    count(distinct p.resp_prog) as numero_responsabili
from 
    impiegato i,
    progetto p
where   
    i.ruolo = 'Progettista' and
    p.resp_prog = i.persona
;
--6 Quanti sono i progettisti che non sono responsabili? Non la sapete fare!

select
    *
from 
    impiegato i,
    progetto p
where   
    i.ruolo = 'Progettista' and
    p.resp_prog <> i.persona
;
--7 Qual è lo stipendio medio dei segretari?


--8 Qual è l'età della/o studente meno giovane?
    --usare select(date_part('year',age(current_date, <DATA DI NASCITA>))) as eta FROM [...];

select
    (date_part('year',age(current_date, p1.data_nascita))) as eta,
    p1.nome as nome
from 
    persona p1,
    persona p2,
    studente s1,
    studente s2
where
    s1.persona = p1.cf and
    s2.persona = p2.cf and
    (date_part('year',age(current_date, p1.data_nascita))) > 
        (date_part('year',age(current_date, p2.data_nascita)))
;
--9 Quanti sono i direttori che hanno assolto agli obblighi militari?
--10 Quanti sono i progetti di cui è responsabile un'impiegata con almeno due figli?
