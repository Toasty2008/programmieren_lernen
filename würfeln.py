import random

def wuerfeln():
    return random.randint(1, 6)

def spiel():
    print("Würfelspiel!")
    spieler1 = input("Name von Spieler 1: ")
    spieler2 = input("Name von Spieler 2: ")
    punkte1 = 0
    punkte2 = 0

    for runde in range(1, 6):
        print(f"\n--- Runde {runde} ---")
        wurf1 = wuerfeln()
        wurf2 = wuerfeln()
        print(f"{spieler1} würfelt: {wurf1}")
        print(f"{spieler2} würfelt: {wurf2}")

        if wurf1 > wurf2:
            print(f"{spieler1} gewinnt die Runde!")
            punkte1 += 1
        elif wurf2 > wurf1:
            print(f"{spieler2} gewinnt die Runde!")
            punkte2 += 1
        else:
            print("Unentschieden!")

    print("Ergebnis ")
    print(f"{spieler1}: {punkte1} Punkte")
    print(f"{spieler2}: {punkte2} Punkte")

    if punkte1 > punkte2:
        print(f"{spieler1} gewinnt das Spiel!")
    elif punkte2 > punkte1:
        print(f"{spieler2} gewinnt das Spiel!")
    else:
        print("Unentschieden!")
spiel()