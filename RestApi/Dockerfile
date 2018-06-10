FROM python:3.5
LABEL lrb restapi
ENV PYTHONUNBUFFERED 1
RUN mkdir /docker_api
WORKDIR /docker_api
COPY . /docker_api
#RUN pip install -r requirements.txt
RUN pip install  -i https://pypi.douban.com/simple/ --trusted-host=pypi.douban.com/simple  -r requirements.txt
