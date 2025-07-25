-- 1
select 
    w.id, w.nome, 
    w.inizio, w.fine 
from 
    progetto p, wp w 
where 
    p.nome = 'Pegasus' and 
    w.progetto = p.id;

-- 2
select distinct 
    pers.nome, cognome, 
    pers.posizione 
from 
    persona pers, attivitaprogetto ap, 
    progetto prog 
where 
    pers.id = ap.persona and 
    ap.progetto = prog.id and 
    prog.nome = 'Pegasus' 
order by cognome desc;


-- 3
select distinct
    pers.nome, pers.cognome,
    pers.posizione
from
    persona pers, attivitaprogetto ap1,
    attivitaprogetto ap2, progetto prog
where
    pers.id = ap1.persona and
    pers.id = ap2.persona and
    ap1.progetto = prog.id and
    prog.nome = 'Pegasus' and 
    ap1.id <> ap2.id;


-- 4
select distinct 
    pers.nome, pers.cognome 
from 
    persona pers, assenza a 
where 
    pers.posizione = 'Professore Ordinario' and 
    a.tipo = 'Malattia' and 
    pers.id = a.persona;

-- 5
select distinct 
    pers.nome, pers.cognome 
from 
    persona pers, assenza a1, 
    assenza a2 
where 
    pers.posizione = 'Professore Ordinario' and 
    a1.tipo = 'Malattia' and 
    a2.tipo = a1.tipo and 
    pers.id = a1.persona and 
    a1.persona = a2.persona and 
    a1.id <> a2.id;

-- 6
select distinct 
    p.nome, p.cognome 
from 
    persona p, attivitanonprogettuale anp 
where 
    p.posizione = 'Ricercatore' and 
    anp.tipo = 'Didattica' and 
    p.id = anp.persona;

-- 7
select distinct 
    p.nome, p.cognome 
from 
    persona p, attivitanonprogettuale anp1, 
    attivitanonprogettuale anp2 
where 
    p.posizione = 'Ricercatore' and 
    anp1.tipo = 'Didattica' and 
    anp2.tipo = anp1.tipo and 
    p.id = anp1.persona and 
    anp1.persona = anp2.persona and 
    anp1.id <> anp2.id;

-- 8
select distinct 
    p.nome, p.cognome 
from 
    persona p, attivitaprogetto ap, 
    attivitanonprogettuale anp 
where 
    ap.giorno = anp.giorno and 
    p.id = ap.persona and 
    ap.persona = anp.persona;

-- 9
select distinct 
    p.nome, p.cognome, ap.giorno, 
    prog.nome, ap.oredurata, anp.tipo, 
    anp.oredurata
from 
    persona p, attivitaprogetto ap, 
    attivitanonprogettuale anp, progetto prog
where 
    ap.giorno = anp.giorno and 
    p.id = ap.persona and 
    ap.persona = anp.persona and 
    prog.id = ap.progetto;

-- 10
select distinct 
    p.nome, p.cognome
from 
    persona p, assenza a, attivitaprogetto ap
where 
    a.giorno = ap.giorno and 
    ap.persona = p.id and 
    a.persona = p.id;

-- 11
select distinct 
    p.nome, p.cognome, a.giorno, 
    a.tipo, prog.nome, ap.oredurata
from 
    persona p, assenza a, attivitaprogetto ap, 
    progetto prog
where 
    a.giorno = ap.giorno and 
    ap.persona = p.id and 
    a.persona = p.id and 
    prog.id = ap.progetto;

-- 12
select distinct 
    wp1.nome
from 
    wp wp1, wp wp2
where 
    wp1.nome = wp2.nome and 
    wp1.progetto <> wp2.progetto;




