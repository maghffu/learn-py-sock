FROM python:3.9.0-alpine3.12

WORKDIR /app

COPY . .

CMD ["python" "server.py"]