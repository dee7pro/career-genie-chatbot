import google.generativeai as genai
import os
from config.settings import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

def get_client():
    return genai

def create_chat_session(client, system_prompt):
    model = client.GenerativeModel("gemini-3-flash-preview")

    return model.start_chat(
        history=[
            {"role": "user", "parts": [system_prompt]}
        ]
    )

def send_message(chat_session, user_input):
    return chat_session.send_message(user_input)