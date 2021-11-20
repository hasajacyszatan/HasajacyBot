from os import path, getcwd
import json

TOKEN = ""

if path.isfile(f"{getcwd()}/data/federation.json"):
    with open(f"{getcwd()}/data/federation.json", "r") as f:
        FEDERATION = json.loads(f.read())
else:
    print(f"FILE {getcwd()}/data/federation.json DOES NOT EXIST")
if path.isfile(f"{getcwd()}/data/haregly.json"):
    with open(f"{getcwd()}/data/haregly.json", "r") as f:
        HAREGLY = json.loads(f.read())
else:
    print(f"FILE {getcwd()}/data/haregly.json DOES NOT EXIST")

if path.isfile(f"{getcwd()}/data/blacklist.json"):
    with open(f"{getcwd()}/data/blacklist.json", "r") as f:
        BLACKLIST = json.loads(f.read())
else:
    print(f"FILE {getcwd()}/data/blacklist.json DOES NOT EXIST")
