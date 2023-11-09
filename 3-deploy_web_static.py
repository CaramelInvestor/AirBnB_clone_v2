#!/usr/bin/python3
""" Fabric script (based on the file 2-do_deploy_web_static.py)
that creates and distributes an archive to your web servers, using the function deploy """

from os.path import exists
from fabric.api import local, env, put, run
from datetime import datetime

env.hosts = ['35.174.208.232', '107.21.39.234']


def do_pack():
    """This function returns archive path if the archive has been correctly generated"""
    now_dt = datetime.utcnow()
    file_path = "versions/web_static_{}{}{}{}{}{}.tgz".format(now_dt.year,
                                                              now_dt.month,
                                                              now_dt.day,
                                                              now_dt.hour,
                                                              now_dt.minute,
                                                              now_dt.second)
    
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file_path)).failed is True:
        return None
    return file_path


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


def deploy():
    """ Distributes archives to your web servers """
    archive_path = do_pack()
    if archive_path is None:
        return False

    return(do_deploy(archive_path))
