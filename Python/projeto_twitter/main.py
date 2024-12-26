from twitter_client import TwitterClient
from data_processing import process_tweets
from dashboard import create_dashboard
import streamlit as st

API_KEY = "sua_api_key"
API_SECRET_KEY = "sua_api_secret_key"
ACCESS_TOKEN = "seu_access_token"
ACCESS_TOKEN_SECRET = "seu_access_token_secret"


def main():
    st.sidebar.title("Configurações")
    query = st.sidebar.text_input("Termo de Busca", "Python")
    client = TwitterClient(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    st.sidebar.text("Buscando tweets...")
    tweets = client.search_tweets(query)
    data = process_tweets(tweets)

    create_dashboard(data)


if __name__ == "__main__":
    main()

