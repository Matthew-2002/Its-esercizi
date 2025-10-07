-- 1. Quante sono le compagnie che operano (sia in arrivo che in partenza) nei diversi
-- aeroporti?

select apo.codice, apo.nome, count(distinct ap.comp)
from ArrPart ap, aeroporto apo
where ap.partenza = apo.codice or ap.arrivo = apo.codice
group by apo.codice, apo.nome
;
-- 2. Quanti sono i voli che partono dall’aeroporto ‘HTR’ e hanno una durata di almeno
-- 100 minuti?

select count(*) as voli_lunghi
from volo v, ArrPart ap 
where v.comp = ap.comp and
    v.codice = ap.codice and
    ap.partenza = 'HTR' and 
    v.durataMinuti > 99
;
-- 3. Quanti sono gli aeroporti sui quali opera la compagnia ‘Apitalia’, per ogni nazione
-- nella quale opera?

select nazione, count(distinct aeroporto)
from LuogoAeroporto l, aeroporto apo, ArrPart ap
where l.aeroporto = apo.codice and
    (ap.arrivo = apo.codice or ap.partenza = apo.codice) and
    ap.comp = 'Apitalia'
group by nazione
;
-- 4. Qual è la media, il massimo e il minimo della durata dei voli effettuati dalla
-- compagnia ‘MagicFly’?

select min(durataMinuti) as volo_piuCorto,
    max(durataMinuti) as volo_piuLungo,
    round(avg(durataMinuti), 2) as media_durate
from volo v
where comp = 'MagicFly'
;
-- 5. Qual è l’anno di fondazione della compagnia più vecchia che opera in ognuno degli
-- aeroporti?

select a.nome as nome_aereoporto,
    max(annoFondaz) as anno_fondazione
from aeroporto a, ArrPart ap, compagnia c 
where (ap.arrivo = a.codice or ap.partenza = a.codice) and
    ap.comp = c.nome
group by a.nome
; -- come far apparire nome compagnia

-- 6. Quante sono le nazioni (diverse) raggiungibili da ogni nazione tramite uno o più
-- voli?

select la1.nazione, count(distinct la2.nazione) as nazioni_raggiungibili
from LuogoAeroporto la1, LuogoAeroporto la2,
    ArrPart ap1
where ap1.partenza = la1.aeroporto and
    ap1.arrivo = la2.aeroporto and 
    la1.nazione <> la2.nazione
group by la1.nazione
;
-- 7. Qual è la durata media dei voli che partono da ognuno degli aeroporti?

select apo.nome, round(avg(durataMinuti), 2) as durata_media_partenze
from volo v, ArrPart ap, aeroporto apo
where v.codice = ap.codice and
    v.comp = ap.comp and
    ap.partenza = apo.codice
group by apo.nome
;
-- 8. Qual è la durata complessiva dei voli operati da ognuna delle compagnie fondate
-- a partire dal 1950?

select c.nome, sum(durataMinuti) as somma_durate
from volo v, compagnia c
where v.comp = c.nome and 
    c.annoFondaz > 1949
group by c.nome
;
-- 9. Quali sono gli aeroporti nei quali operano esattamente due compagnie?

select a.codice, a.nome as nome_aereoporto
from aeroporto a, ArrPart ap 
where (ap.arrivo = a.codice or ap.partenza = a.codice)
group by a.nome, a.codice
having count(distinct comp) = 2
;
-- 10. Quali sono le città con almeno due aeroporti?

select citta
from LuogoAeroporto la
group by citta
having count(aeroporto) >= 2
;
-- 11. Qual è il nome delle compagnie i cui voli hanno una durata media maggiore di 6
-- ore?

select v.comp
from volo v
group by v.comp
having avg(durataMinuti) > 60*6
;
-- 12. Qual è il nome delle compagnie i cui voli hanno tutti una durata maggiore di 100
-- minuti?

select distinct c.nome
from compagnia c, volo v
where v.comp = c.nome
group by c.nome
having min(durataMinuti) > 100
;

-- 14. Qual è il nome delle compagnie che non hanno alcun volo?

select nome 
from compagnia 
except
select distinct comp
from volo v
;


with D as (
    select distinct v.comp
    from volo v
    )
select nome
from compagnia, D
where nome not in (D.comp)
;

