#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from flask import Flask
from flask import redirect, render_template, request

app = Flask(__name__)


@app.route('/')
def hello():
    return redirect('/tpl/sorry/')


@app.route('/tpl/<name>/')
def tpl(name="sorry"):
    app.logger.debug(name)
    return render_template('{name}/index.html'.format(name=name))


@app.route('/tpl/<name>/make', methods=['POST', 'GET'])
def tplmake(name="sorry"):
    if request.method == 'POST':
        a = request.get_data()
        dict1 = json.loads(a)

        sentences = list(dict1.keys())
        for k, v in dict1.items():
            sentences[int(k)] = v

        app.logger.debug(json.dumps(sentences, ensure_ascii=False))
        import render
        path = render.render_gif(name, sentences)
        app.logger.debug(path)
        return '<p><a href="/{path}" target="_blank"><p>点击下载</p></a></p>'.format(path=path)
    else:
        return '<h1>只接受post请求！</h1>'


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=8000)
