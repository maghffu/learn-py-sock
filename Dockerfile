FROM python:3.8-slim
workdir .
copy . .
expose 65432
CMD python3 server.py