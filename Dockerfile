# 优化版 Dockerfile - 减小镜像体积
FROM python:3.11-slim-bookworm

# 设置环境变量
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# 安装系统依赖（合并 RUN 减少层数，清理缓存）
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    fonts-wqy-microhei \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# 创建工作目录
WORKDIR /app

# 先复制依赖文件，利用 Docker 缓存
COPY requirements.txt .

# 安装 Python 依赖
RUN pip install --no-cache-dir -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

# 复制应用代码
COPY app.py render.py ./
COPY static/ ./static/
COPY templates/ ./templates/

# 创建缓存目录
RUN mkdir -p static/cache

# 暴露端口
EXPOSE 5997

# 启动应用
CMD ["python", "app.py"]
