FROM python:3.8-slim
expose 65432
CMD ['python' 'server.py']