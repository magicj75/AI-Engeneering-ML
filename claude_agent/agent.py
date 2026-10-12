import json
import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
MODEL = "claude-haiku-5-5"

# Fake-Maschinendaten (spaeter durch echte Daten ersetzbar)
MACHINES = {
    "press-01": {"status": "running", "temperature_c": 72, "vibration_mm_s": 2.1},
    "press-02": {"status": "running", "temperature_c": 94, "vibration_mm_s": 7.8},
    "cnc-01": {"status": "stopped", "temperature_c": 31, "vibration_mm_s": 0.0},
}


def get_machine_status(machine_id: str) -> str:
    data = MACHINES.get(machine_id)
    if data is None:
        return json.dumps({"error": f"Unbekannte Maschine: {machine_id}"})
    return json.dumps(data)


def list_machines() -> str:
    return json.dumps(list(MACHINES.keys()))


# Beschreibung der Tools fuer Claude
tools = [
    {
        "name": "list_machines",
        "description": "Gibt die IDs aller verfuegbaren Maschinen zurueck.",
        "input_schema": {"type": "object", "properties": {}},
    },
    {
        "name": "get_machine_status",
        "description": "Liefert Status, Temperatur (C) und Vibration (mm/s) einer Maschine.",
        "input_schema": {
            "type": "object",
            "properties": {
                "machine_id": {"type": "string", "description": "z. B. press-01"}
            },
            "required": ["machine_id"],
        },
    },
]

# Zuordnung: Tool-Name -> Python-Funktion
tool_functions = {
    "list_machines": lambda **kwargs: list_machines(),
    "get_machine_status": lambda **kwargs: get_machine_status(**kwargs),
}


def run_agent(question: str) -> str:
    messages = [{"role": "user", "content": question}]

    while True:
        response = client.messages.create(
            model=MODEL,
            max_tokens=1024,
            system="Du bist ein Assistent fuer Fabrikdaten. Nutze die Tools, rate nie. Antworte auf Deutsch.",
            tools=tools,
            messages=messages,
        )

        # Claudes Antwort (inkl. Tool-Wuenschen) in den Verlauf aufnehmen
        messages.append({"role": "assistant", "content": response.content})

        if response.stop_reason != "tool_use":
            return "".join(b.text for b in response.content if b.type == "text")

        # Alle angeforderten Tools ausfuehren und Ergebnisse zurueckgeben
        results = []
        for block in response.content:
            if block.type == "tool_use":
                print(f"[Tool] {block.name}({block.input})")
                output = tool_functions[block.name](**block.input)
                results.append(
                    {
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": output,
                    }
                )
        messages.append({"role": "user", "content": results})


if __name__ == "__main__":
    print(run_agent("Welche Maschinen sind auffaellig? Pruefe alle und begruende kurz."))
