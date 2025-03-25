import streamlit as st # type: ignore
import random #for random number generation
import time #for time delay
import requests # type: ignore #for api calls

st.title("Money Making Machine")

def generate_money():
    return random.randint(1 ,100)

st.subheader("Money Generator")
if st.button("Generate Money"):
    st.write("Generating money...")
    time.sleep(2)
    money=generate_money()
    st.success(f"you made ${money}!")

def fetch_side_hustle():
    try:
        response= requests.get('http://127.0.0.1:8000/side_hustles?api_key=12345678')
        if response.status_code==200:
            hustles = response.json()
            return hustles["side_hustles"]
        else:
            return ("freelancing")


    except:
        return("no side hustle found")

st.subheader("side hustle Ideas")
if st.button("Get Side Hustle Ideas"):
    ideas=fetch_side_hustle()
    st.info(ideas)

def fetch_money_qoutes():
    try:
        response=requests.get('http://127.0.0.1:8000/money_quotes?api_key=12345678')
        if response.status_code==200:
            quotes=response.json()
            return quotes["money_quotes"]
        else:
            return("no money quotes found")
    except:
        return("no money quotes found")

st.subheader("Money Quotes")
if st.button("Get Money Quotes"):
    quotes=fetch_money_qoutes()
    st.info(quotes)
    st.balloons()

st.markdown( # Adding some style to the web app
    """
    <style>
        .stApp {
            background-color: lightblue;
        }
        
    </style>
    """,
    unsafe_allow_html=True
)

