def Permuta(parziale, rimanenti, visto):
    
    if len(rimanenti) == 0:
        if parziale not in visto:
            visto.add(parziale)
            print(parziale)
        return
    
    for i in range(len(rimanenti)):
        nuova_parziale = parziale + rimanenti[i]
        nuove_rimanenti = rimanenti[:i] + rimanenti[i+1:]
        
        Permuta(nuova_parziale, nuove_rimanenti, visto)


def main():
    s = input("Inserisci stringa: ")
    visto = set()
    Permuta("", s, visto)


if __name__ == "__main__":
    main()