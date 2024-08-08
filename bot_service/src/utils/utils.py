from src.message.message import ChatMessage

def stringify_messages(messages_dict: dict):
    result = ""
    for msg in messages_dict:
        message = ChatMessage(**msg)
        result += str(message)
    return result