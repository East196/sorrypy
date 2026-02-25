#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import os
import subprocess
import shlex

from jinja2 import Template


def safe_path(path):
    """验证路径安全性，防止目录遍历攻击"""
    # 移除危险字符
    dangerous = ["..", "~", "\\", "//"]
    for d in dangerous:
        if d in path:
            raise ValueError(f"Invalid path: contains '{d}'")
    return path


def calculate_hash(src):
    m2 = hashlib.md5()
    m2.update(str(src).encode("utf8"))
    return m2.hexdigest()


def render_gif(template_name, sentences):
    template_name = safe_path(template_name)
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
    gif_path = "static/cache/" + safe_path(filename)
    video_path = "static/" + safe_path(template_name) + "/template.mp4"
    print(ass_path, gif_path, video_path)
    
    # 使用参数列表而非 shell 字符串拼接，防止命令注入
    cmd = [
        "ffmpeg",
        "-i", video_path,
        "-r", "8",
        "-vf", f"ass={ass_path},scale=300:-1",
        "-y", gif_path
    ]
    print(" ".join(cmd))
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        return -1


if __name__ == '__main__':
    print(str(["hello"]))
    sentences = ["好啊", "就算你是一流工程师", "就算你出报告再完美", "我叫你改报告你就要改", "毕竟我是客户", "客户了不起啊", "sorry 客户真的了不起", "以后叫他天天改报告", "天天改 天天改"]
    template_name = "sorry"
    path = render_gif(template_name, sentences)
    print(path)
