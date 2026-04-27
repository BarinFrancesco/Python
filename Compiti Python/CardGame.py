import random as rnd

def main():
    arr = GetCards()
    
    print("Carte:")
    for carta in arr:
        print(carta)
    
    risultati = ContaValori(arr)
    
    print("\nCombinazioni trovate:")
    for valore in risultati:
        if risultati[valore] == 2:
            print("Coppia di", valore)
        elif risultati[valore] == 3:
            print("Tris di", valore)
        elif risultati[valore] == 4:
            print("Poker di", valore)


def GetCards():
    semi = ["Cuori", "Quadri", "Fiori", "Picche"]
    mazzo = []
    
    # crea tutto il mazzo
    for seme in semi:
        for valore in range(1, 14):
            mazzo.append((seme, valore))
    
    #mischia le carte
    rnd.shuffle(mazzo)
    
    # prendo le prime 13 carte
    arr = []
    for i in range(13):
        arr.append(mazzo[i])
    
    return arr


def ContaValori(arr):
    conteggio = {}
    
    for carta in arr:
        valore = carta[1]
        
        if valore in conteggio:
            conteggio[valore] += 1 #se la carta ha lo stesso valore aumqnta il count, così conosco coppie trie e poker
        else:
            conteggio[valore] = 1
    
    return conteggio


if __name__ == "__main__":
    main()