#!/usr/bin/python3
""" Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers """
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['35.174.208.232', '107.21.39.234']


def do_deploy(archive_path):
    """ Distribute file to server """
    if not exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')

        file_path = archive_path.split('/')[-1].split('.')[0]
        run('mkdir -p /data/web_static/releases/{}/'.format(file_path))
        run('tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}'
            .format(file_path, file_path))
        run('rm /tmp/{}.tgz'.format(file_path))
        run('mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}'.format(file_path, file_path))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(file_path))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}\
            /data/web_static/current'.format(file_path))
        return True

    except Exception as e:
        print(e)
        return False
