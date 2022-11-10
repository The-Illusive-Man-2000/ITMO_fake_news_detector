FROM python:3.8-slim-buster
RUN apt-get update -y
RUN apt-get install -y python3-pip \
    python3-dev \
    build-essential \
    python-gi-dev \
    libsystemd-dev
WORKDIR /itmo_fake_news
COPY . /itmo_fake_news

RUN python3 -m pip install --upgrade pip
RUN apt-get install -y python-gobject
RUN apt-get --yes install unattended-upgrades
RUN apt-get --yes install python-cairocffi python3-cairocffi
RUN apt-get --yes install libmagickwand-dev
RUN apt-get --yes install libgl1

RUN python3 -m pip install --no-cache-dir --user -r requirements.txt
RUN python3 -m spacy download ru_core_news_sm --user

CMD python3 web_service.py
EXPOSE 8080