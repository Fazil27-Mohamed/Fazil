# === intent_classifier.py ===

import json
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

class IntentClassifier:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.model = LogisticRegression()
        self.intents = []

    def train(self, texts, labels):
        X = self.vectorizer.fit_transform(texts)
        self.model.fit(X, labels)

    def predict(self, text):
        X = self.vectorizer.transform([text])
        return self.model.predict(X)[0]


# === response_generator.py ===

responses = {
    "greeting": ["Hello!", "Hi there!", "Welcome! How can I help you?"],
    "goodbye": ["Goodbye!", "Have a great day!", "See you soon!"],
    "thanks": ["You're welcome!", "No problem!", "Glad to help!"]
}

def generate_response(intent):
    return random.choice(responses.get(intent, ["I'm not sure how to help with that."]))


# === app.py ===

import streamlit as st

st.title("🤖 Intelligent Chatbot")

# Load or simulate model
classifier = IntentClassifier()
classifier.train(["hello", "hi", "thanks", "bye"], ["greeting", "greeting", "thanks", "goodbye"])

# User input
user_input = st.text_input("You:", "")

if user_input:
    intent = classifier.predict(user_input)
    response = generate_response(intent)
    st.write(f"Chatbot: {response}")
