FROM python:3.10.7-slim

COPY . /app
WORKDIR /app

RUN python3 -m venv /opt/venv

RUN /opt/venv/bin/pip install pip --upgrade
RUN /opt/venv/bin/pip install -r requirements.txt
RUN chmod +x migrate.sh && \
    chmod +x collectstatic.sh && \
    chmod +x entrypoint.sh

CMD ["/app/entrypoint.sh"]