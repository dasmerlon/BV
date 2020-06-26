# -*- coding: utf-8 -*-

"""
@author: Merle Hoffmann (7031673), 
         Abdulssatar Khateb (6976879), 
         Felix Swimmer (7162123)
         
Die Detektion von Kanten beschränkte sich bisher auf Grauwertbilder. Nun sollen auch Farbinformationen
zur Ermittlung bestimmter Kanten, hier der Kante zwischen einem Gebäude und dem blauen
Himmel, genutzt werden. Aus diesen Kanten kann in weiteren Schritte etwa eine stilisierte Skyline erzeugt
werden.
"""



"""
1. Ladet euch zunächst das Bild opera.png, das einen Teil des Sydney Opera House vor einem
blauen Himmel zeigt, aus dem Moodle in Python und wandelt es mit der Funktion skimage.
color.rgb2gray() in ein Grauwertbild um. Ermittelt nun die Gradientenstärke je Pixel über die
Sobel-Operatoren und visualisiert das Ergebnis. Welche Kanten werden gefunden und welche sind
besonders stark?
"""



"""
2. Da wir nur an der Kante zwischen dem Gebäude und dem blauen Himmel interessiert sind,
wollen wir nun die Farbinformationen des Bildes nutzen, um die Detektion von Kanten auf jene
Kanten zu fokussieren. Dazu soll das RGB-Bild zunächst in einen anderen Farbraum umgewandelt
werden, der Blau von anderen Farben und Graustufen trennt. Überlegt euch dazu einen Farb-
„Raum“, eigentlich ist es nur eine Achse, in dem der Farbwert in etwa die Blauheit eines Farbtons
wiedergibt. Konstruiert dazu eine Achse im RGB-Farbraum, die dies erfüllt und implementiert die
Umwandlung des Bildes. Das Ergebnis ist wiederum ein Graustufenbild, da alle Farbwerte auf eine
Achse abgebildet werden sollen, ähnlich der Achse der Graustufen im RGB-Farbraum. Allerdings
müssen die Werte nicht notwendigerweise im Bereich 0; : : : ; 255 liegen. Streckt den Kontrast des
Bildes im neuen Farbraum abschließend so, dass das Minimum im Bild 0 ist und das Maximum
255.
Tipp 1: Überlegt euch für den neuen Farbraum eine Achse, an deren einem Ende im RGBFabrraum
Blau ist und an deren anderem Ende die Farbe im RGB-Farbraum ist, die am weitesten
von Blau entfernt liegt.
Tipp 2: Der neue Farbraum sollte im Bereich von 255 : : : 255 liegen und alle Graustufen sollen
den Wert 0 bekommen.
"""



"""
3. Erzeugt euch nun erneut die Gradientenstärke je Pixel über die Sobel-Operatoren und visualisiert
das Ergebnis. Wie unterscheidet es sich vom vorherigen Ergebnis auf Basis der Graustufen?

"""