#!/usr/bin/python3
""" do pack function"""


from fabric.api import local
from time import strftime


def do_pack():
    """generates a .tgz archive from the contents of web_static forlder"""
    now = strftime("%Y%M%d%H%m%S")
    try:
        local("mkdir -p version")
        fle = "version/web_static_{}.tgz".format(now)
        local("tar -czvf {} web_static/".format(fle))
        return fle
    except:
        return None
