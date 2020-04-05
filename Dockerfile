FROM python:3

RUN apt-get update && apt-get install -y \
    curl \
    ffmpeg \
    libxml2

WORKDIR /usr/src/app

COPY ./rec_radiko_ts.sh .
RUN chmod a+x ./rec_radiko_ts.sh

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./main.py .

CMD ["python", "/usr/src/app/main.py"]
