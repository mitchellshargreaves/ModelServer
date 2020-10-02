FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
ENV PYTHONPATH /app/app
ENV PATH=$PATH:/app/app
COPY requirements.txt .
RUN pip install  -r requirements.txt

COPY ./app /app