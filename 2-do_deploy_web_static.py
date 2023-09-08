#!/usr/bin/python3
"""
Fabric script to distribute an archive to your web servers using do_deploy
"""

from fabric.api import env, put, run, local
from os.path import exists
from datetime import datetime

env.hosts = [''54.85.129.38, '18.206.208.173']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """deploys to remote server """
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ directory on the server
        put(archive_path, '/tmp/')

        # Extract the archive to the web server
        archive_filename = archive_path.split('/')[-1]
        release_folder = '/data/web_static/releases/{}'.format(
            archive_filename.split('.')[0])
        run('mkdir -p {}'.format(release_folder))
        run('tar -xzf /tmp/{} -C {}'.format(archive_filename, release_folder))

        # Remove the uploaded archive
        run('rm /tmp/{}'.format(archive_filename))

        # Move the contents of the extracted folder
        run('mv {}/web_static/* {}'.format(release_folder, release_folder))

        # Remove the empty web_static folder
        run('rm -rf {}/web_static'.format(release_folder))

        # Remove the current symlink if it exists
        current_link = '/data/web_static/current'
        if exists(current_link):
            run('rm {}'.format(current_link))

        # Create a new symlink to the deployed version
        run('ln -s {} {}'.format(release_folder, current_link))

        # Check if the symbolic link is updated correctly
        symlink_path = run('readlink -f {}'.format(current_link))
        if symlink_path == release_folder:
            return True
        else:
            return False
    except Exception as e:
        return False
