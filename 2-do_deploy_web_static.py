#!/usr/bin/python3
"""fab file that distributes an archive to your web servers"""

import datetime
from fabric.api import env, put, run, local

env.hosts = ['35.174.208.232', '107.21.39.234']


def do_pack():
    """Function that creates archive files"""
    try:
        local('mkdir -p versions')
        dt = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        local('tar -cvzf "versions/web_static_{}.tgz" ./web_static'.
              format(dt), capture=True)
        return "versions/web_static_{}.tgz".format(dt)
    except Exception as e:
        print(e)
        return None


def do_deploy(archive_path):
    """deploys archives to web servers """
    try:
        filename = archive_path.split("/")[-1]
        fname = filename.split(".")[0]
        filepath = "/data/web_static/releases/%s" % fname

        put(archive_path, "/tmp")
        run("sudo mkdir -p %s" % filepath)
        run("sudo tar -xzf /tmp/%s -C %s" % (filename, filepath))
        run("sudo rm /tmp/%s" % filename)
        run("sudo mv %s/web_static/* %s/" % (filepath, filepath))
        run("sudo rm -rf %s/web_static" % filepath)
        run("rm -rf /data/web_static/current")
        run("sudo ln -s %s/ /data/web_static/current" % filepath)
        return True
    except Exception:
        return False
