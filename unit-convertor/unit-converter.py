import streamlit as st

def unit_converts(value,unit_from,unit_to): # Function to convert units

    conversions = { # Dictionary to store conversion factors
       "meters_kilometers": 0.001,  
    "kilometers_meters": 1000,  
    "meters_miles": 0.000621371,  
    "miles_meters": 1609.34,  
    "kilometers_miles": 0.621371,  
    "miles_kilometers": 1.60934,  
    "celsiuss_fahrenheits": 32,  
    "fahrenheits_celsiuss": 0.5555555555555556,  
    "celsiuss_kelvins": 273.15,  
    "kelvins_celsiuss": -273.15  
        
    }
    key=f"{unit_from}_{unit_to}" # Key to access the conversion factor

    if key in conversions: # Check if the key exists in the dictionary
        conversion=conversions[key] # Get the conversion factor
        return value*conversion # Return the converted value
    else:
        return "Conversion Not Supported" # Return this message if the conversion is not supported
    
# =================== frontend =======================
    
st.title("Unit Converter") # Title of the app
value=st.number_input("Enter the value to convert",min_value=1.0, step=1.0) # Input field to enter the value to convert

unit_from=st.selectbox("convert from",["meters","kilometers","miles","celsiuss","fahrenheits","kelvin"]) # Dropdown to select the unit to convert from
unit_to=st.selectbox("convert to",["meters","kilometers","miles","celsiuss","fahrenheits","kelvins"]) # Dropdown to select the unit to convert to


if st.button("Convert"): # Button to trigger the conversion
    
    result=unit_converts(value,unit_from,unit_to) # Call the function to convert the units
    st.write(f"{value} {unit_from} is equal to {result} {unit_to}") # Display the result


st.markdown( # Add some style to the app
    """
    <style>
        .stApp {
            background-color: lightblue;
        }
        
    </style>
    """,
    unsafe_allow_html=True
)
