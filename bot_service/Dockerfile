FROM python:3.12.4-alpine3.20

RUN apk --no-cache add curl

ENV POETRY_VIRTUALENVS_CREATE=false
ENV PATH="${PATH}:/root/.local/bin"
RUN curl -sSL https://install.python-poetry.org | python3 -

RUN mkdir "/bot_service"
WORKDIR /bot_service

COPY src/ /bot_service/src/
COPY poetry.lock pyproject.toml README.md main.py /bot_service/

RUN poetry install & poetry update

CMD python -m main