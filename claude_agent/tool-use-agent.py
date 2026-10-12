import json
import os 
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client=Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
MODEL="claude-haiku-5-5"

MACHINES = {
    "press-01": {"status": "running", "temperature_c": 72},
    "cnc-01": {"status": "stopped", "temperature_c": 31},
}

def get_temperature(machine_id: str) -> str:
    data=MACHINES.get(machine_id)
    if data is None:
        return json.dumps({"error": f"Unbekannte Maschine: {machine_id}"})
    return json.dumps({"temperature_c": data["temperature_c"]})

def list_machines() -> str:
    return json.dumps(list(MACHINES.keys()))


tools = [
    {
    "name": "get_temperature",
    "description": "Gibt die Temperatur einer Maschine zurück.",
    "input_schema": {
        "type": "object", 
        "properties": {
            "machine_id": {"type": "string", "description": "z.B. press-01"}
            },

        "required": ["machine_id"],
    }
},
    {
        "name": "list_machines",
        "description": "Gibt eine Liste aller Maschinen zurück.",
        "input_schema": {
            "type": "object", "properties": {}
        }

}
]

tool_functions = {
    "get_temperature": get_temperature,
    "list_machines": list_machines
}

def run_tool(name, tool_input):
    return tool_functions[name](**tool_input)

def run_agent(question: str) -> str:
    messages = [{"role": "user", "content": question}]

    while True:
        response = client.messages.create(
            model=MODEL,
            max_tokens=1024,
            tools=tools,
            messages=messages,
        )
        messages.append({"role": "assistant", "content": response.content})

        if response.stop_reason != "tool_use":
            break

        tool_result = []
        for block in response.content:
            if block.type == "tool_use":
                output = run_tool(block.name, block.input)
                tool_result.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": output,
                })
        messages.append({"role": "user", "content": tool_result})

    for block in response.content:
        if block.type == "text":
            print(block.text)


run_agent("Welche Maschinen gibt es und wie warm ist jede?")


