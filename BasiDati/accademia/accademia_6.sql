-- 1. Quanti sono gli strutturati di ogni fascia?

select posizione, count(*)
from persona
group by posizione
;
-- 2. Quanti sono gli strutturati con stipendio ≥ 40000?

select count(*)
from persona p
where stipendio >= 40000
;
-- 3. Quanti sono i progetti già finiti che superano il budget di 50000?

select count(*)
from progetto p
where budget > 50000 and fine < now()
;
-- 4. Qual è la media, il massimo e il minimo delle ore delle attività relative al progetto
-- ‘Pegasus’ ?

select avg(oreDurata), max(oreDurata), min(oreDurata)
from AttivitaProgetto ap, progetto p
where p.nome = 'Pegasus' and ap.progetto = p.id
;
-- 5. Quali sono le medie, i massimi e i minimi delle ore giornaliere dedicate al progetto
-- ‘Pegasus’ da ogni singolo docente?

select pers.nome, pers.cognome, avg(oreDurata) as media, 
    min(oreDurata) as min, max(oreDurata) as max
from progetto p, AttivitaProgetto ap, persona pers
where p.nome = 'Pegasus' and ap.progetto = p.id and ap.persona = pers.id
group by pers.id
;
-- 6. Qual è il numero totale di ore dedicate alla didattica da ogni docente?

select p.nome, p.cognome, sum(oreDurata) as ore
from AttivitaNonProgettuale anp, persona p
where p.id = anp.persona and anp.tipo = 'Didattica'
group by p.id
;
-- 7. Qual è la media, il massimo e il minimo degli stipendi dei ricercatori?

select avg(stipendio), min(stipendio), max(stipendio)
from persona p
where p.posizione = 'Ricercatore'
;
-- 8. Quali sono le medie, i massimi e i minimi degli stipendi dei ricercatori, dei professori
-- associati e dei professori ordinari?

select posizione, avg(stipendio), min(stipendio), max(stipendio)
from persona p
group by posizione
;
-- 9. Quante ore ‘Ginevra Riva’ ha dedicato ad ogni progetto nel quale ha lavorato?

select progetto, prog.nome, sum(oreDurata)
from persona pers, AttivitaProgetto ap, progetto prog
where prog.id = ap.progetto and ap.persona = pers.id 
    and pers.nome = 'Ginevra' and pers.cognome = 'Riva'
group by ap.progetto, prog.id
;
-- 10. Qual è il nome dei progetti su cui lavorano più di due strutturati?

select p. id, p.nome
from AttivitaProgetto ap, progetto p
where ap.progetto = p.id
group by p.id
having count(distinct ap.persona) > 2
;
-- 11. Quali sono i professori associati che hanno lavorato su più di un progetto?

select pers.nome, pers.cognome
from persona pers, AttivitaProgetto ap
where ap.persona = pers.id and pers.posizione = 'Professore Associato'
group by pers.id
having count(ap.progetto) > 1
;
