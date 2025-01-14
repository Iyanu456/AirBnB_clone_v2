#!/usr/bin/python3
"""
fabric script that generates a .tgz from the contents of web_static

"""
from fabric.api import *
from datetime import datetime
import os

env.hosts = ["54.237.87.4", "54.160.105.182"]
env.user = "ubuntu"


def do_pack():
    """
        returns the archive path if archive has been correctly
        created.
        all files in the folder web_static are added to the final archive
        all archives must be stored in the folder versions
        the name of the archive created has the format
        web_static_<year><month><day><hour><minute><second>.tgz
        the function do_pack must return the archive path
        if the archive has been correctly generated.
        otherwise, it should return None
    """

    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    archived_path = "versions/web_static_{}.tgz".format(date)
    t_gzip_archive = local("tar -cvzf {} web_static".format(archived_path))

    if t_gzip_archive.succeeded:
        return archived_path
    else:
        return None


def do_deploy(archive_path):
    """
        Distribute the archive.
        all files in the folder web_static are added to the final archive
        all files in the folder web_static are added to the final archive
        all files in the folder web_static are added to the final archive
        all files in the folder web_static are added to the final
    """
    if os.path.exists(archive_path):
        archived_file = archive_path[9:]
        new_version = "/data/web_static/releases/" + archived_file[:-4]
        archived_file = "/tmp/" + archived_file
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(new_version))
        run("sudo tar -xzf {} -C {}/".format(archived_file,
                                             new_version))
        run("sudo rm {}".format(archived_file))
        run("sudo mv {}/web_static/* {}".format(new_version,
                                                new_version))
        run("sudo rm -rf {}/web_static".format(new_version))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(new_version))

        print("New version deployed!")
        return True

    return False
