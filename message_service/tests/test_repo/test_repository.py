from tests.test_repo.conftest import repository

from src.dto.message import InMessageDTO

import pytest

@pytest.mark.asyncio(scope='module')
async def test_repo_post_get_delete(repository):
    message = InMessageDTO(sender='user', message='hello')

    await repository.post(message)

    messages = await repository.get()

    assert len(messages) == 1

    await repository.delete()

@pytest.mark.asyncio(scope='module')
async def test_repo_post_get_delete_multiple(repository):
    message_1 = InMessageDTO(sender='user', message='hello')
    message_2 = InMessageDTO(sender='user', message='hello2')

    await repository.post(message_1)
    await repository.post(message_2)

    messages = await repository.get()

    assert len(messages) == 2

    await repository.delete()