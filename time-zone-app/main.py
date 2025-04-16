import streamlit as st # type: ignore
from datetime import datetime # type: ignore
from zoneinfo import ZoneInfo  # type: ignore

st.title("Time zone App") # Title of the web app

Time_zone=[ # List of time zones
    "UTC",
    "Asia/Karachi",
    "Asia/Dubai",
    "Asia/Kolkata",
    "Asia/Shanghai",
    "Asia/Tokyo",
    "Europe/London",
    "America/NewYork",
    "America/Los_Angeles",
    "America/Chicago",
    "America/Toronto",
    "America/Mexico_City",
    "America/Sao_Paulo",
    "Australia/Sydney",
    "Australia/Brisbane",
    "Australia/Perth",
    
]

# Displaying the current time in all time zones
selected_timezone= st.multiselect("select a timezone",Time_zone,default=["UTC","Asia/Karachi"])
st.subheader("selected timezone") # Subheader for the selected time zones
for tz in selected_timezone: # Looping through the selected time zones
    current_time=datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I %H:%M:%S %p") # Getting the current time in the selected time zone
    st.info(f" {tz}: {current_time}") # Displaying the current time in the selected time zone


st.subheader("Timezone time between timezone") # Subheader for the time conversion section
current_time=st.time_input("current time", value=datetime.now().time()) # Getting the current time from the user
from_timezone=st.selectbox("from timezone",Time_zone,index=0) # Dropdown for selecting the from timezone
to_timezone=st.selectbox("to timezone",Time_zone,index=1) # Dropdown for selecting the to timezone

if st.button("calculate time"): # Button to calculate the time
    dt=datetime.combine(datetime.today(),current_time,tzinfo=ZoneInfo(from_timezone)) # Combining the date and time with the from timezone
    current_time=dt.astimezone(ZoneInfo(to_timezone)).strftime("%Y-%m-%d %I %H:%M:%S %p") # Converting the time to the to timezone
    st.success(f"the time in {to_timezone} is {current_time}") # Displaying the converted time in the to timezone



st.markdown( # Adding some style to the web app
    """
    <style>
        .stApp {
            background-color: lightgreen;
        }
        .stApp button {
            color: white;
            background-color: red;
        }
        .stApp button :hover {
            
            color: yellow;
        }
    </style>
    """,
    unsafe_allow_html=True
)