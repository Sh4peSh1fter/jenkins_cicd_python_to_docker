FROM python:3.8-slim-buster

COPY . .
RUN cd app
CMD ["python3", "-c", "import os;while(True): print(os.getcwd())"]