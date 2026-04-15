import pickle

model = pickle.load(open("models/arabic_model.pkl", "rb"))
vectorizer = pickle.load(open("victorizers/arabic_vectorizer.pkl", "rb"))

def predict_arabic(text):
    text_vectorized = vectorizer.transform([text])
    prediction = model.predict(text_vectorized)
    return prediction[0]