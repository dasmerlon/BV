# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

"""
@author: Merle Hoffmann (7031673), 
         Abdulssatar Khateb (6976879), 
         Felix Swimmer (7162123)
         
         
Die Anwendung von des Histogrammausgleichs global auf das ganze Bild mit einer Transformationsfunktion
ist manchmal nicht optimal, da unterschiedliche Bildbereiche verschiedene Transformationsfunktionen
zur Optimierung des Kontrasts benötigen. Aus diesen Anforderungen lassen sich Formen der lokaler oder
adaptiver Histogrammausgleiche entwickeln, bei denen verschiedene Bildbereiche mit unterschiedlichen
Transformationsfunktionen behandelt werden.
Hinweis: Bei allen Teilen dieser Aufgabe sollen zur Visualisierung der Bilder mit matplotlib.pyplot.
imshow() die Parameter vmin=0 und vmax=255 gesetzt werden (siehe auch Aufgabenblatt 4, Aufgabe
1).
"""


"""
1. Ladet zunächst das Bild moon.png aus dem Moodle in Python und visualisiert es. Wendet eure
Funktion zum Histogrammausgleich aus Aufgabe 4 auf das Bild an und visualisiert das Ergebnis.
"""





"""
2. Führt nun eure Funktion zum Histogrammausgleich aus Aufgabe 4 auf einzelnen Teilbereichen
des Bildes unabhängig voneinander durch. Zerlegt das Bild dazu virtuell in 4  4 Kacheln zu je
64  64 Pixeln, indem ihr nur die entsprechenden Teilbereiche des Bildes an eure Funktion zum
Histogrammausgleich übergebt. Verfahrt mit den Ergebnis entsprechend, sodass jede Anwendung
eurer Funktion zum Histogrammausgleich nur einen Teilbereich des Ergebnisses ermittelt. Achtet
darauf, dass sich die Kacheln nicht überlappen. Wie verändert sich das visuelle Ergebnis? Ignoriert
dabei die teilweise entstandenen künstlichen Kanten innerhalb des Bildes.
"""





"""
3. Verkleinert nun die Kachelgröße auf 32  32, 16  16, 8  8, 4  4 und 2  2. Die Anzahl der
Kacheln verdoppelt sich pro Dimension entsprechend bei jedem Schritt. Wie verändert sich das
visuelle Ergebnis mit jedem Schritt? Versucht eine Erklärung zu finden.
"""