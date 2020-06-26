# -*- coding: utf-8 -*-

"""
@author: Merle Hoffmann (7031673), 
         Abdulssatar Khateb (6976879), 
         Felix Swimmer (7162123)
         
Im Rahmen dieser Aufgabe soll die Erkennung von Kanten und der Effekt von Störungen darauf am
Testbild mandrill.png genauer betrachtet werden.
"""

"""
1. Ladet euch das Testbild mandrill.png aus dem Moodle in Python. Wendet den Sobel-Filter auf
das Bild an und lasst euch die Gradientenstärke pro Pixel als Ergebnisbild berechnen. Visualisiert
dieses Bild. Wählt nun einen Grenzwert für die minimale Gradientenstärke und zeigt nur noch alle
Pixel, die oberhalb dieses Grenzwerts liegen als Kante an (auf 1 setzen). Der Rest soll unterdrückt
werden (auf 0 setzen). Beschreibt kurz das Ergebnis der Kantendetektion. Wurden die wichtigsten
Kanten des Gesichts gefunden? Wurden zusätzlich weitere Kanten gefunden? Welcher Grenzwert
führt zu einem sinnvollen Ergebnis?
Hinweis: Obwohl es sich beim Ergebnisbild (dem Bild der Gradientenstärken) um ein Graustufenbild
handelt, macht es Sinn, für die Visualisierung auf das Vorgeben der cmap=’gray’ zu
verzichten. Dies führt zu einer Einfärbung des Ergebnisses, wobei hohe Werte gelbliche Farbtöne
und niedrige Werte blaue Farbtöne bekommen.
"""



"""
2. Wendet nun vor der Anwendung des Sobel-Filters und der Berechnung der Gradientenstärken
einen Gauß-Filter auf das Bild an. Experimentiert dabei mit verschiedenen s. Ziel soll es dabei
sein, dass möglichst nur noch die wichtigsten Kanten des Gesichts (Abgrenzungen der farbigen
Nasenpartien, die Augen, Übergang von Nase zu Mund/Bart,...) erkannt werden. Wie verändert
sich dabei das Ergebnis in Bezug auf die noch erkannten Kanten? Visualisiert das eurer Meinung
nach beste Ergebnis erneut und benutzt dabei ebenso wieder einen Grenzwert, um nur recht starke
Kanten zu visualisieren. Wie und warum verändert sich euer Grenzwert dabei mit steigendem ?
Hinweis: Setzt bei der Anwendung des Gauß-Filters den Parameter preserve_range=True, damit
auch das Ergebnis im Bereich 0; : : : 255 bleibt.
"""



"""
3. Extrahiert nun die Bildzeile bei x 􀀀 150 aus dem Originalbild sowie aus der mit einem Gauß-Filter
weichgezeichneten Variante aus der vorherigen Teilaufgabe. Fügt außerdem noch eine weitere
Variante mit einem sehr hohen  hinzu und extrahiert ebenfalls die genannte Bildzeile. Ermittelt
nun eine Approximation der ersten Ableitung, indem ihr jeweils auf die gesamten Bilder den
Sobel-Operator zur Detektion vertikaler Kanten anwendet. Extrahiert erneut die entsprechende
Bildzeile bei x 􀀀 150 aus den Ergebnissen. Erstellt nun drei Plots mit der Funktion matplotlib.
pyplot.plot (s. Aufgabenblatt 6) mit jeweils der extrahierten Bildzeile und der dazu passenden
extrahierten Zeile des Ergebnisses des Sobel-Operators. Beschreibt kurz, wie sich die Kurven durch
die unterschiedlichen Glättungen verändern.
Tipp: Einen neuen Plot könnte ihr über die Funktion matplotlib.pyplot.figure(i) erzeugen,
wobei i die laufende Nummer des Plots ist und bei 1 beginnt.
"""


"""
4. Berechnet nun die Orientierung (in Grad) des Gradienten in jedem Pixel mit Hilfe der Sobel-
Operatoren auf dem Originalbild sowie auf eurem besten weichgezeichneten Ergebnis (Teilaufgabe
2). Erstellt anschließend jeweils ein Histogramm über die Gradientenorientierungen und
visualisiert diese. Nutzt für das Histogramm 9 Behälter und setzt die Grenzen (range-Parameter)
entsprechend. Welche Unterschiede gibt es zwischen den beiden Histogrammen? Wie ändert sich
das Histogramm, wenn ihr den Parameter weights (den Parameter gibt es sowohl bei numpy.
histogram() als auch bei matplotlib.pyplot.hist()) auf die entsprechenden Bilder mit den
Gradientenstärken setzt?
"""