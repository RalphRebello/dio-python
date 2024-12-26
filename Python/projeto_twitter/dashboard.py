import streamlit as st
import pandas as pd

def create_dashboard(data):
    st.title("Análise de Tweets")
    st.dataframe(data)
    st.bar_chart(data["likes"])
    st.bar_chart(data["retweets"])

