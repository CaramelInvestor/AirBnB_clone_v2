#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo, using the function do_pack"""

import os.path
from fabric.api import local
from datetime import datetime


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
