import os #get enviroment variable ko get krnyt k leay
import chainlit as cl  # type: ignore
import google.generativeai as genai  # type: ignore
from dotenv import load_dotenv  # type: ignore

# Load environment variables
load_dotenv()

# Get the API key from the .env file
gemini_api_key = os.getenv("GEMINAI_API_KEY")

# Make sure the key exists
if not gemini_api_key:
    raise ValueError("GEMINAI_API_KEY not found in environment variables")

# Configure Gemini API
genai.configure(api_key=gemini_api_key)

# Initialize the model
model = genai.GenerativeModel(model_name="gemini-2.0-flash")

# Handle chat start
@cl.on_chat_start
async def handle_chat_start():
    await cl.Message(content="👋 Hello! How can I help you today?").send()

# Handle user messages
@cl.on_message
async def handle_message(message: cl.Message):
    prompt = message.content

    try:
        response = model.generate_content(prompt)
        response_text = response.text if hasattr(response, "text") else "⚠️ No response from model."
    except Exception as e:
        response_text = f"❌ Error: {str(e)}"

    await cl.Message(content=response_text).send()
