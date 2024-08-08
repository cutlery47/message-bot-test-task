from src.application.app import Application
from src.controller.contoller import Controller
from src.service.service import Service
from src.repository.repository import Repository

from fastapi import FastAPI
from loguru import logger
import os


mongo_port = int(os.getenv('MONGO_PORT'))
mongo_host = os.getenv('MONGO_HOST')

class ApplicationFactory:

    def create(self,
               RepositoryClass: Repository.__class__,
               ServiceClass: Service.__class__,
               ControllerClass: Controller.__class__,
               ApplicationClass: Application.__class__
               ) -> FastAPI:

        self.setup_loggers()

        repository = RepositoryClass(mongo_host=mongo_host, mongo_port=mongo_port)

        service = ServiceClass(repo=repository)

        controller = ControllerClass(service=service)

        application = ApplicationClass(controller=controller)

        return application.asgi_app()


    @staticmethod
    def setup_loggers():
        logger.remove()

        # file error logger
        logger.add(sink="src/logs/err.json",
                   level="ERROR",
                   format="{time:DD/MM/YYYY/HH:mm:ss} "
                          "|{level}| line {line} in {module}.{function}: {message}",
                   colorize=True,
                   serialize=True,
                   rotation="1 MB",
                   compression="zip")

        # terminal general logger
        logger.add(sink="src/logs/logs.json",
                   level="INFO",
                   format="{time:DD/MM/YYYY/HH:mm:ss} "
                          "|{level}| line {line} in {module}.{function}: {message}",
                   colorize=True,
                   serialize=True,
                   rotation="1 MB",
                   compression="zip")

