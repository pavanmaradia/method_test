# docker build -t ubuntu1604py36
FROM ubuntu:16.04

RUN apt-get update && \
    apt-get install -y software-properties-common vim && \
    add-apt-repository ppa:jonathonf/python-3.6 && \
    apt-get update && \
    apt-get install -y \
        build-essential \
        git \
        nginx \
        python3.6 \
        python3.6-dev \
        python3-pip \
        python3.6-venv \
        supervisor && \
    apt-get install -y git && \
    python3.6 -m pip install pip --upgrade && \
    python3.6 -m pip install wheel && \
    apt-get install lsof && \
    rm -rf /var/lib/apt/lists/*

RUN pip install uwsgi

# update working directories
ADD ./requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt

# setup config
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf
RUN rm /etc/nginx/sites-enabled/default

ADD . /code

RUN mkdir /opt/logs

RUN ln -s /code/nginx.conf /etc/nginx/sites-enabled/
RUN ln -s /code/supervisor.conf /etc/supervisor/conf.d/

EXPOSE 5000

CMD ["supervisord", "-n"]


