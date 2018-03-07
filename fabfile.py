#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import local, lcd


def pull():
    local("git pull https://github.com/East196/aiscrapy")


def commit(doc="clean"):
    local("git add . && git commit -m %s" % doc)


def push(doc="clean"):
    local("git add . && git commit -m %s && git push" % doc)
