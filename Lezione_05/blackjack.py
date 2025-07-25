def blackjack_hand_total(cards: list[int]) -> int:
    punteggio: int = 0
    assi: int = 0
    for i in cards:
        match i:
            case 2|3|4|5|6|7|8|9|10:
                punteggio += i
            case 11:
                punteggio += 11
                assi += 1
            case 1:
                punteggio += 1
    while punteggio > 21 and assi > 0:
        punteggio -= 10
        assi -= 1
    return punteggio


blackjack_hand_total([])