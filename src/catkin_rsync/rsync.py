import os
import shlex
import logging
import subprocess


class Rsync:
    def __init__(self):
        self.rsync = find_executable('rsync')
        if not self.rsync:
            raise RuntimeError('rsync could not be found')

    def run(self, path, remote_path):
        cmd = f'{self.rsync} -av --delete {path}/ {remote_path}'
        try:
            subprocess.call(shlex.split(cmd))
        except subprocess.CalledProcessError as e:
            logging.error(f'Failed to run rsync: {e}')

def find_executable(command):
    for path in os.environ['PATH'].split(os.pathsep):
        abs_path = os.path.join(path, command)

        if os.path.isfile(abs_path) and os.access(abs_path, os.X_OK):
            return abs_path

    return None
