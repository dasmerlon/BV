'''
AUFGABE 3 - LISTEN DREHEN
Hinweis: Für die Lösung dieser Aufgabe ist die Verwendung von Schleifen nicht erlaubt!

Schreibt ein Skript, das zwei Teillisten einer Liste dreht. Dazu soll zunächst eine Liste mit 
den Zahlen von 1 bis 9 erstellt werden und nach dem Index eines Elements gefragt werden. 
Das Element an diesem Index soll nun zur Teilung der Liste in zwei neue Teillisten dienen. 
Die eine Teilliste enthält alle Elemente links des gewählten Elements und die andere Teilliste 
enthält alle Elemente rechts des gewählten Elements. Anschließend sollen beide Teillisten 
gedreht und mit dem gewählten Element zusammen wiederausgegeben werden. 
Ein Beispiel:
[1, 2, 3, 4, 5, 6, 7, 8, 9]
Gib einen Index: 2
[2, 1, 3, 9, 8, 7, 6, 5, 4] #Teillisten 1,2 und 4,5,6,7,8,9

Das Einlesen von Text (str) aus der Konsole (hier: IPython-Konsole) erfolgt in Python über 
die Funktion input(), wobei der eingelesene Text von der Funktion zurückgegeben wird. 
Das reine Schreiben erfolgt mit print().

>>> s = input(’Wie ist dein Name? ’)
Wie ist dein Name? Max
>>> print(s)
’Max’
'''

# Erstellt eine Liste von 1 bis 10 und gibt diese auf die Konsole aus
l = list(range(1,10)) 
print(l)

# Liest den eingegebenen Index ein und wandelt ihn zum Integer um
index = int(input('Gib einen Index: '))

# Bildet die vordere und hintere Teilliste l1 und l2
l1 = l[:index]
l2 = l[index+1:]
# Dreht die Teillisten um und fügt diese zusammen mit einer Liste, 
# die das gewählte Element enthält zusammen
result = l1[::-1] + [l[index]] + l2[::-1]

# Schreibt das Ergebnis auf die Konsole
print(result)




