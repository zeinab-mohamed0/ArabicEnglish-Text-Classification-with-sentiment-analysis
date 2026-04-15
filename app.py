import streamlit as st
from langclassifier import predict_language
from english_text import predict_english    
from arabic_text import predict_arabic

st.title("Language and Sentiment Analysis")
# Input text from user
text = st.text_area("Enter text:")

if text.strip():
    # Predict the language of the input text
    language = predict_language(text)
    st.write(f"The predicted language is: {language}")

    # If the predicted language is Arabic, use the Arabic model to predict the sentiment
    if language == "Arabic":
        prediction = predict_arabic(text)
        st.write(f"The predicted sentiment is: {prediction}")
    else:
        prediction = predict_english(text)
        if prediction == 0:
            prediction = "Negative"
        elif prediction == 1:
            prediction = "Neutral"
        else:
            prediction = "Positive"
        st.write(f"The predicted sentiment is: {prediction}")