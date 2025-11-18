FROM python:3.11-slim

RUN apt-get update && apt-get install -y wget gnupg libnss3 libatk1.0-0 libatk-bridge2.0-0 libx11-xcb1 libxcomposite1 libxdamage1 libxrandr2 libasound2 libgbm1 libpangocairo-1.0-0 libxcb1 libgtk-3-0 ca-certificates --no-install-recommends && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
RUN playwright install --with-deps
COPY . /app
ENTRYPOINT ["pytest"]
