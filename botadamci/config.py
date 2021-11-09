from os import getenv, getcwd
import json

TOKEN = "2141651634:AAEHbB0GNqPXSezz4G5aMLcUZIIglG3zIO4"

with open(f"{getcwd()}/data/federation.json", "r") as f:
    FEDERATION = json.loads(f.read())

with open(f"{getcwd()}/data/haregly.json", "r") as f:
    HAREGLY = json.loads(f.read())

with open(f"{getcwd()}/data/blacklist.json", "r") as f:
    BLACKLIST = json.loads(f.read())
