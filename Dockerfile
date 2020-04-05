FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    curl \
    ffmpeg \
    libxml2

WORKDIR /usr/src/app

COPY ./rec_radiko_ts.sh .
RUN chmod a+x ./rec_radiko_ts.sh

ENTRYPOINT ["/usr/src/app/rec_radiko_ts"]
