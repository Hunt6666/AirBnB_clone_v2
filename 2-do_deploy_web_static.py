#!/usr/bin/python3
""" do pack and do deploy functions"""

import os
from fabric.api import local, env, put, run
from time import strftime

env.host = ['34.73.60.145', '35.185.44.189']
env.user = 'ubuntu'


def do_pack():
    """generates a .tgz archive from the contents of web_static forlder"""
    now = strftime("%Y%M%d%H%m%S")
    try:
        local("mkdir -p versions")
        fle = "versions/web_static_{}.tgz".format(now)
        local("tar -czvf {} web_static/".format(fle))
        return fle
    except:
        return None



def do_deploy(archive_path):
    """ distributes an archive to the web server """
    if not os.path.isfile(archive_path):
        print(archive_path + " is not a file")
        return False
    try:
        fle = archive_path.split('/')[-1]
        fle_dir = fle.split('.')[0]
        pth = "/data/web_static/releases/"
        fle_pth = pth + fle
        sym = "/data/web_static/current"
        put(archive_path, "/tmp/" + fle)
        run("rm -rf" + pth + fle_dir + '/')
        run("mkdir -p " + pth + fle_dir + '/')
        run("tar -xzf /tmp/" + fle + " -C " + pth + fle_dir + '/')
        run("rm /tmp/"+ fle)
        run("mv " + pth + fle_dir + "web_static/* " + pth + fle_dir + '/')
        run("rm -rf " + pth + fle_dir + "web_static")
        run("rm -rf " + sym)
        run("ln -s " + pth + fle_dir + ' ' + sym)
        print('worked')
        return True
    except:
        print('fail')
        return False
    return True
