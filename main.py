import nltk
import streamlit as st
import preprocessor
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

# App title
st.sidebar.title("Whatsapp Chat Analyzer")

# File upload button
file = st.sidebar.file_uploader("Select a file")

# Main heading
st.header("WhatsApp Chat Analysis")

# Sentiment analysis function
def sentiment_analysis(d):
        if d["neutral"] > d["positive"] and d["neutral"] > d["negative"]:
            return 0
        if d["positive"] > d["negative"] and d["positive"] > d["neutral"]:
            return 1
        if d["negative"] >= d["positive"] and d["negative"] >= d["neutral"]:
            return -1

if file is not None:
    raw_data = file.getvalue()
    unprocessed_data = raw_data.decode("utf-8")
    data = preprocessor.preprocess(unprocessed_data)
    sentiments = SentimentIntensityAnalyzer()
    data["positive"] = [sentiments.polarity_scores(i)["positive"] for i in data["message"]]
    data["negative"] = [sentiments.polarity_scores(i)["negative"] for i in data["message"]]
    data["neutral"] = [sentiments.polarity_scores(i)["neutral"] for i in data["message"]]
    data['value'] = data.apply(lambda row: sentiment_analysis(row), axis=1)

    




