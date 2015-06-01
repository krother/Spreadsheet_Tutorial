
# Die Revolution der Letzten Buchstaben

## Ziele

* einen Mittelwert berechnen
* eine Standardabweichung berechnen
* einen Median berechnen

## Aufgaben

Der Babynamenforscherin *Laura Wattenberg* fiel 2007 auf, daß sich die Verteilung der letzten Buchstaben bei Jungennamen in den letzten 100 Jahren erheblich verändert haben (Quelle: [http://www.babynamewizard.com/](http://www.babynamewizard.com/). Wir möchten folgende drei Fragen untersuchen:

1. Können wir diese Beobachtung bestätigen?
2. In welcher Art hat sich die Verteilung der Jungennamen verändert?
3. Hat die gleiche Veränderung auch bei Mädchennamen stattgefunden?

Dazu werden wir **Mittelwert, Standardabweichung** und **Median** der Häufigkeiten der Endbuchstaben untersuchen.

#### Check

Du benötigst die vollständige Untersuchung der Anfangsbuchstaben für Jungen und Mädchen aus der vorangegangenen Übung. Speichere Dir eine Sicherheitskopie ab, dann kannst Du nichts vermasseln. 

### 1. Was sind Mittelwert, Standardabweichung und Median?

Berechne diese drei Werte mit einem einfachen Zahlenbeispiel von Hand. Folgende Berechnungsgrundlage:

| Statistik | Formel |
|-----------|--------|
| Mittlewert | $SUMME(xi)/n$ |
| Standardabweichung | bla |
| Median             |  bla |


### 2. Hypothesen

Formuliere je eine möglichst präzise Hypothese zu den drei Fragen oben. Verwende bei der Formulierung *Mittelwert* und *Standardabweichung*.

### 3. Letzte Buchstaben

Ändere die Tabelle so, daß die letzten statt der ersten Buchstaben ausgewertet werden. Verwende wieder die Funktionsliste (**Einfügen -> Funktion**).

### 4. Daten in einer separaten Tabelle sammeln

Um die Zahlen für Mädchen und Jungen die Jahre 1900 und 2000 besser vergleichen zu können, wäre es schön, alle in einem Tabellendokument zu sammeln. Leider gehen die Referenzen zu den Zellen beim Kopieren in ein anderes Dokument kaputt, so daß die Werte nicht sichtbar sind.

Wir behelfen uns mit einem kleinen Trick:

Wähle die Prozentwerte aus und kopiere sie mit **Strg + c** und **Strg + v** in ein leeres Textdokument (Texteditor oder Word). Von dort kopiere die Werte in eine leere Tabelle. Wiederhole die Prozedur für die verschiedenen Datensätze, so daß Du eine Tabelle mit fünf Spalten erhälst:

* Endbuchstaben A-Z
* prozentuale Häufigkeit für Mädchen, 1900
* prozentuale Häufigkeit für Mädchen, 2000
* prozentuale Häufigkeit für Jungen, 1900
* prozentuale Häufigkeit für Jungen, 2000

Gib den Spalten aussagekräftige Beschriftungen und markiere sie fett.

#### Hinweis

Wenn Du beim Kopieren im Texteditor die Prozentzeichen durch Suchen/Ersetzen löschst, wird es um einiges übersichtlicher.


### 5. Berechnen der statistischen Größen

Berechne Mittelwert, Standardabweichung und Median aus den prozentualen Häufigkeiten der letzten Buchstaben. Unter den einzelnen Spalten sollte dafür genug Platz sein. Verwende folgende Formeln:

    =AVERAGE(A2:A27)
    =STDEV(A2:A27)
    =MEDIAN(A2:A27)

Setze den korrekten Bereich in die Formeln ein. 


### 6. Differenz zwischen 1900 und 2000

Die neue Tabelle erlaubt uns, die Änderung der letzten 100 Jahre direkt zu berechnen. Erstelle zwei neue Spalten, mit dem Inhalt

    =ABS(C2-B2)

und

    =ABS(E2-D2)

und kopiere sie nach unten. Auch für diese Spalte kannst Du Mittelwert und Standardabweichung berechnen.

#### Fragen

* Für welche Buchstaben ist die Änderung am stärksten?
* Ist die Änderung für Jungen oder Mädchen stärker?
* Was sagen Dir die Zahlen über die Verteilung der Endbuchstaben?
* Was kannst Du sonst noch beobachten?


### 7. Kontrollgruppe

Was für eine Vergleichsgruppe könntest Du verwenden, um auszuschließen, daß der beobachtete Effekt nicht einfach aus der höheren Diversität der Namen oder aus Zufall resultiert?

### 8. Schlußfolgerungen

Was kannst Du über die ursprünglichen Hypothesen sagen?
