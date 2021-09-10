
FROM python:3.8-slim
RUN apt-get update 
RUN apt-get install -y ffmpeg ttf-wqy-microhei
RUN mkdir /usr/src/app -p
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN pip install -r requirements.txt -i  https://mirrors.aliyun.com/pypi/simple/
CMD python app.py
            