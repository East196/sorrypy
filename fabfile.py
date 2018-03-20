#!/usr/bin/env python
# -*- coding: utf-8 -*-


from fabric.api import local


def init():
    import imageio
    imageio.plugins.ffmpeg.download()


def run():
    local("python app.py")


if __name__ == '__main__':

    init()
