from flask import Flask, request, jsonify, render_template
import pickle
import random
import json

app = Flask(__name__)

# Load trained model and vectorizer
with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)
with open("model/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Load responses
with open("data/intents.json", "r") as f:
    intents = json.load(f)
response_map = {intent["tag"]: intent["responses"] for intent in intents["intents"]}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    X_input = vectorizer.transform([user_input])
    tag = model.predict(X_input)[0]
    response = random.choice(response_map.get(tag, ["I'm not sure how to help with that."]))
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
