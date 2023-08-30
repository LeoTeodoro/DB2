import json
import os
from bson import json_util  # pip install bson


def writeAJson(data, name: str):
    parsed_json = json.loads(json_util.dumps(data))

    if not os.path.isdir("./Relatório 2/json"):
        os.makedirs("./Relatório 2/json")

    with open(f"./Relatório 2/json/{name}.json", "w") as json_file:
        json.dump(parsed_json, json_file, indent=4, separators=(",", ": "))
