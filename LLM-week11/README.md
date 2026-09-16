# LLM Document Summarizer

Ein kleines Python-Projekt, das Textdokumente mithilfe eines LLM zusammenfasst.

Das Projekt ist im Rahmen meines Lernwegs im Bereich **AI Engineering und LLMs** entstanden. Dabei habe ich unter anderem Prompt Engineering, Structured Outputs, Pydantic und CLI-Argumente mit `argparse` praktisch umgesetzt.

## Features

* Textdateien einlesen
* Tokenanzahl des Dokuments bestimmen
* Zusammenfassungen mit einem LLM erstellen
* verschiedene Schreibstile auswählen
* verschiedene Ausgabeformate auswählen
* strukturierter Output mit Pydantic
* Fehlerbehandlung für fehlende und leere Dateien
* CLI über `argparse`

## Installation

Repository klonen:

```bash
git clone https://github.com/magicj75/AI-Engeneering-ML.git
cd LLM-week11
```

Virtuelle Umgebung erstellen:

```bash
python -m venv .venv
```

Virtuelle Umgebung aktivieren.

Unter Windows:

```bash
.venv\Scripts\activate
```

Abhängigkeiten installieren:

```bash
pip install -r requirements.txt
```

## API-Key

Erstelle eine Datei namens `.env`:

```text
OPENAI_API_KEY=dein_api_key
```

Der API-Key wird nicht direkt im Python-Code gespeichert.

Die `.env`-Datei wird durch `.gitignore` von Git ausgeschlossen.

## Verwendung

Grundlegender Aufruf:

```bash
python summarizer.py dokument.txt
```

### Schreibstil

Es stehen drei Schreibstile zur Verfügung:

```bash
python summarizer.py dokument.txt --style professionell
```

```bash
python summarizer.py dokument.txt --style einfach
```

```bash
python summarizer.py dokument.txt --style technisch
```

### Ausgabeformat

Stichpunkte:

```bash
python summarizer.py dokument.txt --format stichpunkte
```

Absatz:

```bash
python summarizer.py dokument.txt --format absatz
```

Beides kann kombiniert werden:

```bash
python summarizer.py dokument.txt --style einfach --format stichpunkte
```

## Beispiel

Eingabe:

```text
Die Firma Müller GmbH hat im vergangenen Jahr ihren Umsatz um 12 Prozent gesteigert.
Besonders stark entwickelte sich der Online-Vertrieb.
Gleichzeitig stiegen die Personalkosten um 8 Prozent.
```

Mögliche Ausgabe:

```text
Zusammenfassung:
Die Müller GmbH konnte ihren Umsatz steigern, während gleichzeitig die Personalkosten zunahmen.

Wichtigste Punkte:
- Umsatz stieg um 12 Prozent
- Online-Vertrieb entwickelte sich besonders stark
- Personalkosten stiegen um 8 Prozent
```

## Technischer Aufbau

Das Projekt verwendet:

* **Python** für die Anwendung
* **OpenAI API** für die Textzusammenfassung
* **Pydantic** für strukturierte Daten
* **tiktoken** zur Tokenzählung
* **argparse** für die Kommandozeile
* **python-dotenv** zum Laden des API-Keys

Der grundsätzliche Ablauf:

```text
Textdatei
   ↓
Dokument laden
   ↓
Token zählen
   ↓
Prompt erstellen
   ↓
LLM
   ↓
Structured Output
   ↓
Pydantic
   ↓
Zusammenfassung + wichtigste Punkte
```

## Prompt Engineering

Der Summarizer verwendet unter anderem:

* Role-based Prompting
* dynamische Prompt-Parameter
* Structured Outputs
* gezielte Prompt-Iteration

Beispielsweise können Schreibstil und Ausgabeformat über die CLI verändert werden.

## Limitationen

Dieses Projekt ist ein Lernprojekt und kein produktionsreifes Dokumentenanalyse-System.

Mögliche Einschränkungen:

* Die Qualität der Zusammenfassung hängt vom verwendeten LLM und Prompt ab.
* Das Modell kann trotz Anweisung Informationen falsch interpretieren.
* Sehr große Dokumente können die verfügbaren Kontextgrenzen erreichen.
* Die Tokenzählung dient hier hauptsächlich zur Abschätzung und bedeutet nicht automatisch, dass ein Dokument in jedem Fall verarbeitet werden kann.
* Die Anwendung verarbeitet aktuell einfache Textdateien und keine komplexen PDF- oder Word-Dokumente.
* Es gibt aktuell keine Benutzeroberfläche.
* Die API verursacht bei jeder Zusammenfassung Kosten.

## Lernziel

Mit diesem Projekt wollte ich verstehen, wie man einen LLM-basierten Workflow nicht nur über einen einzelnen Prompt, sondern als kleines Python-Programm strukturiert.

Dabei standen besonders **Prompt Engineering, strukturierte Ausgaben, Fehlerbehandlung und CLI-Anwendungen** im Vordergrund.
