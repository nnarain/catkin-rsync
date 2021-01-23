import os
import shlex
import subprocess
from setuptools import setup

root = os.path.dirname(os.path.realpath(__file__))

# Long description from README
readme = os.path.join(root, 'README.rst')

# Read latest git tag
try:
    latest_tag = subprocess.check_output(shlex.split('git describe --tags --abbrev=0'), cwd=root)
except Exception as e:
    print('Error getting latest git tag. {}'.format(str(e)))
    # exit(1)
    latest_tag = '0.0.0'

setup(
    name='catkin-rsync',
    version=latest_tag,
    author='Natesh Narain',
    author_email='nnaraindev@gmail.com',
    description='Sync catkin workspace to remote systems',
    long_description=open(readme).read(),
    license='MIT',
    keywords='catkin ros rsync c++',

    package_dir={'': 'src'},
    packages=['catkin_rsync'],

    install_requires=['catkin-pkg'],

    entry_points= {
        'catkin_tools.commands.catkin.verbs': [
            'rsync = catkin_rsync.main:description'
        ]
    }
)
