-- 1. Quanti sono gli strutturati di ogni fascia?

select posizione, count(*)
from persona
group by posizione
;
-- 2. Quanti sono gli strutturati con stipendio ≥ 40000?

select count(*)
from persona
where stipendio >= 40000
;

-- 3. Quanti sono i progetti già finiti che superano il budget di 50000?

select count(*)
from progetto
where budget > 50000 and fine < CURRENT_DATE
;

-- 4. Qual è la media, il massimo e il minimo delle ore delle attività relative al progetto
-- ‘Pegasus’ ?

select avg(oredurata), max(oredurata), min(oredurata)
from attivitaprogetto ap, progetto p 
where p.nome = 'Pegasus' and ap.progetto = p.id
;

-- 5. Quali sono le medie, i massimi e i minimi delle ore giornaliere dedicate al progetto
-- ‘Pegasus’ da ogni singolo docente?

select p.id, p.nome, p.cognome, avg(oredurata), max(oredurata), min(oredurata)
from attivitaprogetto ap, progetto pr, persona p 
where pr.nome = 'Pegasus' and ap.progetto = pr.id 
    and p.id = ap.persona and (p.posizione = 'Professore Ordinario' or p.posizione = 'Professore Associato')
group by p.id
;

-- 6. Qual è il numero totale di ore dedicate alla didattica da ogni docente?

select p.id, p.nome, p.cognome, sum(oreDurata)
from AttivitaNonProgettuale anp, persona p 
where anp.persona = p.id and anp.tipo = 'Didattica'
group by p.id
;

-- 7. Qual è la media, il massimo e il minimo degli stipendi dei ricercatori?

select avg(stipendio), max(stipendio), min(stipendio)
from persona p
where p.posizione = 'Ricercatore'
;

-- 8. Quali sono le medie, i massimi e i minimi degli stipendi dei ricercatori, dei professori
-- associati e dei professori ordinari?

select posizione, avg(stipendio), max(stipendio), min(stipendio)
from persona p
group by posizione
;

-- 9. Quante ore ‘Ginevra Riva’ ha dedicato ad ogni progetto nel quale ha lavorato?

select prog.nome, sum(oredurata)
from progetto prog, attivitaprogetto ap, persona p 
where p.id = ap.persona and prog.id = ap.progetto and p.nome = 'Ginevra' and p.cognome = 'Riva'
group by prog.id
;

-- 10. Qual è il nome dei progetti su cui lavorano più di due strutturati?

select p.nome
from progetto p, attivitaprogetto a
where p.id = a.progetto
group by p.id
having count(distinct a.persona)> 2
;

-- 11. Quali sono i professori associati che hanno lavorato su più di un progetto?

select p.id, p.nome, p.cognome
from persona p, attivitaprogetto ap
where p.id = ap.persona and p.posizione = 'Professore Associato'
group by p.id
having count(ap.progetto) > 1
;