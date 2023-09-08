#!/usr/bin/python3
"""
Fabric script to distribute an archive to your web servers using do_deploy
"""

from fabric.api import env, put, run, local
from os.path import exists
from datetime import datetime

env.hosts = ['54.85.129.38', '18.206.208.173']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """deploys to remote server"""
    if not exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')
        archive_filename = archive_path.split('/')[-1]
        release_folder = '/data/web_static/releases/{}'.format(
            archive_filename.split('.')[0])
        run('mkdir -p {}'.format(release_folder))
        run('tar -xzf /tmp/{} -C {}'.format(archive_filename, release_folder))

        run('rm /tmp/{}'.format(archive_filename))
        run('mv {}/web_static/* {}'.format(release_folder, release_folder))
        run('rm -rf {}/web_static'.format(release_folder))
        current_link = '/data/web_static/current'
        if exists(current_link):
            run('rm {}'.format(current_link))
        run('ln -s {} {}'.format(release_folder, current_link))

        symlink_path = run('readlink -f {}'.format(current_link))
        if symlink_path == release_folder:
            return True
        else:
            return False
    except Exception as e:
        return False
