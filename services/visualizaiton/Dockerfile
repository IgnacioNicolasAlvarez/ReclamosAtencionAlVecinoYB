FROM python:3.10-slim

WORKDIR /github

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir poetry

COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false && \
    poetry install --no-root

COPY .streamlit /github/.streamlit
COPY app /github/app


CMD ["streamlit", "run", "app/main.py"]
