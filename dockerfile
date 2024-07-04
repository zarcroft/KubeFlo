FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

RUN useradd -m doodle

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN pip install --no-cache-dir poetry

RUN poetry config virtualenvs.create false && \
    poetry install --no-dev --no-interaction --no-ansi

COPY . .

RUN chown -R doodle:doodle /app

EXPOSE 5000

USER doodle

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]
