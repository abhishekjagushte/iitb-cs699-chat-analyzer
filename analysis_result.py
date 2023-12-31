import streamlit as st
import features
import matplotlib.pyplot as plt

def create_monthly_analysis(selected_user, data):
    st.markdown("## Monthly analysis")
    st.markdown("These graphs illustrate the monthly analysis of users expressing positive, negative, and neutral sentiments. It categorizes users based on their sentiment over time.")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### Positive")
        busy_month = features.monthly(selected_user, data, 1)
        fig, ax = plt.subplots()
        ax.bar(busy_month.index, busy_month.values, color='green')
        plt.xticks(rotation='vertical')
        plt.xlabel('Month')
        plt.ylabel('Messages Count')
        st.pyplot(fig)

    with col2:
        st.markdown("### Neutral")
        busy_month = features.monthly(selected_user, data, 0)
        fig, ax = plt.subplots()
        ax.bar(busy_month.index, busy_month.values, color='gray')
        plt.xticks(rotation='vertical')
        plt.xlabel('Month')
        plt.ylabel('Messages Count')
        st.pyplot(fig)

    with col3:
        st.markdown("### Negative")        
        busy_month = features.monthly(selected_user, data, -1)
        fig, ax = plt.subplots()
        ax.bar(busy_month.index, busy_month.values, color='red')
        plt.xticks(rotation='vertical')
        plt.xlabel('Month')
        plt.ylabel('Messages Count')
        st.pyplot(fig)

def create_weekly_analysis(selected, data):
    st.markdown("## Weekly analysis")
    st.markdown("These graphs illustrate the weekly analysis of users expressing positive, negative, and neutral sentiments. It categorizes users based on their sentiment over time.")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### Positive")
        busy_day = features.weekly(selected, data, 1)
        fig, ax = plt.subplots()
        ax.bar(busy_day.index, busy_day.values, color='green')
        plt.xticks(rotation='vertical')
        plt.xlabel('Week')
        plt.ylabel('Messages Count')
        st.pyplot(fig)

    with col2:
        st.markdown("### Neutral")
        busy_day = features.weekly(selected, data, 0)
        fig, ax = plt.subplots()
        ax.bar(busy_day.index, busy_day.values, color='grey')
        plt.xticks(rotation='vertical')
        plt.xlabel('Week')
        plt.ylabel('Messages Count')
        st.pyplot(fig)

    with col3:
        st.markdown("### Negative")
        busy_day = features.weekly(selected, data, -1)
        fig, ax = plt.subplots()
        ax.bar(busy_day.index, busy_day.values, color='red')
        plt.xticks(rotation='vertical')
        plt.xlabel('Week')
        plt.ylabel('Messages Count')
        st.pyplot(fig)

def create_daily_timeline(selected, data):
    # Daily timeline
    st.markdown("## Daily Timeline")
    st.markdown("These graphs illustrate the daily analysis of users expressing positive, negative, and neutral sentiments. It categorizes users based on their sentiment over time.")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### Positive")
        daily_timeline = features.daily(selected, data, 1)
        fig, ax = plt.subplots()
        ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='green')
        plt.xticks(rotation='vertical')
        plt.xlabel('Date')
        plt.ylabel('Messages Count')
        st.pyplot(fig)

    with col2:
        st.markdown("### Neutral")        
        daily_timeline = features.daily(selected, data, 0)
        fig, ax = plt.subplots()
        ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='grey')
        plt.xticks(rotation='vertical')
        plt.xlabel('Date')
        plt.ylabel('Messages Count')
        st.pyplot(fig)

    with col3:
        st.markdown("### Negative")        
        daily_timeline = features.daily(selected, data, -1)
        fig, ax = plt.subplots()
        ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='red')
        plt.xticks(rotation='vertical')
        plt.xlabel('Date')
        plt.ylabel('Messages Count')
        st.pyplot(fig)

def create_monthly_timeline(selected, data):
    # Monthly timeline Analysis
    st.markdown("## Monthly Timeline")
    st.markdown("These graphs illustrate the monthly analysis of users expressing positive, negative, and neutral sentiments. It categorizes users based on their sentiment over time.")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### Positive")
        timeline = features.timeline_monthly(selected, data, 1)
        fig, ax = plt.subplots()
        ax.plot(timeline['time'], timeline['message'], color='green')
        plt.xticks(rotation='vertical')
        plt.xlabel('Month')
        plt.ylabel('Messages Count')
        st.pyplot(fig)
    with col2:
        st.markdown("### Neutral")
        timeline = features.timeline_monthly(selected, data, 0)
        fig, ax = plt.subplots()
        ax.plot(timeline['time'], timeline['message'], color='grey')
        plt.xticks(rotation='vertical')
        plt.xlabel('Month')
        plt.ylabel('Messages Count')
        st.pyplot(fig)
    with col3:
        st.markdown("### Negative")
        timeline = features.timeline_monthly(selected, data, -1)
        fig, ax = plt.subplots()
        ax.plot(timeline['time'], timeline['message'], color='red')
        plt.xticks(rotation='vertical')
        plt.xlabel('Month')
        plt.ylabel('Messages Count')
        st.pyplot(fig)

