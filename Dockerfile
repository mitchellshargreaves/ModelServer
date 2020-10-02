FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
RUN apk update
RUN apk add bash nano make automake gcc g++ subversion python3-dev
COPY ./app /app
COPY requirements.txt .
RUN pip install  -r requirements.txt