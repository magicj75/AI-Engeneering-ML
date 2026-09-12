from search import suche

anfrage = input("Wonach suchst du? ")

ergebnisse = suche(anfrage)

for score, notiz in ergebnisse[:3]:
    print(f"{score:.4f} - {notiz}")