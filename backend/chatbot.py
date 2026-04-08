from backend.gemini_client import send_message
from backend.prompts import get_system_prompt
from backend.logger import get_logger

logger = get_logger()

def get_response(chat_session, user_input):
    try:
        response = send_message(chat_session, user_input)
        reply = response.text

        logger.info(f"User: {user_input}")
        logger.info(f"Bot: {reply}")

        return reply

    except Exception as e:
        logger.error(str(e))
        return "⚠️ Something went wrong. Try again."