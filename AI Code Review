AI Code:

Prompt:

Erstelle einen Python code für einen Krypto Portfolio Tracker. Der Tracker soll mithilfe einer API live Daten fetchen und diese sowohl als Text als auch graphisch darstellen.

In der Basis Funktion soll der Krypto Tracker alle 2 Sekunden den Portfoliobestand (Wert und Menge der einzelnen Währung) als Text in der Konsole ausgeben

Graphisch:
Einerseits sollen die Krypto Bestände in einem Tortendiagramm angezeigt werden (nach Währung), andererseits soll der Portfoliowert mit einem Liniendiagramm dargestellt werden, dass sich alle 2 Sekunden updated.

Portfoliobestand:
BTC: 0.01280118
ETH: 0.4

Ergebnis und Review:
Das Ergebnis ist erstaunlich ähnlich. Auch in der Entwicklung haben wir ChatGPT verwendet, allerdings deutlich schlechtere Ergebnisse bekommen. Wahrscheinlich ist es im Nachheinein (reverse - engineering) einfacher einen akkuraten Prompt zu schreiben
Z.b. hatten wir in der Entwicklung das Problem, dass mit jedem refresh der Grafik ein neues Fenster geöffnet wurde. Das war jetzt nicht der Fall.

Mögliche Leitfragen für die Analyse des AI-Codes
• Funktionalität: Funktioniert der generierte Code? Stimmt die Ausgabe mit der erwarteten Ausgabe überein?

Ja der Code macht, was er tun soll. Allerdings gibt es einen etwas längeren delay, bevor das erste mal der Portfoliiowert als Text in der Konsole ausgegeben wird und bevor die Grafik erscheint.
Außerdem zeigt es folgende Error Message an, die allerdings das Ergebnis nicht beeinträchtigt.

UserWarning: frames=None which we can infer the length of, did not pass an explicit *save_count* and passed cache_frame_data=True.  To avoid a possibly unbounded cache, frame data caching has been disabled. To suppress this warning either pass `cache_frame_data=False` or `save_count=MAX_FRAMES`.
  ani = FuncAnimation(fig, update, interval=2000)

• Datentypen und Variablennamen: Verwendet der generierte Code die richtigen Datentypen und sind die Variablennamen sinnvoll gewählt?

Soweit erkennbar, ja.

• Übersichtlichkeit und Struktur: Ist der generierte Code übersichtlich und gut strukturiert? Ist er leicht zu lesen und zu verstehen?

Der Code ist übersichtlich

• Effizienz: Ist der generierte Code effizient? Gibt es redundante oder ineffiziente Operationen? Kann der Code optimiert werden?

Der Code verwendet sogar ca 30 Zeilen weniger als unser Code, und bringt aber fast genau dasselbe Ergebnis.

• Vergleich mit menschlich geschriebenem Code: Wie unterscheidet sich der generierte Code von eurem Code, der die gleiche Aufgabe erfüllt?



• Methoden der Code-Generierung: Welchen Input hast du zur Code-Generierung benutzt? Bekommst du ein anderes Ergebnis, wenn du die Anfrage anders formulierst?

Prompt: siehe oben. Und ja bei einem anderen Prompt bekommen wir ein anderes Ergebnis.

• Dokumentation: Ist der generierte Code gut dokumentiert? Gibt es Kommentare, die den Code erklären und seine Funktionsweise beschreiben?

Ja, es gibt einige Kommentare die den Code übersichtlich erklären.
