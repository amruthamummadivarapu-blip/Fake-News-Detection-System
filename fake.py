import streamlit as st
import pickle
import re
import string

# Load model and vectorizer
model = pickle.load(open(r'C:\Users\DELL\Desktop\model\fake_news_model.pkl', "rb"))
vectorizer = pickle.load(open(r'C:\Users\DELL\Desktop\model\vectorizer.pkl', "rb"))

# Text cleaning
def clean_text(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub("\\W"," ", text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text

# Prediction
def predict_news(news):
    news = clean_text(news)
    vector = vectorizer.transform([news])
    prediction = model.predict(vector)
    
    return "Fake News" if prediction[0] == 0 else "Real News"

# ---------------- UI ---------------- #

st.title("📰 Fake News Detection System")
st.write("Paste long news text below (auto-expands).")

# Initialize session state
if "text" not in st.session_state:
    st.session_state.text = ""

# Estimate dynamic height based on text length
lines = st.session_state.text.count("\n") + 5
dynamic_height = min(600, max(150, lines * 25))

# Text input (auto-growing)
news_input = st.text_area(
    "Enter News Text",
    value=st.session_state.text,
    height=dynamic_height
)

# Store text
st.session_state.text = news_input

# Detect button
if st.button("Detect"):
    
    if news_input.strip() == "":
        st.warning("⚠️ Please enter some text")
    
    else:
        result = predict_news(news_input)
        
        if result == "Fake News":
            st.error("🚨 This is Fake News")
        else:
            st.success("✅ This is Real News")