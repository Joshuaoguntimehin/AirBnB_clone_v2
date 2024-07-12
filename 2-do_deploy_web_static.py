#!/usr/bin/python3
'''This Fabric script distributes an archive to web servers and sets up the web servers for deployment'''

import os
from fabric import Connection, task
from 1-pack_web_static import do_pack

env.hosts = ['ubuntu@34.207.58.74', 'ubuntu@54.160.99.220']

def do_deploy(archive_path):
    if not os.path.exists(archive_path):
        return False
    
    try:
        # Extract the archive filename and name without extension
        archive_name = os.path.basename(archive_path)
        archive_filename_no_ext = os.path.splitext(archive_name)[0]
        release_folder = f"/data/web_static/releases/{archive_filename_no_ext}"

        # Loop through each server and perform operations
        for host in env.hosts:
            conn = Connection(host)
            
            # Upload the archive to /tmp/ directory on the web server
            conn.put(archive_path, remote='/tmp/')
            
            # Uncompress the archive to the release folder
            conn.run(f'mkdir -p {release_folder}')
            conn.run(f'tar -xzf /tmp/{archive_name} -C {release_folder}')
            
            # Remove the archive from the web server
            conn.run(f'rm /tmp/{archive_name}')
            
            # Move contents out of the web_static directory
            conn.run(f'mv {release_folder}/web_static/* {release_folder}/')
            conn.run(f'rm -rf {release_folder}/web_static')
            
            # Delete the symbolic link /data/web_static/current
            conn.run('rm -rf /data/web_static/current')
            
            # Create a new symbolic link
            conn.run(f'ln -s {release_folder} /data/web_static/current')
        
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

@task
def deploy(c):
    """ Function to pack and deploy the web_static content """
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)

