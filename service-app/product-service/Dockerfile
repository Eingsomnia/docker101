FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir requirements.txt

COPY app.py .

EXPOSE 5002

CMD ["python", "app.py"]