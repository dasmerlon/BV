# -*- coding: utf-8 -*-

"""
@author: Merle Hoffmann (7031673), 
         Abdulssatar Khateb (6976879), 
         Felix Swimmer (7162123)

Ein Problem, das bei der bisherigen Kantendetektion auftrat, ist die Breite der Kanten. Die Breite der
Kanten ist ein Problem, da Kanten im Bild meist idealerweise 1 Pixel breit sind, in den Ergebnissen
der Kantendetektoren jedoch oft durch breitere Bereiche dargestellt werden. Für dieses Problem soll
im Rahmen dieser Aufgabe eine Lösung erarbeitet werden, indem alle Pixel deren Gradientenstärke
bezüglich einer Nachbarschaft nicht maximal ist, unterdrückt werden (auf 0 setzen). Die Nachbarschaft
wird dabei durch die Orientierung der Gradienten bestimmt und verläuft orthogonal zur Kante.



1. Der Ausgangspunkt dieser Aufgabe ist das Ergebnis von Aufgabe 4, d.h. das Bild der Gradientenstärken
auf Basis des neuen Farbraums, der die Blauheit darstellt. Ermittelt zusätzlich zu den
Gradientenstärken die Orientierungen (in Grad) der Gradienten je Pixel. Fasst die Orientierungen
o in vier Bereiche zu neuen Orientierungen oneu zusammen:
oneu

Das heißt, nach dieser Operation sollen alle Pixel den Wert 0; 45;45 oder 90 haben. Erzeugt
zudem ein Ergebnisbild, das Größe und Datentyp des Bildes der Gradientenstärke haben soll,
jedoch mit Nullen gefüllt ist.
"""



"""
2. Nun iteriert durch das Bild und ermittelt zunächst für jedes Pixel jene beiden Nachbarn aus der
3 x 3-Nachbarschaft, die orthogonal zur Kante (s. neu ermittelte Gradientenorientierung) zum
zentralen Pixel benachbart sind. Achtet dabei auch darauf, dass die Nachbarn im Bild existieren
müssen und nicht außerhalb des Bildes liegen dürfen.
"""


"""
3. Ermittelt nun für jedes Pixel, ob die Gradientenstärke des Pixels größer oder gleich ist als jene
seiner beiden in der vorherigen Teilaufgabe ermittelten Nachbarn. Ist dies der Fall, so wird für das
Ergebnisbild die Gradientenstärke in diesem Pixel übernommen. Sollte dies nicht der Fall sein,
wird die Gradientenstärke im Ergebnisbild auf 0 gesetzt. Visualisiert nun das Ergebnis, d.h. das
Ergebnisbild mit den ausgedünnten Gradientenstärken. Hatte die Ausdünnung Erfolg?
"""



"""
4. Binarisiert nun das Ergebnis der ausgedünnten Gradientenstärken. Ist es möglich, einen Grenzwert
zu wählen, sodass ein durchgehender Kantenzug, der die Kante zwischen Gebäude und Himmel
darstellt entsteht? Falls nein, wie könnte man das auf Basis des Bildes der ausgedünnten Gradientenstärken
ändern? Schlagt eine Lösung vor, implementieren müsst ihr sie nicht.
         
"""