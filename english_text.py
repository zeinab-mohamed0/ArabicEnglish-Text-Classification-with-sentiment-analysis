import pickle

model = pickle.load(open("models/english_model.pkl", "rb"))
vectorizer = pickle.load(open("victorizers/english_vectorizer.pkl", "rb"))

def predict_english(text):
    text_vectorized = vectorizer.transform([text])
    prediction = model.predict(text_vectorized)
    return prediction[0]