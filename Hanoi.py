# Funktion zu Errechnung von der Anleitung des Spiels 'Türme von Hanoi' mit n scheiben
# param n Anzahl der Scheiben
# param l, m, r Chars für Links, Rechts, Mitte

def transport(n, l, m, r):
    if n == 1:
        print("Bewege Scheibe 1 von Säule",l,"zu Säule",m)
        return
    
    transport(n-1, l, r, m)

    print("Bewege Scheibe",n,"von Säule",l,"zu Säule",m)

    transport(n-1, r, m, l)

n = int(input("Anzahl der Scheiben: "))
transport(n, 'L', 'M', 'R')
