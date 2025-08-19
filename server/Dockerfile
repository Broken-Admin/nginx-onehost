FROM ubuntu:noble

WORKDIR /root

RUN apt-get update
RUN apt-get install netcat-openbsd -y

COPY run.sh .

EXPOSE 8080

CMD [ "/root/run.sh" ]
