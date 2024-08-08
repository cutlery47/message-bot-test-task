FROM python:3.12.4-alpine3.20

RUN apk --no-cache add curl

ENV POETRY_VIRTUALENVS_CREATE=false
ENV PATH="${PATH}:/root/.local/bin"
RUN curl -sSL https://install.python-poetry.org | python3 -

RUN mkdir "/message_service"
WORKDIR /message_service

COPY src/ /message_service/src/
COPY poetry.lock pyproject.toml README.md start.sh main.py /message_service/

RUN poetry install && poetry update

EXPOSE 8000

CMD sh start.sh