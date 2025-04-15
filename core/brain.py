from services.gemini_api import get_gemini_reply
from core.commands import handle_command
from core.memory import remember, recall

def process_query(query):
    # Check if it's a known command
    command_response = handle_command(query)
    if command_response:
        return command_response

    # Else get smart reply
    reply = get_gemini_reply(query)
    remember(query, reply)
    return reply
