import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('punkt')
nltk.download('wordnet')

def clean_up_sentence(sentence):
    words = nltk.word_tokenize(sentence)
    words = [lemmatizer.lemmatize(word) for word in words]
    return words

def bag_of_words(sentence, words):
    # Create bag of words from the sentence
    bag = [0] * len(words)
    s_words = clean_up_sentence(sentence)
    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
    return bag
