import nltk
import streamlit as st
import preprocessor
import analysis_result
import features
nltk.download('vader_lexicon')

# App title
st.sidebar.title("Analyzer for WhatsApp Chats")

# File upload button
file = st.sidebar.file_uploader("Select a file")

st.markdown("""
    <style>
        .center {
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='center'>Analyzer for WhatsApp Chats</h1>", unsafe_allow_html=True)
# Main heading


if file is not None:
    raw_data = file.getvalue()
    unprocessed_data = raw_data.decode("utf-8")
    
    # Data pre-processing
    data = preprocessor.preprocessing(unprocessed_data)
    
    # Sentiment Analysis. This sets a column "value" which either contains 1 (positive) or -1 (negative) or 0 (neutral)
    data = features.sentiment_analysis(data)
    
    userl = data['user'].unique().tolist()
    userl.sort()
    userl.insert(0, "Overall")
    selected = st.sidebar.selectbox("Show analysis wrt", userl)


    if st.sidebar.button("Show Analysis"):        
        # show monthly analysis
        analysis_result.create_monthly_analysis(selected, data)

        # show weekly analysis
        analysis_result.create_weekly_analysis(selected, data)
        
        # show daily timeline
        analysis_result.create_daily_timeline(selected, data)
        
        # show monthly timeline
        analysis_result.create_monthly_timeline(selected, data)

        # Member contribution
        analysis_result.create_member_contribution(selected, data)

        # Most positive, negative and neutral users
        analysis_result.create_user_sentiment_summary(selected, data)

        # Show a wordcloud
        analysis_result.create_wordcloud(selected, data)
        
        # Common words
        analysis_result.create_word_frequency_analysis(selected, data)

        
