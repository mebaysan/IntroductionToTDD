FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY src/ .

COPY requirements.txt .

COPY entrypoint.sh .

RUN pip install --upgrade pip  

RUN pip install -r requirements.txt

RUN chmod +x entrypoint.sh

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD wget -qO- http://localhost:5000/health/ || exit 1

ENTRYPOINT [ "bash", "entrypoint.sh" ]