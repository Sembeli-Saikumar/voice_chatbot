import pickle, json, random

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
data = json.load(open("../data/intents.json")
)

def get_response(text):
    text_vec = vectorizer.transform([text])
    tag = model.predict(text_vec)[0]

    for intent in data["intents"]:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])
