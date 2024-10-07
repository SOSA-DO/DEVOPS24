import random  # Importera random för att dra slumpmässiga kort

# Funktion som representerar en kortlek där Ess kan vara 1 eller 14
def dra_kort() -> int:
    """
    Drar ett kort med ett slumpmässigt värde mellan 1 och 14.
    Ess kan vara antingen 1 eller 14.
    :return: Värdet av det dragna kortet (int).
    """
    kort: int = random.randint(2, 14)  # Kortens värden sträcker sig från 2 till 14
    if kort == 14:  # Ess (14) kan räknas som 1 eller 14
        return random.choice([1, 14])
    return kort

# Funktion som representerar spelarens tur
def spelar_tur() -> int:
    """
    Spelaren drar kort tills hen väljer att stanna eller går över 21.
    :return: Spelarens totala poäng (int).
    """
    spelar_total: int = 0
    
    while True:
        # Dra ett kort och addera det till spelarens total
        kort: int = dra_kort()
        spelar_total += kort
        print(f"Du drog ett kort med värdet: {kort}. Din totala poäng är nu: {spelar_total}.")
        
        # Kontrollera om spelaren har gått över 21
        if spelar_total > 21:
            print("Du gick över 21! Datorn vinner.")
            return spelar_total
        
        # Fråga spelaren om hen vill dra ett till kort
        choice: str = input("Vill du dra ett till kort? (ja/nej): ").lower()
        if choice == 'nej':
            break
    
    return spelar_total

# Funktion som representerar datorns tur
def dator_tur(spelar_total: int) -> int:
    """
    Datorn drar kort tills den antingen går över 21 eller stannar baserat på spelarens poäng.
    :param spelar_total: Spelarens totala poäng (int) som datorn måste slå.
    :return: Datorns totala poäng (int).
    """
    dator_total: int = 0
    
    while dator_total <= spelar_total and dator_total <= 21:
        # Datorn drar ett kort och adderar det till sin total
        kort: int = dra_kort()
        dator_total += kort
        print(f"Datorn drog ett kort med värdet: {kort}. Datorns totala poäng är nu: {dator_total}.")
        
        # Om datorn går över 21, datorn förlorar
        if dator_total > 21:
            print("Datorn gick över 21! Du vinner.")
            return dator_total
    
    return dator_total

# Funktion som styr hela spelet
def tjugoett_spel() -> None:
    """
    Huvudfunktionen som hanterar hela spelet Tjugoett.
    :return: None
    """
    print("Välkommen till kortspelet Tjugoett!")
    
    # Spelaren börjar sin tur
    spelar_total: int = spelar_tur()
    
    # Om spelaren redan har förlorat (gick över 21), avsluta spelet
    if spelar_total > 21:
        return
    
    # Datorns tur börjar
    dator_total: int = dator_tur(spelar_total)
    
    # Avgör vinnaren efter datorns tur
    if dator_total > 21:
        # Datorn förlorade genom att gå över 21
        print("Grattis! Du vann spelet.")
    elif dator_total > spelar_total:
        # Datorn har mer poäng än spelaren
        print(f"Datorn vinner med {dator_total} poäng mot dina {spelar_total} poäng.")
    else:
        # Spelaren har fler poäng än datorn eller lika många (datorn vinner vid lika poäng)
        print(f"Grattis! Du vann med {spelar_total} poäng mot datorns {dator_total} poäng.")

# Starta spelet
if __name__ == "__main__":
    tjugoett_spel()
