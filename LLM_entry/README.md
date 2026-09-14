# LLM Entry

Ein einfacher CLI-Chatbot mit der OpenAI API und GPT-5.6 Luna.

## Was macht das Projekt?

Der Chatbot läuft direkt im Terminal und kann mehrere Nachrichten innerhalb einer Unterhaltung verarbeiten.

Die Chat-Historie wird von Python gespeichert und bei jeder Anfrage erneut an das Modell geschickt.

Zusätzlich zeigt der Chatbot nach jeder Antwort den verwendeten Tokenverbrauch an.

## Voraussetzungen

* Python 3
* OpenAI API-Key

## Installation

Repository klonen und in den Projektordner wechseln:

```bash
cd LLM_entry
```

Benötigte Pakete installieren:

```bash
pip install -r requirements.txt
```

## API-Key einrichten

Erstelle eine `.env`-Datei:

```text
OPENAI_API_KEY=dein_api_key
```

Der API-Key darf nicht veröffentlicht oder auf GitHub hochgeladen werden.

Die `.env`-Datei sollte deshalb in `.gitignore` stehen:

```text
.env
```

## Starten

```bash
python main.py
```

Beispiel:

```text
Du: Hallo
Bot: Hallo! Wie kann ich dir helfen?

Du: Ich heiße Kian.
Bot: Freut mich, Kian!

Du: Wie heiße ich?
Bot: Du heißt Kian.

Input-Tokens: 78
Output-Tokens: 12
Total-Tokens: 90
```

Mit `exit` kann der Chat beendet werden.

## Was ich dabei gelernt habe

* LLMs generieren Text autoregressiv, also Token für Token.
* LLMs arbeiten mit Tokens statt einfach mit Wörtern.
* Ein LLM besitzt nicht automatisch ein dauerhaftes Gedächtnis.
* Chat-Historie kann von der Anwendung gespeichert und erneut an das Modell geschickt werden.
* System Instructions beeinflussen das Verhalten des Modells.
* API-Antworten enthalten neben dem Text auch weitere Informationen, zum Beispiel den Tokenverbrauch.
* Mehr Chat-Historie kann zu mehr Input-Tokens und damit höheren Kosten führen.
* API-Keys sollten über Umgebungsvariablen bzw. `.env` geschützt werden.

## Bekannte Limitationen

Dieser Chatbot ist ein Lernprojekt und keine produktionsreife Anwendung.

* Die Chat-Historie wird nur im Arbeitsspeicher gespeichert und geht beim Beenden des Programms verloren.
* Die komplette Historie wird bei jeder Anfrage erneut übertragen.
* Dadurch kann der Tokenverbrauch mit längeren Gesprächen steigen.
* Das Modell kann falsche oder erfundene Informationen liefern (Halluzinationen).
* Ein LLM ist nicht automatisch über aktuelle Informationen informiert.
* Die Größe des verfügbaren Kontextfensters ist begrenzt.
* Es gibt keine Benutzerverwaltung oder dauerhafte Speicherung von Gesprächen.

## Zweck

Das Projekt wurde gebaut, um die Grundlagen der Arbeit mit LLM-APIs praktisch zu lernen und einen ersten einfachen AI-Chatbot zu entwickeln.
