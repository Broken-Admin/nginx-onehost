FROM python:latest

WORKDIR /root

RUN mkdir http

WORKDIR /root/http

COPY server.py .

EXPOSE 8080

CMD [ "python3", "server.py"]
