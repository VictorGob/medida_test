# Image for FastAPI application
FROM python:3.11.9-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# To detect if the application is running in a docker container
ENV IN_DOCKER True

USER root
RUN apt-get update && apt-get upgrade -y \
    && rm -rf /var/lib/apt/lists/* && \
    useradd -m -s /bin/bash acme

USER acme
WORKDIR /app
COPY --chown=acme:acme requirements.txt .
COPY --chown=acme:acme log_conf.yaml .
COPY --chown=acme:acme ACMEsports ACMEsports/

RUN pip install -U pip && \
    pip install --no-cache-dir -r requirements.txt

CMD ["python3", "-m", "uvicorn","ACMEsports.main:app", "--host", "0.0.0.0", "--port", "18000", "--log-config=log_conf.yaml"]
