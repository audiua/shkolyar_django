FROM python:onbuild
ENV PYTHONUNBUFFERED 1
RUN apt-get upgrade && apt-get install -y libmysqlclient-dev
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
