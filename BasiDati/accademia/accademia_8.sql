--1. Quali sono le persone (id, nome e cognome) che hanno avuto assenze solo nei
-- giorni in cui non avevano alcuna attivitÃ (progettuali o non progettuali)?

select p.id, p.nome, p.cognome
from assenza a left join attivitaprogetto ap 
    on ap.persona = a.persona and ap.giorno = a.giorno 
        join attivitanonprogettuale anp 
            on a.persona = anp.persona and a.giorno = anp.giorno
                right join persona p 
                    on p.id = a.persona
where a.id is null
order by p.id
;

-- 2. Quali sono le persone (id, nome e cognome) che non hanno mai partecipato ad
-- alcun progetto durante la durata del progetto “Pegasus”?

select pe.id, pe.nome, pe.cognome
from attivitaprogetto ap left join progetto p 
    on p.nome = 'Pegasus'
    and (ap.giorno >= p.inizio and ap.giorno <= p.fine)
        right join persona pe 
            on ap.persona = pe.id
where ap.id is null
order by pe.id
;

-- 3. Quali sono id, nome, cognome e stipendio dei ricercatori con stipendio maggiore
-- di tutti i professori (associati e ordinari)?


select r.id, r.nome, r.cognome, r.stipendio 
from persona r
where r.posizione = 'Ricercatore' 
    and r.stipendio > (
    select max(p.stipendio)
    from persona p
    where p.posizione = 'Professore Associato' 
    or p.posizione = 'Professore Ordinario'
)
;

with max_stipendio as (
    select max(p.stipendio)
    from persona p
    where p.posizione = 'Professore Associato' or p.posizione = 'Professore Ordinario'
)
select r.id, r.nome, r.cognome, r.stipendio 
    from max_stipendio right join persona r on r.stipendio >= max_stipendio.max 
        and r.posizione = 'Ricercatore'
where max is not null
;

-- 4. Quali sono le persone che hanno lavorato su progetti con un budget superiore alla
-- media dei budget di tutti i progetti?

select distinct pe.id, pe.nome, pe.cognome
from progetto p
        right join attivitaprogetto ap 
            on p.id = ap.progetto
                join persona pe 
                    on ap.persona = pe.id
where p.budget > (select avg(pr.budget) from progetto pr)
order by pe.id
;

with media_budget as (
    select avg(p.budget)
    from progetto p
)
select distinct pe.id, pe.nome, pe.cognome
from media_budget right join progetto p2 
    on p2.budget > media_budget.avg
        right join attivitaprogetto ap 
            on p2.id = ap.progetto
                join persona pe 
                    on ap.persona = pe.id
where avg is not null
order by pe.id
;

-- 5. Quali sono i progetti con un budget inferiore allala media, ma con un numero
-- complessivo di ore dedicate alle attività di ricerca sopra la media?

select ap.progetto, p.nome
from progetto p join attivitaprogetto ap 
    on ap.progetto = p.id
where p.budget < (
    select avg(pr.budget)
    from progetto pr
) and ap.tipo = 'Ricerca e sviluppo'
group by ap.progetto, p.nome
having sum(ap.oreDurata) > (
    select avg(ap.oreDurata)
    from attivitaprogetto ap
    where ap.tipo = 'Ricerca e sviluppo'
);

with media_budget as (
    select avg(p.budget)
    from progetto p
), media_ore_ricerca as (
    select avg(ap.oreDurata)
    from attivitaprogetto ap
    where ap.tipo = 'Ricerca e sviluppo'
), tot_ore_ricerca_prog as (
    select sum(oreDurata), ap.progetto
    from attivitaprogetto ap
    where ap.tipo = 'Ricerca e sviluppo' 
    group by ap.progetto
)
select * 
from media_budget join progetto p on p.budget < media_budget.avg
    join tot_ore_ricerca_prog tot on tot.progetto = p.id
        join media_ore_ricerca on tot.sum > media_ore_ricerca.avg
;

        