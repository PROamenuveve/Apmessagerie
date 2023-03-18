import json


with open ("donner_message.json","r") as f:
    donner = json.load(f)


print(donner)