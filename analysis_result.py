import streamlit as st
import features
import matplotlib.pyplot as plt

def create_monthly_analysis(selected_user, data):
    st.markdown("## Monthly analysis")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### Positive")
        busy_month = features.monthly(selected_user, data,1)
        fig, ax = plt.subplots()
        ax.bar(busy_month.index, busy_month.values, color='green')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)
        
    with col2:
        st.markdown("### Negative")        
        busy_month = features.monthly(selected_user, data, -1)
        fig, ax = plt.subplots()
        ax.bar(busy_month.index, busy_month.values, color='red')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

    with col3:
        st.markdown("### Neutral")
        busy_month = features.monthly(selected_user, data, 0)
        fig, ax = plt.subplots()
        ax.bar(busy_month.index, busy_month.values, color='red')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)
        
def create_weekly_analysis(selected, data):
    st.markdown("## Weekly analysis")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### Positive")
        busy_day = features.weekly(selected, data,1)
        fig, ax = plt.subplots()
        ax.bar(busy_day.index, busy_day.values, color='green')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)
    with col2:
        st.markdown("### Neutral")
        busy_day = features.weekly(selected, data, 0)
        fig, ax = plt.subplots()
        ax.bar(busy_day.index, busy_day.values, color='grey')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)
    with col3:
        st.markdown("### Negative")
        busy_day = features.weekly(selected, data, -1)
        fig, ax = plt.subplots()
        ax.bar(busy_day.index, busy_day.values, color='red')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)


def create_daily_timeline(selected, data):
    # Daily timeline
    st.markdown("## Daily Timeline")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### Positive")
        daily_timeline = features.timeline(selected, data, 1)
        fig, ax = plt.subplots()
        ax.plot(daily_timeline['day'], daily_timeline['message'], color='green')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

    with col2:
        st.markdown("### Neutral")        
        daily_timeline = features.timeline(selected, data, 0)
        fig, ax = plt.subplots()
        ax.plot(daily_timeline['day'], daily_timeline['message'], color='grey')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

    with col3:
        st.markdown("### Negative")        
        daily_timeline = features.timeline(selected, data, -1)
        fig, ax = plt.subplots()
        ax.plot(daily_timeline['day'], daily_timeline['message'], color='red')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)
