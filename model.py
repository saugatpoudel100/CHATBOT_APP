import json
import random
import pickle
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

def train_chatbot():
    with open("data/intents.json", "r") as f:
        data = json.load(f)

    X = []
    y = []
    responses = {}

    for intent in data["intents"]:
        tag = intent["tag"]
        responses[tag] = intent["responses"]
        for pattern in intent["patterns"]:
            X.append(pattern)
            y.append(tag)

    vectorizer = TfidfVectorizer()
    model = MultinomialNB()

    X_vec = vectorizer.fit_transform(X)
    model.fit(X_vec, y)

    # Save model and vectorizer
    os.makedirs("model", exist_ok=True)
    with open("model/model.pkl", "wb") as f:
        pickle.dump(model, f)
    with open("model/vectorizer.pkl", "wb") as f:
        pickle.dump(vectorizer, f)

    print("Model trained and saved.")
    return model, vectorizer, responses

if __name__ == "__main__":
    train_chatbot()
