# Errechnet die Insgesamten Möglichkeiten eine Treppe mit n Stufen hochzugehen, mit den Möglichkeiten 2 oder 1 Stufe auf einmal zu gehen
# n sind hier die Anzahl der Stufen

def NumOfPoss(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    
    return NumOfPoss(n-2) + NumOfPoss(n-1)
    
# n ist die Eingabe des Benutzers

n = int(input("Eingabe von n: "))
print(NumOfPoss(n))
