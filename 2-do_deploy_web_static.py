#!/usr/bin/python3
"""import statement"""
from 1-pack_web_static.py import archive_path, connection, run
import os


def do_deploy(archive_path):
    if not os.path.exists(archive_path):
        return False
    else:
        return True

    """ Upload the archive to /tmp/ directory on the server"""
    host = ubuntu@54.160.99.220
    remote_path = '/tmp/'
    with connection(env.host[0])as conn:
        conn.put(archive_path, remote=remote_path)
        """ Uncompress the archive to /data/web_static/releases/
        <archive filename without extension>"""
        release_path = f'/data/web_static/releases/{archive_filename}/'
        conn.run(f'mkdir -p {release_path}')
        conn.run(f'tar - xzvf {remote_path}{archive_filename}.tar.gz
                -C {release_path}')

        """ Delete the archive from the server"""
        conn.run(f'rm {remote_path}{archive_filename}.tar.gz')


        """ Delete the symbolic link /data/web_static/current if it exists"""
        conn.sudo(f'rm -rf /data/web_static/current')

        """ Create a new symbolic link"""
        conn.sudo(f'ln -s {release_path} /data/web_static/current')

         """ Check if the symbolic link is created successfully"""
        result = conn.run('test -L /data/web_static/current && echo "True" || echo "False"')
        if result.stdout.strip() == "True":
            return True
        else:
            return False


