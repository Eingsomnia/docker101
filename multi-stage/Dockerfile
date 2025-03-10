FROM python:3.9 AS builder

WORKDIR /build

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt -t /dependencies

FROM python:3.9-slim

WORKDIR /app

COPY --from=builder /dependencies /usr/local/lib/python3.9/site-packages

COPY app.py .

EXPOSE 5000

CMD [ "python", "app.py"]