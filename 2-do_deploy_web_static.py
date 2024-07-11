#!/usr/bin/python3
"""Fabric script (based on the file 1-pack_web_static.py) that distributes an archive to your web servers, using the function do_deploy"""
import os
from fabric import Connection

# Remote server details
env.hosts = ['ubuntu@54.160.99.220']  # Assuming this is one of your web servers

def do_deploy(archive_path):
    if not os.path.exists(archive_path):
        print(f"Archive file {archive_path} not found.")
        return False

    # Upload the archive to /tmp/ directory on the server
    remote_path = '/tmp/'
    with Connection(env.hosts[0]) as conn:
        conn.put(archive_path, remote=remote_path)

        # Get the filename without extension
        archive_filename = os.path.basename(archive_path).replace('.tgz', '').replace('.tar.gz', '')

        # Uncompress the archive to /data/web_static/releases/<archive filename without extension>
        release_path = f'/data/web_static/releases/{archive_filename}/'
        conn.run(f'mkdir -p {release_path}')
        conn.run(f'tar -xzvf {remote_path}{archive_filename}.tar.gz -C {release_path}')

        # Delete the archive from the server
        conn.run(f'rm {remote_path}{archive_filename}.tar.gz')

        # Delete the symbolic link /data/web_static/current if it exists
        conn.sudo(f'rm -rf /data/web_static/current')

        # Create a new symbolic link
        conn.sudo(f'ln -s {release_path} /data/web_static/current')

        # Check if the symbolic link is created successfully
        result = conn.run('test -L /data/web_static/current && echo "True" || echo "False"')
        if result.stdout.strip() == "True":
            return True
        else:
            return False

    return False

# Example usage
if __name__ == "__main__":
    archive_path = '/path/to/your/archive.tar.gz'
    result = do_deploy(archive_path)
    if result:
        print("Deployment successful.")
    else:
        print("Deployment failed.")

