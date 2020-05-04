# -*- coding: utf-8 -*-


'''
AUFGABE 4 - SCRABBLE 

Erstellt in einem Skript eine Funktion, die ein Wort annimmt und dessen Scrabble-Wert berechnet.
Nutzt dazu die folgenden Werte:

werte = {"a": 1, "b": 3, "c": 4, "d": 1, "e": 1, "f": 4, "g": 2, "h": 2, "i": 1, "j":6, "k": 4, 
        "l": 2, "m": 3, "n": 1, "o": 2, "p": 4, "q": 10, "r": 1, "s": 1, "t":1, "u": 1, "v": 6, 
        "w": 3, "x": 8, "y": 10, "z": 3, "ä": 6, "ö": 8, "ü": 6}

Ein Beispiel sieht dann folgendermaßen aus:

scrabble(’informatikum’)
23

Hinweis 1: Als erste Zeile sollte in eurem Skript Folgendes stehen, damit die Umlaute richtig 
erkannt werden:

# -*- coding: utf-8 -*-
'''

# Ein Dictonary, welches Buchstaben einen Wert zuordnet.
werte = {"a": 1, "b": 3, "c": 4, "d": 1, "e": 1, "f": 4, "g": 2, "h": 2, "i": 1, "j":6, "k": 4, 
        "l": 2, "m": 3, "n": 1, "o": 2, "p": 4, "q": 10, "r": 1, "s": 1, "t":1, "u": 1, "v": 6, 
        "w": 3, "x": 8, "y": 10, "z": 3, "ä": 6, "ö": 8, "ü": 6}

# Eine Funktion, die die Werte der Buchstaben aus dem übergebenen Wort zusammenaddiert.
def scrabble(word):
    summe = 0
    for i in word.lower():
        summe += werte[i]
    print(summe)

# Liest das eingegebene Wort ein und führt auf ihm die Funktion scrabble() aus
scrabble(input('Gib ein Wort: '))