FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY pyproject.toml poetry.lock ./event_manager/
WORKDIR /app/event_manager
RUN pip install poetry && poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi

COPY . /app
WORKDIR /app/event_manager

COPY entrypoint.sh /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
