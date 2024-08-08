from dataclasses import dataclass

@dataclass
class InChatMessage:

    sender: str
    message: str

@dataclass
class ChatMessage(InChatMessage):

    posted_at: str

    def __str__(self):
        return f"Юзер {self.sender} отправил {self.message} | {self.posted_at} \n\n"