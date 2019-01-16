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
        return False
    try:
        fle = archive_path.split('/')[-1]
        fle_pth = "/data/web_static/releases/" + fle + '/'
        sym = "/data/web_static/current"
        put(archive_path, "/tmp/")
        run("mkdri -p " + fle_pth)
        run("tar -xzf /tmp/" + fle + " -C " + fle_pth)
        run("rm /tmp/"+ fle)
        run("mv " + fle_pth + "web_static/*" + fle_pth)
        run("rm -rf " + fle_pth + "web_static")
        run("rm -rf " + sym)
        run("ln -s " + fle_pth + ' ' + sym)
        print('worked')
        return True
    except:
        print('fail')
        return False
    return True


def deploy():
    """creates and distributes an archive to web server"""
    archive = do_pack()
    if archive is None:
        return False
    out = do_deploy(archive)
    return out
