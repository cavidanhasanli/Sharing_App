FROM tiangolo/uvicorn-gunicorn:python3.8

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt
