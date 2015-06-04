
# Die häufigsten Anfangsbuchstaben

## Ziele

* Eine Untersuchung nach Kategorien durchführen
* kompliziertere Funktionen verwenden
* Ein Verhältnis zweier Häufigkeiten berechnen

## Aufgaben

Wir möchten untersuchen, welche Anfangsbuchstaben bei Vornamen beliebt sind, und ob sich an den Vorlieben in den letzten 100 Jahren etwas geändert hat.

#### Check

Du solltest eine dreispaltige Tabelle mit Vornamen geöffnet haben. Diese sollte wie in den vorigen Übungen nach Mädchen und Jungen gegliedert sein. Wenn Du schon weitere Spalten mit Statistiken gefüllt hast, macht das nichts. Für die Übersicht ist es aber besser, die Daten in ein leeres Blatt oder Dokument zu kopieren.

### 1. Neue Spalten hinzufügen

Füge vier leere Spalten hinzu (D-F). Das kannst Du über **Einfügen -> Spalte** oder *Rechtsklicken auf C oben und 'Spalte Einfügen' wählen*.

### 2. Spaltenbeschriftungen

Damit es nicht zu unübersichtlich wird, geben wir den Spalten Namen. Füge ganz oben eine leere Zeile hinzu. Gibt den ersten sechs Spalten die Namen:

    Vorname
    Geschlecht
    Anzahl
    Anfangsbuchstabe
    Geraten
    Häufigkeit

Formatiere diese Spaltenbeschriftungen mit **Strg + b** fett.

### 3. Anfangsbuchstaben ermittlen

Setze in der Spalte D eine Funktion ein, die den Anfangsbuchstaben des Vornamens ermittelt. Suche dazu im Verzeichnis der Funktionen (über das Symbol **f(x)** oder im Menü **Einfügen -> Funktion** in der Gruppe **Text**).

Sobald Du die passende Funktion für den Anfangsbuchstaben gefunden hast, wende diese auf die ganze Spalte an. Fahre in der Tabelle umher und prüfe, ob die richtigen Anfangsbuchstaben in der Tabelle stehen.

#### Frage

Wie lautet die Funktion?

#### Tip

Du kannst die Spalte mit den Anfangsbuchstaben zentriert formatieren. Dann sind sie leichter zu lesen.


### 4. Buchstaben auswählen

Wähle fünf Buchstaben aus, von denen Du glaubst, daß sie besonders häufig oder besonders selten auftreten. Schreibe diese in festWir möchten alle Buchstaben des Alphabets erfassen. Trage diese in der Spalte *geraten* ein, z.B.:

    A
    B
    C
    ...


### 5. Kategorien auszählen

Nun zählen wir, wie oft jeder Anfangsbuchstabe in den Vornamen vorkommt. Dazu verwenden wir die Funktion *COUNTIF*, die unseren Datensatz mit den Kategorien verlgeicht. Trage in die Spalte *Häufigkeit* ein:

#### OpenOffice, Englisch:

    =COUNTIF(D$2:D$333, E2)

#### MS Excel, Deutsch:

    =ZÄHLENWENN(D$2:D$333; E2)

Ersetze die *333* durch die letzte Zeilennummer mit Vornamen. Kopiere dann diese Zeile für alle 26 Buchstaben.

#### Fragen

* Welcher Anfangsbuchstabe kommt am häufigsten vor?
* Welcher Anfangsbuchstabe kommt am seltensten vor?
* Was machen nochmal die beiden Dollarzeichen?

### 6. Prozentuale Anteile der Anfangsbuchstaben

Bilde die Summe über die gesamte Spalte *Häufigkeit*. Berechne in der siebten Spalte den prozentualen Anteil für jeden Anfangsbuchstaben (Wiederholung). 

#### Fragen

* Was sagt uns die Summe der Spalte *Häufigkeit*?

### 7. Anfangsbuchstaben für Jungen

Wiederhole Schritte 1-6 für die Vornamen von Jungen. Welcher Anfangsbuchstabe kommt am häufigsten, welcher am seltensten vor?

### 8. Geschlechterverhältnis berechnen

Wir möchten auf einen Blick sehen, ob bestimmte Anfangsbuchstaben häufiger oder seltener auftreten. Dazu teilen wir die prozentuale Häufigkeit für Mädchen durch die für Jungen. Trage in einer leeren Spalte z.B. für den Buchstaben **A** ein:

    =G2/N2

Achte darauf, daß Du die richtigen Spalten (mit Prozentwerten auswählst). Die Zahlen in der Verhältnis-Spalte bedeuten folgendes:

| Wert | Bedeutung |
|------|-----------|
| > 1.0 | beliebter für Mädchen- als für Jungennamen |
| 1.0   | bei beiden Geschlechtern gleich beliebt    |
| < 1.0 | beliebter bei Jungennamen |

#### Fragen

* Gibt es besonders *"weibliche"* oder *"männliche"* Anfangsbuchstaben?
* Warum haben wir uns den Aufwand gemacht, in Schritt 6 eine Spalte mit Prozentwerten zu berechnen? Hätte es nicht gereicht, einfach die beiden Häufigkeiten durcheinander zu teilen?

### 9. Diagramm

Erstelle ein Balkendiagramm der Buchstabenhäufigkeiten.

