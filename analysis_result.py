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
        ax.bar(busy_month.index, busy_month.values, color='grey')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)
