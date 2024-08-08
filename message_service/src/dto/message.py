from pydantic import BaseModel, ConfigDict

class InMessageDTO(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    sender: str
    message: str


class MessageDTO(InMessageDTO):
    posted_at: str

