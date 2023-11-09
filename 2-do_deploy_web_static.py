#!/usr/bin/python3
'''Fabric module that distributes an archive to your web servers'''
from fabric.api import env, run, put
from os import path

env.hosts = ['35.174.208.232', '107.21.39.234']


def do_deploy(archive_path):
    '''Function that distributes an archive to your web servers'''
    filename = archive_path[9:-4]

    if not path.exists(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}/".format(filename))
        run('tar -zxf /tmp/{} -C /data/web_static/releases/{}/'
            .format(filename + ".tgz", filename))
        run('rm /tmp/{}'.format(filename + '.tgz'))
        run('mv /data/web_static/releases/{}/web_static/* '
            ' /data/web_static/releases/{}/'.format(filename, filename))
        run('rm -rf /data/web_static/releases/{}/web_static'
            .format(filename))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
            .format(filename))
        return True
    except:
        return False
    return False
