# sorrypy

`sorry有钱真的可以为所欲为`

## 说明

[sorry](https://github.com/xtyxtyx/sorry)是一款很有意思的应用，源自于`sorry有钱真的可以为所欲为`这个梗。
亮点是可以换自己的梗生成gif。
可惜部署环境是ubuntu+ruby，我就重制了个全平台的python重置版博大家一笑。
荣誉首先属于[xtyxtyx](https://github.com/xtyxtyx/)

`sorry客户真的可以为所欲为`样例：

![](static/cache/sorry-703a480ff26b72c4b2d2cc195b765f35.gif)

## 部署
1. 下载安装[python3](https://www.python.org/downloads/)
2. cmd命令行安装fabric3,flask,imageio
`
pip install fabric3 flask imageio
`
3. 在sorrypy项目根目录下，运行cmd命令
初始化，下载安装ffmepg（也可以用别的方法安装，但必须安装）
```
fab init
```
运行
```
fab run
```
4. 浏览器打开
[http://localhost:5000/](http://localhost:5000/)
然后你就可以为所欲为了~~~

### CentOS7下ffmpeg安装
```
yum install epel-release -y
rpm --import http://li.nux.ro/download/nux/RPM-GPG-KEY-nux.ro
rpm -Uvh http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-5.el7.nux.noarch.rpm
yum install ffmpeg ffmpeg-devel -y
```

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


## TODO
- [ ] 加入锁机制限制并发
- [ ] 自动生成页面
