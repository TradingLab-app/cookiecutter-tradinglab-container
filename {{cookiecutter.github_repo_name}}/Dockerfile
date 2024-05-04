FROM --platform=linux/amd64 python:3.11.8 AS prod
LABEL authors="{{ cookiecutter.full_name.replace('\"', '\\\"') }}"
RUN apt-get update && apt-get install -y \
    gcc \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

RUN pip install poetry

RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock /app/src/
WORKDIR /app/src

RUN poetry install --only main
RUN apt-get purge -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY . /app/src/
RUN poetry install --only main

CMD ["python", "main.py"]
