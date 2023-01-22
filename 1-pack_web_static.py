#!/usr/bin/python3
"""Create a tar far using fabric"""
from fabric.api import *
import datetime
import os


def do_pack():
    """
    Creates an archive in the /data/webstac directory
    arg:
        No parameter
    return:
        path of the creted argived file
    """
    with settings(warn_only=True):
        dat = datetime.datetime.now()
        name = "web_static_{}{}{}{}{}.tgz".format(
            dat.year, dat.month, dat.hour, dat.minute,
            dat.second
        )
        local("mkdir -p versions")
        result = local('tar -czvf versions/{} web_static'.format(name))
        if result.succeeded:
            return os.getcwd() + '/versions/' + name
        else:
            return None
