import streamlit as st
import pickle
from utils import transform_text


model = pickle.load(open('spam_model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

def predict_spam(text):
    transformed = transform_text(text)
    vector = vectorizer.transform([transformed]).toarray()
    return model.predict(vector)[0]

st.title("📩 SMS Spam Classifier")

input_sms = st.text_area("Enter your message")

if st.button("Predict"):
    result = predict_spam(input_sms)
    st.header("Spam" if result else "Ham (Not Spam)")
