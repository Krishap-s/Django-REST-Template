FROM python:3.8

# Set env variables
ARG DEBUG=True

ENV DEBUG=$DEBUG

ARG DATABASE_URL=postgres://localhost:5432/testing

ENV DATABASE_URL=$DATABASE_URL

WORKDIR /app

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /app

EXPOSE 8000/tcp

CMD ["uvicorn", "server.asgi:application", "--host", "0.0.0.0", "--port", "8000"]
