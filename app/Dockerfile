FROM python:3.9-slim

WORKDIR /app

COPY app.py .

RUN pip install flask prometheus_client

EXPOSE 5000 8000

CMD ["python", "app.py"]
