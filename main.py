import streamlit as st
import preprocessor

# App title
st.sidebar.title("Whatsapp Chat Analyzer")

# File upload button
file = st.sidebar.file_uploader("Select a file")

# Main heading
st.header("WhatsApp Chat Analysis")

if file is not None:
    raw_data = file.getvalue()
    unprocessed_data = raw_data.decode("utf-8")

    data = preprocessor.preprocess(unprocessed_data)

    




