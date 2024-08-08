from src.dto.message import InMessageDTO

def test_message_serialization():
    message = InMessageDTO(message='123123',
                           sender='me')

    assert message.model_dump() == {
        'message': '123123',
        'sender': 'me'
    }