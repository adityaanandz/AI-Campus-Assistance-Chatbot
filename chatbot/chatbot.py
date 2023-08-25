import os
import random
import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model
from preprocess.preprocessing import clean_up_sentence, bag_of_words
from utils.helpers import load_intents

lemmatizer = WordNetLemmatizer()
intents = load_intents()

model = load_model("chatbot/models/intent_classifier.pkl")

# Rest of the code remains the same

def clean_up_sentence(sentence):
    words = nltk.word_tokenize(sentence)
    words = [lemmatizer.lemmatize(word) for word in words]
    return words

def predict_intent(sentence):
    p = clean_up_sentence(sentence)
    return model.predict([bag_of_words(p, words)])[0]

def get_response(intents_list, intents_json):
    tag = intents_list[0]["intent"]
    list_of_intents = intents_json["intents"]
    for i in list_of_intents:
        if i["tag"] == tag:
            response = random.choice(i["responses"])
            break
    return response

def chatbot_response(user_input):
    ints = predict_intent(user_input)
    res = get_response(ints, intents)
    return res

def run():
    print("Chatbot: Hi there! How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Chatbot: Goodbye!")
            break
        response = chatbot_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    run()
