# sorrypy

`sorry有钱真的可以为所欲为`

## 说明

[sorry](https://github.com/xtyxtyx/sorry)是一款很有意思的应用，源自于`sorry有钱真的可以为所欲为`这个梗。
**亮点**是可以换自己的梗生成gif。

可惜部署环境是ubuntu+ruby，我就重制了个全平台的python重置版博大家一笑。

荣誉首先属于[xtyxtyx](https://github.com/xtyxtyx/)

__[Hardy兄弟](https://github.com/q809198545)的[NodeJs版:node-sorry](https://github.com/q809198545/node-sorry)也非常好用，有[DEMO](http://119.23.239.110:3000/sorry/)为证，嘎嘎。__

`sorry客户真的可以为所欲为`样例：

![](static/cache/sorry-703a480ff26b72c4b2d2cc195b765f35.gif)

## Docker部署
一行搞定
```
docker-compose up -d
```
> 如果难以直视`950.18 MB`的 Docker 镜像，请移步`普通安装部署`

## 普通安装部署

1. 下载安装[python3](https://www.python.org/downloads/)

2. cmd命令行安装必须包
`
pip install flask pillow imageio ffmpeg-python moviepy
`
当然也可以
`
pip install -r requirements.txt
`
3. 安装ffmpeg
[ffmepg官网](http://ffmpeg.org/)下载安装ffmepg并加入path。

检验ffmpeg安装
```
ffmpeg -version
```
尽量使用3.4以上版本，低版本可能会`无法生成`或者`生成无字幕gif`。

4. cmd中运行
```
python app.py
```
5. 浏览器打开
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

然后你就可以为所欲为了~~~

### CentOS7下ffmpeg安装
```bash
wget https://ffmpeg.org/releases/ffmpeg-3.4.2.tar.bz2
yum -y install bzip2
yum -y install yasm
yum -y install libass libass-devel
tar -xf ffmpeg-3.4.2.tar.bz2
cd ffmpeg-3.4.2
./configure --enable-libass
make
make install
```
### Windows下ffmpeg安装

方便起见，已直接将最新版ffmpeg.exe放入项目根目录，所以无需下载。

如果需要全局使用ffmpeg，可参考[这篇文章](https://blog.csdn.net/yy3097/article/details/51063950)

## 适配新Gif

目前，想要适配新的gif,需要改动3个文件（修改前建议备份）
```
templates/sorry/index.html
static/sorry/template.mp4
static/sorry/template.tpl
```
其中
```
index.html  按照句子的多少删掉或者增加<input>即可
template.mp4   替换成新视频
template.tpl   替换成新的字幕模板
```

### 字幕模板template.tpl
首先使用aegisub为模板视频创建字幕，保存为sorry.template.ass

>[aegisub教程](https://tieba.baidu.com/p/1360405931)

![图片](https://dn-coding-net-production-pp.qbox.me/56a213df-9ff7-41e0-9b6c-96b1f0fe2cb6.png)

然后把文本替换成模板字符串 ```{{ sentences[n] }}``` 懒得换图了哈，以这个字符串为准

![图片](https://dn-coding-net-production-pp.qbox.me/6b07bc65-c3d7-4251-aad2-bd7b05af9102.png)

最后保存为template.tpl

现在这个网站就可以制作新的gif了

## Note
欢迎 `star` ~ `fork` ~~

[Github](https://github.com/East196/sorrypy) & [Gitee](https://gitee.com/east196/sorrypy)

## 💹 关注统计

### Github
[![Github](https://starchart.cc/East196/sorrypy.svg)](https://starchart.cc/East196/sorrypy)


