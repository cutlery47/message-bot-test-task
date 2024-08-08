from src.application.factory import ApplicationFactory
from src.repository.repository import Repository
from src.service.service import Service
from src.controller.contoller import Controller
from src.application.app import Application

factory = ApplicationFactory()

app = factory.create(RepositoryClass=Repository,
                     ServiceClass=Service,
                     ControllerClass=Controller,
                     ApplicationClass=Application)


