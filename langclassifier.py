import pickle

model = pickle.load(open("models/lang_model.pkl", "rb"))
vectorizer = pickle.load(open("victorizers/lang_vectorizer.pkl", "rb")) 

def predict_language(text):
    text_vectorized = vectorizer.transform([text])
    prediction = model.predict(text_vectorized)
    return prediction[0]