def create_member_contribution(selected, data):
    # Percentage contributed by each member in the chat
    if selected == 'Overall':
        st.markdown("## Member Contribution")
        st.markdown("These dataframes illustrate the percentage contributed by each member in the chat.")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("### Most Positive", unsafe_allow_html=True)
            contributions = features.member_contribution(data, 1)
            # Plot the data
            st.dataframe(contributions)
        with col2:
            st.markdown("### Most Neutral", unsafe_allow_html=True)
            contributions = features.member_contribution(data, 0)
            # Plot the data
            st.dataframe(contributions)
        with col3:
            st.markdown("### Most Negative", unsafe_allow_html=True)
            contributions = features.member_contribution(data, -1)
            # Plot the data
            st.dataframe(contributions)

def create_user_sentiment_summary(selected, data):
    # User-wise sentiment analysis
    if selected == 'Overall':
        st.markdown("## User sentiment summary")
        st.markdown("These graphs illustrate the userwise sentiment analysis. It categorizes users based on their sentiment over time.")
        positive_users, neutral_users, negative_users = features.user_sentiment_summary(data)        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("### Most Positive", unsafe_allow_html=True)
            fig, ax = plt.subplots()
            ax.bar(positive_users.index, positive_users.values, color='green')
            plt.xticks(rotation='vertical')
            plt.xlabel('User')
            plt.ylabel('Messages Count')
            st.pyplot(fig)
        with col2:
            st.markdown("### Most Neutral", unsafe_allow_html=True)
            fig, ax = plt.subplots()
            ax.bar(neutral_users.index, neutral_users.values, color='grey')
            plt.xticks(rotation='vertical')
            plt.xlabel('User')
            plt.ylabel('Messages Count')
            st.pyplot(fig)
        with col3:
            st.markdown("### Most Negative", unsafe_allow_html=True)
            fig, ax = plt.subplots()
            ax.bar(negative_users.index, negative_users.values, color='red')
            plt.xticks(rotation='vertical')
            plt.xlabel('User')
            plt.ylabel('Messages Count')
            st.pyplot(fig)

def create_wordcloud(selected, data):
    st.markdown("## Word Cloud")
    st.markdown("These wordclouds illustrate the most common positive, neutral, and negative words.")
    col1, col2, col3 = st.columns(3)
    with col1:
        try:
            st.markdown("### Positive", unsafe_allow_html=True)
            positive_wordcloud = features.wordcloud(selected, data, 1)
            fig, ax = plt.subplots()
            ax.imshow(positive_wordcloud)
            plt.xlabel('Word')
            plt.ylabel('Frequency')
            st.pyplot(fig)
        except:
            st.image('assets/images/error.webp')
    with col2:
        try:
            st.markdown("### Neutral", unsafe_allow_html=True)
            neutral_wordcloud = features.wordcloud(selected, data, 0)
            fig, ax = plt.subplots()
            ax.imshow(neutral_wordcloud)
            plt.xlabel('Word')
            plt.ylabel('Frequency')
            st.pyplot(fig)
        except:
            st.image('assets/images/error.webp')
    with col3:
        try:
            st.markdown("### Negative", unsafe_allow_html=True)
            negative_wordcloud = features.wordcloud(selected, data, -1)
            fig, ax = plt.subplots()
            ax.imshow(negative_wordcloud)
            plt.xlabel('Word')
            plt.ylabel('Frequency')
            st.pyplot(fig)
        except:
            st.image('assets/images/error.webp')

def create_word_frequency_analysis(selected, data):
    # Most common positive/neutral/negative words
    st.markdown("## Common Words")
    st.markdown("These graphs illustrate the most common positive, neutral, and negative words.")
    col1, col2, col3 = st.columns(3)
    with col1:
        try:
            # Most common positive words.
            common_positive_words = features.common_words(selected, data, 1)
            st.markdown("### Positive Words", unsafe_allow_html=True)
            fig, ax = plt.subplots()
            ax.barh(common_positive_words[0], common_positive_words[1], color='green')
            plt.xticks(rotation='vertical')
            plt.xlabel('Count')
            plt.ylabel('Word')
            st.pyplot(fig)
        except:
            st.image('assets/images/error.webp')
    with col2:
        try:
            # Most common neutral words.
            common_neutral_words = features.common_words(selected, data, 0)
            st.markdown("### Neutral Words", unsafe_allow_html=True)
            fig, ax = plt.subplots()
            ax.barh(common_neutral_words[0], common_neutral_words[1], color='grey')
            plt.xticks(rotation='vertical')
            plt.xlabel('Count')
            plt.ylabel('Word')
            st.pyplot(fig)
        except:
            st.image('assets/images/error.webp')
    with col3:
        try:
            # Most common negative words.
            common_negative_words = features.common_words(selected, data, -1)
            st.markdown("### Negative Words", unsafe_allow_html=True)
            fig, ax = plt.subplots()
            ax.barh(common_negative_words[0], common_negative_words[1], color='red')
            plt.xticks(rotation='vertical')
            plt.xlabel('Count')
            plt.ylabel('Word')
            st.pyplot(fig)
        except:
            st.image('assets/images/error.webp')
