from src.repository.repository import Repository

from motor.motor_asyncio import AsyncIOMotorClient

import pytest
import os

os.environ['DATABASE_NAME'] = 'test'
os.environ['COLLECTION_NAME'] = 'messages'

@pytest.fixture(scope='module')
def mongo():
    return AsyncIOMotorClient('mongodb://localhost:27017/')

@pytest.fixture(scope='module')
def repository(mongo):
    repository = Repository(mongo=mongo)

    yield repository