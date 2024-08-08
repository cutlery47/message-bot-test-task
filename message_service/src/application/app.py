from src.controller.contoller import Controller

from fastapi import FastAPI
from fastapi.testclient import TestClient

class Application:

    def __init__(self, controller: Controller):
        self._controller = controller
        self._app = FastAPI()
        self._app.include_router(self._controller.get_routes())

    def asgi_app(self):
        return self._app

    def test_client(self) -> TestClient:
        return TestClient(app=self.asgi_app(), follow_redirects=True)
