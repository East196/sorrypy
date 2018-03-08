#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import os
from subprocess import Popen, PIPE

from jinja2 import Template


def calculate_hash(src):
    m2 = hashlib.md5()
    m2.update(str(src).encode("utf8"))
    return m2.hexdigest()


def render_gif(template_name, sentences):
    filename = template_name + "-" + calculate_hash(sentences) + ".gif"
    gif_path = "static/cache/" + filename
    if os.path.exists(gif_path):
        return gif_path
    make_gif_with_ffmpeg(template_name, sentences, filename)
    return gif_path


def ass_text(template_name):
    with open("static/%s/template.tpl" % template_name) as fp:
        content = fp.read()
    return content


def render_ass(template_name, sentences, filename):
    output_file_path = "static/cache/%s.ass" % filename
    template = ass_text(template_name)
    rendered_ass_text = Template(template).render(sentences=sentences)
    with open(output_file_path, "w", encoding="utf8") as fp:
        fp.write(rendered_ass_text)
    return output_file_path


def make_gif_with_ffmpeg(template_name, sentences, filename):
    ass_path = render_ass(template_name, sentences, filename)
    gif_path = "static/cache/" + filename
    video_path = "static/" + template_name + "/template.mp4"
    print(ass_path, gif_path, video_path)
    cmd = "ffmpeg -i {video_path} -r 8 -vf ass={ass_path},scale=300:-1 -y {gif_path}" \
        .format(video_path=video_path, ass_path=ass_path, gif_path=gif_path)
    print(cmd)
    p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
    p.wait()
    if p.returncode != 0:
        print("Error.")
        return -1


if __name__ == '__main__':
    print(str(["hello"]))
    sentences = ["好啊", "就算你是一流工程师", "就算你出报告再完美", "我叫你改报告你就要改", "毕竟我是客户", "客户了不起啊", "sorry 客户真的了不起", "以后叫他天天改报告", "天天改 天天改"]
    template_name = "sorry"
    path = render_gif(template_name, sentences)
    print(path)
