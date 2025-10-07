-- 1. Quali sono i voli (codice e nome della compagnia) la cui 
-- durata supera le 3 ore?

select distinct
    v.codice, v.comp
from
    volo v
where
    v.durataMinuti > 60*3;

-- 2. Quali sono le compagnie che hanno voli che superano le 3 ore?

select distinct
    comp
from
    volo v
where
    v.durataMinuti > 60*3;

-- 3. Quali sono i voli (codice e nome della compagnia) che partono 
-- dall’aeroporto con codice ‘CIA’ ?

select distinct
    ap.codice, ap.comp
from 
    ArrPart ap
where 
    ap.partenza = 'CIA';

-- 4. Quali sono le compagnie che hanno voli che arrivano all’aeroporto 
-- con codice ‘FCO’ ?

select distinct
    ap.comp
from 
    ArrPart ap
where 
    ap.arrivo = 'FCO';

-- 5. Quali sono i voli (codice e nome della compagnia) che partono 
-- dall’aeroporto ‘FCO’ e arrivano all’aeroporto ‘JFK’ ?

select distinct
    ap.codice, ap.comp
from 
    ArrPart ap
where 
    ap.partenza = 'FCO' and
    ap.arrivo = 'JFK';

-- 6. Quali sono le compagnie che hanno voli che partono dall’aeroporto 
-- ‘FCO’ e atterrano all’aeroporto ‘JFK’ ?

select distinct
    ap.comp
from 
    ArrPart ap
where 
    ap.partenza = 'FCO' and
    ap.arrivo = 'JFK';

-- 7. Quali sono i nomi delle compagnie che hanno voli diretti dalla 
-- città di ‘Roma’ alla città di ‘New York’ ?

select distinct
    ap.comp
from 
    ArrPart ap, LuogoAeroporto la1, 
    LuogoAeroporto la2
where 
    la1.citta = 'Roma'and
    la2.citta = 'New York' and
    la1.aeroporto = ap.partenza and
    la2.aeroporto = ap.arrivo;

-- 8. Quali sono gli aeroporti (con codice IATA, nome e luogo) nei 
-- quali partono voli della compagnia di nome ‘MagicFly’ ?

select distinct
    la.aeroporto, a.nome, 
    la.nazione, la.citta
from
    LuogoAeroporto la, ArrPart ap,
    aeroporto a
where
    'MagicFly' = ap.comp and
    ap.partenza = la.aeroporto and
    la.aeroporto = a.codice;


-- 9. Quali sono i voli che partono da un qualunque aeroporto della 
-- città di ‘Roma’ e atterrano ad un qualunque aeroporto della 
-- città di ‘New York’ ? Restituire: codice del volo, nome della compagnia, 
-- e aeroporti di partenza e arrivo.

select 
    ap.codice as codice_volo,
    ap.comp as compagnia,
    la1.aeroporto as aereoporto_partenza, 
    la2.aeroporto as aereoporto_arrivo
from 
    ArrPart ap, LuogoAeroporto la1,
    LuogoAeroporto la2
where
    la1.citta = 'Roma' and
    la2.citta = 'New York' and
    ap.partenza = la1.aeroporto and
    ap.arrivo = la2.aeroporto;

-- 10. Quali sono i possibili piani di volo con esattamente un cambio 
-- (utilizzando solo voli della stessa compagnia) da un qualunque 
-- aeroporto della città di ‘Roma’ ad un qualunque aeroporto della città di 
-- ‘New York’ ? Restituire: nome della compagnia, codici dei voli, e 
-- aeroporti di partenza, scalo e arrivo.

select distinct
    ap1.comp as compagnia,
    ap1.codice as volo1,
    ap2.codice as volo2,
    ap1.partenza as partenza,
    ap1.arrivo as scalo,
    ap2.arrivo as arrivo
from 
    ArrPart ap1, ArrPart ap2,
    LuogoAeroporto l1, LuogoAeroporto l2
where 
    l1.citta = 'Roma' and
    l2.citta = 'New York' and
    ap1.comp = ap2.comp and
    l1.aeroporto = ap1.partenza and
    l2.aeroporto = ap2.arrivo and
    ap1.arrivo = ap2.partenza;

-- 11. Quali sono le compagnie che hanno voli che partono dall’aeroporto 
-- ‘FCO’, atterrano all’aeroporto ‘JFK’, e di cui si conosce l’anno di fondazione?

select distinct
    ap.comp
from
    ArrPart ap, compagnia c
where
    ap.partenza = 'FCO' and
    ap.arrivo = 'JFK' and
    ap.comp = c.nome and
    c.annoFondaz > 1899;
