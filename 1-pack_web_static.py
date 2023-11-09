#!/usr/bin/python3
# Fabfile that generates a .tgz archive from the contents of web_static.
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """This function create an archive of the directory web_static."""
    dte = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dte.year,
                                                         dte.month,
                                                         dte.day,
                                                         dte.hour,
                                                         dte.minute,
                                                         dte.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file
