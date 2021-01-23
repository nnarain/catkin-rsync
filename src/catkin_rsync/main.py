import os
import logging

from catkin_tools.context import Context
from catkin_tools.metadata import find_enclosing_workspace

from .rsync import Rsync

space_choices = ['all', 'source', 'install']

def prepare_arguments(parser):
    parser.add_argument('space', choices=space_choices, help='Catkin workspace space to sync')
    parser.add_argument('remote', help='The remote part of the rsync command')
    return parser

def run_rsync(args):
    cwd = os.getcwd()
    ws = find_enclosing_workspace(cwd)

    context = Context.load(ws)

    if ws:
        sync_pathes = get_sync_pathes(context, args.space)
        run_sync_pathes(sync_pathes, args.remote)
    else:
        logging.error(f'No catkin workspace found. Is "{cwd}" contained in a workspace?')

def run_sync_pathes(pathes, remote_path):
    rsync = Rsync()
    for path in pathes:
        rsync.run(path, remote_path)

def get_sync_pathes(context, option):
    if option == 'all':
        return [context.source_space_abs, context.build_space_abs, context.devel_space_abs, context.install_space_abs]
    elif option == 'source':
        return [context.source_space_abs]
    elif option == 'install':
        return [context.install_space_abs]
    else:
        raise RuntimeError(f'Invalid option: {option}')

description = dict(
    verb='rsync',
    description='Sync catkin workspace with remote system',
    main=run_rsync,
    prepare_arguments=prepare_arguments,
)
