import json

def load_intents():
    with open("chatbot/data/intents.json") as file:
        return json.load(file)["intents"]
