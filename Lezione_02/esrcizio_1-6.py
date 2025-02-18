ITS_menù:dict = {"Pizza": 9.00, "Pasta": 10.50, "Zuppa": 7.00,
"Hamburger": 15.50, "Cotoletta": 10.00, "Salmone": 20.20,
"Patatine fritte": 5.50, "Patate al forno": 5.50, "Verdura del giorno": 7.00,
"Cheescake": 6.00, "Tiramisù": 6.00, "Focaccia con nutella": 6.00,
"Coca Cola": 3.50, "Acqua": 1.50, "Vino": 5.00}
ordine:dict = {"Pizza": 9.00, "Cotoletta": 10.00, "Verdura del giorno": 7.00, "Cheescake": 6.00, "Acqua": 1.50}
totale = 0 
for value in ordine.values():
    totale += value
print(f"Il totale dell'ordine è: €{totale:.2f}")