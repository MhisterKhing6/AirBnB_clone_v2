#!/usr/bin/python3
"""Create a tar far using fabric"""
from fabric.api import *
import datetime
import os

env.hosts = ['52.72.27.194', '52.201.158.148']
env.user = "ubuntu"


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


def do_deploy(archive_path):
    """
    deploy and archieved to a server
    args:
        no arguemetn
    return:
        boolean
    """
    if os.path.exists(archive_path):
        with settings(warn_only=True):
            a = put(archive_path, '/tmp/')
            filname = os.path.basename(archive_path)
            filname_with = filname.strip('.tgz')
            save_path = '/data/web_static/releases/{}'.format(filname_with)
            b = run('mkdir -p {}'.format(save_path))
            c = run(
                'tar -xzf /tmp/{}\
                -C {}'.format(filname, save_path)
                )
            f = run("mv -f {}/web_static/* {} ".format(save_path, save_path))
            g = run('rm -rf {}/web_static'.format(save_path))
            d = run('rm /tmp/{}'.format(filname))
            h = run('rm -rf /data/web_static/current')
            e = run('ln -s {} /data/web_static/current'.format(save_path))
            if a.succeeded and b.succeeded and c.succeeded and \
               e.succeeded and d.succeeded:
                return True
            else:
                return False
    else:
        return False
