#!/usr/bin/python3
"""import statement"""
from fabric.api import local
from datetime import datetime

def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    """
    # Create versions directory if it doesn't exist
    local("mkdir -p versions")

    # Get the current date and time to include in the archive name
    date = datetime.now().strftime("%Y%m%d%H%M%S")

    # Define the archive name
    archive_name = "versions/web_static_{}.tgz".format(date)

    # Create the .tgz archive
    result = local("tar -czvf {} web_static".format(archive_name))

    # Return the archive path if the command was successful
    if result.succeeded:
        return archive_name
    else:
        return None

