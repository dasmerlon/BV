'''
AUFGABE 5 - 5ER LISTEN

Wir wollen ein bisschen mehr über Listen von Zahlen wissen. Schreibt ein Skript, das fünf 
Zahlen in der Konsole einliest (floats) und folgende Informationen auf der Konsole ausgibt:
    • Liste aller Eingaben
    • Minimum mit Index
    • Maximum mit Index
    • Median
    • Anzahl der unterschiedlichen Elemente
    • Anzahl der ganzen Zahlen (Z)
    • Anzahl der weiteren Zahlen (R ohne Z).

Ein Beispiel:

Eine Zahl bitte: 5
Eine Zahl bitte: 4
Eine Zahl bitte: 2.2
Eine Zahl bitte: 3
Eine Zahl bitte: 5
[5.0, 4.0, 2.2, 3.0, 5.0]
min 2.2 2
max 5.0 0
median 4.0
unterschiedlich 4
ganze Zahlen 4
reelle Zahlen ohne ganze Zahlen 1 
'''

# Zählt die Integer in der übergebenen  Liste
def integer(l):
    counter = 0
    for i in l:
        if i == int(i)
            counter += 1
    return counter


def listOfFive():
    # Liest 5x die Eingabe aus, wandelt diese in Float um und fügt sie in eine Liste
    l = list()
    for i in range(5):
        l += [float(input('Eine Zahl bitte: '))]
    # Schreibt die Liste auf die Konsole:
    print(l)
    # min() und max() finden das Mini- und Maximum aus der Liste. l.index() gibt die Position                                               
    print('min', min(l), l.index(min(l)))                   
    print('max', max(l), l.index(max(l)))
    # Gibt das mittlere Element (an Index 2) aus der sortierten Liste aus
    print('median', sorted(l)[2])
    # Gibt die Länge der Menge aus. Die Menge filtert alle doppelten Elemente
    print('unterschiedlich', len(set(l))) 
    # Zählt die Integer in der übergebenen Liste
    print('ganze Zahlen', integer(l)) 
    # Zieht die Anzahl der Integer von der Anzahl der Elemente in der Liste ab
    print('reelle Zahlen ohne ganze Zahlen', 5-integer(l))


# Führt die Funktion listOfFive() aus
listOfFive()

