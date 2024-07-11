#!/usr/bin/python3
""" Assuming this is one of"""
"""import statement"""
import 1-pack_web_static
import os
from fabric import Connection

def do_deploy(archive_path):
    file_path = '/data/web_static/releases/archive'
    if os.path.exists(file_path):
        return True
    else:
        return False
    # Remote server details
    host = 'ubuntu@54.160.99.220'

    local_archive = '/path/to/your/archive.tar.gz'
    # Destination path on the server
    remote_path = '/tmp/'
    symbolic_link = '/data/web_static/current'

    with Connection(host) as conn:
     conn.put(local_archive, remote=remote_path)
     conn.run(f'tar -xzvf {remote_path}archive.tar.gz -C {remote_path}')
       # Connect to the server
    with Connection(host) as conn:
        conn.run(f'rm {archive_path}')
        # Connect to the server
    with Connection(host) as conn:
        # Delete the symbolic link
        conn.run(f'rm {symbolic_link}')
         #  Get the filename without extension
         archive_filename = conn.run(f'basename {remote_path}archive.tar.gz .tar.gz').stdout.strip()
         # Create symbolic link
        conn.sudo(f'ln -sfn /data/web_static/releases/{archive_filename} /data/web_static/current')
        result = conn.run('test -L /data/web_static/current && echo "True" || echo "False"')
        return result.stdout.strip() == "True"

    # Connect to the servers and execute commands
    results = c.run(execute_commands)

    # Return True if all operations were successful on both servers, otherwise False
    return all(results.values())
