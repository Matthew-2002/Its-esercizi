-- 1. Elencare tutti i progetti la cui fine è successiva al
-- 2023-12-31. [2 punti]

select *
from progetto p
where p.fine > '2023-12-31'
;

-- 2. Contare il numero totale di persone per ciascuna posizione
-- (Ricercatore, Professore Associato, Professore Ordinario).
-- [3 punti]

select posizione, count(*)
from persona p
group by posizione
;

-- 3. Restituire gli id e i nomi delle persone che hanno almeno
-- un giorno di assenza per "Malattia". [2 punti]

select distinct p.id, p.nome, p.cognome
from persona p, assenza a 
where p.id = a.persona and a.tipo = 'Malattia'
;

-- 4. Per ogni tipo di assenza, restituire il numero complessivo
-- di occorrenze. [3 punti]

select tipo, count(*)
from assenza
group by tipo
;

-- 5. Calcolare lo stipendio massimo tra tutti i "Professori
-- Ordinari". [2 punti]

select max(stipendio)
from persona p
where posizione = 'Professore Ordinario'
;

-- 6. Quali sono le attività e le ore spese dalla persona con id 1
-- nelle attività del progetto con id 4, ordinate in ordine
-- decrescente. Per ogni attività, restituire l’id, il tipo e il
-- numero di ore. [3 punti]

select oredurata
from persona p, attivitaprogetto ap
where ap.progetto = 4 and p.id = 1
order by oredurata desc
;

-- 7. Quanti sono i giorni di assenza per tipo e per persona. Per
-- ogni persona e tipo di assenza, restituire nome, cognome,
-- tipo assenza e giorni totali. [4 punti]

select p.id, p.nome, p.cognome, a.tipo, count(a.id)
from persona p, assenza a
where p.id = a.persona
group by tipo, p.id
;

-- 8. Restituire tutti i “Professori Ordinari” che hanno lo
-- stipendio massimo. Per ognuno, restituire id, nome e
-- cognome [4 punti]

select id, nome, cognome, stipendio
from persona p 
where posizione = 'Professore Ordinario'
    and stipendio = (
        select max(stipendio)
        from persona p 
        where posizione = 'Professore Ordinario'
);

-- 9. Restituire la somma totale delle ore relative alle attività
-- progettuali svolte dalla persona con id = 3 e con durata
-- minore o uguale a 3 ore. [3 punti]

select sum(oredurata)
from attivitaprogetto ap
where ap.oredurata <= 3 and ap.persona = 3
;

-- 10. Restituire gli id e i nomi delle persone che non hanno
-- mai avuto assenze di tipo "Chiusura Universitaria" [4
-- punti]

select p.id, p.nome, p.cognome
from persona p left join assenza a on 
    p.id = a.persona and a.tipo = 'Chiusura Universitaria'
where a.id is null
;