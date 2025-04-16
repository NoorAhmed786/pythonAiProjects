import google.generativeai as ai # type: ignore
from dotenv import load_dotenv # type: ignore
import os # to get env variable 


load_dotenv() 

ai.configure(api_key=os.environ["GEMINAI_API_KEY"]) # api configuration

model= ai.GenerativeModel(model_name="gemini-2.0-flash") # models name

while True:
    user_input = input("Ask me anything (or type 'quit' to exit): ") # get input from user
    
    if user_input.lower() == 'quit':
        print("Goodbye!")
        break
        
    response = model.generate_content(user_input) #generate content based on user input
    print(response.text)
    print("\n") # Add a blank line between responses for readability