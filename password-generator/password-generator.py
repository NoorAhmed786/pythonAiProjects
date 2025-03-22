import streamlit as st     # type: ignore # Importing Streamlit library
import random               # Importing random library
import string               # Importing string library


def generator_password(length,use_digits,use_special):
    
    characters = string.ascii_letters  # All the alphabets

    if use_digits:
        characters += string.digits     # Adding digits to the characters
    if use_special:
        characters += string.punctuation # Adding special characters to the characters
    return ''.join(random.choice(characters) for _ in range(length)) # Generating password
# multiple value store in one string variable  ''
# dont know loop value thn use _

# =========================== frontent code ==========================
st.title("Password Generator") # Title of the web app
st.write("Select the length of the password and the type of characters you want to include in your password")
 # Description of the web app
length = st.slider("select the length of the password", min_value=6, max_value=30,value=12) # Slider for selecting the length of the password
use_digits=st.checkbox("Use digits") # Checkbox for using digits

use_special=st.checkbox("Use special characters") # Checkbox for using special characters

if st.button("generate password"): # Button to generate password
    password = generator_password(length,use_digits,use_special) # Generating password
    st.write(f"Generate Password : `{password}`") # Displaying the password

    st.write("---------------------------------------------------------------------") # Displaying the line
    st.balloons() # Displaying balloons animation
    st.success("Password generated successfully") # Displaying the success message

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