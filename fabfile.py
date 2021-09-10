"""
一个Flask专用的fabfile
1. 安装 Python3
2. 安装 fabric3
   `pip install fabric3`
3. 运行脚本
   **必须**在 bash 命令行当前目录下运行
   eg：git 中的 git-bash 命令行
   
   `fab env`   建立 pipenv 环境
   `fab init`  初始化 flask 环境
   ------ 开发中 ------
   `fab req`     导出 requirements.txt
   `fab docker`  建立 docker 配置
   `fab run`     运行 docker 容器
"""
import codecs

from fabric.api import local, lcd

def env():
    local("pipenv --python 3.8")

def init():
    local("pipenv install flask flask_cors")

def req():
    local("pipenv run pip freeze > requirements.txt")

def docker():
    with codecs.open("Dockerfile", "w", encoding="utf-8") as f:
        f.write(f'''
FROM python:3.8-alpine
RUN mkdir /usr/src/app -p
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN pip install -r requirements.txt -i  https://mirrors.aliyun.com/pypi/simple/
CMD python application.py
            ''')
    with codecs.open("docker-compose.yml", "w", encoding="utf-8") as f:
        f.write(f'''
version: '3'
services:
  web:
    build: .
    ports:
     - "5000:5000"
            ''')

def run():
    local("docker-compose up -d")

def stop():
    local("docker-compose stop")
    local("docker-compose down")
    local("docker-compose down --rmi all")
    local("docker-compose down -v")

