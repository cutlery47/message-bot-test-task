from fastapi import HTTPException
from starlette import status

class RepositoryException(HTTPException):

    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = "При обработке вашего запроса произошла неизвестная ошибка"

class DataNotFoundException(RepositoryException):

    status_code = status.HTTP_404_NOT_FOUND
    detail = "Запрашиваемые данные не были найдены"

    def __init__(self, detail: str):
        self.detail = f"{self.detail}: {detail}"
