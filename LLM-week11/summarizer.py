import os
import argparse
import tiktoken
from pydantic import BaseModel
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def lade_dokument(pfad):
    try:
        with open(pfad, "r", encoding="utf-8") as datei:
            text = datei.read()

        if not text.strip():
            print("Fehler: Die Datei ist leer.")
            return None

        return text

    except FileNotFoundError:
        print(f"Fehler: Die Datei '{pfad}' wurde nicht gefunden.")
        return None

    except OSError as e:
        print(f"Fehler beim Lesen der Datei: {e}")
        return None

class Summary(BaseModel):
    zusammenfassung: str
    wichtigste_punkte: list[str]

def summarize(text, style, ausgabe_format):
    try:
        response = client.responses.parse(
            model="gpt-5.6-luna",
            instructions=f"""
            Du bist ein professioneller Dokumentenanalyst.

            Fasse das Dokument präzise zusammen.
            Erfinde keine Informationen.

            Konzentriere dich auf die wichtigsten Informationen.
            Lass unwichtige Details und Wiederholungen weg.

            Die Zusammenfassung soll kurz sein.
            Die wichtigsten Punkte sollen konkrete Fakten aus dem Dokument enthalten.

            Schreibstil: {style}
            Ausgabeformat: {ausgabe_format}
            """,
            input=f"""
            Fasse das folgende Dokument zusammen:

            {text}
            """,
            text_format=Summary
        )

        return response.output_parsed

    except Exception as e:
        print(f"Fehler bei der Zusammenfassung: {e}")
        return None


parser = argparse.ArgumentParser(
    description="Fasst ein Textdokument mit einem LLM zusammen."
)

parser.add_argument(
    "datei",
    help="Pfad zur Textdatei"
)

parser.add_argument(
    "--style",
    choices=["professionell", "einfach", "technisch"],
    default="professionell",
    help="Stil der Zusammenfassung"
)

parser.add_argument(
    "--format",
    dest="ausgabe_format",
    choices=["stichpunkte", "absatz"],
    default="stichpunkte",
    help="Ausgabeformat der Zusammenfassung"
)


args = parser.parse_args()


text = lade_dokument(args.datei)

if text is None:
    raise SystemExit(1)

encoding = tiktoken.get_encoding("o200k_base")
tokens = encoding.encode(text)

print(f"Tokenanzahl: {len(tokens)}")


zusammenfassung = summarize(
    text,
    args.style,
    args.ausgabe_format
)

if zusammenfassung is None:
    print("Keine Zusammenfassung konnte erstellt werden.")
else:
    print("\nZusammenfassung:")
    print(zusammenfassung.zusammenfassung)

    print("\nWichtigste Punkte:")
    for punkt in zusammenfassung.wichtigste_punkte:
        print("-", punkt)