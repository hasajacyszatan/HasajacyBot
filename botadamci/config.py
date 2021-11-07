from os import getenv, getcwd
import json

TOKEN = "TOKEN"

with open(f"{getcwd()}/data/federation.json", "r") as f:
    FEDERATION = json.loads(f.read())

with open(f"{getcwd()}/data/haregly.json", "r") as f:
    HAREGLY = json.loads(f.read())
