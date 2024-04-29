# Image for FastAPI application
FROM python:3.11.9-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

USER root
RUN apt-get update && apt-get upgrade -y \
    && rm -rf /var/lib/apt/lists/* && \
    useradd -m -s /bin/bash acme

USER acme
WORKDIR /app
COPY --chown=acme:acme requirements.txt .
COPY --chown=acme:acme ACMEsports ACMEsports/

RUN pip install -U pip && \
    pip install --no-cache-dir -r requirements.txt

CMD ["python3", "-m", "uvicorn","ACMEsports.main:app", "--host", "0.0.0.0", "--port", "18000"]
