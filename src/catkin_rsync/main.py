from catkin_pkg.packages import find_package_paths
from catkin_tools.metadata import find_enclosing_workspace

def prepare_arguments(parser):
    pass

def run_rsync(args):
    pass

description = dict(
    verb='rsync',
    description='Sync catkin workspace with remote system',
    main=run_rsync,
    prepare_arguments=prepare_arguments,
)
